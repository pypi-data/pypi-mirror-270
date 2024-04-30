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
import scipy.spatial
import domutils.radar_tools as radar_tools
import domutils.geo_tools as geo_tools
from collections import Counter
import pickle
from pathlib import Path
import domcmc.fst_tools as fst_tools
import shutil
import pandas as pd

def make_input_db(filein, this_time):

    """make a separate db oneintervale of time
  
    This db is saved in memory and allows quich search of observation
  
    args: 
    ---------------
    
    filein                 : input sqlite file containing many radars and times
    this_time              : end time of this one volume san
    
    output:
    ----------------

    sqlite connection to the created db

    """
    
    # https://tools.ietf.org/html/rfc3986  Uniform Resource Identifier (URI)
    # The advantage of using a URI filename is that query parameters on the
    # URI can be used to control details of the newly created database connection in parallel
    conn_ppi_db = sqlite3.connect("file::memory:?cache=shared",uri=True)
    # off the journal
    conn_ppi_db.execute("""PRAGMA journal_mode=OFF;""")
    # SQLite continues without syncing as soon as it has handed data off to the operating system
    conn_ppi_db.execute("""PRAGMA synchronous=OFF;""")
  
    schema = radvelso.qcavg.find_schema('schema')
    with open(schema) as f:
        schema = f.read()
    conn_ppi_db.executescript(schema)
    # improve searches with index tables
    radvelso.qcavg.create_index_tables_elevation_azimuth(conn_ppi_db)
    radvelso.qcavg.create_index_tables_idobs_iddata(conn_ppi_db)
    # attach database
    conn_ppi_db.execute("ATTACH DATABASE ? AS db_all", (filein,)) 
    #select headers in desirec PPI
    order_sql = """ INSERT into header 
                    SELECT 
                      * 
                    FROM
                      db_all.header 
                    WHERE
                      time = ? 
                      ;"""
    conn_ppi_db.execute(order_sql, ( this_time,))
    #select associated data entries
    order_sql = """ INSERT into data 
                    SELECT
                      * 
                    FROM
                      db_all.data 
                    WHERE
                      id_obs in (SELECT
                                   id_obs 
                                 FROM
                                   header  );"""
    conn_ppi_db.execute(order_sql)
  
    conn_ppi_db.commit()
  
    return conn_ppi_db
  
def create_info_midas_tables(filein,conn_pathfileout):

    """ Create header entry
    A header is created matching a bunch of entries in data table
  
    args:
    ----------------

    filein        : input sqlite file with raw data
    conn_pathfileout  : connextion to output file
    
    output:
    ----------------

    Nothing
      info table entry is written in output sqlite file
    
    """
    conn_pathfileout.execute("""ATTACH DATABASE ? AS db_all""", (filein,) ) 
  
    # Info table
    order_sql ="""CREATE TABLE info( NAME, DESCRIPTION, UNIT );"""
    conn_pathfileout.execute( order_sql)
    order_sql =""" INSERT  into  info (
                     NAME, DESCRIPTION, UNIT) 
                   SELECT * 
                     from  db_all.info """
    conn_pathfileout.execute( order_sql)
  
  
    # Resume table 
    order_sql ="""CREATE TABLE resume(date integer , time integer , run varchar(9));"""
    conn_pathfileout.execute( order_sql)
  
    order_sql = """INSERT into resume (
                      date, time, run) 
                    SELECT * 
                     from  db_all.resume """
    conn_pathfileout.execute( order_sql)
    
    # rdb4_schema table
    order_sql ="""CREATE TABLE rdb4_schema( schema  varchar(9) );"""
    conn_pathfileout.execute( order_sql)
    order_sql ="""INSERT into rdb4_schema (
                   schema)
                  SELECT *   
                     from  db_all.rdb4_schema  """
    conn_pathfileout.execute( order_sql)
  
    # commint and detach database
    conn_pathfileout.commit()
    conn_pathfileout.execute("DETACH DATABASE db_all")


