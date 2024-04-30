#!/usr/bin/python3

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

def avg_std_all(file_list,
                pathout,
                this_radar,
                start_date,
                end_date,
               
                setting_average):

  """ STD and AVG for a time series

  This function calculates the STD and AVG for a time series.

  args:
    file_list                : list of json file to joint 
    pathout                  : output json file for a time series per radar and elevation
    this radar               : name of radar to evaluated
    start_date               : start date of the time series
    end_date        :         : end date of the time series

  output:
    This function outputs nothing

  """

  ppi_list = glob.glob(f"{file_list}/*")
  SUM_RangeXNumber_obs = []
  SUM_HXNumber_obs     = []
  SUM_AVGOMPXNumber_obs   = []
  SUM_STDOMP2XNumber_obs = []
  SUM_Number_obs = []
  result_serie = []
  Ranges_obs = []
  Height_obs = []
  SUM_AVGNYQUIST = []
  if not os.path.isdir(pathout):
      os.makedirs(pathout)
  # Loop of json files for the time series 
  for this_ppi in ppi_list:
    with open(this_ppi) as json_file:
      data = json.load(json_file)
      for dataLevel in data:
        if dataLevel['AVGompomp_AVGompomp']!=None:
          LevelObs  = np.where(Ranges_obs == round(dataLevel['RANGE'],0))[0]
          if LevelObs.size != 0:
            SUM_Number_obs[LevelObs]         += dataLevel['Number_obs']
            SUM_AVGOMPXNumber_obs[LevelObs]  += dataLevel['AVGomp']*dataLevel['Number_obs']
            SUM_STDOMP2XNumber_obs[LevelObs] += (dataLevel['AVGompomp_AVGompomp']**2+dataLevel['AVGomp']**2)*dataLevel['Number_obs']
            SUM_AVGNYQUIST[LevelObs]         += dataLevel['AVGNYQUIST']*dataLevel['Number_obs']

          else:
            Ranges_obs = np.append(Ranges_obs,round(dataLevel['RANGE'],0))
            Height_obs = np.append(Height_obs, dataLevel['VCOORD'])
            SUM_Number_obs         = np.append(SUM_Number_obs, dataLevel['Number_obs'])
            SUM_AVGOMPXNumber_obs  = np.append(SUM_AVGOMPXNumber_obs, dataLevel['AVGomp']*dataLevel['Number_obs'])
            SUM_AVGNYQUIST         = np.append(SUM_AVGNYQUIST, dataLevel['AVGNYQUIST']*dataLevel['Number_obs'])
            SUM_STDOMP2XNumber_obs = np.append(SUM_STDOMP2XNumber_obs, (dataLevel['AVGompomp_AVGompomp']**2+dataLevel['AVGomp']**2)*dataLevel['Number_obs'])
  # It is possible that OMP has no value according to the expected tests.
  if len(Ranges_obs)!=0:

    str_end_date   = end_date.strftime('%Y%m%d%H')
    str_start_date = start_date.strftime('%Y%m%d%H')
    str_elevavion  = os.path.basename(pathout)[10::]
    namefileout = f'{this_radar}_{str_start_date}_{str_end_date}_e_{str_elevavion}_nmobs_{setting_average}_json'

    if not os.path.isdir(pathout):
      os.makedirs(pathout)


    Range  = Ranges_obs
    Height = Height_obs
    AVGOMP = SUM_AVGOMPXNumber_obs/SUM_Number_obs 
    STDOMP = np.sqrt(SUM_STDOMP2XNumber_obs/SUM_Number_obs-(AVGOMP)**2)
    AVGNYQUIST = SUM_AVGNYQUIST/SUM_Number_obs 
    inds = Range.argsort()
    sortedRange  = Range[inds]
    sortedHeight = Height[inds] 
    sortedAVGOMP = AVGOMP[inds] 
    sortedSTDOMP = STDOMP[inds]
    sortedSUM_Number_obs = SUM_Number_obs[inds]
    sortedAVGNYQUIST = AVGNYQUIST[inds]
 
    for i in range(0,len(sortedRange)):
    #  print (sortedRange[i],sortedHeight[i],sortedAVGOMP[i],sortedSTDOMP[i],sortedSUM_Number_obs[i])  

      result_serie.append( {'Range':sortedRange[i], 
                            'Height':sortedHeight[i],
                            'AVGOMP':sortedAVGOMP[i], 
                            'STDOMP':sortedSTDOMP[i], 
                            'Number_obs':sortedSUM_Number_obs[i], 
                            'AVGNYQUIST':sortedAVGNYQUIST[i] } )
    # Saving data in JSON format 
    path_json = f"{pathout}/{namefileout}"
    with open(path_json, 'w') as f:
      json.dump(result_serie, f)

