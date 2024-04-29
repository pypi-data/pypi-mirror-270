import pandas as pd
from astroquery.mast import Catalogs

from cross_referencing_tess_and_gaia import get_tess_input_catalog_row_for_tic_id

import pandas as pd

def get_tic_ids_for_gaia_source_ids(gaia_source_ids: list[int]) -> list[int]:
    tic_row_for_gaia_source_id_astropy_table = Catalogs.query_criteria(catalog="TIC", GAIA=gaia_source_ids)
    tic_row_for_gaia_source_id_data_frame = tic_row_for_gaia_source_id_astropy_table.to_pandas()
    tic_id_strings = tic_row_for_gaia_source_id_data_frame['ID'].values
    tic_ids = [int(tic_id_string) for tic_id_string in tic_id_strings]
    return tic_ids

# getting the TIC id's for the objects using their GAIA source id's
def tic_id_for_rrlyrae():
    data_file = Path('first_10_rr_lyrae_from_gaia.csv')
    data = pd.read_csv(data_file)
    gaia_source_ids = data['source_id'].tolist()
    tic_ids = get_tic_ids_for_gaia_source_ids(gaia_source_ids)
    return tic_ids


# getting the TIC rows for all the tic id's in the TIC_id - input parameter - TIC_id array
def tic_df_for_rrlyrae(x):
    rrl_dataframe = pd.DataFrame()
    for id in x:
        row = get_tess_input_catalog_row_for_tic_id(id)
        rrl_dataframe = pd.concat([rrl_dataframe, row], axis=1)
    rrl_dataframe = rrl_dataframe.T
    return rrl_dataframe


from Get_TIC_dataframe_for_rrlyrae import tic_df_for_rrlyrae,tic_id_for_rrlyrae
tic_ids = tic_id_for_rrlyrae()
tic_dataframe_rrlyrae = tic_df_for_rrlyrae(tic_ids)



tic_dataframe_rrlyrae.head()

tic_dataframe_rrlyrae.info()

tic_dataframe_rrlyrae['ID'] = pd.to_numeric(tic_dataframe_rrlyrae['ID'])

# THIS IS THE CODE TO DOWNLOAD THE LIGHT CURVE DATA FOR RR LYRAE STARS
# _______________________________________________________________________
from pathlib import Path

import numpy as np

from ramjet.data_interface.tess_data_interface import (
    download_spoc_light_curves_for_tic_ids,
)


tic_ids = tic_dataframe_rrlyrae.ID.unique()
# splitting the tic_ids as train-validation-test
tic_ids_splits = np.split(np.array(tic_ids), [int(len(tic_ids) * 0.8), int(len(tic_ids) * 0.9)])
train_tic_ids = tic_ids_splits[0].tolist()
validation_tic_ids = tic_ids_splits[1].tolist()
test_tic_ids = tic_ids_splits[2].tolist()


sectors = list(range(27, 56))
print('Retrieving metadata...')

print(f'Downloading light curve for {tic_ids}')
download_spoc_light_curves_for_tic_ids(
    tic_ids=train_tic_ids,
    download_directory=Path('data_rrlyrae/train_rrl'),
    sectors=sectors,
    limit=2000)
download_spoc_light_curves_for_tic_ids(
    tic_ids=validation_tic_ids,
    download_directory=Path('data_rrlyrae/validation_rrl'),
    sectors=sectors,
    limit=2000)
download_spoc_light_curves_for_tic_ids(
    tic_ids=test_tic_ids,
    download_directory=Path('data_rrlyrae/test_rrl'),
    sectors=sectors,
    limit=2000)
#  _____________________________________________________________________
# '''