def get_obs_from_interval_time(infile_list, assim_T0, pathout, conn_filememory, startdate, enddate, firstintervale):

    """ Copies in memory only the observations to be processed in the required time interval
         
    args:
    ----------------

    conn_filein: connection to initial sqlite file
    conn_filememory: memory connection
    filein: qlite file
    startdate: start date to use observation
    enddate: final date to use observation
    
    output:
    ----------------

    obs have been copied into memory for your use.
    """
    n_files=0
    for this_sqlite_file in infile_list:

        basename = os.path.basename(this_sqlite_file)
        thisdate = basename[5:13] 
        thistime = basename[14:20]  


        this_datetime = datetime.datetime.strptime(f'{thisdate}{thistime}', '%Y%m%d%H%M%S')

        if firstintervale:

           condition = (this_datetime >= startdate) and (this_datetime <= enddate)
        else:
           condition = (this_datetime > startdate) and (this_datetime <= enddate) 
         
            
        if  condition : 
        #         if ( ('uscxx' in this_sqlite_file) or
        #                ('usenx' in this_sqlite_file) or
        #                ('usdix' in this_sqlite_file) or
        #                ('ustyx' in this_sqlite_file) or
        #                ('uspbz' in this_sqlite_file) or
        #                ('usccx' in this_sqlite_file) or
        #                ('usokx' in this_sqlite_file) or
        #                ('usbox' in this_sqlite_file) or
        #                ('usbgm' in this_sqlite_file) or
        #                ('usbuf' in this_sqlite_file) or
        #                ('cawkr' in this_sqlite_file) or
        #                ('casts' in this_sqlite_file) or
        #                ('cawbi' in this_sqlite_file) or
        #                ('casla' in this_sqlite_file) or
        #                ('caslm' in this_sqlite_file) or
        #                ('casft' in this_sqlite_file) or
        #                ('casbv' in this_sqlite_file) or
        #                ('usgyx' in this_sqlite_file) or
        #                ('cawvy' in this_sqlite_file) or
        #                ('casma' in this_sqlite_file) or
        #                ('cawmb' in this_sqlite_file) or
        #                ('uscbw' in this_sqlite_file) or
        #                ('casam' in this_sqlite_file) or
        #                ('casnc' in this_sqlite_file) or
        #                ('caxam' in this_sqlite_file) or
        #                ('caxft' in this_sqlite_file) or 
        #                ('caxgo' in this_sqlite_file) or 
        #                ('caxla' in this_sqlite_file) or 
        #                ('caxlm' in this_sqlite_file) or 
        #                ('caxnc' in this_sqlite_file) or 
        #                ('casgo' in this_sqlite_file) 
        #              ):


            #temporarily attach ppi db to output file
            conn_filememory.execute(f'ATTACH DATABASE "{this_sqlite_file}" AS conn_ppi_db') 
            order_sql = """ INSERT into header
                          SELECT
                           *
                          FROM conn_ppi_db.header;"""
            conn_filememory.execute(order_sql) 
            order_sql = """ INSERT into data
                          SELECT
                            *
                          FROM conn_ppi_db.data;"""
            conn_filememory.execute(order_sql)
  
            conn_filememory.commit()
            conn_filememory.execute(""" DETACH DATABASE conn_ppi_db """)
  
            #conn_ppi_db.close()

            n_files += 1
    print(f'{n_files} files found in interval: {startdate} - {enddate}')
    radvelso.qcavg.create_index_tables_idobs_iddata(conn_filememory)
    conn_filememory.commit()

    return n_files

def to_xyz(lon, lat, obs_height):
    """spherical to cartesian coords on unit sphere
    """

    rad_lon = np.deg2rad(lon)
    rad_lat = np.deg2rad(lat)

    re = radvelso.qcavg.dict_constans()['approximate_radius_of_earth']

    x = (re + obs_height)*np.cos(rad_lon)*np.cos(rad_lat)
    y = (re + obs_height)*np.sin(rad_lon)*np.cos(rad_lat)
    z = (re + obs_height)*np.sin(rad_lat)

    return x, y, z
import numpy as np
import pandas as pd
import sqlite3

def make_dict_of_obs(conn_filememory):
    """Makes a dictionary with the information from the observations.

    Args:
    ----------------
    conn_filememory: memory connection

    Output:
    ----------------

    dict_obs: dictionary with the information from the observations
    """

    c = conn_filememory.cursor()
    c.row_factory = sqlite3.Row

    # Fetch header data using pandas
    header_query = """SELECT ID_OBS, LAT, LON, ANTENNA_ALTITUDE,
                      CENTER_ELEVATION, CENTER_AZIMUTH, DATE, TIME, ID_STN
                      FROM header ORDER BY id_obs ASC;"""
    c.execute(header_query)
    header_entries = c.fetchall()

    # Fetch the number of data entries
    data_query = """SELECT COUNT(*) FROM data;"""
    c.execute(data_query)
    num_data_entries = c.fetchone()[0]

    # Initialize NumPy arrays
    np_id_data = np.zeros(num_data_entries, dtype=int)
    np_id_stn = np.empty(num_data_entries, dtype=object)
    np_obs_lats = np.zeros(num_data_entries)
    np_obs_lons = np.zeros(num_data_entries)
    np_obs_height = np.zeros(num_data_entries)
    np_pos_x = np.zeros(num_data_entries)
    np_pos_y = np.zeros(num_data_entries)
    np_pos_z = np.zeros(num_data_entries)

    # Index for position in NumPy arrays
    ii = 0
    for header_entry in header_entries:
        id_obs = header_entry['ID_OBS']
        beamElevation = header_entry['CENTER_ELEVATION']
        beamAzimuth = header_entry['CENTER_AZIMUTH']
        radarAltitude = header_entry['ANTENNA_ALTITUDE']
        radar_lon = header_entry['LON']
        radar_lat = header_entry['LAT']

        # Fetch data entries for the current header
        data_query = f"""SELECT RANGE, ID_DATA FROM data
                         WHERE ID_OBS = ? ORDER BY id_obs ASC;"""
        c.execute(data_query, (id_obs,))
        data_entries = c.fetchall()

        for data_entry in data_entries:
            this_range = data_entry['RANGE']
            this_id_data = data_entry['ID_DATA']

            # Calculate lat, lon, and height of observation
            obs_height = radar_tools.model_43(elev=beamElevation, dist_beam=this_range/1e3, hrad=radarAltitude/1e3, want='height') * 1000.
            dist_earth = radar_tools.model_43(elev=beamElevation, dist_beam=this_range/1e3, hrad=radarAltitude/1e3, want='dist_earth')
            obs_lon, obs_lat = geo_tools.lat_lon_range_az(radar_lon, radar_lat, dist_earth, beamAzimuth)
            obs_lon = np.where(obs_lon < 0., obs_lon + 360., obs_lon)

            # Convert from spherical to cartesian coordinates
            pos_x, pos_y, pos_z = to_xyz(obs_lon, obs_lat, obs_height)

            np_id_data[ii] = this_id_data
            np_id_stn[ii] = header_entry['ID_STN']
            np_obs_lats[ii] = obs_lat
            np_obs_lons[ii] = obs_lon
            np_obs_height[ii] = obs_height
            np_pos_x[ii] = pos_x
            np_pos_y[ii] = pos_y
            np_pos_z[ii] = pos_z

            ii += 1

    # Create the dictionary
    dict_obs = {
        'id_data': np_id_data,
        'id_stn': np_id_stn,
        'obs_lats': np_obs_lats,
        'obs_lons': np_obs_lons,
        'obs_height': np_obs_height,
        'pos_x': np_pos_x,
        'pos_y': np_pos_y,
        'pos_z': np_pos_z,
    }
    print (type(dict_obs['id_stn']), len(dict_obs['id_stn']))

    return dict_obs

