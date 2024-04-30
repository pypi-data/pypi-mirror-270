#!/usr/bin/python3

import os
import tempfile
import argparse 
import numpy as np
import sqlite3
import time 
import glob
import dask
import dask.distributed
from dask.delayed import delayed
import copy
import sys
import datetime
import radvelso
from datetime import  timedelta
import domutils.radar_tools as radar_tools
import domutils.geo_tools as geo_tools
from scipy.interpolate import LinearNDInterpolator
from radvelso.unravel import find_reference
from radvelso.cthinning import cthinning
from radvelso.unravel.core import Dealias as DealiasBase
import xarray as xr
import pickle 
import scipy.spatial
import cartopy.crs as ccrs
import warnings
import joblib
import domcmc.fst_tools as fst_tools
from dask.distributed import Client
import subprocess
import shlex
import csv
import shutil
import re
from pathlib import Path


class Dealias(DealiasBase):
    
    """
    Dealiasing class.
    """

    def __init__(
        self, ppi_ranges, ppi_azimuths, ppi_elevation, ppi_velocity, nyquist, alpha=0.6):
       
        """
        Constructor.

        arg:
        ----------
        ppi_ranges: array[bins]
            PPI's bins range in meters.
        ppi_azimuths: array[rays]
            PPI's rays angle in degrees.
        ppi_elevation: float
            PPI elevation angle in degrees.
        ppi_velocity: array[rays, bins]
            Doppler velocity.
        nyquist: float
            PPI nyquist velocity.
        alpha: float
            Coefficient for which the nyquist velocity periodicity range is
            considered valid.
        """

        super().__init__(
            ppi_ranges,
            ppi_azimuths,
            ppi_elevation,
            ppi_velocity.copy(),
            nyquist,
            alpha=alpha,
        )
        self._initialized = False

    def initialize(self, model_dop_velocity, beta=0.25, missing=-9999.0, undetect=-3333.0):
     
        """
        Initialize the dealiasing finding the radials of reference.

        1. Consider as "reference velocities" dealiased velocities close to the model's doppler velocity.
           This step is an initial dealiasing that helps the sbsequent dealiasing steps.
        2. Find reference radials (section 3.a.2, Leuf et al, 2020).

        Notes
        -----
        Louf, V., Protat, A., Jackson, R. C., Collis, S. M., & Helmus, J. (2020).
        UNRAVEL: A Robust Modular Velocity Dealiasing Technique for Doppler Radar,
        Journal of Atmospheric and Oceanic Technology, 37(5), 741-758. Retrieved Mar 2, 2022.
        https://journals.ametsoc.org/view/journals/atot/37/5/jtech-d-19-0020.1.xml
        """

        model_dop_velocity = model_dop_velocity.copy()

        # Prepare the data
        invalid = (self.velocity == missing) | (self.velocity == undetect)
        valid = ~invalid
        self.velocity[invalid] = np.nan
        self.dealias_vel = self.velocity.copy()

        #####################################
        # Initial dealiasing using model data
        #print (invalid)
        model_dop_velocity[invalid] = missing
        self.velocity[invalid] = missing

        # Find reference velocities close to the model_velocity (reference)
        # 1. Generate velocity candidates at +/- 2*Ny*i intervals.
        vel_candidates = []
        for i in range(-3, 4):
            vel_candidates.append(self.velocity + 2 * i * self.nyquist)
        vel_candidates = np.stack(vel_candidates, axis=-1)

        # 2. Keep the closest one to the model_velocity (reference)
        sorting_idx = np.argsort(
            np.abs(vel_candidates - model_dop_velocity[:, :, None]), axis=2
        )[:, :, 0].squeeze()
        xi, yi = np.meshgrid(
            range(sorting_idx.shape[0]), range(sorting_idx.shape[1]), indexing="ij"
        )
        vel_candidate = vel_candidates[xi, yi, sorting_idx]

        # 3. Check if the candidate is |Vcand-Vobs|< beta*Vny
        #    If True, accept that that candidate.

        # Check is the candidate is equal to the original velocity.
        # not_modified = np.abs(vel_candidate - self.velocity) < 0.0001
        vel_diff = np.abs(vel_candidate - model_dop_velocity)
        accepted_candidates = vel_diff < beta * self.nyquist  # & (~not_modified)
        
        # not_modified = not_modified & valid
        model_valid = (model_dop_velocity != missing) & (model_dop_velocity != undetect)
        accepted_candidates = accepted_candidates & valid & model_valid

        if np.count_nonzero(accepted_candidates.size > 0):

            self.dealias_vel[accepted_candidates] = vel_candidate[accepted_candidates]
            self.flag[accepted_candidates] = 2  # Dealiased
            # self.flag[not_modified] = 0  # Consider as unprocessed.

            # NOTE: Once a velocity has been flagged 1 or 2, it is not modified anymore by
            # subsequent steps.
        self.dealias_vel[invalid] = np.nan
        self.flag[invalid] = -1

        ########################
        # Find reference radials
        start_beam, end_beam = find_reference.find_reference_radials(
            self.azimuth, self.dealias_vel)

        azi_start_pos = np.argmin(np.abs(self.azimuth - start_beam))
        azi_end_pos = np.argmin(np.abs(self.azimuth - end_beam))

        self.azi_start_pos = azi_start_pos
        self.azi_end_pos = azi_end_pos

        self._initialized = True

    def dealiase(self):

        """
        Dealise the doppler velocity.

        Dealiasing flags:
        -3: Missing values
        0: Unprocessed. This velocity could not be dealiased.
        1: Processed and unchanged value
        2: Processed and dealiased value.
        """

        if not self._initialized:
            raise RuntimeError(
                "The dealiasing object was not initialized.\n"
                "Run the initialize(*args,**kwargs) method first.")

        for window in [6, 12, 24]:
            self.correct_range(window)
            self.correct_clock(window)
            if self.check_completed():
                break

        if not self.check_completed():
            for window in [(5, 5), (10, 10), (20, 20), (40, 40)]:
                self.correct_box(window)
                if self.check_completed():
                    break

        self.correct_closest()
        self.flag[self.flag > 2] = 2

def load_extension_sqlite(conn_ppi_obsdb):
    """
    Load custom SQLite extensions for the radvelso module.

    This function loads two custom SQLite extensions, blobint and series, that are used in the radvelso module.

    Args:
    ----------------
    conn_ppi_obsdb: sqlite3.Connection - SQLite connection object to which the extensions will be loaded.

    Returns:
    ----------------
    None

    Notes:
    ----------------
    The extensions are loaded from the radvelso package, and they provide additional functionality for handling
    binary large objects (BLOBs) and generating series of numbers in SQLite queries.

    """

    # Get the full path of the radvelso module directory
    radvelso_dir = os.path.dirname(radvelso.__file__)

    # Get the package directory (one level above the radvelso module)
    package_dir = os.path.dirname(radvelso_dir)

    # Define the full path to the extension directory
    extension_dir = f'{package_dir}/radvelso/extension/'

    # Enable loading extensions in the SQLite connection
    conn_ppi_obsdb.enable_load_extension(True)

    # Load the blobint extension
    conn_ppi_obsdb.execute(f"SELECT load_extension('{extension_dir}/blobint.so')")

    # Load the series extension
    conn_ppi_obsdb.execute(f"SELECT load_extension('{extension_dir}/series.so')")

def find_schema(schema):
    """
    Find the schema file contained in the radvelso Python package.

    This function searches for the specified schema file within the radvelso package.

    Args:
    ----------------
    schema: str - The name of the schema file to be located.

    Returns:
    ----------------
    schema_file: str - Full path of the found schema file.

    """

    # Get the full path of the radvelso module directory
    radvelso_dir = os.path.dirname(radvelso.__file__)

    # Get the package directory (one level above the radvelso module)
    package_dir = os.path.dirname(radvelso_dir)

    # Define the full path to the schema file we are looking for
    schema_file = f'{package_dir}/radvelso/schema/{schema}'

    # Check if the schema file exists in the package
    if not os.path.isfile(schema_file):
        raise ValueError(f'Schema file: {schema_file} does not exist')

    return schema_file

def make_input_ppi_db(filein,
                      id_antenna,
                      this_time,
                      nominal_ppi_elevation,
                      min_range_in_ppi,
                      max_range_in_ppi,
                      obs_nyquist,
                      timeana=False):
    """
    Make a separate SQLite database for one PPI scan.

    This database is stored in memory and allows quick searches of averaging boxes.

    Args:
    ----------------
    filein : str - Input SQLite file containing data from many radars and times.
    id_antenna : str - Radar for this one volume scan.
    this_time : datetime - End time of this one volume scan.
    nominal_ppi_elevation : float - Nominal elevation angle of the PPI scan.
    min_range_in_ppi : float - Minimum range in the PPI scan.
    max_range_in_ppi : float - Maximum range in the PPI scan.
    obs_nyquist : float - Nyquist velocity used for quality control.
    timeana : (bool, optional) - lag to enable time analysis, by default False.

    Returns:
    ----------------
    conn_ppi_db,: chema_filesqlite3.Connection - SQLite connection to the created database.
    result: int - Number of data entries in the created database.

    """
    if timeana: tc_0 = time.time()

    # Create a URI filename for the database connection with query parameters
    uri_filename = f"file:{id_antenna}_{this_time}_{round(nominal_ppi_elevation, 2)}?mode=memory&cache=shared"

    # Connect to the database using the URI filename
    conn_ppi_db = sqlite3.connect(uri_filename, uri=True)

    # Optimize database settings for faster processing
    conn_ppi_db.execute("""PRAGMA journal_mode=OFF;""")
    conn_ppi_db.execute("""PRAGMA synchronous=OFF;""")
    conn_ppi_db.execute("""PRAGMA journal = off;""")
    conn_ppi_db.execute("""PRAGMA temp_store = MEMORY;""")
    conn_ppi_db.execute('PRAGMA journal_mode = WAL')

    # Find and execute the database schema
    schema = find_schema('schema')
    load_and_execute_schema(conn_ppi_db)

    # Improve searches with index tables
    create_index_tables_elevation_azimuth(conn_ppi_db)
    create_index_tables_idobs_iddata(conn_ppi_db)

    # Attach the input database to the PPI database
    conn_ppi_db.execute(f'ATTACH DATABASE "file:{id_antenna}_{this_time}?mode=memory&cache=shared" AS db_all')

    # Select headers in the desired PPI scan
    order_sql = """INSERT INTO header
                   SELECT *
                   FROM db_all.header
                   WHERE round(nominal_ppi_elevation, 1) = ?
                   AND time = ?;"""
    conn_ppi_db.execute(order_sql, (round(nominal_ppi_elevation, 1), this_time))

    # Select associated data entries
    order_sql = """INSERT INTO data
                   SELECT *
                   FROM db_all.data
                   WHERE id_obs IN (SELECT id_obs FROM header);"""
    conn_ppi_db.execute(order_sql)

    conn_ppi_db.commit()

    # Get the number of data entries in the database
    query = f'select count(*) from data;'
    c = conn_ppi_db.cursor()
    c.execute(query)
    result = c.fetchone()

    if timeana: print(f"Runtime e1: {round(time.time() - tc_0, 4)} s")

    return conn_ppi_db, result[0]

