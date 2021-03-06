# work on exploratory analysis of ESGF data archive

For now looking at TAS (near-surface air temperature) and ozone trends using different time frequency data.

Includes 

- script to query ESGF and BADC data holdings to ascertain model data availability.

- dummy script to select a single gridbox based on lat/lon and dump to netCDF file - to make file easier to download/work with.

- script to plot temperature for UK under various CMIP climate scenarios

- TAS uses 3hr data to start to look for changes to frequency distributions, aim to look for heatwaves.  Focus on single grid box representative of e.g. Cambridge

- O3 uses monthly mean data to look for regions with largest trend → S3 project


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
