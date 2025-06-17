import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from DB_Context import *

def to_csv_allAlamat_pengguna():
    all_alamat_pengguna = get_all_alamatpenggunaDB()
    all_alamat_pengguna_df = pd.DataFrame(all_alamat_pengguna)
    all_alamat_pengguna_df.to_csv('all_alamat_pengguna.csv', mode='a', header=False, index=False)
    return all_alamat_pengguna_df