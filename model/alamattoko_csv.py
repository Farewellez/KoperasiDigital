import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from DB_Context import *

def to_csv_allAlamat_toko():
    all_alamat_toko = get_all_alamat_tokoDB()
    all_alamat_toko_df = pd.DataFrame(all_alamat_toko)
    all_alamat_toko_df.to_csv('all_alamat_toko.csv', mode='a', header=False, index=False)
    return all_alamat_toko_df