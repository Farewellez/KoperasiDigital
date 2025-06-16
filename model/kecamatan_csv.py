import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from DB_Context import *

def to_csv_allKecamatan():
    all_kecamatan = get_all_kecamatanDB()
    all_kecamatan_df = pd.DataFrame(all_kecamatan)
    all_kecamatan_df.to_csv('all_kecamatan.csv', mode='a', header=False, index=False)
    return all_kecamatan_df