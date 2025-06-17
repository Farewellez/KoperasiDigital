import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from DB_Context import *

def to_csv_allKategoriDB():
    all_kategori = get_all_kategoriDB()
    all_kategori_df = pd.DataFrame(all_kategori)
    all_kategori_df.to_csv('allkategori.csv', mode='a', header=False, index=False)
    return all_kategori_df