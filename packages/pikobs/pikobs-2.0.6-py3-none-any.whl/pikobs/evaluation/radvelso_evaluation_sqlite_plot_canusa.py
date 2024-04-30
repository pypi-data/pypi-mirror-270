#/usr/bin/python3
import os
import tempfile
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
import json
import radvelso
from numpy import save
from os.path import basename,splitext
import matplotlib.pyplot as plt

def make_input_ppi_db_statistics(filein, 
                      stn, 
                      nominal_ppi_elevation,
                      ):

  """make a separate db for one PPI

   This db is saved in memory and allows quich search of averaging boxes

   args: 
     filein                 : input sqlite file containing many radars and times
     stn                    : radar for this one volume scan
     nominal_ppi_elevation  : nominal elevation

   output: 
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

  schema = radvelso.find_schema('schema_statistics')
  with open(schema) as f:
    schema = f.read()
  conn_ppi_db.executescript(schema)
  # improve searches with index tables
  # create_index_tables_elevation_azimuth(conn_ppi_db)
  #  create_index_tables_idobs_iddata(conn_ppi_db)
  # attach database
  print (stn, "DAVID")
  conn_ppi_db.execute("ATTACH DATABASE ? AS db_all", (filein,)) 
  #select headers in desirec PPI
  order_sql = """ INSERT into statistics
                  SELECT 
                    * 
                  FROM
                    db_all.statistics
                  WHERE
                    id_stn like ?   
                    and round(nominal_ppi_elevation, 1) = ? ;"""
  conn_ppi_db.execute(order_sql, (stn, nominal_ppi_elevation))

 # order_sql = """ INSERT into statistics
 #                 SELECT 
 #                   * 
 #                 FROM
 #                   db_all.statistics
 #                 WHERE
 #                   id_stn like ''  
 #                   and round(nominal_ppi_elevation, 1) = ? ;"""
 # conn_ppi_db.execute(order_sql, ( nominal_ppi_elevation,))



  order_sql = """ INSERT into info
                  SELECT 
                    * 
                  FROM
                    db_all.info;"""
  conn_ppi_db.execute(order_sql)

  conn_ppi_db.commit()

  return conn_ppi_db

def make_input_ppi_db_statistics_step(filein, 
                      stn):

  """make a separate db for one PPI

   This db is saved in memory and allows quich search of averaging boxes

   args: 
     filein                 : input sqlite file containing many radars and times
     stn                    : radar for this one volume scan
     nominal_ppi_elevation  : nominal elevation

   output: 
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

  schema = radvelso.find_schema('schema_statistics')
  with open(schema) as f:
    schema = f.read()
  conn_ppi_db.executescript(schema)
  # improve searches with index tables
  # create_index_tables_elevation_azimuth(conn_ppi_db)
  #  create_index_tables_idobs_iddata(conn_ppi_db)
  # attach database
  conn_ppi_db.execute("ATTACH DATABASE ? AS db_all", (filein,)) 
  #select headers in desirec PPI
  order_sql = """ INSERT into statistics
                  SELECT 
                    * 
                  FROM
                    db_all.statistics
                  WHERE
                    id_stn like ?   
                 ;"""
  conn_ppi_db.execute(order_sql, (stn,))

 # order_sql = """ INSERT into statistics
 #                 SELECT 
 #                   * 
 #                 FROM
 #                   db_all.statistics
 #                 WHERE
 #                   id_stn like ''  
 #                   and round(nominal_ppi_elevation, 1) = ? ;"""
 # conn_ppi_db.execute(order_sql, ( nominal_ppi_elevation,))



  order_sql = """ INSERT into info
                  SELECT 
                    * 
                  FROM
                    db_all.info;"""
  conn_ppi_db.execute(order_sql)

  conn_ppi_db.commit()

  return conn_ppi_db

def create_index_tables_elevation_azimuth(conn):
  """ Create index tables
  args:
    conn          : connextion to sqlite file
  output:
    Nothing
    index tables i sqlite file
 
  """

  order_sql ="""CREATE INDEX 
                  NOMINAL_PPI_ELEVATIONS 
                ON header (NOMINAL_PPI_ELEVATION);"""
  conn.execute(order_sql)

  order_sql ="""CREATE INDEX
                  CENTER_AZIMUTHS 
                ON header (CENTER_AZIMUTH);"""
  conn.execute(order_sql)


