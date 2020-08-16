"""
Script for exploring ESGF results.
"""

import json
import re

import pandas as pd


def split_esgf_string(model_data):
    """
    Use re to split as split method takes only one split string
    :param model_data:
    :return:
    """
    model_data = re.split('\.|\|', esgf_holdings_master_list['id'].loc[1])
    return model_data


if __name__ == '__main__':

    # Read in the ESGF results
    with open("data_json/ESGF_results_2020-07-25.json", "r") as read_file:
        esgf_data = json.load(read_file)

    # first look at this dictionary - they're nested
    # esgf_data.keys()
    # an array of dictionaries
    esgf_holdings_master_list = pd.DataFrame.from_dict(esgf_data['response']['docs'])
    esgf_holdings_master_list.assign()

    props_of_interest = ['CMIP', 'MIP', 'Centre', 'Model', 'Ensemble', 'Experiment', 'Realm', 'Variable', 'Grid', 'Date']
    esgf_holdings = pd.DataFrame(columns=props_of_interest)
    for ivar, col_label in zip(range(0, len(props_of_interest)), props_of_interest):
        # create a series that is the model ensemble and assign to the column of interest
        esgf_holdings[col_label] = esgf_holdings_master_list.apply(lambda x: split_esgf_string(x)[ivar])
    esgf_holdings.set_index(esgf_holdings['Model'], drop=True, inplace=True)
    esgf_holdings.sample(5)