def flush_pathout(pathout):
    if os.path.isdir(pathout):
        shutil.rmtree(pathout)
    if not os.path.isdir( pathout):
        os.makedirs(pathout)

def thinning(pathin,
             infile_struc,
             infile_combine,
             height_bin_bounds,
             assim_T0,
             pathout,
             filein, 
             startdate,
             enddate,
             firstintervale,
             delta_distance_neighbours_m,
             delta_height_vertical_m,
             delta_distance_couple_m,
             timer=False):

    """ Average  a volume scan
    
    This function takes in raw measurements in an sqlite file and 
    creates an average volume scan based on the content of the 
    provided averaging structure. 
  
    args:
    ----------------
    filein        : input sqlite file with raw data
    this_datetime : vdistance_between_two_points(alid date time of radar observation 
    ray_list      : averaging template containing info for how to average PPIs
    ops_run_name  : name of operational run 
    timer         : activation of time analysis, only the first PPI in a volume scan will be averaged
  
    output:
    ----------------
    This function outputs nothing
    However, the thinning data is put in a sqlite file
  
    """ 
  
    t1 = time.time()
    #Prepare file in memory
    filememory=f'file:{startdate}_{enddate}?mode=memory&cache=shared'
    
    print(filememory)
    t0=time.time()

    #print(f'Averaging volume scan for radar {stn} at time {hhmiss_pad} into {os.path.basename(filememory)}')
    conn_filememory = sqlite3.connect(filememory, uri=True, check_same_thread=False)
    # off the journal
    conn_filememory.execute("""PRAGMA journal_mode=OFF;""")
    # SQLite continues without syncing as soon as it has handed data off to the operating system
    conn_filememory.execute("""PRAGMA synchronous=OFF;""")
  
    schema = radvelso.qcavg.find_schema('schema')
    with open(schema) as f:
        schema = f.read( )
    conn_filememory.executescript(schema)

    seed = 42
    np_rng = np.random.default_rng(seed)
    search_str = assim_T0.strftime(infile_struc)
    infile_list = glob.glob(f'{pathin}/*')
    n_files_found = get_obs_from_interval_time(infile_list,
                                               assim_T0,
                                               pathout, 
                                               conn_filememory, 
                                               startdate,
                                               enddate,
                                               firstintervale)

    if n_files_found == 0:
        return
    dict_obs = make_dict_of_obs(conn_filememory)

    # dict is of the form
    #dict_obs = {'indices'    : np_indices, 
    #            'id_data'    : np_id_data, 
    #            'id_stn'     : np_id_stn,
    #            'obs_lats'   : np_obs_lats,
    #            'obs_lons'   : np_obs_lons,
    #            'obs_height': np_obs_height,
    #            'pos_x'      : np_pos_x, 
    #            'pos_y'      : np_pos_y, 
    #            'pos_z'      : np_pos_z, 
    #            }

    all_id_data_considered = set()
    clusters_id_data_set   = set()
    single_id_data_set     = set()
    id_data_to_remove_set  = set()
    # we perform thinning for each height intervals
    #print ('id_data',len(dict_obs['id_data']))
    #print ('obs_height', len(dict_obs['obs_height']))
    #print (dict_obs['obs_height'])
    t2 = time.time()
    print(f'Time spent reading in data: {t2-t1} seconds')
    # TODO  for debug and example only
    for height_low, height_high in zip(height_bin_bounds[0:-1], height_bin_bounds[1:]):


        # 1   -----------------------------
        # First we first identify all clusters of nearby observations

        #indices of obs in and near the layer of interest
        obs_inds_near_layer = np.nonzero( (dict_obs['obs_height'] >  (height_low  - delta_height_vertical_m)) & 
                                          (dict_obs['obs_height'] <= (height_high + delta_height_vertical_m)) )[0]
        id_data_arr = dict_obs['id_data'][obs_inds_near_layer]
        order_sql = """UPDATE data set flag1=? where ID_DATA = ?;"""
        values_to_update = [(height_low,int(id_data),) for id_data in id_data_arr]
        conn_filememory.executemany(order_sql, values_to_update)

        if obs_inds_near_layer.size == 0 :
            # no obs in layer
            continue

        #subset of observations in layer +- delta_height_vertical_m
        x_arr       = dict_obs['pos_x'][obs_inds_near_layer]
        y_arr       = dict_obs['pos_y'][obs_inds_near_layer]
        z_arr       = dict_obs['pos_z'][obs_inds_near_layer]
        height_arr  = dict_obs['obs_height'][obs_inds_near_layer]
        id_data_arr = dict_obs['id_data'][obs_inds_near_layer]
        id_stn_arr  = dict_obs['id_stn'][obs_inds_near_layer]

        # kdtree for all observaions in extended atmosphere layer
        src_xyz = np.transpose(np.vstack((x_arr, y_arr, z_arr)))
        kdtree = scipy.spatial.KDTree(src_xyz)

        # we identify clusters of mesurements from different radars
        # a list of sets containing the id_data contained in different clusters
        cluster_list   = []
        # a list of same size as above containing x,y,z position of the center of clusters
        cluster_x_list = []
        cluster_y_list = []
        cluster_z_list = []
        # a list of same size as above containing distance of point furthest from the cluster center
        cluster_maxd_list = []

        # in this loop, we find all clusters in layer, not caring for overlaps
        for pt_1, (this_id_data, this_x, this_y, this_z) in enumerate(zip(id_data_arr, x_arr, y_arr, z_arr)):

            # require that the first point of a cluster be in the layer of interest
            if (height_arr[pt_1] <=  height_low) or (height_arr[pt_1] > height_high):
                continue

            neighbor_list = kdtree.query_ball_point((this_x,this_y,this_z), delta_distance_couple_m)

            if len(neighbor_list) <= 1:
                # there are no neighbors
                continue

            # find all neighbors from different radars whose height is within tolerence
            this_cluster_set = set([this_id_data])
            radar_set        = set([id_stn_arr[pt_1]])
            this_cluster_xyz_list = [(this_x, this_y, this_z)]
            for pt_2 in neighbor_list:
                if pt_2 == pt_1 :
                    # neighbor is reference point, we do nothing
                    continue
                if id_stn_arr[pt_2] not in radar_set:
                    # we have a measurement from a radar not already encountered
                    if np.abs(height_arr[pt_1] - height_arr[pt_2]) <= delta_height_vertical_m:
                        # measurements are vertically located within tolerance -> we have a cluster
                        this_cluster_set.add(id_data_arr[pt_2])
                        radar_set.add(id_stn_arr[pt_2])
                        this_cluster_xyz_list.append( (x_arr[pt_2], y_arr[pt_2], z_arr[pt_2]) )
            
            if len(this_cluster_set) >= 2:
                # we found a cluster!

                # list of all individual clusters
                cluster_list.append(this_cluster_set)

                # compute mean x,y,z position of cluster
                x_sum = 0.
                y_sum = 0.
                z_sum = 0.
                for xx, yy, zz in this_cluster_xyz_list:
                    x_sum += xx
                    y_sum += yy
                    z_sum += zz
                mean_x = x_sum/len(this_cluster_set)
                mean_y = y_sum/len(this_cluster_set)
                mean_z = z_sum/len(this_cluster_set)

                # return distance square of furthest point from center
                max_d = 0.
                for xx, yy, zz in this_cluster_xyz_list:
                    this_max_d = (xx - mean_x)**2. +  (yy - mean_y)**2. + (zz - mean_z)**2. 
                    max_d = np.maximum(max_d, this_max_d)

                cluster_x_list.append(mean_x)
                cluster_y_list.append(mean_y)
                cluster_z_list.append(mean_z)
                cluster_maxd_list.append(max_d)

        print(f'We have {len(cluster_list)} clusters on this level with possible overaps')


        # 2   -----------------------------
        # We now compare clusters against one another to eliminate those with overlapping observations
        # priority is given to larger and tighter cluster 

        rejected_cluster_overlapping_points = set()
        for ii, cluster_1 in enumerate(cluster_list):
            if ii in rejected_cluster_overlapping_points:
                continue

            for jj, cluster_2 in enumerate(cluster_list):
                if jj in rejected_cluster_overlapping_points:
                    continue

                # skip if a cluster is itself
                if ii == jj:
                    continue

                # check if the two clusters have common entries
                common_ids = set.intersection(cluster_1, cluster_2)

                if len(common_ids) > 0:
                    # some observations are in the two clusters
                    # we must chosse one or the other

                    # priority given to larger cluster
                    if   len(cluster_1) > len(cluster_2):
                        # we eliminate cluster 2 that is the smallest
                        rejected_cluster_overlapping_points.add(jj)
                    elif len(cluster_1) < len(cluster_2):
                        # we eliminate cluster 1 that is the smallest
                        rejected_cluster_overlapping_points.add(ii)
                    else:
                        # the two clusters have the same size
                        if cluster_maxd_list[ii] < cluster_maxd_list[jj]:
                            # cluster 1 is "tighter" we eliminate cluster 2
                            rejected_cluster_overlapping_points.add(jj)
                        elif cluster_maxd_list[ii] > cluster_maxd_list[jj]:
                            # cluster 2 is "tighter" we eliminate cluster 1
                            rejected_cluster_overlapping_points.add(ii)
                        else:
                            # the two cluster have points in identical positions 
                            # this happens for multiple volume scans in the same thinning time window
                            # in this case, we randomly pick one
                            if np_rng.uniform(size=1) < 0.5:
                                rejected_cluster_overlapping_points.add(ii)
                            else:
                                rejected_cluster_overlapping_points.add(jj)

        # get list of selected cluster indices by exclusion
        all_cluster_inds = set(np.arange(0,len(cluster_list)))
        selected_cluster_inds = all_cluster_inds - rejected_cluster_overlapping_points
        if len(selected_cluster_inds) > 0:

            # 3   -----------------------------
            # We apply thinning to clusters based on their center positions

            # first we rebuild list of clusters this time, keeping only those selected above
            cluster_list   = [cluster_list[ind]   for ind in selected_cluster_inds]
            cluster_x_list = [cluster_x_list[ind] for ind in selected_cluster_inds]
            cluster_y_list = [cluster_y_list[ind] for ind in selected_cluster_inds]
            cluster_z_list = [cluster_z_list[ind] for ind in selected_cluster_inds]

            print(f'We have {len(cluster_list)} clusters with non-overlapping points')

            # we thin clusters within a certain horizontal radius
            src_xyz = np.transpose(np.vstack((cluster_x_list, cluster_y_list, cluster_z_list)))
            kdtree = scipy.spatial.KDTree(src_xyz)

            rejected_clusters_thinning = set()
            for ii, cluster_1 in enumerate(cluster_list):

                if ii in rejected_clusters_thinning:
                    # we already flagged this cluster for deletion
                    continue

                neighbor_list = kdtree.query_ball_point((cluster_x_list[ii],
                                                         cluster_y_list[ii],
                                                         cluster_z_list[ii]), delta_distance_neighbours_m/2.) 
                for neighbor in neighbor_list:

                    if neighbor == ii :
                        # neighbor is point ii we do nothing
                        continue

                    # we remove closeby neighbors from list of protected pairs
                    rejected_clusters_thinning.add( neighbor )



            # we update cluster list one last time
            all_cluster_inds = set(np.arange(0,len(cluster_list)))
            selected_cluster_inds = all_cluster_inds - rejected_clusters_thinning
            cluster_list   = [cluster_list[ind] for ind in selected_cluster_inds]
            print(f'We have {len(cluster_list)} clusters after thinning on this level')

            # we all all id_data participating in a cluster to the protected list
            for cluster_ids in cluster_list:
                clusters_id_data_set.update(cluster_ids)


        # 4   -----------------------------
        # Now thinning "regular" observations

        # we consider regular observations only within the layer of interest
        obs_inds_in_layer = np.nonzero( (dict_obs['obs_height'] >  height_low ) & 
                                        (dict_obs['obs_height'] <= height_high) )[0]
        if obs_inds_in_layer.size == 0 :
            # no obs in layer 
            continue

        # subset of points strictly in layer 
        x_arr = dict_obs['pos_x'][obs_inds_in_layer]
        y_arr = dict_obs['pos_y'][obs_inds_in_layer]
        z_arr = dict_obs['pos_z'][obs_inds_in_layer]
        id_data_arr = dict_obs['id_data'][obs_inds_in_layer]
        id_stn_arr  = dict_obs['id_stn'][obs_inds_in_layer]

        # build set of id_data that are examined throughout the thinning process
        all_id_data_considered.update(id_data_arr)

        # thin observations 
        src_xyz = np.transpose(np.vstack((x_arr, y_arr, z_arr)))
        kdtree = scipy.spatial.KDTree(src_xyz)

        for pt_1, (this_id_data, this_x, this_y, this_z) in enumerate(zip(id_data_arr, x_arr, y_arr, z_arr)):

            if this_id_data in id_data_to_remove_set:
                # we already flagged this observation for deletion
                continue

            # if code gets here, we want to keep this point but eliminate all neighbors
            neighbor_list = kdtree.query_ball_point((this_x,this_y,this_z), delta_distance_neighbours_m)
            for neighbor in neighbor_list:

                # neighbor is in fact the reference point at the center of the ball
                if neighbor == pt_1:
                    continue

                neighbor_id_data = id_data_arr[neighbor]
                if neighbor_id_data in id_data_to_remove_set:
                    # point already eliminated
                    continue
                
                if not neighbor_id_data in clusters_id_data_set:
                    # id_data gets eliminated if it was not previously 
                    # identified as part of a cluster
                    id_data_to_remove_set.add(neighbor_id_data)


    # end of vertical layers loop
    #
    #

    t3 = time.time()
    print(f'Time spent thinning data: {t3-t2} seconds')


    # all id_data that are not part of a cluster or rejected
    single_id_data_set = all_id_data_considered - clusters_id_data_set - id_data_to_remove_set

    #take no chance approach, we mark all observations as thinned

    #order_sql = """UPDATE data set flag1=0 ;"""
    #conn_filememory.execute(order_sql)

    # ONLY for debugging and illustrative purposes  -----------------------

    # flag 1 for all observations that were considered for thinning
    order_sql = """UPDATE data set flag1=flag1 + 1 where ID_DATA = ?;"""
    values_to_update = [(int(id_data),) for id_data in all_id_data_considered]
    #print(f'num flag 1 id_data -> all data considered : {len(values_to_update)}')
    conn_filememory.executemany(order_sql, values_to_update)

    order_sql = """UPDATE data set flag=2048 where ID_DATA = ?;"""
    conn_filememory.executemany(order_sql, values_to_update)

    # flag 77 for observations in clusters
    order_sql = """UPDATE data set flag1=flag1 + 77 where ID_DATA = ?;"""
    values_to_update = [(int(id_data),) for id_data in clusters_id_data_set]
    #print(f'num flag 77 id_data -> clusters : {len(values_to_update)}')
    conn_filememory.executemany(order_sql, values_to_update)
 
    order_sql = """UPDATE data set flag=0 where ID_DATA = ?;"""
    conn_filememory.executemany(order_sql, values_to_update)


    # flag 88 for single observations that will be assimilated
    order_sql = """UPDATE data set flag1=flag1 + 88 where ID_DATA = ?;""" 
    values_to_update = [(int(id_data),) for id_data in single_id_data_set]
    #print(f'num flag 88 id_data -> singles : {len(values_to_update)}')
    conn_filememory.executemany(order_sql, values_to_update)

    order_sql = """UPDATE data set flag=0 where ID_DATA = ?;"""
    conn_filememory.executemany(order_sql, values_to_update)

    # ---------------------------------------------------------------------

    conn_filememory.commit()

    #order_sql = """UPDATE data set flag=replace(flag, 0, 1) where ID_DATA IN (?);"""
    #values_to_update = [(int(id_data),) for id_data in list_id_data_height]
    #conn_filememory.executemany(order_sql, values_to_update)

    ## combine in one file from filememory
    #order_sql = """UPDATE data set flag=replace(flag, 1, 2048) where ID_DATA IN (?);"""
    #values_to_update = [(int(id_data),) for id_data in id_data_to_remove_set]
    #conn_filememory.executemany(order_sql, values_to_update)
    #order_sql = "delete from data where flag=0;"
    #conn_filememory.execute(order_sql)

    #conn_filememory.commit()
    print(f'opening file: {infile_combine}')
    conn_filein = sqlite3.connect(f'{infile_combine}', uri=True, isolation_level=None, timeout=999)

    # copy content of filememory into actual sqlite file
    combine(conn_filein, filememory)

    #radvelso.qcavgobsdb.create_index_tables_idobs_iddata(conn_filein)
    #radvelso.qcavgobsdb.create_index_tables_elevation_azimuth(conn_filein)

    conn_filememory.close()
    conn_filein.commit()
    conn_filein.close()

    t4 = time.time()
    print(f'Time spent adjusting flags and updating sqlite file: {t4-t3} seconds')
   
    

