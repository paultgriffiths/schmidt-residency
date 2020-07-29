# %%%
# exploration of BKK AQ dataset
# feather to improve R-python interoperability 
# https://blog.rstudio.com/2016/03/29/feather/
import pylab as plt
import feather
import pandas as pd
import datetime
import seaborn as sns
import matplotlib
import numpy as np
# %%
import socket
host = socket.gethostname()
print(host)
if host=='ptg21.local':
    disk='/Users/ptg21/Github/schmidt-residency/projects/S1_BKK-AQ/'
datapath = disk + '' #FIXME
figpath = disk + '/figs/'

#%%%
sns.set_style('darkgrid')


#%%
debug=False
#%%
matplotlib.rcParams['axes.grid'] = True
matplotlib.rcParams['axes.grid.which'] = 'both'
matplotlib.rcParams['xtick.minor.visible'] = False
# %%
# data processing on processed data - station data from another R script [TODO: add ref]
station_02a  = feather.read_dataframe(disk+'/bkk_aq_df_processed_data/bkk_df1.feather')
station_02a.index = pd.to_datetime(station_02a.dtLong, format='%Y-%m-%d %H:%M:%S')
station_02a.index = pd.Index.rename(station_02a.index, 'local_time')
station_02a.drop('dtLong',axis=1, inplace=True)

if debug:
    station_02a.head()# %%
#%%

# %%
fig, ax = plt.subplots(figsize=(20,5), dpi=200.)
station_02a['O3'].plot(ax=ax )# alpha=0.4
ax.set_xlim([datetime.date(2014, 4, 1), datetime.date(2016, 4, 1)])
ax.set_xlabel('Local Time')
ax.set_ylabel('Ozone mixing ratio / ppbv')
ax.set_ylim(0,125)
# sns.set_context('talk')
ax.yaxis.grid(True) # Show the horizontal gridlines
ax.xaxis.grid(True) # Show the vertical gridlines

# %%
fig, ax = plt.subplots(figsize=(20,5))
mm_02a_o3 = station_02a['O3'].groupby(by=pd.Grouper(freq="M"))
mm_02a_o3.plot(ax=ax,lw=1)
mm_02a_o3.aggregate(Mean=('O3', 'mean')).plot(ax=ax, lw=5, color='k')
ax.set_xlim([datetime.date(2013, 7, 1), datetime.date(2016, 12, 30)])
ax.set_xlabel('Local Time')
ax.set_ylim(0,125)
ax.set_ylabel('Ozone level / ppb')
# sns.set_context('talk')
ax.yaxis.grid(True) # Show the horizontal gridlines
ax.xaxis.grid(True) # Show the vertical gridlines
plt.title('BKK shows worse air quality in the dry season - Nov-Feb')
plt.savefig(figpath+'/BKK_Station_02a_grouped_by_yrs_months.png')

# %%
# calculate trend in 95%-ile in monthly mean data
# think this is a group by and then apply to each group and return in another DF
# this gets into terrible trouble when plotting as the x-axis is two-level, month and year, which 
# is not a datetime object
mm_02a_o3 = station_02a['O3'].groupby(by=[station_02a.index.year, station_02a.index.month])
mm_02a_o3.unstack(level=0).plot() # for more details