def make_input_vs_qind_db(filein, id_antenna, this_time, min_range_in_ppi, max_range_in_ppi, obs_nyquist, pathout, timeana=False):
    """
    Make a separate database for one PPI.

    This database is saved in memory and allows quick search of averaging boxes.

    Args:
    ----------------
    filein: str - Input SQLite file containing many radars and times.
    id_antenna: str - Radar for this one volume scan.
    this_time: datetime object - End time of this one volume scan.
    min_range_in_ppi: float - Minimum range in PPI.
    max_range_in_ppi: float - Maximum range in PPI.
    obs_nyquist: float - Nyquist for QC.
    pathout: str - Output directory where SQLite files are stored.
    timeana: bool, optional - Flag to enable time analysis. Default is False.

    Returns:
    ----------------
    conn_vs_db : sqlite3.Connection - SQLite connection to the created database.
    result : tuple - Result containing the count of data in the database.
    """
    # Enable time analysis if requested
    if timeana:tc_0 = time.time()

    # Create a connection to the in-memory SQLite database
    conn_vs_db = sqlite3.connect(f"file:{id_antenna}_{this_time}?mode=memory&cache=shared", uri=True)

    # Set SQLite connection optimizations
    conn_vs_db.execute("PRAGMA journal_mode=OFF;")
    conn_vs_db.execute("PRAGMA synchronous=OFF;")
    conn_vs_db.execute("PRAGMA journal = off;")
    conn_vs_db.execute("PRAGMA temp_store = MEMORY;")
    conn_vs_db.execute("PRAGMA journal_mode = WAL")

    # Attach the main database to the in-memory database
    conn_vs_db.execute("ATTACH DATABASE ? AS db_all", (filein,))

    # Load extension blobint and generate_series
    load_extension_sqlite(conn_vs_db)

    # Time analysis for this part (if enabled)
    if timeana:print(f"Runtime e2: {round(time.time() - tc_0, 4)} s")

    # Create temporary table T_HEADER
    if timeana: tc_0 = time.time()
    order_sql = """
        CREATE TEMP TABLE T_HEADER AS
        WITH x AS (
            SELECT s.id_scan,
                   r.latitude AS lat,
                   r.longitude AS lon,
                   CAST(strftime('%Y%m%d', r.date_validite) AS INTEGER) AS date,
                   CAST(strftime('%H%M%S', r.date_validite) AS INTEGER) AS time,
                   id_stn,
                   location,
                   r.stn_elev AS ele,
                   CAST(strftime('%H%M%S', s.start_date) AS INTEGER) AS start_time,
                   CAST(strftime('%H%M%S', s.end_date) AS INTEGER) AS end_time,
                   s.rstart AS range_start,
                   s.rstart + (s.rscale * s.nbins) AS range_end,
                   s.rscale / 2 AS DELTA_RANGE,
                   s.nbins AS n_ranges,
                   s.elangle AS elevation_angle,
                   NI,
                   version
            FROM rapport r
            INNER JOIN scan s USING (id_rapport)
            WHERE time = ?
        )
        SELECT o.rowid AS id_obs,
               o.no_rayon,
               (o.stop_azimuth - o.start_azimuth) / 2 AS DELTA_AZM,
               (o.start_azimuth + o.stop_azimuth) / 2 AS center_azimuth,
               o.angle_elevation AS center_elevation,
               x.*
        FROM x
        INNER JOIN ObservationVRADH o USING (id_scan)
        -- ORDER BY id_obs
        ;"""
    conn_vs_db.execute(order_sql, (this_time,))
    # Time analysis for this part (if enabled)
    if timeana: print(f"Runtime e2: {round(time.time() - tc_0, 4)} s")

    # Create temporary table t_dataQIND
    if timeana: tc_0 = time.time()
    
    # Quality control for doppler data applying the following steps:
    # A) Baltrad Step:
    #    1. Apply the DR  QC for non-weather removal. QI=0.0 (QI Raw=1)
    #    2. Identification of large structures that intersects the radar beam (e.g. wind farms).QI=0.1
    #    3. Apply an speckle filter to remove isolated bins with doppler velocity. QI=0.2
    #    4. Remove bins with low reflectivity (low signal). QI=0.3
    variables = dealias_radar_variables()
    qind_step_6 = variables['qind_step_6']

    order_sql = """
        CREATE TEMP TABLE t_dataQIND AS
        SELECT
            scan.id_scan,
            obs.no_rayon,
            rstart + rscale/2 + rscale*(idx.value-1) AS bin,
            (obs.gain * blobint(obs.valeurs, idx.value)) + obs.offset AS obsvalue
        FROM
            ObservationQIND obs
        INNER JOIN
            scan scan USING (id_scan)
        JOIN
            generate_series(1, scan.nbins) idx
        WHERE
            blobint(obs.valeurs, idx.value) NOT IN (nodata, undetect)
            AND
            obs.id_scan IN (SELECT id_scan FROM t_header)
            AND
            obsvalue > ?;
        """
    conn_vs_db.execute(order_sql, (qind_step_6,))
    # Time analysis for this part (if enabled)
    if timeana: print(f"Runtime e3: {round(time.time() - tc_0, 4)} s")

    # Create temporary table t_data
    if timeana: tc_0 = time.time()

    order_sql = """
        CREATE TEMP TABLE t_data AS
        SELECT
            scan.id_scan,
            obs.no_rayon,
            rstart + rscale/2 + rscale*(idx.value-1) AS bin,
            (obs.gain * blobint(obs.valeurs, idx.value)) + obs.offset AS obsvalue
        FROM
            ObservationVRADH obs
        INNER JOIN
            scan scan USING (id_scan)
        JOIN
            generate_series(1, scan.nbins) idx
        WHERE
            blobint(obs.valeurs, idx.value) NOT IN (nodata, undetect)
            AND
            obs.id_scan IN (SELECT id_scan FROM t_header);
        """
    conn_vs_db.execute(order_sql)
    # Time analysis for this part (if enabled)
    if timeana:print(f"Runtime e4: {round(time.time() - tc_0, 4)} s")

    # Execute schema for the new database
    if timeana: tc_0 = time.time()
    load_and_execute_schema(conn_vs_db)
    # Time analysis for this part (if enabled)
    conn_vs_db.execute("DETACH DATABASE db_all")
    if timeana:print(f"Runtime e5: {round(time.time() - tc_0, 4)} s")

    if timeana: tc_0 = time.time()
    order_sql = """INSERT INTO data (   
                   ID_DATA,
                   ID_OBS,
                   RANGE,
                   vcoord,
                   VARNO,
                   OBSVALUE,
                   QUALITY_INDEX,
                   vcoord_type,
                   FLAG, 
                   OMA,
                   OMP,
                   OBS_ERROR,
                   FG_ERROR,
                   HALF_DELTA_AZIMUTH,
                   HALF_DELTA_RANGE,
                   NUMBER_OBS)
                 SELECT
                   d.rowid AS id_data,
                   h.id_obs,
                   d.bin AS RANGE,
                   null AS VCOORD,
                 
                   21014 AS varno,
                   d.obsvalue  AS obsvalue,
                   qind.obsvalue AS QUALITY_INDEX,
                   7007 AS vcoord_type,
                   NULL AS FLAG,
                   NULL AS OMA,
                   NULL AS OMP,
                   NULL AS OBS_ERROR,
                   NULL AS FG_ERROR,
                   h.DELTA_AZM,
                   h.DELTA_RANGE,
                   1 AS NUMBER_OBS
                 FROM       
                   t_dataQIND  qind 
                  INNER JOIN 
                   t_data   d   USING(id_scan, no_rayon, bin ) 
                 INNER JOIN 
                   t_header h   USING(id_scan, no_rayon);"""
    conn_vs_db.execute(order_sql)
    if timeana: print(f"Runtime e6:, {round(time.time()-tc_0,4)} , s")

    # Insert data into the header table
    if timeana:tc_0 = time.time()

    order_sql = """
        INSERT INTO header (ID_OBS, LAT, LON, CODTYP, DATE, TIME, ID_STN, LOCATION, ANTENNA_ALTITUDE, TIME_START,
                            TIME_END, RANGE_START, RANGE_END, CENTER_AZIMUTH, CENTER_ELEVATION, NOMINAL_PPI_ELEVATION,
                            NYQUIST)
        SELECT
            id_obs,
            lat,
            lon,
            163 AS codtyp,
            date,
            time,
            id_stn,
            location,
            ele AS ANTENNA_ALTITUDE,
            start_time AS TIME_START,
            end_time AS TIME_END,
            range_start AS RANGE_START,
            range_end AS RANGE_END,
            CENTER_AZIMUTH,
            CENTER_ELEVATION,
            elevation_angle AS NOMINAL_PPI_ELEVATION,
            NI AS NYQUIST
        FROM t_header
        WHERE id_obs IN (SELECT id_obs FROM data);
        """
    conn_vs_db.execute(order_sql)
    # Time analysis for this part (if enabled)
    if timeana:print(f"Runtime e7: {round(time.time() - tc_0, 4)} s")

    # Query the count of data in the database
    query = f"SELECT COUNT(*) FROM data;"
    c = conn_vs_db.cursor()
    c.execute(query)
    result = c.fetchone()

    # Commit and return the connection and the result
    conn_vs_db.commit()
    return conn_vs_db, result

def num_obs_in_ppi(conn_ppi_db, min_range_in_ppi, max_range_in_ppi):
    """
    Count the total number of observations in a specified range in a PPI scan.

    Parameters:
    ----------------
    conn_ppi_db : sqlite3.Connection - Connection to the SQLite database for the PPI scan.
    min_range_in_ppi : float - Minimum range in the PPI scan.
    max_range_in_ppi : float - Maximum range in the PPI scan.

    Returns:
    ----------------
    number_obs_ppi: int - Number of observations in the specified range in the PPI scan.

    """
    # SQL query to count the number of observations within the specified range in the PPI scan
    order_sql = """SELECT COUNT(*)
                   FROM data
                   WHERE range >= ?
                   AND range <= ?"""

    # Set row_factory to retrieve results as dictionaries
    conn_ppi_db.row_factory = sqlite3.Row
    cursor = conn_ppi_db.cursor()

    # Execute the SQL query with the provided range values
    cursor.execute(order_sql, (min_range_in_ppi, max_range_in_ppi))

    # Fetch the result and retrieve the number of observations
    result = cursor.fetchone()
    number_obs_ppi = result[0]

    return number_obs_ppi

def average_boxes(conn, id_obs, id_data, azimuth, half_delta_range_box, range_bin_centers, half_delta_azimuth_box, obs_percentage, nominal_ppi_elevation):
    """
    Average input data found in the specified range and azimuth "box" in a PPI scan.

    Parameters:
    ----------------
    conn    : sqlite3.Connection - Connection to the output file (and the attached PPI database).
    id_obs  : int - id_obs for this ray.
    id_data : int - id_data for this averaging box.
    azimuth : float - Center azimuth of the averaging box.
    half_delta_range_box : float - Half of the delta_range for this averaging box.
    range_bin_centers : float - Range center for this averaging box.
    half_delta_azimuth_box : float - Half of the azimuthal span of the averaging box.
    obs_percentage : float - Percentage of observations used in this average.
    nominal_ppi_elevation : float - Nominal elevation of the PPI scan.

    Returns:
    ----------------
    inumber_obs_box: int - Number of observations used in this average.
    sum_elevation: float - Sum of center elevations for this box.
    number_obs_percentage: float - Percentage of observations used in this average.
    """
    # Constants for azimuth-centered at zero
    AZIMUTH_CENTERED_AT_ZERO = 360.0
    HALF_DELTA_AZIMUTH_DEFAULT = 0.5
    HALF_DELTA_RANGE_DEFAULT = 125.0

    # Bounds of the box
    right_azimuth = azimuth + half_delta_azimuth_box
    left_azimuth = azimuth - half_delta_azimuth_box
    range_box_start = range_bin_centers - half_delta_range_box
    range_box_end = range_bin_centers + half_delta_range_box

    # Condition changes for azimuth centered at zero
    condition = "and"
    if left_azimuth < 0:
        left_azimuth = AZIMUTH_CENTERED_AT_ZERO - half_delta_azimuth_box
        condition = "or"

    # SQL query to get the number of observations, sum elevation, and number of observations for this box
    order_sql = """SELECT COUNT(*),
                          half_delta_azimuth,
                          half_delta_range,
                          SUM(center_elevation)
                   FROM db_ppi.data
                   NATURAL JOIN db_ppi.header
                   WHERE range >= ? 
                   AND range < ?
                   AND ROUND(nominal_ppi_elevation, 1) = ?
                   AND id_obs IN (
                     SELECT id_obs
                     FROM db_ppi.header
                     WHERE center_azimuth >= ? """ + condition + """ center_azimuth < ?
                   )"""

    cursor = conn.execute(order_sql, (range_box_start, range_box_end, nominal_ppi_elevation, left_azimuth, right_azimuth))
    result = cursor.fetchone()

    # Get the number of observations for this box, half delta azimuth, half delta range, and sum elevation
    number_obs_box = result[0]
    half_delta_azimuth = result[1]
    half_delta_range = result[2]
    sum_elevation = result[3]

    number_obs_percentage = 0.0
    if number_obs_box == 0:
        # No observations in the averaging box, we exit here
        return 0, 0.0, 0.0
    else:
        if half_delta_azimuth == 0:
            half_delta_azimuth = HALF_DELTA_AZIMUTH_DEFAULT
        if half_delta_range == 0:
            half_delta_range = HALF_DELTA_RANGE_DEFAULT

        number_obs_max = (half_delta_azimuth_box / half_delta_azimuth) * (half_delta_range_box / half_delta_range)
        if (100 * number_obs_box / number_obs_max) >= obs_percentage:
            # Write the found values of avg (obsvalue) (among others) in the box
            order_sql = """INSERT INTO data (
                            id_obs, 
                            range, 
                            obsvalue, 
                            half_delta_azimuth, 
                            half_delta_range, 
                            id_data, 
                            quality_index,
                            number_obs
                          ) 
                          SELECT
                            ?, ?,
                            AVG(obsvalue), 
                            ?, ?, ?,
                            AVG(quality_index), ?
                          FROM
                            db_ppi.data 
                          WHERE
                            range >= ? 
                            AND range < ? 
                            AND id_obs IN (
                              SELECT 
                                id_obs 
                              FROM 
                                db_ppi.header 
                              WHERE 
                                center_azimuth >= ? """ + condition + """ center_azimuth < ?
                            )"""

            conn.execute(order_sql, (id_obs, range_bin_centers, half_delta_azimuth_box, half_delta_range_box, id_data, number_obs_box, range_box_start, range_box_end, left_azimuth, right_azimuth,))
            number_obs_percentage = number_obs_box

    return number_obs_box, sum_elevation, number_obs_percentage