def make_input_ppi_db(filein, 
                      stn, 
                      nominal_ppi_elevation,
                      ):

  """make a separate db for one PPI

   This db is saved in memory and allows quich search of averaging boxes

   args: 
     filein                 : input sqlite file containing many radars and times
     stn                    : radar for this one volume scan
     nominal_ppi_elevation  : nominal elevation

   output: 
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

  schema = radvelso.find_schema('schema2')
  with open(schema) as f:
    schema = f.read()
  conn_ppi_db.executescript(schema)
  # improve searches with index tables
  create_index_tables_elevation_azimuth(conn_ppi_db)
#  create_index_tables_idobs_iddata(conn_ppi_db)
  # attach database
  conn_ppi_db.execute("ATTACH DATABASE ? AS db_all", (filein,)) 
  #select headers in desirec PPI
  order_sql = """ INSERT into header 
                  SELECT 
                    * 
                  FROM
                    db_all.header 
                  WHERE
                    id_stn like ?   
                    and round(nominal_ppi_elevation, 1) = ? ;"""
  conn_ppi_db.execute(order_sql, (stn, nominal_ppi_elevation))


  order_sql = """ INSERT into header 
                  SELECT 
                    * 
                  FROM
                    db_all.header 
                  WHERE
                    and round(nominal_ppi_elevation, 1) = ? and id_stn like 'us%';"""
#  conn_ppi_db.execute(order_sql, ( nominal_ppi_elevation))





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
  order_sql = """ INSERT into info
                  SELECT
                    * 
                  FROM
                    db_all.info;"""
  conn_ppi_db.execute(order_sql)

  conn_ppi_db.commit()

  return conn_ppi_db

def datafromSqlite_step(file_name, this_radar, nominal_ppi_elevation, nyquist):
    """ datafrom
  
    args:
    path              : path to SQlite files of time series

    output:
    This function outputs nothing

    """
    #print (file_name, file_name, nominal_ppi_elevation)
    conn_ppi_db = make_input_ppi_db_statistics_step(file_name, 
                                            this_radar)
    order_sql =""" select  
                   RANGE
                 from  
                   statistics 
                 WHERE
                   round(nominal_ppi_elevation,1) = round(?,1);
                   """
    ranges = [ range_[0]  for range_  in conn_ppi_db.execute(order_sql,(nominal_ppi_elevation,)).fetchall() ]
   # print (ranges)
    #exit()
    ranges = np.array(ranges)
    order_sql =""" select  
                   VCOORD
                 from  
                   statistics 
                 WHERE
                   round(nominal_ppi_elevation,1) = round(?,1);
                   """
    height = [ height_[0]  for height_  in conn_ppi_db.execute(order_sql,(nominal_ppi_elevation,)).fetchall() ]
    height = np.array(height)

    order_sql =""" select  
                   avgomp
                 from  
                   statistics 
                 WHERE
                   round(nominal_ppi_elevation,1) = round(?,1);
                   """

    avgomp = [ omp_[0]  for omp_ in conn_ppi_db.execute(order_sql,(nominal_ppi_elevation,)).fetchall() ]
    ranges = np.array(ranges)
    order_sql =""" select  
                   Number_obs
                 from  
                   statistics 
                 WHERE
                    round(nominal_ppi_elevation,1) = round(?,1);
                   """

    nn = [ nn_[0]  for nn_ in conn_ppi_db.execute(order_sql,(nominal_ppi_elevation,)).fetchall() ]
    nn = np.array(nn)
   
    order_sql =""" select  
                   STDOMP
                 from  
                   statistics 
                 WHERE
                     round(nominal_ppi_elevation,1) = round(?,1);
                   """

    stdomp = [ stdomp_[0]  for stdomp_ in conn_ppi_db.execute(order_sql,(nominal_ppi_elevation,)).fetchall() ]
    stdomp = np.array(stdomp)

    order_sql =""" select  distinct
                   name
                 from  
                   info            
                   ORDER BY 
                    1;"""
                  
    name = [ name_[0]  for name_ in conn_ppi_db.execute(order_sql) ]
    conn_ppi_db.close()
    return avgomp, stdomp, ranges, height, nn, name[0]
  
def datafromSqlite(file_name, this_radar, nominal_ppi_elevation, nyquist):
    """ datafrom
  
    args:
    path              : path to SQlite files of time series

    output:
    This function outputs nothing

    """
    print ("NI", nyquist)
    #print (file_name, file_name, nominal_ppi_elevation)
    conn_ppi_db = make_input_ppi_db_statistics(file_name, 
                                            this_radar, 
                                            nominal_ppi_elevation)
    order_sql =""" select  
                   RANGE
                 from  
                   statistics 
                 WHERE
                   abs(nominal_ppi_elevation-?) < .1;
                   """
    ranges = [ range_[0]  for range_  in conn_ppi_db.execute(order_sql,(nominal_ppi_elevation,)).fetchall() ]
    ranges = np.array(ranges)
    order_sql =""" select  
                   VCOORD
                 from  
                   statistics 
                 WHERE
                   abs(nominal_ppi_elevation-?) < .1;
                   """
    height = [ height_[0]  for height_  in conn_ppi_db.execute(order_sql,(nominal_ppi_elevation,)).fetchall() ]
    height = np.array(height)

    order_sql =""" select  
                   avgomp
                 from  
                   statistics 
                 WHERE
                   abs(nominal_ppi_elevation-?) < .1;
                   """

    avgomp = [ omp_[0]  for omp_ in conn_ppi_db.execute(order_sql,(nominal_ppi_elevation,)).fetchall() ]
    ranges = np.array(ranges)
    order_sql =""" select  
                   Number_obs
                 from  
                   statistics 
                 WHERE
                   abs(nominal_ppi_elevation-?) < .1;
                   """

    nn = [ nn_[0]  for nn_ in conn_ppi_db.execute(order_sql,(nominal_ppi_elevation,)).fetchall() ]
    nn = np.array(nn)
   
    order_sql =""" select  
                   STDOMP
                 from  
                   statistics 
                 WHERE
                   abs(nominal_ppi_elevation-?) < .1;
                   """

    stdomp = [ stdomp_[0]  for stdomp_ in conn_ppi_db.execute(order_sql,(nominal_ppi_elevation,)).fetchall() ]
    stdomp = np.array(stdomp)

    order_sql =""" select  distinct
                   name
                 from  
                   info            
                   ORDER BY 
                    1;"""
                  
    name = [ name_[0]  for name_ in conn_ppi_db.execute(order_sql) ]
    conn_ppi_db.close()
    return avgomp, stdomp, ranges, height, nn, name[0]
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def matplotlibGlobalSettings():
    # Configuration of the image
    mpl.use('Agg')

    # Matplotlib global settings
    mpl.rcParams.update({'font.size': 22})
    # Use this for editable text in svg
    mpl.rcParams['figure.dpi'] = 150
    mpl.rcParams['text.usetex'] = False
    mpl.rcParams['svg.fonttype'] = 'none'
    mpl.rcParams.update({'font.size': 25})

    left = 0.15
    width = 0.6
    bottomn = 0.3
    levels_color = 50

    cmap = plt.cm.get_cmap('gist_ncar', levels_color)
    return left, width, bottomn, cmap, levels_color, plt


def plot(left, bottomn, width):
    fig = plt.figure(figsize=(22, 22))
    ax = plt.axes([left, bottomn, width, 0.6])
    # Ajustar los márgenes
    ax.margins(x=0.05)
    
    # Aumentar el tamaño de fuente en los ejes x e y
    ax.tick_params(axis='both', which='major', labelsize=22)

    # Aumentar el tamaño de fuente para los valores en los ejes x e y
    for tick in ax.get_xticklabels():
        tick.set_fontsize(22)
    for tick in ax.get_yticklabels():
        tick.set_fontsize(22)
    return fig, ax


def axplot(ax, avgomp, stdomp,  nn, xx, cc, ss):
    import seaborn as sns
    
    ax.plot(avgomp, xx / 1000, color=cc, linestyle='-', marker='', ms=25, linewidth=5.0)
    ax.plot(stdomp, xx / 1000, color=cc, linestyle='--', marker='', ms=25, linewidth=5.0)
   # ax.set_xlim(-1, 3.5) 
    pre =  xx[0]/1000
    for x, y, sumNtot in zip(avgomp, xx / 1000, nn):
        if int(sumNtot) > 0:
            max_x = 3.6 # Obtener el valor máximo de xx
            
            xytext = (max_x + ss, y)
           # print (y, pre, pre-y, int(sumNtot))
            if y-pre <0.2 and y-pre !=0:
               xytext = (max_x + ss, y + 0.14)

            pre = y
          #  ax.annotate(int(sumNtot), xy=(x, y), xytext= xytext, fontsize=25, color=cc, va='center', ha='left', textcoords='data')

   # ax.plot(avgomp, xx / 1000, color=cc, linestyle='-', marker='', ms=20, linewidth=5.0)
   # ax.plot(stdomp, xx / 1000, color=cc, linestyle='-', marker='', ms=20, linewidth=5.0)
   # ax.set_xlim(-0.9, 3.5)

   # data_to_display = ax.transData.transform
   # display_to_ax = ax.transAxes.inverted().transform
   # ax_pts = display_to_ax(data_to_display([(0, y / 1000) for y in xx]))

   # adjusted_y_coords = []

   # for y, (ix, iy) in zip(xx, ax_pts):
   #     sumNtot = nn[np.where(xx == y)[0][0]]
   #     
   #     if int(sumNtot) > 0:
   #         adjusted_y = iy
   #         print ('ppp')
   #         adjusted_y_coords.append(adjusted_y)
   #         ax.text(0.1, adjusted_y, int(sumNtot), fontsize=10, color=cc, transform=ax.transAxes, va='center')


def matplotlibGlobalSettings1():
   ################################################
   # Configuration of the imagen
    ################################################
    import matplotlib as mpl
    from os.path import basename,splitext
    import matplotlib as mpl
    import pylab
    import matplotlib.pyplot as plt
    from matplotlib import cm

    mpl.use('Agg')

    #matplotlib global settings
    mpl.rcParams.update({'font.size': 18})
    #Use this for editable text in svg
    mpl.rcParams['figure.dpi'] = 150
    mpl.rcParams['text.usetex']  = False
    mpl.rcParams['svg.fonttype'] = 'none'
    mpl.rcParams.update({'font.size': 25})

    left=0.1
    width=0.3
    bottomn =0.3
    levels_color = 50
   
    cmap =plt.cm.get_cmap('gist_ncar', levels_color)
    return left, width, bottomn, cmap, levels_color, plt


def plot1( left, bottomn, width):


 fig = plt.figure(figsize=(17,17))
 ax = plt.axes([left, bottomn, width, 0.6])




 return fig, ax


def avg_std_plot(pathout,
                 list_files, 
                 this_radar, 
                 start_date, 
                 end_date):

  """ Plot AVG and STD in fuction range/height per elevation for time series
  
  args:
    path              : path to json files of time series
    this_radar        : name of radar
    start_date        : start date of the time series
    end_date          : end date of the time series

  output:
    This function outputs nothing

  """
#  from os.path import basename,splitext
#  import matplotlib as mpl
#  import pylab
  import matplotlib.pyplot as plt
#  from matplotlib import cm
 
  left, width, bottomn, cmap, levels_color, wwplt = matplotlibGlobalSettings()
  print ("----->",list_files[0])

  conn_elevation = sqlite3.connect(list_files[0])
  order_sql = """ SELECT 
                    distinct nominal_ppi_elevation 
                  FROM
                     statistics 
                  WHERE
                    id_stn like  ?
                    and 
                   Number_obs>0
                  ORDER BY 
                    1;"""
 # result_set = conn_elevation.execute(order_sql, (this_radar,)).fetchall()                  
 # nominal_ppi_elevations = [np.round(row[0], 4) for row in result_set]
 # nyquist_values = [row[1] for row in result_set]
  nominal_ppi_elevations = [ np.round(elev[0],4) for elev in conn_elevation.execute(order_sql, (this_radar,)).fetchall() ]

  print ("-1-->" ,nominal_ppi_elevations)


  order_sql = """ SELECT 
                    distinct nominal_ppi_elevation,nyquist
                  FROM
                     statistics 
                  WHERE
                    id_stn like ?
                    and 
                   Number_obs>0
                  ORDER BY 
                    1;"""
  result_set = conn_elevation.execute(order_sql, (this_radar,)).fetchall()                  
  nominal_ppi_elevations_my_list = [np.round(row[0], 4) for row in result_set]
  nyquist_values_my_list = [row[1] for row in result_set]

#  nominal_ppi_elevations = [ np.round(elev[0],4) for elev in conn_elevation.execute(order_sql, (this_radar,)).fetchall() ]

#  print ("-2-->" , nominal_ppi_elevations) 
#  print ("-2-->" ,  nyquist_values)

 # sys.exit()




#   print ( "nominal_ppi_elevations", nominal_ppi_elevations )
#  order_sql = """ SELECT 
#                    distinct nominal_ppi_elevation 
#                  FROM
#                     statistics 
#                  WHERE
#                    id_stn like 'us%'
#                    and 
#                   Number_obs>0
#                  ORDER BY 
#                    1;"""
  # Define the number of nominal_ppi_elevations
  num_elevations = len(nominal_ppi_elevations*2)
  # Choose a different color map with distinct colors, e.g., 'tab10', 'tab20', 'Set1', etc.
  cmap = plt.get_cmap('tab20') 
  # Create the figures outside the loop
  oneg = False
  allg = True
  print ("this_radar",this_radar)
  if this_radar=='c%':
      this_radart = 'Canadiens radars'
  if this_radar=='u%':
      this_radart = 'USA radars'

  omt = 'O-P'

  if allg:
   fig1, ax1 = plot(left, bottomn, width)
   fig2, ax2 = plot(left, bottomn, width)
   typ = '_all'
  
   # Initialize legendlist, cc, and ss
   legendlist = []
   colorlist  = []

  ss = 0
  pathout_plot = f'{pathout}/elevation_all'
  if not os.path.isdir(pathout_plot):
          os.mkdir(pathout_plot)
  print (nominal_ppi_elevations)
 # nominal_ppi_elevations = np.arange(1,20) 
  #print (nominal_ppi_elevations)
  import math
 # exit()
  # Initialize the integer part of the first number
  previous_integer_part = math.floor(nominal_ppi_elevations[0])
  for i, nominal_ppi_elevation in enumerate(nominal_ppi_elevations):

   #fig1, ax1 = plot(left, bottomn, width)
   #fig2, ax2 = plot(left, bottomn, width)

    #if i!=0:
    #    current_integer_part = math.floor( nominal_ppi_elevation)
    #    print ("current_integer_part", current_integer_part, "previous_integer_part", previous_integer_part)
    #    if current_integer_part == previous_integer_part:
    #      
    #       continue
    #    previous_integer_part = current_integer_part

    # Update the previous integer part for the next iteration
  #  previous_integer_part = current_integer_part   
    all_indices = [i for i, value in enumerate(nominal_ppi_elevations_my_list) if value ==  nominal_ppi_elevation]
  #  print ('-1-2->',all_indices)

    #for nyquist  in  all_indices:
  #  print ("nyquist",nyquist)
    nyquist = [nyquist_values_my_list[i] for i in all_indices]
    min_nyquist = np.min(nyquist)
   # min_nyquist =1
   # nyquist =1

   # print ("nyquist",nyquist)
     
    if (round(nominal_ppi_elevation,1)) > 0: # ==0.9 or (round(nominal_ppi_elevation,1)) ==1.5 or (round(nominal_ppi_elevation,1)) == 2.4:
      print (round(nominal_ppi_elevation,1))
     # if oneg:
     #   fig1, ax1 = plot(left, bottomn, width)
     ##   fig2, ax2 = plot(left, bottomn, width)
    #    typ =''
        # Initialize legendlist, cc, and ss
     #   legendlist = []
      #  colorlist  = []

      #ss = 0

      # Calculate the index for cc to get a different color for each elevation
      cc = cmap(int(i*3) / num_elevations)
      legendlist.append(f'BIAS ({omt})')
      legendlist.append(f'STDDEV ({omt}) ele={nominal_ppi_elevation}, nyquist = {round(min_nyquist,1)}')
      colorlist.append(cc)

      for files in list_files:
          avgomp, stdomp, ranges, height, nn, name = datafromSqlite(files, this_radar, nominal_ppi_elevation, nyquist)
          print (nn)
        #if np.min(nn)>100:
          axplot(ax1, avgomp, stdomp,  nn, ranges, cc, ss)
          surname = f'{name}{typ}'
          model = 'GDPS'
          plot_close(ax1, fig1, legendlist,colorlist, pathout_plot, nominal_ppi_elevation, start_date, end_date, this_radart,
                     surname, model, scale_nobs=True, Rangemode=True, Heightmode=False)
  
        # Get indices that would sort array A in descending order
          sorted_indices = sorted(range(len(height)), key=lambda i:height[i])

          # Create new arrays with elements of A and B sorted and reordered according to A's sorting
          sorted_height = np.array([height[i] for i in sorted_indices])
          sorted_avgomp = np.array([avgomp[i] for i in sorted_indices])
          sorted_stdomp = np.array([stdomp[i] for i in sorted_indices])
          print (sorted_height, sorted_stdomp)

          axplot(ax2,sorted_avgomp, sorted_stdomp, nn, sorted_height, cc, ss)
          surname =  f'{name}{typ}'
          model = 'GDPS'
          plot_close(ax2, fig2, legendlist, colorlist, pathout_plot, nominal_ppi_elevation, start_date, end_date, this_radart,
                     surname, model, scale_nobs=True, Rangemode=False, Heightmode=True)
          if allg:
             ss += 0.6
