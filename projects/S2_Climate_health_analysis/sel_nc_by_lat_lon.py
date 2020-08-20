
import xarray as xr
import numpy as np

def roll_longitude(filename, chunks):
    filetoroll = xr.open_dataset(filename, chunks=chunks)
    lon_name = 'lon'  # whatever name is in the data
    # Adjust lon values to make sure they are within (-180, 180)
    filetoroll['_longitude_adjusted'] = xr.where(
    filetoroll[lon_name] > 180,
    filetoroll[lon_name] - 360,
    filetoroll[lon_name])

    # reassign the new coords to as the main lon coords
    # and sort DataArray using new coordinate values
    filetoroll = (
        filetoroll
        .swap_dims({lon_name: '_longitude_adjusted'})
        .sel(**{'_longitude_adjusted': sorted(filetoroll._longitude_adjusted)})
        .drop(lon_name))
    filetoroll = filetoroll.rename({'_longitude_adjusted': lon_name})
    return filetoroll

mohc = roll_longitude(filename='/badc/cmip6/data/CMIP6/ScenarioMIP/MOHC/UKESM1-0-LL/ssp126/r1i1p1f2/3hr/tas/gn/latest/tas_3hr_UKESM1-0-LL_ssp126_r1i1p1f2_gn_205001010300-210001010000.nc', chunks={'time':120})
darwin = {'name': 'Darwin, Australia', 'lat': -12.45, 'lon': 130.83}
beijing = {'name': 'Beijing, China',   'lat': 39.91,  'lon': 116.3833}
jungfraujoch = {'name': 'Jungfraujoch, Switzerland',   'lat': 46.5,  'lon': 7.6, 'height':3466}
tokyo = {'name': 'Tokyo, Japan',   'lat': 35.45 ,  'lon': 139.45, 'height':0} ##
edmonton = {'name': 'Edmonton, Canada',   'lat': 53.5 ,  'lon': 360-139.45, 'height':0}# 53.5 113.5W
cambridge = {'name': 'Cambridge, UK',   'lat': 52.2 ,  'lon': 0.1218, 'height':0}# 52.2 0.12E




# Find the nearest latitude and longitude for Tokyo
lat_idx = np.abs(mohc.lat - cambridge['lat']).argmin()
lon_idx = np.abs(mohc.lon - cambridge['lon']).argmin()


uk_temps = mohc.isel(lat = lat_idx, lon=lon_idx)
uk_temps.to_netcdf('CBG_2050_2100.nc')