def create_header(conn, ray, avg_elevation, id_obs):
    """
    Create header entry in the database.

    Args:
    ----------------
    conn: sqlite3.Connection - Connection to the SQLite database file.
    ray: dict -  Data structure of the averaging ray.
    avg_elevation: float - Average elevation encountered along the averaging ray.
    d_obs: int - id_obs of the radar beam.

    Returns:
    ----------------
    None. Header entry is written in the output SQLite file.

    """
    # Get the first header in the PPI (as a sample)
    order_sql = "SELECT * FROM db_ppi.header"
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(order_sql)
    sample_header = cursor.fetchone()

    # Extract constant variables from the sample header
    id_antenna = sample_header['id_stn']
    location = sample_header['location']
    lat = sample_header['lat']
    lon = sample_header['lon']
    date = sample_header['date']
    time = sample_header['time']
    codtyp = sample_header['codtyp']
    antenna_altitude = sample_header['antenna_altitude']
    nyquist = sample_header['nyquist']
    nominal_ppi_elevation = sample_header['nominal_ppi_elevation']
    time_start = sample_header['time_start']
    time_end = sample_header['time_end']

    # Extract variables that depend on averaging parameters for this ray
    azimuth = ray['azimuth']
    range_start = ray['min_range_in_ppi']
    range_end = ray['max_range_in_ppi']

    # Variables that depend on the data that was averaged for this ray
    # avg_elevation, time_start, time_end

    # Insert new header entry into the database
    order_sql = """INSERT INTO header (
                      id_obs, id_stn, location, lat, lon, date, time, codtyp,
                      antenna_altitude, nyquist, nominal_ppi_elevation,
                      center_azimuth, range_start, range_end,
                      center_elevation, time_start, time_end)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    conn.execute(order_sql, (id_obs, id_antenna, location, lat, lon, date, time, codtyp,
                             antenna_altitude, nyquist, nominal_ppi_elevation, azimuth,
                             range_start, range_end, avg_elevation, time_start, time_end))
  
def create_index_tables_elevation_azimuth(conn):
    """Create index tables for elevation and azimuth in the SQLite file.

    Args:
    ----------------
    conn: sqlite3.Connection - Connection to the SQLite database file.

    Returns:
    ---------------- 
    None. Index tables are created in the SQLite file.

    """
    # Create an index table for the 'NOMINAL_PPI_ELEVATION' column in the 'header' table
    order_sql = """CREATE INDEX IF NOT EXISTS
                    NOMINAL_PPI_ELEVATIONS 
                  ON header (NOMINAL_PPI_ELEVATION);"""
    conn.execute(order_sql)

    # Create an index table for the 'CENTER_AZIMUTH' column in the 'header' table
    order_sql = """CREATE INDEX IF NOT EXISTS
                    CENTER_AZIMUTHS 
                  ON header (CENTER_AZIMUTH);"""
    conn.execute(order_sql)

def create_table(conn, assim_T0):
    # Create an index table for the 'id_data' column in the 'data' table

    order_sql = """create table rdb4_schema (schema varchar(9));"""
    conn.execute(order_sql)
    order_sql = """insert into rdb4_schema values ('radvel');"""
    conn.execute(order_sql)
    order_sql = """create table resume (date integer, time integer, run varchar(9));"""
    conn.execute(order_sql)
    order_sql = f"insert into resume values ('{assim_T0.strftime('%Y%m%d%H')[0:8]}','{assim_T0.strftime('%Y%m%d%H')[8:10]}','G2');"
    conn.execute(order_sql)
    conn.commit()






def create_index_tables_idobs_iddata(conn):
    """Create index tables for id_obs and id_data in the SQLite file.

    Args:
    ----------------
    conn: sqlite3.Connection - Connection to the SQLite database file.

    Returns:
    ----------------
    None. Index tables are created in the SQLite file.

    """
    # Create an index table for the 'id_obs' column in the 'header' table
    order_sql = """CREATE INDEX IF NOT EXISTS
                      idx1
                    ON header(id_obs);"""
    conn.execute(order_sql)

    # Create an index table for the 'id_obs' column in the 'data' table
    order_sql = """CREATE INDEX IF NOT EXISTS
                     idx2 
                   ON data(id_obs);"""
    conn.execute(order_sql)

    # Create an index table for the 'id_data' column in the 'data' table
    order_sql = """CREATE INDEX IF NOT EXISTS
                     idx3 
                   ON data(id_data);"""
    conn.execute(order_sql)
  
def create_info_midas_tables(filein, conn_pathfileout, n_rays, delta_range, ops_run_name, obs_percentage, obs_nyquist):
    """
    Create header entry. A header is created matching a bunch of entries in the data table.

    Parameters:
    ----------------
    filein: str - Input SQLite file with raw data.
    conn_pathfileout: sqlite3.Connection - Connection to the output SQLite file.
    n_rays: int - Number of rays.
    delta_range: float - Delta range of the boxes.
    ops_run_name: str - Name of the operational run.
    obs_percentage: float - Minimum percentage of observations per box to calculate average.
    obs_nyquist: float - Minimum Nyquist in ppi to calculate average.

    Returns:
    ----------------
    None
    (The function writes an info table entry in the output SQLite file.)
    """

    # Attach the input database file to access its info table
    conn_pathfileout.execute("""ATTACH DATABASE ? AS db_all""", (filein,))

    # Info table
    order_sql = """CREATE TABLE info( NAME, DESCRIPTION, UNIT );"""
    conn_pathfileout.execute(order_sql)
    order_sql = """ INSERT INTO info (
                     NAME, DESCRIPTION, UNIT) 
                   SELECT * 
                     FROM db_all.info """
    conn_pathfileout.execute(order_sql)

    order_sql = """ INSERT INTO info (
                     NAME, DESCRIPTION, UNIT) VALUES
                   (?,?,?)"""
    conn_pathfileout.execute(order_sql, ('Maximun nyquist', 'Maximum Nyquist permitted', obs_nyquist,))

    order_sql = """ INSERT INTO info (
                     NAME, DESCRIPTION, UNIT) VALUES
                   (?,?,?)"""
    conn_pathfileout.execute(order_sql, ('Minus percentage of observation in the box', 'Percentage of observation in the box to average', obs_percentage,))

    order_sql = """ UPDATE info SET DESCRIPTION = REPLACE(DESCRIPTION,'OFF','ON') WHERE name = 'SUPEROBBING';"""
    conn_pathfileout.execute(order_sql)
    order_sql = """ UPDATE info SET DESCRIPTION = ? WHERE name = 'SUPEROBBING_NUMBER_RAYS';"""
    conn_pathfileout.execute(order_sql, (n_rays,))
    order_sql = """ UPDATE info SET DESCRIPTION = ? WHERE name = 'SUPEROBBING_DELTA_RANGE';"""
    conn_pathfileout.execute(order_sql, (delta_range,))

    # Resume table
    order_sql = """CREATE TABLE resume(date INTEGER , time INTEGER , run VARCHAR(9));"""
    conn_pathfileout.execute(order_sql)
    YYYYMMDD = os.path.basename(filein)[:8]
    HH = os.path.basename(filein)[8:10]
    order_sql = """INSERT INTO resume VALUES(?,?,?);"""
    conn_pathfileout.execute(order_sql, (YYYYMMDD, HH, ops_run_name,))

    # rdb4_schema table
    order_sql = """CREATE TABLE rdb4_schema( schema VARCHAR(9) );"""
    conn_pathfileout.execute(order_sql)
    order_sql = """INSERT INTO rdb4_schema VALUES('radvel');"""
    conn_pathfileout.execute(order_sql)

    # Commit and detach the attached database
    conn_pathfileout.commit()
    conn_pathfileout.execute("DETACH DATABASE db_all")

def superobs(filein, 
             id_antenna,
             this_datetime, 
             ops_run_name, 
             obs_percentage,
             obs_nyquist, 
             pathout,   
             model_valid_date_list,
             assim_T0,
             assim_window_width,
             model_files_list, 
             model_data_dir,
             timeana=False):
             
    """Average a volume scan
    
    This function takes in raw measurements in an SQLite file and 
    creates an average volume scan based on the content of the provided 
    averaging structure.
  
    Args:
    ----------------
    filein: str - Input SQLite file with raw data
    id_antenna: str -  Name of the radar that generated the volume scan being processed
    this_datetime:  datetime - Valid date time of radar observation
    ops_run_name: str - Name of operational run
    obs_percentage: float - Minimum percentage of observations per box to calculate the average
    obs_nyquist: float - Minimum Nyquist velocity in PPI to calculate average
    pathout: str - Directory where the model data is stored in FST format.
    model_valid_date_list:  list - List of valid dates for the model
    assim_T0: Assimilation start time
    assim_window_width: Assimilation window width
    model_files_list:  list - List of model files
    model_data_dir: str - Directory containing model data
    timeana: (bool, optional) - Activation of time analysis, only the first PPI in a volume scan will be averaged.

    Returns:
    ----------------
    This function outputs nothing. However, the averaged data is put in a SQLite file with the same name as the original 
    but with the suffix "_superobs".
  
    """
    # Time the execution
    tc_total_0 = time.time()
    # Check if data with a Nyquist velocity greater than obs_nyquist exists in the original database
    order_sql = """SELECT DISTINCT elangle FROM scan WHERE NI > ? and elangle>0 and round(elangle,1) != 2.5 and round(elangle,1) != 3.5 and round(elangle,1) != 4.5;"""
    with sqlite3.connect(filein) as conn_loops:
       cursor = conn_loops.cursor()
       try:
          cursor.execute(order_sql, (obs_nyquist,))
       except sqlite3.Error as e:
           print("Error al conectarse a la base de datos: DAVID", filein)   
    result = cursor.fetchone()
    if not result:
       # If no data with the required Nyquist velocity is found, print the runtime and return
       print (f' {id_antenna} Runtime =, {round(time.time()-tc_total_0,2)}, Runtime schema=, 0, Runtime dealias=,0,')
       conn_loops.close
       return
    
    hhmiss_pad =  this_datetime.strftime('%H%M%S') 
    # No zeros on left but still 0 if 000000
    hhmiss_nopad = str(int(hhmiss_pad))
  
    # Figure out minimum and maximum ranges in averaged PPI
    file = open(f"{pathout}/pickle_files/averaging_template.pkl",'rb')
    ray_list = pickle.load(file)
    file.close()
    n_rays = len(ray_list)
    min_range_in_ppi = 1.e9
    max_range_in_ppi = 0. 
    for this_ray in ray_list:
        min_range_in_ppi = np.amin([this_ray['min_range_in_ppi'], min_range_in_ppi])
        max_range_in_ppi = np.amax([this_ray['max_range_in_ppi'], max_range_in_ppi])
  
    # Prepare file in memory
    file_to_join = f'{pathout}/sqlites_to_join/{os.path.basename(filein)}'
    conn_file_to_join = sqlite3.connect(file_to_join, uri=True)
    # Turn off journaling
    conn_file_to_join.execute("""PRAGMA journal_mode=OFF;""")
    # SQLite continues without syncing as soon as it has handed data off to the operating system
    conn_file_to_join.execute("""PRAGMA synchronous=OFF;""")
    conn_file_to_join.execute("""PRAGMA journal = off;""")
    conn_file_to_join.execute("""PRAGMA temp_store = MEMORY;""")
    load_and_execute_schema(conn_file_to_join)
    # Improve searches with index tables
    create_index_tables_idobs_iddata(conn_file_to_join)
    # Construct a new Generator with the default BitGenerator (PCG64).
    rng = np.random.default_rng()
    maxsize = sys.maxsize
    ids = rng.integers(maxsize, size=2)
    id_data = ids[0].tolist()
    id_obs = ids[1].tolist()
  
    tc_0 = time.time()
    conn_vs_db, nobs1 = make_input_vs_qind_db(filein, 
                                              id_antenna, 
                                              hhmiss_nopad, 
                                              min_range_in_ppi, 
                                              max_range_in_ppi,
                                              obs_nyquist,
                                              pathout,
                                              timeana)
    create_index_tables_idobs_iddata(conn_vs_db)
 
    if timeana: tc_0 = time.time()
    order_sql = """ SELECT 
                      distinct nominal_ppi_elevation 
                    FROM
                      header 
                    WHERE
                      nyquist >= ?
                    ORDER BY 
                      1;"""
    nominal_ppi_elevations = [np.round(elev[0], 4) for elev in conn_vs_db.execute(order_sql, (obs_nyquist,)).fetchall()]
    time_schema_obsd = time.time() - tc_0

    time_schema = 0
    time_dealias = 0
    for nominal_ppi_elevation in nominal_ppi_elevations:

        tc_0 = time.time()
        conn_ppi_db, nobs = make_input_ppi_db(filein, 
                                              id_antenna, 
                                              hhmiss_nopad, 
                                              nominal_ppi_elevation, 
                                              min_range_in_ppi, 
                                              max_range_in_ppi,
                                              pathout,
                                              timeana)

        create_index_tables_idobs_iddata(conn_ppi_db)
        create_index_tables_elevation_azimuth(conn_ppi_db)
                
        time_schema += time.time()-tc_0

        if nobs >0:
            tc_0 = time.time()
            make_dealias(this_datetime,
                         model_files_list, 
                         model_valid_date_list,
                         assim_T0,
                         assim_window_width,
                         conn_ppi_db,
                         filein,
                         id_antenna,
                         model_data_dir,
                         nominal_ppi_elevation,
                         pathout,
                         timeana)
            time_dealias += time.time() - tc_0
  
        # Temporarily attach PPI database to the output file
        conn_file_to_join.execute(f'ATTACH DATABASE "file:{id_antenna}_{hhmiss_nopad}_{round(nominal_ppi_elevation, 2)}?mode=memory&cache=shared" AS db_ppi') 

        # Iterate over rays of the averaged PPI
        number_obs_ppi = 0 
        for ray in ray_list:    
  
            # Variables that do not change for a given ray
            azimuth = ray['azimuth']
            half_delta_range = ray['half_delta_range']
  
            # Average boxes and write the result in the data table of the file_to_join db (Memory)
            sum_elev_ray = 0.
            number_obs_ray = 0.
            number_obs_ray_percentage = 0.
            for range_bin_center, half_delta_azimuth in zip(ray['range_bin_centers'], ray['half_delta_azimuth']):
                number_obs_box, sum_elev_box, number_obs_percentage = average_boxes(conn_file_to_join,
                                                                                    id_obs,
                                                                                    id_data,
                                                                                    azimuth, 
                                                                                    half_delta_range,
                                                                                    range_bin_center,                                                                                    half_delta_azimuth,
                                                                                    obs_percentage,
                                                                                    nominal_ppi_elevation)
                if number_obs_box > 0:
                    number_obs_ray += number_obs_box
  
                if number_obs_percentage > 0:
                    sum_elev_ray += sum_elev_box
                    id_data = (rng.integers(maxsize, size=1))[0].tolist()
                    number_obs_percentage += number_obs_percentage 
                    number_obs_ray_percentage += number_obs_box
            
            # If any data was found in the ray, create a header entry matching average bins
            # already entered in the data table
            if number_obs_ray_percentage > 0:
                avg_elevation = sum_elev_ray / number_obs_ray_percentage
                create_header(conn_file_to_join, 
                              ray, 
                              avg_elevation,
                              id_obs)
                id_obs  = (rng.integers(maxsize, size=1))[0].tolist()
            
            # Keep track of how many observations have been averaged in PPI
            number_obs_ppi += number_obs_ray
  
        # Test number of observations in the source PPI vs the number of observations used in averaging boxes
        number_obs_in_source_ppi = num_obs_in_ppi(conn_ppi_db, 
                                                  min_range_in_ppi, 
                                                  max_range_in_ppi)
        if (number_obs_ppi != number_obs_in_source_ppi): 
            raise RuntimeError(f""" {id_antenna} {this_datetime} number_obs_ppi = {number_obs_ppi} 
            number_obs_in_source_ppi = {number_obs_in_source_ppi}  Error: number of 
            observations in the source ppi is different from the number of obs used in average""")
        conn_file_to_join.commit() 
        conn_file_to_join.execute("DETACH DATABASE db_ppi")
        conn_ppi_db.close()
  
    # Update flag, varno, and vcoord_type
    conn_file_to_join.execute("UPDATE data SET flag=0, varno=21014, vcoord_type=7007")
    conn_file_to_join.commit() 
    # Close connection 
    conn_vs_db.close()
    conn_file_to_join.close()
    print (f' {id_antenna} Runtime =, {round(time.time()-tc_total_0,2)}, Runtime schema=,{round(time_schema_obsd,2)}, Runtime dealias=,{round(time_dealias,2)},')
       
def combine(pathfileout, infile):
    """
    Combine multiple sqlite files into a single sqlite file.

    Parameters:
    ----------------
    pathfileout: str - Output path and filename for the combined sqlite file.
    infile: str - Name of the input sqlite file to be combined.

    Output:
    ----------------
    None

    The function assumes that the 'pathfileout' sqlite file already has the
    necessary table structures in place to receive the combined data.

    """
    # Connect to the output averaging sqlite file
    conn_pathfileout = sqlite3.connect(pathfileout, uri=True, isolation_level=None, timeout=999)

    # Disable journaling to improve write performance
    conn_pathfileout.execute("""PRAGMA journal_mode=OFF;""")

    # Disable synchronous mode to improve write performance
    conn_pathfileout.execute("""PRAGMA synchronous=OFF;""")

    # Attach the 'infile' database to the 'pathfileout' database
    conn_pathfileout.execute("ATTACH DATABASE ? AS this_vsavg_db;", (infile,))

    # Insert the 'header' data from 'infile' into 'pathfileout'
    header_insert_sql = """INSERT INTO header
                           SELECT * FROM this_vsavg_db.header;"""
    conn_pathfileout.execute(header_insert_sql)

    # Insert the 'data' from 'infile' into 'pathfileout'
    data_insert_sql = """INSERT INTO data
                         SELECT * FROM this_vsavg_db.data;"""
    conn_pathfileout.execute(data_insert_sql)

    # Commit the changes to the 'pathfileout' database
    conn_pathfileout.commit()

    # Detach the 'infile' database from the 'pathfileout' database
    conn_pathfileout.execute("""DETACH DATABASE this_vsavg_db""")

def surrounding_model_files(scan_datetime,
                            model_files_list,
                            model_valid_date_list,
                            assim_T0=None,
                            assim_window_width=None):
    """
    Return the model files just before and just after a volume scan.
    Also, return the time difference between each file and volume scan time.

    Args:
    ----------------
    scan_datetime: datetime - Time of volume scan to be bracketed.
    model_files_list: list -List of model files to choose from.
    model_valid_date_list: list - Validity date for each file in model_files_list.
    assim_T0: (datetime, optional) - Time of assimilation. Default is None.
    assim_window_width: (float, optional)- Width of the assimilation window in hours.
                                          Default is None.

    Output:
    ----------------
    [file_before, file_after]: list - Names of the model files just before and after the volume scan.
    [dt_file_before, dt_file_after]:  list - Time differences (in seconds) between each model file and
                                            the volume scan time.

    Raises:
    ----------------
    ValueError: If model files do not bracket the volume scan time.

    """
    # Define the assimilation window if provided
    if assim_T0 is not None and assim_window_width is not None:
        assim_window_start = assim_T0 - datetime.timedelta(seconds=int(assim_window_width / 2. * 3600.))
        assim_window_end = assim_T0 + datetime.timedelta(seconds=int(assim_window_width / 2. * 3600.))
    else:
        # No limits on time
        assim_window_start = datetime.datetime(0, 0, 0, 0, 0)
        assim_window_end = datetime.datetime(3000, 0, 0, 0, 0)

    # Search for model files that bracket the volume scan time

    for ii, this_model_vdate in enumerate(model_valid_date_list):
        if ii + 1 == len(model_valid_date_list):
            raise ValueError('Model files do not bracket volume scan time')
        if assim_window_start <= this_model_vdate <= assim_window_end:
            dt_before = (scan_datetime - model_valid_date_list[ii])
            dt_before_seconds = dt_before.days * 24 * 3600 + dt_before.seconds
            dt_after = (scan_datetime - model_valid_date_list[ii + 1])
            dt_after_seconds = dt_after.days * 24 * 3600 + dt_after.seconds

            if dt_before_seconds >= 0. and dt_after_seconds <= 0.:
                break

    # Get the names of the model files before and after the volume scan time
    file_before = model_files_list[ii]
    file_after = model_files_list[ii + 1]

    # Return the model files and their corresponding time differences
    return [file_before, file_after], [dt_before_seconds, dt_after_seconds]

def collision_test(conn_pathfileout):
    """
    Check for collisions and verify that the id_obs from the header have an associated id_data in the data table.

    Args:
    ----------------
    conn_pathfileout: sqlite3.Connection - Connection to the output averaging sqlite file.

    Returns:
    ----------------
    None

    Raises:
    ----------------
    RuntimeError: If there is a collision with id_obs in the header or data tables.
                  If id_obs from the header is not associated properly with id_data in the data table.

    Description:
    ----------------
    This function performs a collision test on the provided output averaging sqlite file (conn_pathfileout).
    It checks for the uniqueness of id_obs and id_data in their respective tables and ensures that each
    id_obs in the header table has a corresponding id_data in the data table.

    The function first retrieves the counts of distinct id_obs and total id_obs from the header table.
    It then retrieves the counts of distinct id_obs, distinct id_data, and total id_data from the data table.

    The function compares the counts to check for any collisions or mismatches:
    - If the number of distinct id_obs in the header is not the same as in the data table, it raises a
      RuntimeError indicating that id_obs is not associated properly.
    - If the number of distinct id_obs in the header is not the same as the total count of id_obs in the header
      table, it raises a RuntimeError indicating that there is a collision with id_obs.
    - If the number of distinct id_data in the data table is not the same as the total count of id_data in the
      data table, it raises a RuntimeError indicating that there is a collision with id_data.

    If no collisions or mismatches are found, the function finishes successfully without any exceptions.

    """
    # Count distinct id_obs from the header table
    order_sql = """SELECT COUNT(DISTINCT id_obs) FROM header;"""
    cursor = conn_pathfileout.cursor()
    cursor.execute(order_sql)
    result = cursor.fetchone()
    distinct_id_obs_from_header = result[0]

    # Count total id_obs from the header table
    order_sql = """SELECT COUNT(id_obs) FROM header;"""
    cursor.execute(order_sql)
    result = cursor.fetchone()
    count_id_obs_from_header = result[0]

    # Count distinct id_obs from the data table
    order_sql = """SELECT COUNT(DISTINCT id_obs) FROM data;"""
    cursor.execute(order_sql)
    result = cursor.fetchone()
    distinct_id_obs_from_data = result[0]

    # Count distinct id_data from the data table
    order_sql = """SELECT COUNT(DISTINCT id_data) FROM data;"""
    cursor.execute(order_sql)
    result = cursor.fetchone()
    distinct_id_data_from_data = result[0]

    # Count total id_data from the data table
    order_sql = """SELECT COUNT(id_data) FROM data;"""
    cursor.execute(order_sql)
    result = cursor.fetchone()
    count_id_data_from_data = result[0]

    # Check for collisions and mismatches
    if distinct_id_obs_from_header != distinct_id_obs_from_data:
        raise RuntimeError("Error: id_obs is not associated properly")
    if distinct_id_obs_from_header != count_id_obs_from_header:
        raise RuntimeError("Error: id_obs is in collision")
    if distinct_id_data_from_data != count_id_data_from_data:
        raise RuntimeError("Error: id_data is in collision")

def extract_winds_from_fst(fst_file, valid_time):
    """
    Extract the rotated winds from a standard file.

    Args:
    ----------------
    fst_file: str - Standard file containing model output for a single time.
    valid_time: datetime - Validity date of data to read.

    Returns:
    ----------------
        dict: Dictionary with the following keys:
            'model_latitudes': Latitude values.
            'model_longitudes': Longitude values.
            'model_uuwe': West-east component of wind.
            'model_vvsn': South-north component of wind.
            'model_heights': Altitude of grid points.

    Description:
        This function reads wind data from a standard file (fst_file) at the given validity time (valid_time).
        The function extracts the model latitudes, longitudes, west-east (uuwe) component of wind,
        south-north (vvsn) component of wind, and altitude (heights) of grid points from the file.
        It then processes the data, including removing the diagnostic surface level and capping the model top
        at a maximum height to avoid saving unnecessary data.
        Finally, it returns a dictionary containing the extracted wind data along with other relevant information.
    """

    # Read wind data from std file
    wind_dict = fst_tools.get_data(file_name=fst_file,
                                   var_name="wind_vectors",
                                   datev=valid_time,
                                   latlon=True)

    # Extract wind components and vertical levels
    model_latitudes = wind_dict["lat"]
    model_longitudes = wind_dict["lon"]
    model_uuwe = wind_dict["uuwe"]  # west-east component of wind
    model_vvsn = wind_dict["vvsn"]  # south-north component of wind
    ip1_momentum = wind_dict["ip1_list"]  # list of momentum vertical levels

    # Get rid of diagnostic surface level
    # (this step should not be necessary for newer GEM outputs without diagnostic wind)
    model_uuwe = model_uuwe[:, :, 1:]
    model_vvsn = model_vvsn[:, :, 1:]
    ip1_momentum = ip1_momentum[1:]

    # Calculate altitude of grid points
    gz_dict = fst_tools.get_data(file_name=fst_file,
                                 var_name="GZ",
                                 ip1=ip1_momentum,
                                 datev=valid_time)
    model_heights = gz_dict["values"] * 10  # decameter to meters
    model_heights_average = model_heights.mean(axis=(0, 1))

    # Cap the model top at a maximum height to avoid saving unnecessary data
    MAX_HEIGHT = 20000  # Maximum height in meters
    max_z_index = np.where(model_heights_average > MAX_HEIGHT)[0][0]
    model_heights = model_heights[:, :, 0:max_z_index]
    model_uuwe = model_uuwe[:, :, 0:max_z_index]
    model_vvsn = model_vvsn[:, :, 0:max_z_index]

    # Adjust longitudes to be in the range [-180, 180]
    model_longitudes = ((model_longitudes + 180) % 360) - 180

    # Create a dictionary containing the extracted wind data and other relevant information
    model_dict = {'model_latitudes': model_latitudes,
                  'model_longitudes': model_longitudes,
                  'model_uuwe': model_uuwe,
                  'model_vvsn': model_vvsn,
                  'model_heights': model_heights}

    return model_dict

def make_process_dealiasing(ppi_radar,
                            model_velocity_interpolated,
                            elevation, 
                            infile,
                            this_datetime,
                            id_antenna,
                            timeana=False):
    """
    Calculate the dealiased velocity.

    Args:
    ----------------
    ppi_radar: dict - Dictionary with radar ppi information.
    model_velocity_interpolated: np.ndarray - Velocity model interpolated from floor and ceil velocity model.
    elevation: float - Elevation angle of the radar scan.
    infile: str - Input file name.
    this_datetime: datetime - Current datetime.
    id_antenna: str - Station name.
    timeana: (bool, optional) - Flag to enable timing analysis.

    Returns:
    ----------------
    ppi_obsvalue_dealiasing (np.ndarray): Dealiased velocity.

    Note:
        Quality control for doppler data applying the following steps:
        A) Baltrad Step:
        1. Apply the DR QC for non-weather removal. qind=0.0 (qind Raw=1)
        2. Identification of large structures that intersects the radar beam (e.g. wind farms).qind=0.1
        3. Apply a speckle filter to remove isolated bins with doppler velocity. qind=0.2
        4. Remove bins with low reflectivity (low signal). qind=0.3

        B) Radvelso Step
        5. Dealias velocity data. qind=0.4 for bins couldn't be dealiased.
        6. OmP noise filter. qind=0.5

        A qind=1 is assigned to good quality bins (weather) with dealiased velocities.
    """

    # Read constants for dealiasing from an external file (/radvelso/database/dealias_radar_variables.csv)
    variables = dealias_radar_variables()
    kernel_az = variables['kernel_az']          # Azimuthal kernel size for dealiasing
    kernel_r = variables['kernel_r']            # Range kernel size for dealiasing
    azimuth_valid_bins_ratio = variables['azimuth_valid_bins_ratio']  # Ratio to determine minimum valid bins in azimuth direction
    range_valid_bins_ratio = variables['range_valid_bins_ratio']      # Ratio to determine minimum valid bins in range direction
    filter_threshold = variables['filter_threshold']  # Threshold for dealiasing quality control
    dkernel_r = variables['dkernel_r']          # Range increment for dealiasing kernel
    betai = variables['betai']                  # Weighting parameter for dealiasing
    qind_step_5 = variables['qind_step_5']      # Quality control for doppler data
    qind_step_6 = variables['qind_step_6']      # Quality control for doppler data

    if timeana: t0 = time.time()
    # Dealias (Dealiasing object)
    _dealias = Dealias(ppi_radar['ppi_ranges'],
                       ppi_radar['ppi_azimuths'],
                       ppi_radar['ppi_elevation'], 
                       ppi_radar['ppi_velocity'].copy(),
                       ppi_radar['nyquist'])

    # Initialize the dealiasing process with the model_velocity_interpolated and beta parameter
    _dealias.initialize(model_velocity_interpolated, beta=betai)

    # Perform the dealiasing calculation
    _dealias.dealiase()

    if timeana: print(f"Runtime dea1 total {id_antenna}: {round(time.time()-t0,4)} s")

    if timeana:t0 = time.time()
    # Set Quality Control (QC) flag for pixels with no data (value = -9999)
    nodata_mask = np.where(ppi_radar['ppi_velocity'] == -9999.)

    # from  5. Dealias velocity data. qind=0.4 for bins couldn't be dealiased.
    ppi_radar['qind'][nodata_mask] = variables['qind_step_5']

    if timeana: print(f"Runtime dea2 total {id_antenna}: {round(time.time()-t0,4)} s")

    if timeana:t0 = time.time()
    # Calculate the dealiasing offset (difference between dealiased velocity and model_velocity_interpolated)
    OmP = _dealias.dealias_vel - model_velocity_interpolated

    # Set NaN values for pixels with no data
    OmP[nodata_mask] = np.nan

    if timeana:print(f"Runtime dea3 total {id_antenna}: {round(time.time()-t0,4)} s")

    if timeana:t0 = time.time()
    # Create a DataArray from OmP with dimensions ('rays', 'bins')
    da = xr.DataArray(data=OmP, dims=("rays", "bins"))

    # Determine the minimum number of valid bins required to perform dealiasing
    min_valid_bins = int(round(azimuth_valid_bins_ratio * kernel_az * (kernel_r + range_valid_bins_ratio)))

    if timeana: print(f"Runtime dea4 total {id_antenna}: {round(time.time()-t0,4)} s")

    if timeana: t0 = time.time()
    # Calculate the standard deviation of OmP using a rolling window
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        OmP_std = (
            da.rolling(
                rays=int(kernel_az),
                bins=int(kernel_r) + int(dkernel_r),
                center=True,
                min_periods=min_valid_bins,
            )
            .std(skipna=True)
            .values
        )

    # Set NaN values to 0 in OmP_std
    OmP_std[np.isnan(OmP_std)] = 0
    OmP_std[np.isnan(OmP)] = 0

    if timeana: print(f"Runtime dea5 total {id_antenna}: {round(time.time()-t0,4)} s")

    if timeana: t0 = time.time()
    # Apply quality control based on the standard deviation (OmP_std) and QC flag (ppi_qc)
    # Set the QC flag to 0.5 for pixels with high standard deviation and existing data (ppi_qc > 0.4)
    # from  6. OmP noise filter. qind=0.5 
    ppi_radar['qind'][(OmP_std > filter_threshold) & 
                        (ppi_radar['qind'] > variables['qind_step_5'])] = variables['qind_step_6']

    # Create a mask for pixels with qind <= 0.5 (Quality control for doppler data applying)
    mask_qc = np.where(ppi_radar['qind'] <= variables['qind_step_6'])

    # Create a copy of ppi_velocity to store the dealiased data
    ppi_obsvalue_dealiasing = ppi_radar['ppi_velocity'].copy()

    # Set -9999 values for pixels that do not meet the QC criteria
    ppi_obsvalue_dealiasing[mask_qc] = -9999.

    # Set NaN values to -9999
    ppi_obsvalue_dealiasing[np.isnan(ppi_obsvalue_dealiasing)] = -9999.

    if timeana: print(f"Runtime dea6 total {id_antenna}: {round(time.time()-t0,4)} s")

    return ppi_obsvalue_dealiasing

def index_from_latlon(grid_lats, grid_lons,lats, lons):

    """
    Given the arrays of latitudes and longitudes, calculates the nearest i, j indices in the model grid.

    Args:
    ----------------
    grid_lats (np.ndarray): Model latitudes grid.
    grid_lons (np.ndarray): Model longitudes grid.
    lats (np.ndarray): Array of latitudes.
    lons (np.ndarray): Array of longitudes.

    Returns:
    ----------------
    Union[Tuple[int, int], None]: The nearest i, j indices from (lat, lon) in the model grid, or None if no indices are found.

    """

    radar_lats = np.array([lats])
    radar_lons = np.array([lons])
    grid_shape = grid_lats.shape

    # Convert latlon to XYZ coords
    proj_ll = ccrs.Geodetic()
    geo_cent = proj_ll.as_geocentric()
    grid_xyz = geo_cent.transform_points(proj_ll, grid_lons.flatten(), grid_lats.flatten())
    radar_xyz = geo_cent.transform_points(proj_ll, radar_lons.flatten(), radar_lats.flatten())

    # Build KDTree from model grid
    kdtree = scipy.spatial.cKDTree(grid_xyz, balanced_tree=False)

    # Search nearest neighbor using the tree
    _, indices = kdtree.query(radar_xyz, k=1)
    for ii, index in enumerate(indices):
        nearest_i, nearest_j = np.unravel_index(index, grid_shape)
        return nearest_i, nearest_j

    return None  # If no indices are found, return None

def dict_constans():

    """"
    Get a dictionary containing constants used in radvelso.

    Returns:
    ----------------
    dictconstans: dict - Dictionary with the following constant:
        - 'approximate_radius_of_earth': Approximate radius of the Earth in meters.
    """

    dictconstans = {'approximate_radius_of_earth' : 6371007.1809}
    return dictconstans

def distance_between_two_points(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the distance between two points on the Earth's surface
    using their latitude and longitude coordinates.

    Args:
    ----------------
    lat1: loat - Latitude of the first observation.
    lon1: float - Longitude of the first observation.
    lat2: float - Latitude of the second observation.
    lon2:  float - Longitude of the second observation.

    Returns:
    ----------------
    distance2point: float - Distance between the two points in kilometers.
    """
    # approximate radius of the Earth in km
    radius_of_earth = radvelso.qcavg.dict_constans()['approximate_radius_of_earth']

    # Convert latitude and longitude to radians
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)

    # Calculate the differences in longitude and latitude
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Haversine formula to calculate distance
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    # Calculate the distance using the Earth's radius
    distance2point = radius_of_earth * c

    return distance2point

