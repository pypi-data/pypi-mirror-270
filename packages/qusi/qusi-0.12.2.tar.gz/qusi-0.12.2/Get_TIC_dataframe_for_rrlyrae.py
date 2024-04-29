from pathlib import Path

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


if __name__ == "__main__":
    tic_df_for_rrlyrae()
    tic_id_for_rrlyrae()