def avg_std_one(this_file,
                this_radar,
                this_elevation,
                this_date,
                start_date,
                end_date,
                
                pathout,
                setting_average):
  """  STD and AVG for PPI

  This function calculates the STD and AVG for one PPI

  args:
    this_file                : sqlite file where is the PPI
    pathout                  : output json file for a time series 
    this_radar               : name of radar to evaluated
    start_date               : start date of the time series
    end_date                 : end date of the time series

  output:
    This function outputs nothing

  """
  
  str_this_date  = this_date.strftime('%Y%m%d%H')
  str_end_date   = end_date.strftime('%Y%m%d%H')
  str_start_date = start_date.strftime('%Y%m%d%H')
  str_elevavion  = round(this_elevation,1) 
  namefileout = f'{this_radar}_{str_start_date}_{str_this_date}_{str_end_date}_e_{str_elevavion}_{setting_average}_json'
  pathfileout=(f"{pathout}/{this_radar}/elevation_{str_elevavion}/{namefileout}")
  #Prepare file in memory
  filememory=f'file:{namefileout}?mode=memory&cache=shared'


  # https://tools.ietf.org/html/rfc3986  Uniform Resource Identifier (URI)
  # The advantage of using a URI filename is that query parameters on the
  # URI can be used to control details of the newly created database connection in parallel
  conn = sqlite3.connect(filememory,uri=True)
  conn.execute("pragma temp_store = 2;")
  conn.execute("""PRAGMA journal_mode=OFF;""")
  conn.execute("""PRAGMA synchronous=OFF;""")

  schema = radvelso.find_schema('schema')
  with open(schema) as f:
                 schema = f.read()
  conn.executescript(schema)
  
  conn.execute("ATTACH DATABASE ? AS db_all",( this_file,)) 
  #zero padded string 020100
#  hhmiss_pad =  this_date.strftime('%H%M%S') 
  #no zeros on left but still 0 if 000000
#  hhmiss_nopad = str(int(hhmiss_pad))
  tc_s3 = time.time()

  order_sql = """ insert into header 
                  select 
                    ID_OBS integer, LAT, LON real, CODTYP integer, DATE, TIME, ID_STN, LOCATION, ANTENNA_ALTITUDE, TIME_START, TIME_END, RANGE_START, RANGE_END, CENTER_AZIMUTH, CENTER_ELEVATION, NOMINAL_PPI_ELEVATION,  NYQUIST 
                  from
                    db_all.header 
                  natural join db_all.data
                    
                  where 
                    round(nominal_ppi_elevation,1) = ? 
                    and flag=4096
                    and id_stn like ?  """
  conn.execute( order_sql,(round(float(this_elevation),1),this_radar)) 
  #select associated data entries

  order_sql =""" insert into data  
                    select
                      *
                    from
                      db_all.data
                    where
                      id_obs in ( select 
                                    id_obs
                                  from header) """
  conn.execute(order_sql)
  conn.commit()
  order_sql =""" select distinct 
                   RANGE 
                 from  
                   data order by 1 ;"""
  ranges_values = conn.execute(order_sql).fetchall()
  vol_scan_result = []
  for range in ranges_values:
    print (range)
    # STDEV = SQRT( round(((sum(omp)*sum(omp) - sum(omp * omp))/((count(*)-1)*(count(*)))),3))
    # STDEV = SQRT( AVG(omp*omp) - AVG(omp)*AVG(omp)
    order_sql ="""select 
                  sqrt(AVG(omp*omp) - AVG(omp)*AVG(omp)), avg(omp), range, vcoord, count(*), AVG(NYQUIST) 
                  --  sqrt(AVG(omp*omp) - AVG(omp)*AVG(omp)), avg(omp), range, vcoord-ANTENNA_ALTITUDE, count(*), AVG(NYQUIST) 

                  from 
                    header natural join data 
                  where 
                    abs(range-?) < .1 ;"""
    for  AVGompomp_AVGompomp, AVGomp, RANG, VCOORD, Number_obs, AVGNYQUIST in conn.execute(order_sql,(range[0],)):
      if AVGomp!=None:
        
        vol_scan_result.append({'AVGompomp_AVGompomp':AVGompomp_AVGompomp, 'AVGomp':AVGomp,
                                'RANGE':range[0], 'VCOORD':VCOORD, 'Number_obs':Number_obs, 'AVGNYQUIST':AVGNYQUIST } )


  conn.close()

  # Saving data in JSON format s
  with open(pathfileout, 'w') as f:
    json.dump(vol_scan_result, f)