def clip_outputs_near_radar(model_dict, model_filename, i_radar, j_radar, model_resolution):
    """
    Clip a large grid of model outputs to keep only datapoints
    that are within a certain distance of a given radar.

    Args:
    ----------------
    model_dict: dict - Dictionary with all the information of the model.
    model_filename: str - Model file name.
    i_radar:int - i-pixel position of the radar.
    j_radar: int - j-pixel position of the radar.
    model_resolution: float - Estimation of model resolution.

    Returns:
    ----------------
    model_radar: dict - Dictionary with model information around the radar (~290 km).
    """

    model_latitudes  = model_dict['model_latitudes']
    model_longitudes = model_dict['model_longitudes']
    model_uuwe       = model_dict['model_uuwe']
    model_vvsn       = model_dict['model_vvsn']
    model_heights    = model_dict['model_heights']

    # Estimation of delta ij 290000 (an estimated value of maximum range considered)
    delta = int(290000 / model_resolution)

    # Clip horizontally
    clipped_heights    = model_heights[i_radar - delta:i_radar + delta, j_radar - delta:j_radar + delta, :]
    clipped_uuwe       = model_uuwe[i_radar - delta:i_radar + delta, j_radar - delta:j_radar + delta, :]
    clipped_vvsn       = model_vvsn[i_radar - delta:i_radar + delta, j_radar - delta:j_radar + delta, :]
    clipped_latitudes  = model_latitudes[i_radar - delta:i_radar + delta, j_radar - delta:j_radar + delta]
    clipped_longitudes = model_longitudes[i_radar - delta:i_radar + delta, j_radar - delta:j_radar + delta]

    clipped_dict = {
        'model_heights': clipped_heights,
        'model_uuwe': clipped_uuwe,
        'model_vvsn': clipped_vvsn,
        'model_latitudes': clipped_latitudes,
        'model_longitudes': clipped_longitudes
    }

    return clipped_dict