def find_sample_entry(src_dir, file_type, variable=None, prefix=None):
   
    """find first entry of a given variable in a given directory
    



    """

    if prefix is None:
        prefix = '2*'

    found = False
    if file_type == 'fst':
        file_list = sorted(Path(src_dir).glob(prefix))
        file_list = sorted(Path(src_dir).glob(prefix))
        file_list = sorted(Path(src_dir).glob(prefix))
        for this_file in file_list:
            if this_file.is_file():
                
                out_dict = fst_tools.get_data(str(this_file), var_name=variable, latlon=True )
                if out_dict is not None:
                    found = True
                    break

    else:
        raise ValueError('filetype not supported')

    if not found:
        raise ValueError(f'sample file not found in {src_dir}')

    return out_dict


def combine(conn_fileout, filememory):
 
    """ Creating a single sqlite file from multiple sqlite files
   
    args:
    ----------------
    pathfileout   : output averaging  sqlite file 
    filememory    : name of the sqlite file in memory to copy
    
    output:
    ----------------
    Nothing
    A sqlite file is made with all averaged volume scans

    """
  
    # write in output averaging  sqlite file
    #sqlite3.connect(pathfileout, uri=True, isolation_level=None, timeout=999)
    # off the journal
    conn_fileout.execute("""PRAGMA journal_mode=OFF;""")
    # SQLite continues without syncing as soon as it has handed data off to the operating system
    conn_fileout.execute("""PRAGMA synchronous=OFF;""")
    # Wait to read and write until the next process finishes
    # attach the sqlite file in memory for one PPI
    conn_fileout.execute("ATTACH DATABASE ? AS this_avg_db;", (filememory,))
    order_sql = """ INSERT into header
                      SELECT
                       *
                      FROM  this_avg_db.header;"""
    conn_fileout.execute(order_sql) 

    order_sql = """ INSERT into data
                      SELECT
                        *
                      FROM  this_avg_db.data;"""
    conn_fileout.execute(order_sql)
    conn_fileout.commit()

    conn_fileout.execute(""" DETACH DATABASE this_avg_db """)
    conn_fileout.commit()



