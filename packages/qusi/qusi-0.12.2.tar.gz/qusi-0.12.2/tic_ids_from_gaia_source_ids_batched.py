from pathlib import Path

import pandas as pd
from astroquery.mast import Catalogs


def get_tic_ids_for_gaia_source_ids(gaia_source_ids: list[int]) -> list[int]:
    tic_row_for_gaia_source_id_astropy_table = Catalogs.query_criteria(catalog="TIC", GAIA=gaia_source_ids)
    tic_row_for_gaia_source_id_data_frame = tic_row_for_gaia_source_id_astropy_table.to_pandas()
    tic_id_strings = tic_row_for_gaia_source_id_data_frame['ID'].values
    tic_ids = [int(tic_id_string) for tic_id_string in tic_id_strings]
    return tic_ids


if __name__ == '__main__':
    gaia_rr_lyrae_csv_file_path = Path('first_10_rr_lyrae_from_gaia.csv')
    gaia_rr_lyrae_data_frame = pd.read_csv(gaia_rr_lyrae_csv_file_path)
    gaia_source_ids = gaia_rr_lyrae_data_frame['source_id'].tolist()
    tic_ids = get_tic_ids_for_gaia_source_ids(gaia_source_ids)
    print(tic_ids)
