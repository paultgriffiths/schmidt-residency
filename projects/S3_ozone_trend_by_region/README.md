# work on exploratory analysis of ESGF data archive

For now looking at ozone trends using geopandas to aggregrate regular lat-lon gridded data by country, uses monthly mean data to look for regions with largest trend.


### Install

#### Basic

```
conda create -n climate_ml python==3.7
conda install pandas xmltodict
pip install requests
```

#### Full

```
conda create --name myenv --file spec-file.txt
```