#
          ###############
          if oneg:
            ss +=0.0
            plt.close(fig1)
            plt.close(fig2)

      # Close the figures after the loop
     # if allg:
  plt.close(fig1)
  plt.close(fig2)
  return
  
 


def plot_close(ax, 
              fig, 
              legendlist,
              colorlist,
              path_source, 
              elevation,
              start_date, 
              end_date, 
              this_radar, 
              surname,
              model,
              scale_nobs=False,
              Rangemode=False, 
              Heightmode=False):

    import matplotlib.pyplot as plt
    """ 
  
    program to close the graphic

    args:
    ax                : plot
    fig               : figure
    path_source       : source of jsona
    elevation         : elevation of PPI
    start_date        : start date of the time series
    end_date          : end date of the time series
    this_radar        : name of radar
    Rangemode         : setting for range images
    Heightmode        : setting for height images 

    output:
      This function outputs nothing

    """
   
    ax.grid(visible=True, which='major', color='b', linestyle='-')
    ax.set_xlabel('[m/s]', fontsize=30)
    if Rangemode:
        ax.set_ylabel('RANGE [km]',fontsize=30)
        type_x ='range' 
        ax.set_xlim(-5,5)
        ax.set_ylim(0,250)

    if Heightmode:
        ax.set_ylabel('HEIGHT [km]',fontsize=30)
        type_x ='height'
        ax.set_xlim(-5,5)
        ax.set_ylim(0,20)
    ax.tick_params(axis='x', labelsize=24)
    ax.tick_params(axis='y', labelsize=24)

    fig.subplots_adjust(top=0.85)
    ax.set_title(f"{start_date.strftime('%Y%m%d%H')}-{end_date.strftime('%Y%m%d%H')} ({model}) \n {this_radar}",fontsize=30)
    
    ax.legend(legendlist,loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=2)
    # Crear las columnas de leyendas
    legend_col1 = legendlist[::2]  # Elementos impares
    legend_col2 = legendlist[1::2]  # Elementos pares\
    color_col1  = colorlist[::2]
    color_col2  = colorlist[1::2]
    # Combina las leyendas en una lista de tuplas
    combined_legends = legend_col1 + legend_col2
    combined_color   = colorlist  + colorlist 
    # Agregar leyendas utilizando la lista de tuplas
    legends =ax.legend(combined_legends, loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True,  ncol=2)
    # Asignar los colores combinados a las etiquetas de la leyenda
    for legend, color in zip(legends.legendHandles, combined_color):
        legend.set_color(color)
   # ax.legend(legendlist, prop={'size': 30},loc='upper center', bbox_to_anchor=(0.0, 0.12), ncol=3)
    #, bbox_to_anchor=(0.5, -0.1), ncol=len(legendlist))

    str_end_date   = end_date.strftime('%Y%m%d%H')
    str_start_date = start_date.strftime('%Y%m%d%H')
    namefileout = f'{type_x}_{this_radar}_{str_start_date}_{str_end_date}_{model}_e_{elevation}_{surname}'

    print ("MMMMM")
    fig.savefig(f"{path_source}/{namefileout}.svg", dpi=40, format='svg')
    fig.savefig(f"{path_source}/{namefileout}.png", dpi=40, format='png')