def compute_thinning(assim_T0,
                     assim_window_width,
                     infile_list, 
                     height_bin_bounds,
                     pathout, 
                     infile_struc,
                     outfile_struc, 
                     n_cpus,
                     delta_time_thinning_min,
                     delta_distance_neighbours_m,
                     delta_height_vertical_m,
                     delta_distance_couple_m,
                     mode_cluster,
                     mode_qsub):
  

    """launch computation of average volums scans, possibly in parallel
  
    args:
    ----------------

    center_time  : datetime object,  center time of the assimilation window
    window_width : [hours] Width of the assimilation window
    infile_list  : list of input files to be thinned
    pathout      : output average sqlite file(s) 
    outfile_struc: structure of output file name ; will be passed to strftime
    timing       : activation of time analysis, only the first PPI in a volume scan will be averaged
    n_cpus      : number of cpu
    delta_time_thinning_min: time slices for thinning
    delta_distance_neighbours_m: minimum distance to exclude neighbors
    delta_height_vertical_m: vertical distance where horizontal thinning takes place.
    delta_distance_couple_m: maximum distance to consider couples of observations from different radars
  
    output:
    ----------------

    Nothing
    Average sqlite file(s) are created with the '_thin' suffix
  
    """

    # #start and stop time of assimilation window
    from dask.distributed import Client
    #if mode_cluster:
    #     client = Client(scheduler_file='scheduler-file')
    #elif mode_qsub:
    #     client = Client(threads_per_worker=1, n_workers=80)
     #client = Client(threads_per_worker=1, n_workers=80)
    #print ("outfile_struc",outfile_struc)
    #print (f'{pathout}/{assim_T0.strftime(outfile_struc)}')

    infile_combine = f'{pathout}/{assim_T0.strftime(outfile_struc)}'
   # print ( infile_combine)
    #sys.exit(0)
    if os.path.isfile(infile_combine):
        os.remove(infile_combine)
    if not os.path.isdir(pathout):
        os.mkdir(pathout)
  
    con_infile_combine = sqlite3.connect(f'{infile_combine}')
    con_infile_combine.execute("pragma temp_store = 2;")
    schema = radvelso.qcavg.find_schema('schema')
    with open(schema) as f:
        schema = f.read()
    con_infile_combine.executescript(schema)

    window_t0 = assim_T0 - datetime.timedelta(seconds=3600*assim_window_width/2.)
    window_tf = assim_T0 + datetime.timedelta(seconds=3600*assim_window_width/2.) - datetime.timedelta(minutes=15)
    vol_scan_list = []
    firstintervale = True
    while window_t0 <= window_tf :
        window_t1 = window_t0 + datetime.timedelta(minutes=delta_time_thinning_min)

        vol_scan_list.append( {'file':infile_combine, 'date0':window_t0, 'date1':window_t1, 'firstintervale':  firstintervale})
        firstintervale = False
        window_t0 = window_t1 
    
    #sys.exit(0)
    if len(vol_scan_list) == 0:
        raise RuntimeError("""List of volume scan to process is empty. 
                          Check that files are available and search criteria are correct.""")
    tc_0 = time.time() 
    
    if n_cpus == 1:
            # usefull for debugging
            print(f'Compute {len(vol_scan_list)} volume scans in serial execution')
            for vscan in vol_scan_list:
                tc_0s = time.time() 

                thinning(infile_list,
                         infile_struc,
                         infile_combine,
                         height_bin_bounds,
                         assim_T0,
                         pathout,
                         vscan['file'] , 
                         vscan['date0'], 
                         vscan['date1'],   
                         vscan['firstintervale'], 
                         delta_distance_neighbours_m, 
                         delta_height_vertical_m, 
                         delta_distance_couple_m)
                tc_1s = time.time()
     
               # print(f"Runtime total: {round(tc_1s-tc_0s,2)} s")


    else:
            print(f'Compute {len(vol_scan_list)} volume scans in parallel')

            joblist = [delayed(thinning)(infile_list,
                                         infile_struc,
                                         infile_combine,
                                         height_bin_bounds,
                                         assim_T0,
                                         pathout,
                                         vscan['file'],
                                         vscan['date0'], 
                                         vscan['date1'],
                                         vscan['firstintervale'], 
                                         delta_distance_neighbours_m, 
                                         delta_height_vertical_m, 
                                         delta_distance_couple_m) for vscan in vol_scan_list]
            dask.compute(joblist)
    #radvelso.qcavgobsdb.create_index_tables_idobs_iddata( con_infile_combine)
    #radvelso.qcavgobsdb.create_index_tables_elevation_azimuth(con_infile_combine)
    radvelso.qcavgobsdb.create_table(con_infile_combine, assim_T0)
    con_infile_combine.close()
    
    tc_1 = time.time()
     
    print(f"Runtime total thinning: {round(tc_1-tc_0,4)} s")

