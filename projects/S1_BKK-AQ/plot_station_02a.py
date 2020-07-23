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
# %%
import socket
print(socket.gethostname())
#%%%
sns.set_style('darkgrid')
# sns.set_context('talk')
ax.yaxis.grid(True) # Show the horizontal gridlines
ax.xaxis.grid(True) # Show the vertical gridlines

#%%
debug=False
#%%
matplotlib.rcParams['axes.grid'] = True
matplotlib.rcParams['axes.grid.which'] = 'both'
matplotlib.rcParams['xtick.minor.visible'] = True
# %%
# data processing on processed data - station data from another R script [TODO: add ref]
station_02a  = feather.read_dataframe('../bkk_aq_df_processed_data/bkk_df1.feather')
station_02a.index = pd.to_datetime(station_02a.dtLong, format='%Y-%m-%d %H:%M:%S')
station_02a.index = pd.Index.rename(station_02a.index, 'local_time')
station_02a.drop('dtLong',axis=1, inplace=True)

if debug:
    station_02a.head()# %%
#%%

# %%
fig, ax = plt.subplots(figsize=(20,5))
station_02a['NO'].plot(ax=ax )# alpha=0.4
ax.set_xlim([datetime.date(2014, 1, 1), datetime.date(2014, 12, 31)])
ax.set_ylim(0,250)
ax.set_xlabel('Local Time')
ax.set_ylabel('Ozone mixing ratio / ppbv')

# %%
fig, ax = plt.subplots(figsize=(20,5))
mm_02a_no = station_02a['NO'].groupby(by=[station_02a.index.year, station_02a.index.month])
mm_02a_no.plot(ax=ax,lw=1)
ax.set_xlim([datetime.date(2014, 1, 1), datetime.date(2014, 12, 31)])

# %%
# calculate trend in 95%-ile in monthly mean data
# think this is a group by and then apply to each group and return in another DF
mm_02a_no = station_02a['NO'].groupby(by=[station_02a.index.year, station_02a.index.month])
mm_02a_no

# something along lines of 
#[station_02a['NO']> station_02a['NO'].quantile(0.995)].count()