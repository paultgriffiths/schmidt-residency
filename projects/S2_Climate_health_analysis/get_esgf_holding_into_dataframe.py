#!/usr/bin/env python
import requests
import pandas as pd
import xmltodict
#import pprint
#import json

# working example
# http://esgf-node.jpl.nasa.gov/esg-search/search?project=obs4MIPs&variable=hus&variable=ta&model!=Obs-AIRS
# http://https://esgf-index1.ceda.ac.uk/esg-search/search?project=obs4MIPs&variable=hus&variable=ta&model!=Obs-AIRS
r = requests.get('https://esgf-index1.ceda.ac.uk/esg-search/search?',                  params={'mip_era':'CMIP6', 'realm':'aerosol', "table_id":'AERmon', 'experiment_id':'historical','variable':'o3', "limit":"1000"
                        }
                )
# another mirror
# r = requests.get('http://esgf-data.dkrz.de/esg-search/search?', \
#                  params={'mip_era':'CMIP6', 'realm':'aerosol', "table_id":'AERmon', 'experiment_id':'historical','variable':'o3'
#                         }
#                 )

# returning JSON should be an option but is not implemented yet!

# if required - save xml for processing into JSON?
#file = open("resp_text.txt", "w")
#file.write(r.text)


a= xmltodict.parse(r.text)

esgf_results_breakdown=pd.DataFrame()
for jvar in range (0, len(a['response']['result']['doc'])):
    b = pd.DataFrame.from_dict(a['response']['result']['doc'][jvar]['arr'])
    b.set_index(['@name'], inplace=True)
    b.columns=[b.loc['source_id'].values[0]]
    esgf_results_breakdown= pd.concat([esgf_results_breakdown,b], axis=1)
esgf_results_breakdown=esgf_results_breakdown.T
esgf_results_breakdown = esgf_results_breakdown.reindex(columns= ['activity_id', 'institution_id','experiment_id', 'variant_label','table_id', 'variable_id','grid', 'grid_label', 'source_type'])
# esgf_results_breakdown.drop(['access', 'citation_url', 'data_specs_version', 'dataset_id_template_','directory_format_template_','further_info_url','geo', 'geo_units',
#          'pid','branch_method'], inplace=True, axis=1)
# more than one way to do it?

esgf_results_breakdown.sort_index(inplace=True)

# SCRATCH
# indexnames=[]
# for jvar in range (0, len(a['response']['result']['doc'][0]['arr'])):
#     indexnames.append(a['response']['result']['doc'][0]['arr'][jvar]['@name'])
# print(indexnames)