def model2ppi_linear( model_latitudes,
                      model_longitudes,
                      model_heights,
                      ppi_latitudes,
                      ppi_longitudes,
                      ppi_heights,
                      model_vars=None,
                      valid_mask=None):
    """
    Interpolate the model output into the PPI scan using bilinear interpolation.

    (Based on Dominik Jacques interpolation routine)

    Args:
    ----------------

    model_latitudes: array[lon,lat] Model latitudes in degrees.
    model_longitudes: array[lon,lat] Model longitudes in degrees.
    model_heights: array[lon,lat, level] Model height in meters ASL.
    ppi_latitudes: array[rays,bins] Radar bin latitudes in degrees.
    ppi_longitudes: array[rays,bins] Radar bin longitude in degrees.
    ppi_heights: array[rays,bins] Radar bin heights in meters ASL.
    model_vars: array[lon, lat, level] or list of arrays List of model data to interpolate. 
        Each element of the list corresponds to a different variable.
    invalid_mask: array[rays,bins] Mask indicating the invalid values in the PPI.
    
    Returns:
    ----------------
    model_vars_at_ppi: array[rays,bins] model data interpolated for ppi


    """

    if model_vars is None:
        raise ValueError("The list of model variables to interpolate cannot be emtpy.")

    if not isinstance(model_vars, (tuple, list)):
        model_vars = [model_vars]
    # IMPORTANT! Only locations with valid values are interpolated
    nrays, nbins = ppi_latitudes.shape
    nz = model_heights.shape[2]
    if valid_mask is None:
        valid = np.ones_like(ppi_latitudes, dtype=bool)
    else:
        valid = ~valid_mask

    # Define grids
    ppi_grid = np.stack((ppi_longitudes[valid], ppi_latitudes[valid]), axis=1)
    n_valid_ppi_points = ppi_grid.shape[0]
    model_grid = np.stack((model_longitudes.ravel(), model_latitudes.ravel()), axis=1)

    # 1. The model-> PPI interpolation is done by first interpolating each model level at the radar bins lats/lons (the PPI grid).
    # Then, we interpolate along the vertical at the bins hights.
    # This approach is faster than a 3D interpolation.

    def interpolate2D(data_values, input_grid):
        """Interpolate model data into the ppi grid."""
        interpolator = LinearNDInterpolator(input_grid, data_values.ravel())
        res = interpolator(ppi_grid)
        return res, interpolator.tri

    # [n_valid_ppi_points, nz]
    model_height_at_ppi = np.zeros((n_valid_ppi_points, nz)).copy()
    model_vars_at_ppi3D = [model_height_at_ppi.copy() for _ in model_vars]

    # Iterate over vertical levels and interpolate along the horizontal
    tri = model_grid
    for z in range(model_vars[0].shape[2]):
        model_height_at_ppi[:, z], tri = interpolate2D(model_heights[:, :, z], tri)
        for var_idx, var in enumerate(model_vars):
            model_vars_at_ppi3D[var_idx][:, z], tri = interpolate2D(
                var[:, :, z].ravel(), tri)

    # 2. Interpolate the data in the vertical
    z_diff = model_height_at_ppi - ppi_heights[valid][:, None]

    # Variables dimensions:
    # z_diff: [n_valid_ppi_points, nz]
    # model_height_at_ppi: [n_valid_ppi_points, nz]
    nan_diff = np.where(z_diff < 0.0, np.nan, z_diff)
    within_bounds = np.isfinite(nan_diff).any(axis=1)
    outside_bounds = ~within_bounds

    outside_bounds_2d_mask = np.zeros_like(valid)

    idx = np.arange(valid.size)
    idx = idx[valid.ravel()][outside_bounds]
    if len(idx) > 0:
        outside_bounds_2d_mask_flat = outside_bounds_2d_mask.reshape(-1)
        outside_bounds_2d_mask_flat[idx] = True

    nan_diff[outside_bounds] = 0

    k_just_above = np.nanargmin(nan_diff, axis=1)
    k_just_below = k_just_above - 1
    k_just_above[outside_bounds] = nz - 1
    k_just_below[outside_bounds] = nz - 2

    # points below model level
    too_low_inds = np.asarray(k_just_below < 0).nonzero()
    if len(too_low_inds[0]) >= 0:
        k_just_above[too_low_inds] = 1
        k_just_below[too_low_inds] = 0

    # k_just_below: [n_valid_ppi_points,]
    ii = np.arange(n_valid_ppi_points)

    vert_interp_weights = z_diff[ii, k_just_above] / (
        model_height_at_ppi[ii, k_just_above] - model_height_at_ppi[ii, k_just_below])

    def interp_vertically(data_in_3d):
        data_1d_interpolated = (
            vert_interp_weights * data_in_3d[ii, k_just_below]
            + (1.0 - vert_interp_weights) * data_in_3d[ii, k_just_above])

        data2d = np.zeros((nrays, nbins))
        data2d[valid] = data_1d_interpolated
        data2d[outside_bounds_2d_mask] = np.nan
        return data2d

    # Interpolate variables
    model_vars_at_ppi = tuple(interp_vertically(var) for var in model_vars_at_ppi3D)

    if len(model_vars_at_ppi) == 1:
        return model_vars_at_ppi[0]

    return model_vars_at_ppi

def model2ppi_interpolation(model_radar, ppi_radar, elevation):
    """
    Calculate the doppler velocity operator obtained from the interpolation of
    the ppi and the model.

    Args:
    ----------------
    model_radar (dict): Dictionary with model information about the radar model.
    ppi_radar (dict): Dictionary with radar ppi information.
    elevation (float): Elevation angle of the radar scan.

    Returns:
    ----------------
    model_velocity (np.ndarray): Velocity model from the ppi-related model.
    """

    data_mask = np.logical_not(ppi_radar['ppi_velocity'] != -9999.)

    # Interpolate model UU and VV to PPI grid
    model_uuvv = model2ppi_linear(model_radar['model_latitudes'],
                                  model_radar['model_longitudes'],
                                  model_radar['model_heights'],
                                  ppi_radar['ppi_latitudes'],
                                  ppi_radar['ppi_longitudes'],
                                  ppi_radar['ppi_heights'],
                                  model_vars=[model_radar['model_uuwe'], model_radar['model_vvsn']],
                                  valid_mask=data_mask)

    model_uuInterpolate = model_uuvv[0]
    model_vvInterpolate = model_uuvv[1]

    dim1 = len(ppi_radar['ppi_heights'])
    dim2 = len(ppi_radar['ppi_heights'][0])
    ppi_azimuths = np.broadcast_to(ppi_radar['ppi_azimuths'][:, np.newaxis], (dim1, dim2))

    # Doppler velocity is the projection of wind along the direction of the radar beam
    # Positive values indicate velocities "away" from the radar
    model_velocity = (model_uuInterpolate * np.sin(np.radians(ppi_azimuths)) +
                      model_vvInterpolate * np.cos(np.radians(ppi_azimuths))) * np.cos(np.radians(elevation))

    return model_velocity

def get_model_velocity_interpolated(this_vol_scan_time, id_antenna, model_files_list, model_valid_date_list,
                                    assim_T0, assim_window_width, ppi_radar, pathoutpkl, elevation, timeana=False):
    """
    Given a floor model and a ceil model, linear interpolation for a time between them.

    Args:
    ----------------
    this_vol_scan_time (datetime): Time of the radar volume scan.
    id_antenna (str): Radar name.
    model_files_list (list): List of model file names.
    model_valid_date_list (list): List of valid dates for model files.
    assim_T0 (int): Assimilation window center (in seconds).
    assim_window_width (int): Assimilation window width (in seconds).
    ppi_radar (dict): Dictionary with ppi information.
    pathoutpkl (str): Path to the pickle files.
    elevation (float): Elevation angle of the radar scan.
    timeana (bool, optional): Flag to enable timing analysis.

    Returns:
    ----------------
    model_velocity_interpolated (np.ndarray): Velocity model interpolated from floor and ceil velocity model.
    """

    if timeana: tc_0 = time.time()
    hhmiss_pad = this_vol_scan_time.strftime('%H%M%S')

    # Get files before and after the current radar volume scan time
    files_before_after, dt_before_after = surrounding_model_files(this_vol_scan_time,
                                                                  model_files_list,
                                                                  model_valid_date_list,
                                                                  assim_T0,
                                                                  assim_window_width)

    # Load floor and ceil model radar data from pickle files
    file = open(f"{pathoutpkl}/pickle_files/wind_radar_{os.path.basename(files_before_after[0])}_{hhmiss_pad}_{id_antenna}.pkl", 'rb')
    model_radar_floor = pickle.load(file)
    file.close()

    file = open(f"{pathoutpkl}/pickle_files/wind_radar_{os.path.basename(files_before_after[1])}_{hhmiss_pad}_{id_antenna}.pkl", 'rb')
    model_radar_ceil = pickle.load(file)
    file.close()

    if timeana: print(f"Runtime inter1 total {id_antenna}:, {round(time.time()-tc_0, 4)}, s")

    if timeana: tc_0 = time.time()
    dt = dt_before_after[0]
    model_velocity_floor = model2ppi_interpolation(model_radar_floor, ppi_radar, elevation)
    model_velocity_ceil = model2ppi_interpolation(model_radar_ceil, ppi_radar, elevation)
    tc_1 = time.time()

    if timeana: print(f"Runtime inter2 total {id_antenna}:, {round(tc_1-tc_0, 4)}, s")

    if timeana: tc_0 = time.time()
    t_floor = 0.
    t_ceil = 900  # seconds
    Diff = model_velocity_ceil - model_velocity_floor
    model_velocity_interpolated = model_velocity_floor + Diff * ((dt) / (t_ceil - t_floor))

    # Convert nan values to -9999
    nodata_mask = np.where(ppi_radar['ppi_velocity'] == -9999.)
    model_velocity_interpolated[nodata_mask] = -9999.


    if timeana:print(f"Runtime intera3 total {id_antenna}:, {round(time.time()-tc_0, 4)} ,s")

    return model_velocity_interpolated