def avg_std_plot(path,
                 this_radar,
                 start_date,
                 end_date,
                 
                 setting_average):

  """ Plot AVG and STD in fuction range/height per elevation for time series
  
  args:
    path              : path to json files of time series
    this_radar        : name of radar
    start_date        : start date of the time series
    end_date          : end date of the time series

  output:
    This function outputs nothing

  """
  from os.path import basename,splitext
  import matplotlib as mpl
  mpl.use('Agg')
  import pylab
  import matplotlib.pyplot as plt
  from matplotlib import cm

  ppi_list=glob.glob(f"{path}/elevation_*")
  ppi_list=sorted(glob.glob(f"{path}/elevation*"), key=os.path.getmtime)
  try:
     ppi_list.sort(key=lambda x: float(os.path.basename(x)[10::]))
  except:
     print ("elevation all")
  setting_average_in = setting_average
  ################################################
  # Configuration of the imagen
  ################################################

  # matplotlib global settings
  # mpl.rcParams.update({'font.size': 18}
  # Use this for editable text in svg
  mpl.rcParams['figure.dpi'] = 150
  mpl.rcParams['text.usetex']  = False
  mpl.rcParams['svg.fonttype'] = 'none'
  mpl.rcParams.update({'font.size': 25})

  legendlist_all= []
  left=0.1
  width=0.3
  bottomn =0.3

  fig_all_range = plt.figure(figsize=(27,17))
  ax_all_range = plt.axes([left, bottomn, width, 0.6])
  
  fig_all_height = plt.figure(figsize=(27,17))
  ax_all_height = plt.axes([left, bottomn, width, 0.6])
  ss=0.05
  ss_all=0.05
  cc_all=0.05
  cc_all1=0.05
  cc_all2=0.05
  cc_all3=0.05
  cc_all4=0.05
  cc_all5=0.05


  import matplotlib.pyplot as pltt
  levels_color = 19
  cmap =pltt.cm.get_cmap('gist_ncar', levels_color)
  cmap = plt.cm.get_cmap('tab20')
  modesave=False
  cc_all =0
  for path_source in  ppi_list:
    fig1 = plt.figure(figsize=(27,17))
    ax1 = plt.axes([left, bottomn, width, 0.6])

    fig4 = plt.figure(figsize=(27,17))
    ax4 = plt.axes([left, bottomn, width, 0.6])

    fig6 = plt.figure(figsize=(27,17))
    ax6 = plt.axes([left, bottomn, width, 0.6])

    fig7 = plt.figure(figsize=(27,17))
    ax7 = plt.axes([left, bottomn, width, 0.6])
 
    fig8 = plt.figure(figsize=(27,17))
    ax8 = plt.axes([left, bottomn, width, 0.6])

    fig9 = plt.figure(figsize=(27,17))
    ax9 = plt.axes([left, bottomn, width, 0.6])



    legendlist = []
    legendlist_ave = []
    legendlist_ave1 = []
    setting_average = 'N10_R10km'
    cc_x1 =0

    cc_x4 =0
    cc_x6 =0
    cc_x7 =0
    cc_x8 =0
    cc_x9 =0
    #cc_all =0
    print ('pathsource',path_source)
    #apath_source = "evaluation_congress/plot_2019062700_2019062700/*/elevation_0.4"
    print ('--->in')
    for path_json in   glob.glob(f"{path_source}/*_json"):
      print (path_json)

      modesave=True
      cc=cmap(cc_all/levels_color)
       
      AVGNYQUIST =evaluation_plot(cc, ss_all, ax_all_range, path_source,setting_average_in, path_json,scale_nobs=False, Rangemode= True, Heightmode= False) 
      AVGNYQUIST =evaluation_plot(cc, ss_all, ax_all_height, path_source, setting_average_in,path_json,scale_nobs=False, Rangemode= False, Heightmode=True)
      cc_all=cc_all+1
      print ("cc_all/levels_color=",cc_all ,cc_all/levels_color)
      AVGNYQUIST =evaluation_plot(cc, ss, ax1, path_source, setting_average_in,path_json,scale_nobs=True, Rangemode= True, Heightmode= False)
      AVGNYQUIST =evaluation_plot(cc, ss, ax4, path_source, setting_average_in,path_json,scale_nobs=True, Rangemode= False, Heightmode= True)

      AVGNYQUIST =evaluation_plot(cc, ss, ax6, path_source, setting_average_in,path_json,scale_nobs=True, Rangemode= True, Heightmode= False)
      AVGNYQUIST =evaluation_plot(cc, ss, ax7, path_source, setting_average_in,path_json,scale_nobs=True, Rangemode=False, Heightmode= True)

    legendlist.append(f'BIAS ele={os.path.basename(path_source)[10::]}, Nyquiste={round(AVGNYQUIST,0)}')
    legendlist.append(f'STDDEV ele={os.path.basename(path_source)[10::]}, Nyquiste={round(AVGNYQUIST,0)}')
    legendlist_all.append(f'BIAS ele={os.path.basename(path_source)[10::]}, Nyquiste={round(AVGNYQUIST,0)}')
    legendlist_all.append(f'STDDEV ele={os.path.basename(path_source)[10::]}, Nyquiste={round(AVGNYQUIST,0)}')


    legendlist_ave.append(f'BIAS ele={os.path.basename(path_source)[10::]}, Nyquiste={round(AVGNYQUIST,0)}')
    legendlist_ave.append(f'STDDEV ele={os.path.basename(path_source)[10::]}, Nyquiste={round(AVGNYQUIST,0)}')
    
    



 

   







    elevation = f'{os.path.basename(path_source)[10::]}'

    if modesave:
      surname = f'{setting_average_in}'

      plot_close(ax1, 
                fig1, 
                legendlist, 
                path_source, 
                elevation, 
                start_date,
                end_date, 
                this_radar,
                surname,
                scale_nobs=True,
                Rangemode=True,
                Heightmode=False)
      plt.close(fig1)
      

      plot_close(ax4, 
                fig4,
                legendlist, 
                path_source,
                elevation,
                start_date, 
                end_date, 
                this_radar,  
                surname,
                scale_nobs=True,
                Rangemode=False, 
                Heightmode=True)
      plt.close(fig4)
      plot_close(ax6, 
                fig6, 
                legendlist, 
                path_source, 
                elevation, 
                start_date,
                end_date, 
                this_radar,
                surname,
                scale_nobs=True,
                Rangemode=True,
                Heightmode=False)
      plt.close(fig6)
      

      plot_close(ax7, 
                fig7,
                legendlist, 
                path_source,
                elevation,
                start_date, 
                end_date, 
                this_radar,  
                surname,
                scale_nobs=True,
                Rangemode=False, 
                Heightmode=True)
      plt.close(fig7)
      
      surname = f'{setting_average_in}'



      


  elevation='all'
  path_source=f'{path}/elevation_all'
  if modesave:
    if not os.path.isdir(path_source):
      os.makedirs(path_source)
    surname = f'{setting_average_in}'
  
    plot_close(ax_all_range, 
              fig_all_range,
              legendlist_all,
              path_source,
              elevation,
              start_date, 
              end_date, 
              this_radar,
              surname,
              scale_nobs=False,
              Rangemode= True, 
              Heightmode = False)
    plt.close(fig_all_range)
    surname = f'{setting_average_in}'
    plot_close(ax_all_height,
               fig_all_height,
               legendlist_all,
               path_source, 
               elevation, 
               start_date,
               end_date, 
               this_radar, 
               surname,
               scale_nobs=False,
               Rangemode = False,
               Heightmode= True)
    plt.close(fig_all_height)
    plt.close('all')
