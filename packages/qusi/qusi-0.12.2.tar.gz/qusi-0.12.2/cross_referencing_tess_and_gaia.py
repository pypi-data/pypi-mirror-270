from typing import Optional

import pandas as pd
from astroquery.gaia import Gaia
from astroquery.mast import Catalogs


def get_gaia_source_row_for_gaia_source_id(gaia_source_id: int) -> pd.Series:
    gaia_job = Gaia.launch_job(f'select * from gaiadr3.gaia_source where source_id={gaia_source_id}')
    query_results_data_frame = gaia_job.get_results().to_pandas()
    gaia_row = query_results_data_frame.iloc[0]
    return gaia_row


def get_tess_input_catalog_row_for_tic_id(tic_id: int) -> pd.Series:
    tic_row = Catalogs.query_criteria(catalog='TIC', ID=tic_id).to_pandas()
    return tic_row.iloc[0]


def get_gaia_source_id_for_tic_id(tic_id: int) -> Optional[int]:
    tic_row = get_tess_input_catalog_row_for_tic_id(tic_id)
    gaia_source_id_string = tic_row['GAIA']
    if pd.notna(gaia_source_id_string):
        gaia_source_id = int(gaia_source_id_string)
        return gaia_source_id
    else:
        return None


def get_tic_id_for_gaia_source_id(gaia_source_id: int) -> Optional[int]:
    tic_row_for_gaia_source_id_astropy_table = Catalogs.query_criteria(catalog="TIC", GAIA=str(gaia_source_id))
    tic_row_for_gaia_source_id_data_frame = tic_row_for_gaia_source_id_astropy_table.to_pandas()
    if tic_row_for_gaia_source_id_data_frame.shape[0] > 0:
        return int(tic_row_for_gaia_source_id_data_frame['ID'].iloc[0])
    else:
        return None


tic_id = 270491267
tic_row = get_tess_input_catalog_row_for_tic_id(tic_id)
gaia_source_id_for_tic_id = get_gaia_source_id_for_tic_id(tic_id)
other_gaia_source_id = 6030078867485330048
gaia_source_row = get_gaia_source_row_for_gaia_source_id(other_gaia_source_id)
other_tic_id = get_tic_id_for_gaia_source_id(other_gaia_source_id)