def main_plot(start_date,
         end_date,
         desired_radar_list,
         infile_list, 
         pathoutwork, 
         n_cpus,
         setting_average,
         model):
  """launch computation of std and avg omp for time series  possibly in parallel

   args:
     start_date:     start time of time series
     end_date  :     end   time of time series
     radar_list:     list of radars to process
     infile_list:    input sqlite file to average
     pathout:        where json  files will be put
     n_cpus:         number of rays for averaging
 
  output:
    Nothing

  """
  from termcolor import colored
  import shutil 

  #################################################################################################
  # launch avg_std_plot: Plot AVG and STD in fuction of range/height  per elevation of the time series
  #################################################################################################
  
  tc_0 = time.time()
  evaluation_plot = True


  if  evaluation_plot:


      pathout_plot=f"{pathoutwork}/series_{start_date.strftime('%Y%m%d%H')}_{end_date.strftime('%Y%m%d%H')}/"
     
     # print ('---->',infile_list)
      with sqlite3.connect(infile_list[0]) as conn_loops:
          conn_loops.execute("pragma temp_store = 2;")
          conn_loops.execute("""PRAGMA journal_mode=OFF;""")
          conn_loops.execute("""PRAGMA synchronous=OFF;""")
      order_sql = """select distinct
                           ID_STN 
                         from 
                           header order by 1;"""
         
      avail_radar_list  = [ stn[0] for stn in conn_loops.execute(order_sql).fetchall() ]
      #print (avail_radar_list)
      conn_loops.close()
      file_list=[]
     # avail_radar_list = ['all']
      for this_radar in avail_radar_list:
        this_radar=os.path.basename(this_radar)
       # if desired_radar_list != 'all':
       #   if this_radar not in desired_radar_list:
       #    continue
        pathout=f'{pathout_plot}/{this_radar}'
        if not os.path.isdir(pathout):
           os.mkdir(pathout)
     
        file_list.append( {'pathout':pathout ,'files':infile_list, 'radar':this_radar,'start_date':start_date,'end_date':end_date})
       # print ( this_radar) 
      #exit()
      file_list =  file_list[0:1]
      n_cpus =40
      n_cpus = 1 
      if n_cpus == 1:
        #serial execution, usefull for debugging
        for ppi in file_list:
          avg_std_plot(ppi['pathout'],ppi['files'], ppi['radar'], ppi['start_date'], ppi['end_date']) 
      else:
        with tempfile.TemporaryDirectory() as tmpdir:
          #the directory dask-worker-space/ will be in tmpdir
          dask.config.set({'distributed.comm.timeouts.connect': '20s'})
          with dask.distributed.Client(processes=True, threads_per_worker=1, 
                                     n_workers=n_cpus, 
                                    local_directory=tmpdir, 
                                     silence_logs=40) as client:

            #delay data 
            joblist = [delayed(avg_std_plot)(ppi['pathout'],ppi['files'], ppi['radar'], ppi['start_date'], ppi['end_date']) for ppi in file_list]

            dask.compute(joblist)

            
     #a file_control=np.append(file_control, f'{this_radar}')
     # save(f'file_control_{pathoutwork}/file_control_fig.npy', file_control)

  tc_1 = time.time()
  print(f"Runtime total: {round(tc_1-tc_0,4)} s")