def plot_close(ax, 
              fig, 
              legendlist,
              path_source, 
              elevation,
              start_date, 
              end_date, 
              this_radar, 
              surname,
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
    ax.set_xlabel('[m/s]', fontsize=20)
    if Rangemode:
        ax.set_ylabel('RANGE [km]',fontsize=20)
        type_x ='range' 
        ax.set_xlim(-10,10)
        numeros_x= [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
        ax.set_xticks(numeros_x)
        ax.set_ylim(0,250)

    if Heightmode:
        ax.set_ylabel('HEIGHT [km]',fontsize=20)
        type_x ='height'
        ax.set_xlim(-10,10)
        numeros_x= [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
        ax.set_xticks(numeros_x)
        numeros_y= [0,1,2,3,4,5,6,7,8,9,10,11,12,14,13,15,16,17,18,19,20]
        ax.set_yticks(numeros_y)
        ax.set_ylim(0,20)



    ax.set_title(f"{start_date.strftime('%Y%m%d%H')}-{end_date.strftime('%Y%m%d%H')}  ({this_radar})" )#,fontsize=18)
  #  ax.legend(legendlist,prop={'size':14},loc=4) 
    # Shrink current axis's height by 10% on the bottom
  #  box = ax.get_position()
  #  ax.set_position([box.x0, box.y0 + box.height * 0.1,
  #               box.width, box.height * 0.9])

    # Put a legend below current axis
    ax.legend(legendlist,prop={'size':18},loc='upper center', bbox_to_anchor=(1.3, -0.1), ncol=4)
  # ax.legend(legendlist,prop={'size':14}, bbox_to_anchor=(0.5, -0.05))
    str_end_date   = end_date.strftime('%Y%m%d%H')
    str_start_date = start_date.strftime('%Y%m%d%H')
    namefileout = f'{type_x}_{this_radar}_{str_start_date}_{str_end_date}_e_{elevation}_{surname}'


    fig.savefig(f"{path_source}/{namefileout}.svg", dpi=40, format='svg')
    fig.savefig(f"{path_source}/{namefileout}.png", dpi=40, format='png')
    

def evaluation_plot(cc, ss, ax, pathfileout, setting_average, path_json,scale_nobs=True,Rangemode=False,Heightmode=False,):

    from matplotlib import cm
    """ evaluation_plot
  
    Graphical generation from json files

    args:
    cc                 : coulor line
    ss                 : position number obs in images
    ax                 : plot
    pathfileout        : path to out the images
    path_json          : source of json
    Rangemode          : setting for range images
    Heightmode         : setting for height images 

    output:
      This function outputs nothing

    """


   # import matplotlib as mpl
   # mpl.use('Agg')
   # import pylab
   # import matplotlib.pyplot as plt
   # from matplotlib import cm
    with open(path_json) as json_file:
      data = json.load(json_file)
    stdevOMP = np.array([ p['STDOMP']  for p in data])
    avgOMP   = np.array([ p['AVGOMP']  for p in data])
    AVGNYQUIST = np.array([ p['AVGNYQUIST']  for p in data])

    if Rangemode:
      xx       = np.array([ p['Range']  for p in data])
      ax.set_ylim(0,250)

    if Heightmode:
      xx       = np.array([ p['Height']  for p in data])
      ax.set_ylim(0,20)

    nn       = [ p['Number_obs'] for p in data]

    
    ax.plot( avgOMP   , xx/1000, color= cc, linestyle='-', marker='x',ms=10,linewidth=2.0)
    ax.plot( stdevOMP , xx/1000, color= cc, linestyle='--' , marker='x',ms=10,linewidth=2.0)
    if scale_nobs:
     
      if setting_average == 'N10_R10km':
        n = 1
      if setting_average == 'N20_R5km':
        n=2
      if setting_average == 'N30_R2_5km':
        n=3   
      xlim=ax.get_xlim()
      n = 1

      datapt=[]
      print ('xx',xx)
      print ('nn',nn)
      print ('avgOMP',avgOMP)
      for y in  range(0,len(xx)):
        datapt.append(( xlim[1]  , xx[y]/1000 ) )
      print ( 'datapta=',datapt)
      data_to_display = ax.transData.transform
      display_to_ax = ax.transAxes.inverted().transform
      #if ( len(datapt) > 0):
      ax_pts = display_to_ax(data_to_display(datapt))
      count = 0
      print (xx)
      for y in  range(0,len(xx),n):
        
        #index,value =min(enumerate(xx), key=lambda x: abs(x[1]-xx[y]))
        #sumNtot=np.sum(nn[count:index])
        ix,iy=ax_pts[y]
        if int(nn[y])>0:
          ax.text(ix+ss, iy, int(nn[y]) , fontsize = 20, color= cc, transform=ax.transAxes )
        #count = index
    return AVGNYQUIST[0]

def main(start_date,
         end_date,
         desired_radar_list,
         infile_list, 
         pathoutwork, 
         n_cpus,
         setting_average):
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
  #################################################################################################
  # launch evaluation_one_6h: STD and AVG for all PPI in a time series
  #################################################################################################
  tc_0 = time.time()
  evaluation_one_6 = True
  evaluation_one_6_clobber = False
  import shutil 
  pathout_serie=f"{pathoutwork}/series_{start_date.strftime('%Y%m%d%H')}_{end_date.strftime('%Y%m%d%H')}/"
  if evaluation_one_6:


    if evaluation_one_6_clobber:
      if os.path.isdir(pathout_serie):
        shutil.rmtree(pathout_serie)
    if not os.path.isdir(pathout_serie):
      os.makedirs(pathout_serie)
    # make list of files, radars and times that will be processed in parallel
    infile_list.sort()
    for this_file in infile_list:
    # if this_file not in file_control:
      this_date = datetime.datetime.strptime(os.path.basename(this_file)[0:10], '%Y%m%d%H')
      if (this_date >= start_date) and (this_date <= end_date):


        vol_scan_list = []

        tc_0 = time.time()
          
        with sqlite3.connect(this_file) as conn_loops:
          avail_radar_list = [stn[0] for stn in conn_loops.execute("SELECT distinct ID_STN FROM header ORDER BY 1;").fetchall()]
          
          conn_loops.execute("pragma temp_store = 2;")
          conn_loops.execute("""PRAGMA journal_mode=OFF;""")
          conn_loops.execute("""PRAGMA synchronous=OFF;""")

          # Correct the index creation statements
          conn_loops.execute("CREATE INDEX IF NOT EXISTS times ON header (time);")
          conn_loops.execute("CREATE INDEX IF NOT EXISTS reles ON header (NOMINAL_PPI_ELEVATION);")
      #    conn_loops.execute("CREATE INDEX IF NOT EXISTS radar ON header (ID_STN);")

          # list of radars in the file
        
        
          avail_radar_list=desired_radar_list
          for this_radar in avail_radar_list:
          #select radars if desired radar_list is specified
            if desired_radar_list != 'all' or desired_radar_list == 'c%' or desired_radar_list == 'u%'   :
              print ("david")
              #if this_radar not in desired_radar_list:
              #  continue
              order_sql = f"""select distinct nominal_ppi_elevation from header where ID_STN like '{desired_radar_list[0]}' 
                    and  round(nominal_ppi_elevation,1) != 3.5
                    and  round(nominal_ppi_elevation,1) != 2.5
                    and  round(nominal_ppi_elevation,1) != 4.5
                    and  round(nominal_ppi_elevation,1) > 0;"""
             # print (order_sql)
              nominal_ppi_elevation_list = [nominal_ppi_elevation[0] for nominal_ppi_elevation in conn_loops.execute(order_sql).fetchall() ]
              for this_elevation in nominal_ppi_elevation_list:
                  
                
            
                  str_this_date  = this_date.strftime('%Y%m%d%H')
                  str_end_date   = end_date.strftime('%Y%m%d%H')
                  str_start_date = start_date.strftime('%Y%m%d%H')
                  str_elevavion  = round(this_elevation,1) 
                  pathout_serie_number_min_obs=f"{pathout_serie}/{this_radar}/elevation_{round(this_elevation,1)}/"
                  if not os.path.isdir(pathout_serie_number_min_obs):
                    os.makedirs(pathout_serie_number_min_obs)
       
                  #pathfileout=f"{pathout_serie_number_min_obs}/{this_radar}_{str_start_date}_{str_this_date}_{str_end_date}_e_{str_elevavion}_nmobs_{number_min_obs}_{setting_average}_json"
                  #if not os.path.isfile(pathfileout):
                  vol_scan_list.append( {'file':this_file, 
                                         'radar':this_radar,
                                         'nominal_ppi_elevation':this_elevation,
                                         'start_date':start_date,
                                         'this_date': this_date,
                                         'end_date':end_date,
                                         
                                         'setting_average': setting_average})
      
        tc_1 = time.time()
        print (vol_scan_list)

      #  sys.exit()
        print(f"Runtime list  total: {round(tc_1-tc_0,4)} s")

        print ("launch avg_std_one: STD and AVG for all PPI in a time series")
        if len(vol_scan_list)>0:
         
         if n_cpus == 1:
           #serial execution, usefull for debugging
           for vscan in vol_scan_list:
             avg_std_one(vscan['file'], vscan['radar'], vscan['nominal_ppi_elevation'], vscan['this_date'],
                      vscan['start_date'], vscan['end_date'],  pathout_serie, vscan['setting_average']) 
         else:
           print (colored(f'Computed {len(vol_scan_list)} PPI in parallel ', 'green'))
           with tempfile.TemporaryDirectory() as tmpdir:
             #the directory dask-worker-space/ will be in tmpdir
             with dask.distributed.Client(processes=False, threads_per_worker=1, 
                                         n_workers=n_cpus, 
                                         local_directory=tmpdir, 
                                         silence_logs=40) as client:
               #delay data 
               joblist = [delayed(avg_std_one)(vscan['file'], vscan['radar'], vscan['nominal_ppi_elevation'],
                                            vscan['this_date'], vscan['start_date'], vscan['end_date'], 
                                            pathout_serie, vscan['setting_average']) for vscan in vol_scan_list]
               dask.compute(joblist)
       
       #file_control=np.append(file_control, this_file)
      #  save(f'file_control_radvelsoe/file_control_{desired_radar_list}_{setting_average}', file_control)



#       tc_2 = time.time()
 #       print(f"Runtime  total: {round(tc_2-tc_1,4)} s")
  
  #################################################################################################
  # launch avg_std_all:  STD and AVG for time series
  #################################################################################################
  tc_0 = time.time()
  evaluation_all_one_6= True
  evaluation_all_one_6_clobber=True
  pathout_plot = f"{pathoutwork}/plot_{start_date.strftime('%Y%m%d%H')}_{end_date.strftime('%Y%m%d%H')}"
  #sys.exit()
  if evaluation_all_one_6:
    if evaluation_all_one_6_clobber:

      if os.path.isdir(pathout_plot):
        shutil.rmtree(pathout_plot)

   
      radar_list = glob.glob(f'{pathout_serie}/*')
      file_list=[]
      for this_radar in radar_list:
        this_radar=os.path.basename(this_radar)

        if desired_radar_list != 'all' or desired_radar_list == 'u%' or desired_radar_list == 'c%' :

          if this_radar not in desired_radar_list:
             continue
      
        ppi_list = glob.glob(f'{pathout_serie}/{this_radar}/*')
        for this_ppi in ppi_list:


          pathout = f"{pathout_plot}/{this_radar}/{os.path.basename(this_ppi)}/"
          file_list.append( {'file':this_ppi,'pathout':pathout,'radar':this_radar,'start_date':start_date,'end_date':end_date, 'setting_average': setting_average})
      # avg_std_all
      if n_cpus == 1:
        #serial execution, usefull for debugging
        print (file_list)
      #  sys.exit()
        for ppi in file_list:
          avg_std_all(ppi['file'], 
                      ppi['pathout'], 
                      ppi['radar'], 
                      ppi['start_date'],
                      ppi['end_date'],
                     
                      ppi['setting_average'] ) 
      else: 
        print (colored(f'Computed {len(file_list)} VS in parallel for time serie ', 'green'))
        with tempfile.TemporaryDirectory() as tmpdir:
        #the directory dask-worker-space/ will be in tmpdir
          with dask.distributed.Client(processes=True, threads_per_worker=1, 
                                     n_workers=n_cpus, 
                                     local_directory=tmpdir, 
                                     silence_logs=40) as client:
#
#            #delay data 
            joblist = [delayed(avg_std_all)(ppi['file'], 
                                            ppi['pathout'],
                                            ppi['radar'],
                                            ppi['start_date'], 
                                            ppi['end_date'], 
                                            
                                            ppi['setting_average']) for ppi in file_list]
            dask.compute(joblist)
    
  tc_1 = time.time()
  print(f"Runtime otal: {round(tc_1-tc_0,4)} s")
  
  #################################################################################################
  # launch avg_std_plot: Plot AVG and STD in fuction of range/height  per elevation of the time series
  #################################################################################################
  
  tc_0 = time.time()
  evaluation_plot = True
  if  evaluation_plot:

    radar_list = glob.glob(f'{pathout_plot}/*')
    file_list=[]
    radar_ele = []
    radar_ = []
    print ('daviddd',radar_list)
    for this_radar in radar_list:
      this_radar=os.path.basename(this_radar)
      if desired_radar_list != 'all' or desired_radar_list == 'c%' or desired_radar_list == 'u%' :
        if this_radar not in desired_radar_list:
           continue
      pathout=f'{pathout_plot}/{this_radar}'
      print (pathout)
      if not os.path.isdir(pathout):
           os.mkdir(pathout)
     
      file_list.append( {'pathout':pathout ,
                         'radar'  :this_radar,
                         'start_date':start_date,
                         'end_date':end_date,
                        
                         'setting_average': setting_average})
         

    n_cpus = 1
    if n_cpus == 1:
        #serial execution, usefull for debugging
        for ppi in file_list:
         
          avg_std_plot(ppi['pathout'],
                       ppi['radar'],
                       ppi['start_date'],
                       ppi['end_date'], 
                       ppi['setting_average']) 
    else:
        print (colored(f'Compute {len(file_list)} radar in parallel for plotting', 'green'))
        with tempfile.TemporaryDirectory() as tmpdir:
          #the directory dask-worker-space/ will be in tmpdir
          with dask.distributed.Client(processes=True, threads_per_worker=1, 
                                     n_workers=n_cpus, 
                                     local_directory=tmpdir, 
                                     silence_logs=40) as client:

            #delay data 
            joblist = [delayed(avg_std_plot)(ppi['pathout'],
                                             ppi['radar'], 
                                             ppi['start_date'], 
                                             ppi['end_date'], 
                                           
                                             ppi['setting_average']) for ppi in file_list]
            dask.compute(joblist)
  #sys.exit(0)    
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

  args = parser.parse_args()
  if args.inputfiles == 'undefined' and args.pathin == 'undefined':
    args.start_date  = '2019080100'
    args.end_date    = '2019081600'

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
    args.pathin = f'/home/dlo001/data_maestro/eccc-ppp3/maestro_archives/DJA900E19DLO_{args.averaged}/banco/bgckalt/'
   # args.pathin = f'/fs/homeu1/eccc/cmd/cmda/dlo001/RADAR/radvelso/radvelso/evaluation/test_trials/'
   # args.pathin = '/fs/homeu1/eccc/cmd/cmda/dlo001/RADAR/radvelso/radvelso/evaluation/tt/'
   # args.pathin = '/home/dlo001/data_maestro/eccc-ppp3/maestro_archives/RADAR/banco/bgckalt/'
    args.pathout = './radvelsoe_work'
  #  args.radar_list = 'all'  
    args.radar_list = 'casbv' 
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
    print ( f'{args.pathin} david' )
    if not os.path.isdir(args.pathin):
      raise ValueError(f'pathin: {args.pathin} does not exist.')
    infile_list = glob.glob(f'{args.pathin}/*radar')
    print (f'{args.pathin}/*radar')
  else:
    raise ValueError('At least one of inputfiles ot pathin must be provided')

  #check infile_list
  if len(infile_list) == 0:
    raise ValueError('infile_list is empty, we stop here')

  else:
    for this_file in infile_list:
      if not os.path.isfile(this_file):
        raise ValueError(f'inputfiles: {this_file} does not exist.')
  if not os.path.isdir(args.pathout):
    os.mkdir(args.pathout)
  #sys.exit is used to the return status of main is catched and passed to caller
  sys.exit(main(args.start_date,
                args.end_date,
                args.radar_list,
                infile_list, 
                args.pathout,
                args.n_cpus,
                args.averaged))

if __name__ == '__main__':
    arg_call()