def get_ppi(conn,  id_antenna, timeana=False):
    """
    Fetch radar PPI information from the memory connection.

    Args:
    ----------------
    conn: sqlite3.Connection - Connection to the PPI information.
    id_antenna: str - tation name.
    timeana (bool, optional): Flag to enable timing analysis.

    Returns:
    ----------------
    ppi_radar: dict - Dictionary with radar PPI information.
    """

    if timeana: tc_0 = time.time()

    cursor = conn.cursor()

    # Get header information for the radar PPI scan
    order_sql = '''select
                     center_elevation,
                     lat,
                     lon,
                     antenna_altitude,
                     nyquist,
                     half_delta_range,
                     range_start,
                     range_end
                   from
                     header
                     join data on header.id_obs=data.id_obs ;'''

    result_header = cursor.execute(order_sql).fetchone()
    elevation = result_header[0]
    radar_lat = result_header[1]
    radar_lon = result_header[2]
    hrad = result_header[3]
    nyquist = result_header[4]
    half_delta_range = result_header[5]
    range_start = result_header[6]
    range_end = result_header[7]

    if timeana: getppi1 = round(time.time() - tc_0, 4)  #(f"Runtime getppi1 {id_antenna}:, {round(time.time()-tc_0,4)}, s")

    if timeana: tc_0 = time.time()
    # Get data information for the radar PPI scan
    order_sql = '''select
                     range,
                     obsvalue,
                     center_azimuth,
                     id_data,
                     quality_index
                   from
                     data
                     join header ON data.id_obs = header.id_obs;'''

    result_data = cursor.execute(order_sql).fetchall()

    if timeana: getppi2 = round(time.time() - tc_0, 2)  #print(f"Runtime getppi2 {id_antenna}:, {round(time.time()-tc_0,4)} ,s")

    if timeana: tc_0 = time.time()
    # Extract data from the query results
    ranges = np.fromiter((row[0] for row in result_data), dtype=float)
    obsvalues = np.fromiter((row[1] for row in result_data), dtype=float)
    azimuths = np.fromiter((row[2] for row in result_data), dtype=float)
    id_datas = np.fromiter((row[3] for row in result_data), dtype=int)
    qinds = np.fromiter((row[4] for row in result_data), dtype=float)
    no_data = -9999.
    delta_azimuth = 0.5
    azimuth_arr = np.arange(0., 360., delta_azimuth) + delta_azimuth / 2.
    n_azimuths = azimuth_arr.size

    delta_r = int(2 * half_delta_range)
    min_range = range_start
    max_range = range_end

    range_bounds_arr = np.arange(min_range, max_range + delta_r, delta_r)
    range_bin_arr = range_bounds_arr[0:-1] + (range_bounds_arr[1:] - range_bounds_arr[0:-1]) / 2
    n_range_bins = range_bin_arr.size

    ppi_velocity = np.full((n_azimuths, n_range_bins), no_data)
    ppi_heights = np.full((n_azimuths, n_range_bins), no_data)
    ppi_latitudes = np.full((n_azimuths, n_range_bins), no_data)
    ppi_longitudes = np.full((n_azimuths, n_range_bins), no_data)
    ppi_qind = np.full((n_azimuths, n_range_bins), no_data)
    ppi_id_data = np.full((n_azimuths, n_range_bins), no_data)
    ppi_ranges = np.full((n_range_bins), no_data)
    ppi_azimuths = np.full((n_azimuths), no_data)
    ppi_elevation = np.full((n_azimuths, n_range_bins), no_data)
    ppi_qind = np.full((n_azimuths, n_range_bins), 1)

    if timeana: getppi3 = round(time.time() - tc_0, 2)  # print(f"Runtime getppi2 {id_antenna}:, {round(time.time()-tc_0,4)} ,s")

    if timeana: tc_0 = time.time()
    # Calculate latitude, longitude, and height values for each data point
    dist_earth = radar_tools.model_43(elev=elevation, dist_beam=ranges / 1e3, hrad=hrad / 1e3, want='dist_earth')
    obsvalue_longitudes, obsvalue_latitudes = geo_tools.lat_lon_range_az(radar_lon, radar_lat, dist_earth, azimuths)
    obsvalue_heights = radar_tools.model_43(elev=elevation, dist_beam=ranges / 1e3, hrad=hrad / 1e3, want='height')

    if timeana:getppi4 = round(time.time() - tc_0, 2)   #print(f"Runtime average 3 {id_antenna}:, {round(time.time()-tc_0,4)} ,s")

    # Determine the indices of azimuths and ranges to place the data in the ppi arrays
    ind_range = np.where(ranges <= range_bin_arr[-1], np.searchsorted(range_bin_arr, ranges), len(range_bin_arr) - 1)
    ind_azimuth = np.where(azimuths <= azimuth_arr[-1], np.searchsorted(azimuth_arr, azimuths), len(azimuth_arr) - 1)

    # Populate the ppi arrays with the data
    ppi_velocity[ind_azimuth, ind_range] = obsvalues
    ppi_heights[ind_azimuth, ind_range] = obsvalue_heights
    ppi_longitudes[ind_azimuth, ind_range] = obsvalue_longitudes
    ppi_latitudes[ind_azimuth, ind_range] = obsvalue_latitudes
    ppi_qind[ind_azimuth, ind_range] = qinds
    ppi_id_data[ind_azimuth, ind_range] = id_datas
    ppi_ranges[ind_range] = ranges
    ppi_azimuths[ind_azimuth] = azimuths
    ppi_elevation[ind_azimuth, ind_range] = round(elevation, 2)

    ppi_radar = {
        'ppi_azimuths': ppi_azimuths,
        'ppi_velocity': ppi_velocity,
        'ppi_heights': ppi_heights,
        'ppi_longitudes': ppi_longitudes,
        'ppi_latitudes': ppi_latitudes,
        'ppi_azimuths': ppi_azimuths,
        'ppi_ranges': ppi_ranges,
        'ppi_elevation': ppi_elevation,
        'radar_lat': radar_lat,
        'radar_lon': radar_lon,
        'nyquist': nyquist,
        'qind':  ppi_qind,
        'id_data': ppi_id_data
    }

    if timeana: print(f' {id_antenna} Runtime getppi1=, {getppi1}, getppi2=, {getppi2}, getppi3=, {getppi3}, getppi4=, {getppi4}, getppi5=, {round(time.time() - tc_0, 2)}')

    return ppi_radar

def dealias_radar_variables():
    """
    Read variables related to dealiasing from a text file and return them as a dictionary.

    Args:
    ----------------

    Returns:
    ----------------
        dict: A dictionary containing the extracted variables related to dealiasing.

    """
    #full path of radvelso module
    radvelso_dir = os.path.dirname(radvelso.__file__)
    #root path of radvelso package (one dir up from radvelso module)
    package_dir = os.path.dirname(radvelso_dir)
    #full path to extension
    filename = f'{package_dir}/radvelso/database/dealias_radar_variables.csv'

    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read the content of the file
        content = file.read()

    # Split the content into words
    words = content.split()

    # Create a dictionary to store the variables
    variables = {}

    # Iterate through the words and extract the variables
    for word in words:
        # Separate the variable name and its value
        name, value = word.split('=')
        # Convert the value to an integer
        value = float(value)
        # Add the variable to the dictionary
        variables[name] = value

    # Return the dictionary containing the variables
    return variables
  
def flag_for_dealisaing(conn_filememory, id_data):

    """ delete observation from memory due to dealias
    
    Args:
    ----------------

    conn_filememory: connection of memory  with ppi infromation
    id_data: id_data of observation

    Returns:
    ----------------

    Nothing, observation deleted from memory to calcula averaged

    """
    order_sql = """delete from data where ID_DATA = ?;"""
    conn_filememory.execute(order_sql,(int(id_data),)) 

def make_dealias(this_datetime,
                 model_files_list, 
                 model_valid_date_list,
                 assim_T0,
                 assim_window_width,
                 conn_ppi_db,
                 infile,
                 id_antenna,
                 model_data_dir,
                 elevation,
                 pathoutpkl,
                 timeana=True):
    """
    Determine observations that will not be taken into account in the average according to dealias.

    Args:
    ----------------
    this_datetime: datetime - Date of the PPI scan.
    model_files_list:list -List of model files.
    model_valid_date_list: list - List of model valid dates.
    assim_T0: datetime - Center time of the assimilation window.
    assim_window_width: float - Width of the assimilation window in hours.
    conn_ppi_db: sqlite3.Connection - Connection to the PPI information.
    infile: str - Path to the input SQLite file.
    id_antenna: str - Name of the radar.
    model_data_dir: str - Directory where the model data is stored in fst format.
    elevation: float - Elevation of the PPI.
    pathoutpkl: str - Path to output pickle files.
    timeana: (bool, optional) -  Flag to enable timing analysis.

    Returns:
    ----------------
    - None: Determines observations as not assimilable.
    """

    if timeana: t0 = time.time()  # Start the timer

    # Get PPI radar information from the memory database
    ppi_radar = get_ppi(conn_ppi_db, id_antenna, False)

    if timeana: getmodel_total = time.time() - t0  # Time taken to get model information

    if timeana: t0 = time.time()

    # Get interpolated model velocity
    model_velocity_interpolated = get_model_velocity_interpolated(this_datetime,
                                                                  id_antenna,
                                                                  model_files_list, 
                                                                  model_valid_date_list,
                                                                  assim_T0,
                                                                  assim_window_width,
                                                                  ppi_radar,
                                                                  pathoutpkl,
                                                                  elevation,
                                                                  timeana)

    if timeana: inter_total = time.time() - t0  # Time taken for model interpolation

    if timeana: t0 = time.time()

    # Calculate non-assimilable observations according to dealiasing
    ppi_obsvalue_dealiasing = make_process_dealiasing(ppi_radar,
                                                      model_velocity_interpolated, 
                                                      elevation, 
                                                      infile,
                                                      this_datetime, 
                                                      id_antenna, 
                                                      timeana)

    if timeana: dea_total = time.time() - t0  # Time taken for the dealiasing process

    if timeana: t0 = time.time()

    # Mark non-assimilable observations in the database
    flag_index = np.where(ppi_obsvalue_dealiasing != ppi_radar['ppi_velocity'])
    if np.any(flag_index):
        for obs in ppi_radar['id_data'][flag_index]:
            flag_for_dealisaing(conn_ppi_db, obs)
        conn_ppi_db.commit()

    if timeana: flag_total = time.time() - t0  # Time taken to mark non-assimilable observations

    if timeana:
        print(f'{id_antenna} Rutime getmodel_total= {round(getmodel_total, 2)}, inter_total= {round(inter_total, 2)}, dea_total= {round(dea_total, 2)}, flag_total= {round(flag_total, 2)}')

def get_model_resolution(wind_dict, latitude, longitude):

    """given a standard model file estimation of the resolution at a point defined by lat and lon

    Args:
    ----------------
 
    model_latitudes:Array[n,m] of lotitudes from model
    model_longitudes:Array[n,m] of latitudes from model
    latitude: value of latitude
    longitude: value of longitude 


    Returns:
    ----------------
   
    model_resolution
    i_model_for_radar: i of model grid
    j_model_for_radar: j of model grid
    
    """
    model_latitudes  = wind_dict['model_latitudes']
    model_longitudes = wind_dict['model_longitudes']
    i_model_for_radar, j_model_for_radar = index_from_latlon(model_latitudes, 
                                                             model_longitudes,
                                                             latitude, 
                                                             longitude)
    model_resolution = distance_between_two_points(model_latitudes[i_model_for_radar,  j_model_for_radar], 
                                                   model_longitudes[i_model_for_radar, j_model_for_radar], 
                                                   model_latitudes[i_model_for_radar,  j_model_for_radar+1], 
                                                   model_longitudes[i_model_for_radar, j_model_for_radar+1])
   
    return model_resolution, i_model_for_radar, j_model_for_radar                                    
 
def save_pkl (name, tosave): 
 
    """ save a dictionary in a pickle file
    
    Args:
    ----------------
    name: str - name of file to save
    tosave: Array to save

    Returns:
    ----------------
    nothing one file information to save

    """

    if os.path.exists(name):
        os.remove(name)
    f = open(name,"wb")
    # write the python object (dict) to pickle file
    pickle.dump( tosave, f)
    # close file
    f.close()

def get_date_from_filename(this_file, 
                           kind):
    """Compute validity date from a filename

    Args:
    ----------------
    this_file: name of file to parse
    kind:      what kind of file ar we dealing with

    Returns:
    ----------------

    valid_date

    """
    file_bname = os.path.basename(this_file)
    if kind == 'G1':
        fcst_T0_date = datetime.datetime.strptime(file_bname[0:10], '%Y%m%d%H')
        minutes = int(file_bname[11:14])
        valid_date = fcst_T0_date + datetime.timedelta(seconds=minutes*60)

    elif kind == 'pickles':
       #write code here to get date from pickle name
       pass

    else:
        raise ValueError(f'Dont know what to do with kind={kind}')

    return valid_date

