#%%
import json
#%%
with open("data_json/ESGF_results_2020-07-25.json", "r") as read_file:
    esgf_data = json.load(read_file)
#%%
# first look at this dictionary - they're nested
esgf_data.keys()
# an array of dictionaries
esgf_data2 = esgf_data['response']['docs']

# %%
for ivar in range(0, len(esgf_data2)):
    print(esgf_data2[ivar]['source_id'])

# %%