def arg_call():

  import argparse 

  parser = argparse.ArgumentParser()
  parser.add_argument('--start_date',   default='undefined', type=str,  help="YYYYMMDDHH start time of time serie")
  parser.add_argument('--end_date',     default='undefined', type=str,  help="YYYYMMDDHH end   time of time serie")
  parser.add_argument('--radar_list', nargs="+", default='all',         help="List of radars to process")
  parser.add_argument('--inputfiles', nargs="+",   default='undefined', type=str,   help="input sqlite file to average")
  parser.add_argument('--pathin',       default='undefined', type=str,  help="directory where are input sqlite files")
  parser.add_argument('--pathout',      default=os.getcwd(), type=str,  help="where json  files will be put")
  parser.add_argument('--n_cpus',       default=3,           type=int,  help="Number of rays for averaging" )
  parser.add_argument('--averaged',     default='undefined', type=str,  help="setting for averaged" )
  parser.add_argument('--model',       default='HRDPS', type=str,  help="setting for averaged" )

  args = parser.parse_args()
  if args.inputfiles == 'undefined' and args.pathin == 'undefined':
    args.start_date  = '2019061500'
    args.end_date    = '2019071500'

    args.window_width = 6
    #option1: explicitely specify inputfiles
    #args.inputfiles = ['/space/hall4/sitestore/eccc/cmd/a/dlo001/data/doppler_qc/doppler_qc_v0.3/sqlite_v1.0.0_qc/split_6h/USVNX/2019073100_ra',
    #                   '/space/hall4/sitestore/eccc/cmd/a/dlo001/data/doppler_qc/doppler_qc_v0.3/sqlite_v1.0.0_qc/split_6h/CASRA/2019073100_ra']
    #option2: specify pathin + infile_struc and let Python search for files
    #full path of radvelso module
    radvelso_dir = os.path.dirname(radvelso.__file__)
    #root path of radvelso package (one dir up from radvelso module)
    package_dir = os.path.dirname(radvelso_dir)
    #full path of schema we are looking for
    args.pathin = f'{package_dir}/test_data/evaluation'
    args.averaged = 'N10_R10km'
    args.pathin = f'/home/dlo001/RADAR/radvelso/radvelso/evaluation/radvelsoe_all/series_2019061500_2019071500/'
   # args.pathin = f'/fs/homeu1/eccc/cmd/cmda/dlo001/RADAR/radvelso/radvelso/evaluation/test_trials/'
   # args.pathin = '/fs/homeu1/eccc/cmd/cmda/dlo001/RADAR/radvelso/radvelso/evaluation/tt/'
   # args.pathin = '/home/dlo001/data_maestro/eccc-ppp3/maestro_archives/RADAR/banco/bgckalt/'
    args.pathout = './radvelsoe_all'
    args.radar_list = 'all'  
  #  args.radar_list = 'casbv'  
  #  args.radar_list = 'casbv' /home/dlo001/data_maestro/eccc-ppp3/maestro_archives/HDJA900E19DLO_N10_R10km/banco/bgckalt/
    args.timing = False
    args.n_cpus = 40
    print(f'superobs called with no input filename(s)')
    print(f'We are running demo with:')
    for arg in vars(args):
      print(f'--{arg}  {getattr(args, arg)}')

  #argument checking

  if args.start_date == 'undefined':
      raise ValueError('Start date must be provided')
  else:
     args.start_date = datetime.datetime.strptime(args.start_date, '%Y%m%d%H')
 
  if args.end_date == 'undefined':
      raise ValueError('End date must be provided')
  else:
     args.end_date = datetime.datetime.strptime(args.end_date, '%Y%m%d%H')
 
  if args.inputfiles != 'undefined':
    #if inputfiles argument is provided, we use that
    infile_list = args.inputfiles 

  elif args.pathin != 'undefined': 
    #alternatively, search for files with pathin+infile_struc 
    
    if not os.path.isdir(args.pathin):
      print ("args.pathin=",args.pathin)
      raise ValueError(f'pathin: {args.pathin} does not exist.')
    print (f'{args.pathin}/*/sqlite_*')
  
    infile_list = glob.glob(f'{args.pathin}/*/sqlite_*')
    print ( infile_list)
  else: 
    raise ValueError('At least one of inputfiles ot pathin must be provided')

  #check infile_list
  #if len(infile_list) == 0:
  #  raise ValueError('infile_list is empty, we stop here')
 #
 # else:
 ##   for this_file in infile_list:
 #     if not os.path.isfile(this_file):
 #       raise ValueError(f'inputfiles: {this_file} does not exist.')
  if not os.path.isdir(args.pathout):
    os.mkdir(args.pathout)
  #sys.exit is used to the return status of main is catched and passed to caller
  sys.exit(main_plot(args.start_date,
                args.end_date,
                args.radar_list,
                infile_list, 
                args.pathout,
                args.n_cpus,
                args.averaged,
                args.model))

if __name__ == '__main__':
    arg_call()