def savepkl_for_radardomain(id_antenna, 
                            vol_scan_datetime_list,
                            sqlite_file,
                            model_files_list,
                            model_valid_date_list,
                            assim_T0,
                            assim_window_width,
                            ops_run_name,
                            pathout,
                            obs_nyquist):
    """
    Save a dictionary with model winds to interpolate for the radar in a pickle file.

    Args:
    ----------------
    id_antenna: str - Radar name.
    vol_scan_datetime_list: list - List of datetimes of each volume scan.
    sqlite_file: str - Path to the SQLite file.
    model_files_list: list - List of model files.
    model_valid_date_list: list - List of model valid dates.
    assim_T0: datetime - Central time of the assimilation window.
    assim_window_width: float - Width of the assimilation window.
    ops_run_name: str -Name of the operational run.
    pathout: str - Path to work.
    obs_nyquist: float - Minimum Nyquist velocity for observations.

    Returns:
    ----------------
    None: Saves one pickle file for the radar with model winds.
    """

    # Extract winds around the radar and save them to pickle files
    model_resolution = None
    this_vol_scan_time = vol_scan_datetime_list
    hhmiss_nopad = this_vol_scan_time.strftime('%H%M%S') 

    # No zeros on the left, but still 0 if 000000
    # hhmiss_nopad = str(int(hhmiss_pad))
    this_radar_lat, this_radar_lon  = search_id_antenna_and_update(sqlite_file, id_antenna)
   
    order_sql = """SELECT DISTINCT
                   elangle
              FROM scan
              WHERE NI > ?;"""
    print ('DAMA',sqlite_file)
    with sqlite3.connect(sqlite_file) as conn_loops:
       cursor = conn_loops.cursor()
       try :
          cursor.execute(order_sql, (obs_nyquist,))
       except sqlite3.Error as e:
         print("Error al conectarse a la base de datos DAVID:",sqlite_file)   
    result = cursor.fetchone()
    if not result:
       # If there are no results, skip the dealiasing
       conn_loops.close
       return

    files_before_after, dt_before_after = surrounding_model_files(this_vol_scan_time, 
                                                                  model_files_list, 
                                                                  model_valid_date_list,
                                                                  assim_T0,
                                                                  assim_window_width)

    for this_model_file in files_before_after:
        if os.path.exists(f"{pathout}/pickle_files/wind_radar_{id_antenna}_{hhmiss_nopad}_{os.path.basename(this_model_file)}.pkl"):
             continue
        else:
            model_filename = os.path.basename(this_model_file)
            valid_time = model_valid_date_list[model_files_list.index(this_model_file)]
            file = open(f"{pathout}/pickle_files/wind_fulldomain_{model_filename}.pkl", 'rb')
            wind_dict_fulldomain = pickle.load(file)
            file.close()

            if model_resolution is None:
                (model_resolution, 
                i_model_for_radar, 
                j_model_for_radar) = get_model_resolution(wind_dict_fulldomain,  
                                                          this_radar_lat,
                                                          this_radar_lon)

            wind_dict_radardomain = clip_outputs_near_radar(wind_dict_fulldomain,
                                                            model_filename,
                                                            i_model_for_radar,
                                                            j_model_for_radar,
                                                            model_resolution)

            save_pkl(f"{pathout}/pickle_files/wind_radar_{os.path.basename(this_model_file)}_{hhmiss_nopad}_{id_antenna}.pkl", wind_dict_radardomain)

def savepkl_for_fulldomain(this_model_file, model_files_list, model_valid_date_list, pathout):
    """
    Save a dictionary with model winds to interpolate for the radar in a pickle file.

    Parameters:
    ----------------
    this_model_file: str - Path to the current model file.
    model_files_list: list - List of model file paths.
    model_valid_date_list: list - List of validity dates corresponding to the model files.
    pathout: str - Output directory for saving pickle files.

    Returns:
    ----------------
    None
    (The function saves a pickle file containing model winds.)
    """
    print(f"Extract model file: {os.path.basename(this_model_file)}")
    
    # Get the validity time of the current model file
    valid_time = model_valid_date_list[model_files_list.index(this_model_file)]
    
    # Extract model winds from the current model file
    wind_to_save = extract_winds_from_fst(this_model_file, valid_time)
    
    # Save the extracted model winds as a pickle file in the specified output directory
    save_pkl(f"{pathout}/pickle_files/wind_fulldomain_{os.path.basename(this_model_file)}.pkl", wind_to_save)

def get_model_valid_date_list(assim_T0, assim_window_width, ops_run_name, model_files_search_pattern, model_outputs_for_dealiasing):
    """
    Make a list of available model files and their validity dates.

    Args:
    ----------------
    assim_T0: datetime - Center time of the assimilation window.
    assim_window_width: float - Width of the assimilation window in hours.
    ops_run_name: str - Name of the operational run.
    model_files_search_pattern: str - Search pattern for model files.
    model_outputs_for_dealiasing: str - Path containing model output files.

    Returns:
    ----------------
    model_files_list: list - A list of model file paths.
    model_valid_date_list: list - A list of validity dates corresponding to the model files.
    """
    # Calculate the trial_T0 based on assim_T0 and assim_window_width
    trial_T0 = assim_T0 - datetime.timedelta(seconds=assim_window_width * 3600)
    
    # Construct the search pattern using the trial_T0 and model_files_search_pattern
    search_pattern = os.path.join(model_outputs_for_dealiasing, trial_T0.strftime(model_files_search_pattern))
    print ('david',model_outputs_for_dealiasing, trial_T0.strftime(model_files_search_pattern))
    # Find model files based on the search pattern and filter out certain file endings
    model_files_list = sorted(glob.glob(search_pattern))
    print ('david',model_files_list)
    model_files_list = [filterf for filterf in model_files_list if not filterf.endswith(('000', '000m', '060m', '120m'))]

    if len(model_files_list) == 0:
        raise RuntimeError(f'No model files found for criterion: {search_pattern}')
    
    # Get validity dates from the model file names using the ops_run_name
    model_valid_date_list = [get_date_from_filename(this_file, ops_run_name) for this_file in model_files_list]

    return model_files_list, model_valid_date_list