def arg_call():

    import argparse 

    parser = argparse.ArgumentParser()
    parser.add_argument('--assim_T0',  default='undefined', type=str,   help="YYYYMMDDHH center time of assimilation window")
    parser.add_argument('--assim_window_width', default=0.,          type=float, help="[hours] width of assimilation window")
    parser.add_argument('--inputfiles', nargs="+", default='undefined',    help="input sqlite file to average")
    parser.add_argument('--pathin',       default='undefined', type=str,   help="directory where are input sqlite files")
    parser.add_argument('--infile_struc', default='/%Y%m%d%H_ra',type=str,help="structure of input file name")
    parser.add_argument('--pathout',      default=os.getcwd(), type=str,   help="where averaged sqlite files will be put")
    parser.add_argument('--outfile_struc',default='%Y%m%d%H_superobbed_dvel_ground_radars.sqlite', type=str,   help="structure of output file name")
    parser.add_argument('--n_cpus',       default=1,           type=int,   help="Number of rays for averaging" )
    parser.add_argument('--delta_time_thinning_min',   default=10,         type=float, help="window_width to average (min)" )
    parser.add_argument('--delta_distance_neighbours_m', default=50000,        type=float, help="min distance neighbours (m)" )
    parser.add_argument('--delta_height_vertical_m', default=1000,         type=int, help="delta distance for vertical interval (m)" )
    parser.add_argument('--delta_distance_couple_m',   default=1000,         type=int, help="min distance for couple of different radars is considered (m)" )
    parser.add_argument('--mode_cluster',  default=False, type=str, help="search pattern for model files" )
    parser.add_argument('--mode_qsub',  default=False, type=str, help="search pattern for model files" )

    args = parser.parse_args()

    if args.inputfiles == 'undefined' and args.pathin == 'undefined':

        args.assim_T0 = '2019062706'
        args.assim_window_width = 6.
        #option1: explicitely specify inputfiles
        #args.inputfiles = ['/space/hall4/sitestore/eccc/cmd/a/dlo001/data/doppler_qc/doppler_qc_v0.3/sqlite_v1.0.0_qc/split_6h/USVNX/2019073100_ra',
        #                   '/space/hall4/sitestore/eccc/cmd/a/dlo001/data/doppler_qc/doppler_qc_v0.3/sqlite_v1.0.0_qc/split_6h/CASRA/2019073100_ra']
        #option2: specify pathin + infile_struc and let Python search for files
        args.pathin = '/fs/site6/eccc/cmd/a/dlo001/data/doppler_qc/doppler_qc_v0.4/sqlite_v1.0.0_qc/split_6h/'
        args.pathout = './work'
        args.timing = False
        args.plot   = False
        args.n_cpus = 80

        print(f'superobs called with no input filename(s)')
        print(f'We are running demo with:')
    for arg in vars(args):
        print(f'--{arg}  {getattr(args, arg)}')
    if args.assim_T0 == 'undefined':
        raise ValueError('Center time of assimilation window must be provided')
    else:
        args.assim_T0 = datetime.datetime.strptime(args.assim_T0, '%Y%m%d%H')

    if args.inputfiles != 'undefined':
        #if inputfiles argument is provided, we use that
        infile_list = args.inputfiles 

    elif args.pathin != 'undefined': 
        #alternatively, search for files with pathin+infile_struc 
        if not os.path.isdir(args.pathin):
            raise ValueError(f'pathin: {args.pathin} does not exist.')
        search_str = args.assim_T0.strftime(args.infile_struc)
        infile_list = glob.glob(f'{args.pathin}/{search_str}*')
    else:
        raise ValueError('At least one of inputfiles ot pathin must be provided')

    #check infile_list
    if len(infile_list) == 0:
        raise ValueError('infile_list is empty, we stop here')
        sys.exit(1)

    else:
        for this_file in infile_list:
            if not os.path.isfile(this_file):
                raise ValueError(f'inputfiles: {this_file} does not exist.')

    if not os.path.isdir(args.pathout):
        os.mkdir(args.pathout)

    # vertical height bounds (ASL)
    height_bin_bounds = np.arange(0., 20000+args.delta_height_vertical_m, args.delta_height_vertical_m, dtype=float)

    #sys.exit is used to the return status of main is catched and passed to caller
    sys.exit(compute_thinning(args.assim_T0,
                              args.assim_window_width,
                              args.pathin, 
                              height_bin_bounds,
                              args.pathout, 
                              args.infile_struc,
                              args.outfile_struc, 
                              args.n_cpus,
                              args.delta_time_thinning_min,
                              args.delta_distance_neighbours_m,
                              args.delta_height_vertical_m,
                              args.delta_distance_couple_m,
                              args.mode_cluster,
                              args.mode_qsub))

if __name__ == '__main__':
    arg_call()