def extract_lat_lon_from_header(sqlite_file, csv_output_file):

    """
    Extracts 'lat' and 'lon' data from the 'header' table in a SQLite file and saves it to a CSV file.

    Args:
    ----------------
    sqlite_file: str - The name of the SQLite file.
    csv_output_file: str - The name of the CSV file where the data will be saved.

    Returns:
    ----------------
    None (The function writes the 'lat' and 'lon' data to the CSV file.)
    """

    import csv
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(sqlite_file)
        cursor = conn.cursor()

        # Query to fetch 'lat' and 'lon' columns from the 'header' table
        query = "SELECT id_stn, latitude, longitude FROM rapport;"

        # Execute the query
        cursor.execute(query)

        # Fetch one row of results (unique 'lat' and 'lon' values)
        id_antenna_lat_lon = cursor.fetchone()

        # Close the database connection
        cursor.close()
        conn.close() 

        #full path of radvelso module
        radvelso_dir = os.path.dirname(radvelso.__file__)
        #root path of radvelso package (one dir up from radvelso module)
        package_dir = os.path.dirname(radvelso_dir)
        #full path to extension
        path_to_file = f'{package_dir}/radvelso/database/'

         
        # Check if the CSV file already exists
        csv_file_exists = os.path.isfile(f'{path_to_file}/radar_lat_lon.csv')

        # Append the data to the existing CSV file
        with open(csv_output_file, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Write the data to the CSV file
            csv_writer.writerow(id_antenna_lat_lon)

        print("Data has been extracted and added to", csv_output_file)
        return id_antenna_lat_lon[1], id_antenna_lat_lon[2]
    except Exception as e:
        print("Error processing the data:", e)

def search_id_antenna_and_update(sqlite_file, id_antenna):
    """
    Searches for 'id_antenna' in the CSV file. If found, returns the corresponding 'lat' and 'lon' values.
    If 'id_antenna' is not found, extracts 'lat' and 'lon' data from the 'header' table in a SQLite file
    and adds a new row to the CSV file with the 'id_antenna', 'lat', and 'lon' values.

    Args:
    ----------------
    sv_output_file: str-The name of the CSV file to search and update.
    id_antenna: str-The ID value to search for in the CSV file.

    Returns:
    ----------------
    lat: str - The latitude value corresponding to the 'id_antenna'.
    lon: str - The longitude value corresponding to the 'id_antenna'.
    """
    # Verifying if the CSV file already exists

    radvelso_dir = os.path.dirname(radvelso.__file__)
    #root path of radvelso package (one dir up from radvelso module)
    package_dir = os.path.dirname(radvelso_dir)
    #full path to extension
    path_to_file = f'{package_dir}/radvelso/database/radar_lat_lon.csv'

    csv_file_exists = os.path.isfile(f'{path_to_file}')
    if csv_file_exists:
        # If the file exists, search for the 'id_antennna'
        with open(path_to_file, 'r', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)

            # Searching for the 'id_antenna' in the CSV file
            for row in csv_reader:
                if row['id_antenna'] == id_antenna:
                    # If 'id_antenna' is found, return the corresponding 'lat' and 'lon' values
                    return float(row['lat']), float(row['lon'])

    # If 'id_antenna' is not found in the CSV file or the file doesn't exist,
    # call the 'extract_lat_lon_from_header' function to extract the coordinates
    lat, lon = extract_lat_lon_from_header(sqlite_file, path_to_file)
   # remove_duplicates_from_csv()
    
    return float(lat), float(lon)

def remove_duplicates_from_csv():
    """
    Removes duplicate lines from a CSV file based on the 'id_stn' column.

    Args:
    ----------------
    file_path: str - The path to the CSV file.

    Returns:
    ----------------
    None (The function modifies the CSV file in place, removing duplicates.)
    """
    radvelso_dir = os.path.dirname(radvelso.__file__)
    #root path of radvelso package (one dir up from radvelso module)
    package_dir = os.path.dirname(radvelso_dir)
    #full path to extension
    path_to_file = f'{package_dir}/radvelso/database/radar_lat_lon.csv'

    with open(path_to_file, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # Read the header

        # Create a set to keep track of seen 'id_antenna' values
        seen_id_antenna = set()
        unique_rows = []

        # Check each row and add it to 'unique_rows' if the 'id_antenna' is not seen before
        for row in csv_reader:
            id_antenna = row[0]
            if id_antenna not in seen_id_antenna:
                seen_id_antenna.add(id_antenna)
                unique_rows.append(row)

    # Write back the unique rows to the CSV file
    with open(path_to_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(header)
        csv_writer.writerows(unique_rows)
        
def get_vol_scan_list(infile_list, desired_radar_list, path_pattern, assim_window_width,assim_T0, file_pattern):
    """
    Extracts information from SQLite files and builds a list of volume scan data.

    This function searches for relevant files using the specified path pattern and extracts
    'radar_name', 'this_datetime', and 'sqlite_src_file' data from the file names.
    It filters the data based on the desired radar list and assimilation time ('assim_T0').

    Args:
    ----------------
    infile_list: list - List of input file paths for the first part of volume scan data.
    desired_radar_list: list - List of radars to be considered or 'all' for all radars.
    path_pattern: str - Path pattern to glob for files containing additional volume scan data.
    assim_T0: datetime - Center time of the assimilation window.
    file_pattern: str - The regular expression pattern to extract information from file names.

    Returns:
    ----------------
    vol_scan_list (list): A list of dictionaries, each containing 'sqlite_src_file', 'radar_name', and 'this_datetime'.
    """
    vol_scan_list = []  # Initialize the list to store volume scan data
    seen_combinations = set()  # Keep track of seen combinations of radar_name and this_datetime

    # Iterate through files matching the path pattern
    for this_sqlite_file in infile_list: #glob.glob(path_pattern):

        # Extract the radar_name, thistime, and thisdate from the this_sqlite_file string using regex
        match = re.search(file_pattern, this_sqlite_file)
        if match:
            thisdate, thistime, radar_name = match.groups()

            # Check if the radar_name is in the desired_radar_list or 'all' is specified
            if radar_name in desired_radar_list or 'all' in desired_radar_list:
                # Convert the date and time strings into a datetime object
                this_datetime = datetime.datetime.strptime(f'{thisdate}{thistime}', '%Y%m%d%H%M%S')
                assim_window_start = assim_T0 - datetime.timedelta(seconds=int(assim_window_width / 2. * 3600.))
                assim_window_end = assim_T0 + datetime.timedelta(seconds=int(assim_window_width / 2. * 3600.))
                if ( assim_window_start <= this_datetime <= assim_window_end):
                    # Construct the sqlite_src_file path
                    sqlite_src_file = f"{Path(os.path.dirname(infile_list[0])).parent}/{radar_name}/file_{thisdate}_{thistime}_{radar_name}"
                    # Check if the combination of radar_name and this_datetime has been seen before
                    if (radar_name, this_datetime) not in seen_combinations:
                        # Append the data to the vol_scan_list and add it to the seen_combinations set
                        vol_scan_list.append({'sqlite_src_file': sqlite_src_file,
                                              'radar_name': radar_name,
                                              'this_datetime': this_datetime,})
                        seen_combinations.add((radar_name, this_datetime)) 

    return vol_scan_list

def flush_pathout(pathout):
    """
    Flush (delete and recreate) the specified directory.

    Parameters:
    ----------------
    pathout: str - The path to the directory that needs to be flushed.

    Returns:
    ----------------
    None
    """
    # Check if the directory exists, and if so, delete it and its contents
    if os.path.isdir(pathout):
        shutil.rmtree(pathout)

    # Create the directory if it doesn't exist
    if not os.path.isdir(pathout):
        os.makedirs(pathout)

def load_and_execute_schema(conn):
    """
    Load schema from the 'schema' file and execute it in the given connection.

    Parameters:
    ----------------
    conn: sqlite3.Connection - The SQLite database connection to which the schema will be applied.

    Returns:
    ----------------
    None
    """
    # Find the 'schema' file
    schema_file = find_schema('schema')

    # Open and read the contents of the schema file
    with open(schema_file) as f:
        schema = f.read()

    # Execute the schema in the provided database connection
    conn.executescript(schema)

def join_sqlites(pathout, assim_T0, outfile_struc):
    """
    Join multiple SQLite files into a single SQLite file.

    Args:
    ----------------
    pathout: str - Output directory where SQLite files are stored.
    assim_T0: datetime object - Center time of the assimilation window.
    outfile_struc: str - Structure of the output file name; will be passed to strftime.

    Returns:
    ----------------
    None
    """
    t0c = time.time()

    # Get a list of SQLite files to join

    sqlites_to_join_list = glob.glob(os.path.join(pathout, 'sqlites_to_join', '*'))

    # Remove the output file if it already exists
    pathfileout_join = os.path.join(pathout, assim_T0.strftime(outfile_struc))
    if os.path.isfile(pathfileout_join):
        os.remove(pathfileout_join)

    # Create a connection to the output SQLite file
    with sqlite3.connect(pathfileout_join) as conn_pathfileout_join:
        conn_pathfileout_join.execute("pragma temp_store = 2;")
        load_and_execute_schema(conn_pathfileout_join)

        # Combine data from all SQLite files into the output SQLite file
        for this_file_to_join in sqlites_to_join_list:
            combine(pathfileout_join, this_file_to_join)

        # Improve searches with index tables
        create_index_tables_idobs_iddata(conn_pathfileout_join)


        # Perform collision test
        collision_test(conn_pathfileout_join)

    print(f"Runtime combine total: {round(time.time()-t0c, 4)} s")

def compute_qcavgobsdb(assim_T0,
                       assim_window_width,
                       desired_radar_list,
                       infile_list, 
                       pathout, 
                       outfile_struc, 
                       ops_run_name, 
                       n_rays, 
                       delta_range,
                       n_cpus,
                       obs_percentage,
                       obs_nyquist,
                       model_outputs_for_dealiasing,
                       model_files_search_pattern,
                       mode_cluster,
                       mode_qsub,
                       thinning, 
                       outfile_struc_thinning, 
                       delta_time_thinning_min,
                       delta_distance_neighbours_m,
                       delta_height_vertical_m,
                       delta_distance_couple_m,
                       joinsqlitefiles):
    """
    Launch computation of average volume scans, possibly in parallel.

    Args:
    ----------------
    assim_T0: datetime object - Center time of the assimilation window.
    assim_window_width: float - Width of the assimilation window in hours.
    desired_radar_list: list - List of radars to process.
    infile_list: list - List of input files to be superobbed.
    pathout: str - Output directory to store average SQLite file(s).
    outfile_struc: str - Structure of the output file name; will be passed to strftime.
    ops_run_name: str - Name of the operational run.
    n_rays: int - Number of rays.
    delta_range: float - Delta range of the boxes.
    n_cpus: int - Number of CPUs for parallel execution. If n_cpus=1, jobs are launched sequentially, and Dask is not invoked.
    obs_percentage: float - Percentage of observations in the box to average.
    obs_nyquist: float - Maximum Nyquist velocity for processing AVG+dealias.
    model_outputs_for_dealiasing: str - Path containing fst files with model winds. Setting this path will trigger dealiasing.
    model_files_search_pattern: str - Search pattern for model files.
    mode_cluster: bool - Flag for calculation in a cluster.
    mode_qsub: bool - Flag for calculation with qsub.
    thinning: str - Description of thinning.
    outfile_struc_thinning: str - Structure of the output file name for thinning; will be passed to strftime.
    delta_time_thinning_min: float - Delta time for thinning in minutes.
    delta_distance_neighbours_m: float - Delta distance for neighbors in meters.
    delta_height_vertical_m: float - Delta of height in the vertical in meters.
    delta_distance_couple_m: float - Delta distance for coupling in meters.
    joinsqlitefiles: str - Description of joinsqlitefiles.

    Returns:
    ----------------
    None
    Average SQLite file(s) are created
    """    
    # Initialize the Dask client based on the mode (cluster or qsub) 
    # without them it could be used in series
    if mode_cluster:
        client = Client(scheduler_file='scheduler-file')
    elif mode_qsub:
        print ( mode_qsub ,"Client(threads_per_worker=1, n_workers=n_cpus)")
        client = Client(threads_per_worker=1, n_workers=n_cpus)

    # Create directories to store pickle and SQLite files if they don't exist
    flush_pathout(f"{pathout}/sqlites_to_join")
    flush_pathout(f"{pathout}/pickle_files")

    # Prepare the averaging template for radar velocity data
    t0t = time.time()
    averaging_template = radvelso.fill_ray.fill_ray_dict(n_rays=n_rays,
                                                         min_range_in_ppi=delta_range,
                                                         max_range_in_ppi=240000.,
                                                         delta_range=delta_range)
    save_pkl(f'{pathout}/pickle_files/averaging_template.pkl', averaging_template)
    print(f"Runtime total averaging template: {round(time.time() - t0t, 4)} s")


    # Get a list of volume scan files from input files and desired radars
    t0t = time.time()
    vol_scan_list = get_vol_scan_list(infile_list,
                                      desired_radar_list,
                                      f'{Path(os.path.dirname(infile_list[0])).parent}/*/file_*',
                                      assim_window_width,
                                      assim_T0,
                                      r'file_(\d{8})_(\d{6})_(\w+)$')
    print(f"Runtime total volume scan files: {round(time.time() - t0t, 4)} s")

    if len(vol_scan_list) == 0:
        raise RuntimeError("List of volume scans to process is empty. "
                           "Check that files are available and search criteria are correct.")

    # Get a list of model files and valid dates for dealiasing
    model_files_list, model_valid_date_list = get_model_valid_date_list(assim_T0,
                                                                        assim_window_width,
                                                                        ops_run_name,
                                                                        model_files_search_pattern,
                                                                        model_outputs_for_dealiasing)
    # Prepare the fulldomain wind data and save as pickle files
    t0t = time.time()
    joblib.Parallel(n_jobs=20)(joblib.delayed(savepkl_for_fulldomain) (this_model_file,
                                                                      model_files_list,
                                                                      model_valid_date_list,
                                                                      pathout) for this_model_file in model_files_list)                                                                  
    #
    print(f"Runtime total fulldomain wind data: {round(time.time() - t0t, 4)} s")

    # Prepare the radar wind data and save as pickle filesa
    t0t = time.time()
    #for vol_scan in vol_scan_list:
    #   print ('david',vol_scan['radar_name'], vol_scan['this_datetime'], vol_scan['sqlite_src_file'])
    #   savepkl_for_radardomain (vol_scan['radar_name'],
    #                                                       vol_scan['this_datetime'],
    #                                                       vol_scan['sqlite_src_file'],
    #                                                       model_files_list,
    #                                                       model_valid_date_list,
    #                                                       assim_T0,
    #                                                       assim_window_width,
    #                                                       ops_run_name,
    #                                                       pathout,
    #                                                       obs_nyquist)
       
    delayed_funcs = [dask.delayed(savepkl_for_radardomain)(vol_scan['radar_name'],
                                                           vol_scan['this_datetime'],
                                                           vol_scan['sqlite_src_file'],
                                                           model_files_list,
                                                           model_valid_date_list,
                                                           assim_T0,
                                                           assim_window_width,
                                                           ops_run_name,
                                                           pathout,
                                                           obs_nyquist) for vol_scan in vol_scan_list]
    # Compute the delayed functions using Dask
    dask.compute(*delayed_funcs)
    print(f"Runtime total radar wind data: {round(time.time() - t0t, 4)} s")
    
    # Get a list of volume scan files (takes into account the Nyquist value)
    #t0t = time.time()
    #vol_scan_list = get_vol_scan_list(infile_list,
    #                                  desired_radar_list,
    #                                  f'{pathout}/pickle_files/wind_radar*',
    #                                  assim_window_width,
    #                                  assim_T0,
    #                                  r'wind_radar_(\d{10})_\d+m\_(\d+)_(\w+)\.pkl')
    # Sort the vol_scan_list by 'this_datetime'
    vol_scan_list = sorted(vol_scan_list, key=lambda x: x['this_datetime'])
    print(f"Runtime total scan files (takes into account the Nyquist value): {round(time.time() - t0t, 4)} s")

    if len(vol_scan_list) == 0:
        raise RuntimeError("List of volume scans to process is empty."
                           "Check that files are available and search criteria are correct.")

    # Perform superobbing (averaging) either in parallel or sequentially based on the number of CPUs
    t0t = time.time()
   # serial = True
    if not mode_qsub and not mode_cluster: 
   # if serial:
        print(f'Serial execution VS:{len(vol_scan_list)}')
        for vscan in vol_scan_list[0:1]:

            superobs(vscan['sqlite_src_file'],
                     vscan['radar_name'],
                     vscan['this_datetime'],
                     ops_run_name,
                     obs_percentage,
                     obs_nyquist,
                     pathout,
                     model_valid_date_list,
                     assim_T0,
                     assim_window_width,
                     model_files_list,
                     model_outputs_for_dealiasing)
    else:
        print(f'Parallel execution VS:{len(vol_scan_list)}')
        delayed_funcs = [dask.delayed(superobs)(vscan['sqlite_src_file'],
                                                vscan['radar_name'],
                                                vscan['this_datetime'],
                                                ops_run_name,
                                                obs_percentage,
                                                obs_nyquist,
                                                pathout,
                                                model_valid_date_list,
                                                assim_T0,
                                                assim_window_width,
                                                model_files_list,
                                                model_outputs_for_dealiasing) for vscan in vol_scan_list]
        dask.compute(*delayed_funcs)

    print(f"Runtime total qcavgobsdb: {round(time.time() - t0t, 4)} s")
    
    if joinsqlitefiles:
       print ("make join") 
       t0t = time.time()
       join_sqlites(pathout, assim_T0, outfile_struc)
       print(f"Runtime total join: {round(time.time()-t0t,4)} s")

    if thinning:
       print ("make_thinning")
       paththinning=f'{pathout}/sqlites_to_join/'
       t0t = time.time()
       height_bin_bounds = np.arange(0., 20000+delta_height_vertical_m, delta_height_vertical_m, dtype=float)
       cthinning.compute_thinning(assim_T0,
                                  assim_window_width,
                                  paththinning,
                                  height_bin_bounds,
                                  pathout,
                                  outfile_struc,
                                  outfile_struc_thinning, 
                                  n_cpus,
                                  delta_time_thinning_min,
                                  delta_distance_neighbours_m,
                                  delta_height_vertical_m,
                                  delta_distance_couple_m,
                                  mode_cluster=False,
                                  mode_qsub=False)
    
    #client.close()

def arg_call():
    import argparse 

    parser = argparse.ArgumentParser()
    parser.add_argument('--assim_T0',  default='undefined', type=str,   help="YYYYMMDDHH center time of assimilation window")
    parser.add_argument('--assim_window_width', default=0.,          type=float, help="[hours] width of assimilation window")
    parser.add_argument('--desired_radar_list', nargs="+", default='all',          help="List of radars to process")
    parser.add_argument('--inputfiles', nargs="+", default='undefined',    help="input sqlite file to average")
    parser.add_argument('--pathin',       default='undefined', type=str,   help="directory where are input sqlite files")
    parser.add_argument('--infile_struc', default='*/%Y%m%d%H_ra',type=str,help="structure of input file name")
    parser.add_argument('--pathout',      default=os.getcwd(), type=str,   help="where averaged sqlite files will be put")
    parser.add_argument('--outfile_struc',default='%Y%m%d%H_superobbed_dvel_ground_radars.sqlite', type=str,   help="structure of output file name")
    parser.add_argument('--ops_run_name', default='undefined', type=str,   help="Name of operational run (will show up in rdb4_schema)" ) 
    parser.add_argument('--n_rays',       default=20,          type=int,   help="Number of rays for averaging" )
    parser.add_argument('--delta_range',  default=5000.,       type=float, help="Delta_range  for averaging" )
    parser.add_argument('--n_cpus',       default=1,           type=int,   help="Number of rays for averaging" )
    parser.add_argument('--obs_percentage',default=50,         type=float, help="Percentage of observation in the box to average" )
    parser.add_argument('--obs_nyquist'   ,default=100,        type=float, help="Nyquist for QC" )
    parser.add_argument('--model_outputs_for_dealiasing',default='undefined', type=str, help="Path of model outputs used for dealiasing" )
    parser.add_argument('--model_files_search_pattern',  default='undefined', type=str, help="search pattern for model files" )
    parser.add_argument('--mode_cluster',  default=False, type=str, help="search pattern for model files" )
    parser.add_argument('--mode_qsub',  default=False, type=str, help="search pattern for model files" )
    parser.add_argument('--joinsqlitefiles',  default=False, type=str, help="join sqlite files" )
    parser.add_argument('--thinning',  default=True,        help="Average only one PPI for time analysis" ) 
    parser.add_argument('--delta_time_thinning_min',     default=10,         type=float, help="window_width to average (min)" )
    parser.add_argument('--delta_distance_neighbours_m', default=30000,        type=float, help="min distance neighbours (m)" )
    parser.add_argument('--delta_height_vertical_m', default=1000,         type=int, help="delta distance for vertical interval (m)" )
    parser.add_argument('--delta_distance_couple_m', default=1000,         type=int, help="min distance for couple of different radars is considered (m)" )
    parser.add_argument('--outfile_struc_thinning',default='%Y%m%d%H_superobbed_dvel_ground_radars.sqlite', type=str,   help="structure of output file name")
  
    args = parser.parse_args()
    for arg in vars(args):
        print(f'--{arg}  {getattr(args, arg)}')

    #argument checking
    if args.assim_T0 == 'undefined':
        raise ValueError('Center time of assimilation window must be provided')
    else:
        args.assim_T0 = datetime.datetime.strptime(args.assim_T0, '%Y%m%d%H')

    if np.isclose(args.assim_window_width, 0.) :
        raise ValueError('Window width must be provided')

    if args.inputfiles != 'undefined':
        #if inputfiles argument is provided, we use that
        infile_list = args.inputfiles 

    elif args.pathin != 'undefined': 
        #alternatively, search for files with pathin+infile_struc 
        if not os.path.isdir(args.pathin):
            raise ValueError(f'pathin: {args.pathin} does not exist.')

        search_str = args.assim_T0.strftime(args.infile_struc)
        infile_list = glob.glob(f'{args.pathin}/*/{search_str}')

        assim_window_end = args.assim_T0 - datetime.timedelta(seconds=int(args.assim_window_width / 2. * 3600.))
        search_str2 = assim_window_end.strftime(args.infile_struc)
        infile_list2 = glob.glob(f'{args.pathin}/*/{search_str2}')

        if ( infile_list2 != infile_list):
           infile_list = infile_list + infile_list2
    else:
        raise ValueError('At least one of inputfiles ot pathin must be provided')
    if len(infile_list) == 0:
        raise ValueError('infile_list is empty, we stop here')
        sys.exit(1)

    else:
        for this_file in infile_list:
            if not os.path.isfile(this_file):
                raise ValueError(f'inputfiles: {this_file} does not exist.')

    if not os.path.isdir(args.pathout):
        os.mkdir(args.pathout)

    if args.model_outputs_for_dealiasing == 'undefined':
        warnings.warn("Model outputs for dealiasing are not specified, NO DEALIASING of Doppler velocities will be performed.")
        args.model_outputs_for_dealiasing = None
    else:
        if not os.path.isdir(args.model_outputs_for_dealiasing):
            raise ValueError('The provided path: "model_outputs_for_dealiasing" does not exist!')

    if args.model_files_search_pattern == 'undefined':
        raise ValueError('You mush specify a model_files_search_pattern')

    print ("in")
    #sys.exit is used to the return status of main is catched and passed to caller
    sys.exit(compute_qcavgobsdb(args.assim_T0,
                                args.assim_window_width,
                                args.desired_radar_list,
                                infile_list, 
                                args.pathout, 
                                args.outfile_struc, 
                                args.ops_run_name, 
                                args.n_rays, 
                                args.delta_range, 
                                args.n_cpus,
                                args.obs_percentage,
                                args.obs_nyquist,
                                args.model_outputs_for_dealiasing, 
                                args.model_files_search_pattern,
                                args.mode_cluster,
                                args.mode_qsub, 
                                args.thinning, 
                                args.outfile_struc_thinning, 
                                args.delta_time_thinning_min,
                                args.delta_distance_neighbours_m,
                                args.delta_height_vertical_m,
                                args.delta_distance_couple_m,
                                args.joinsqlitefiles))


if __name__ == '__main__':
    arg_call()
