import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from DB_Context import *

def to_csv_alldetail_keranjang():
    all_detail_keranjang = get_all_detail_keranjangDB()
    all_detail_keranjang_df = pd.DataFrame(all_detail_keranjang)
    all_detail_keranjang_df.to_csv('allDetail_Keranjang.csv', mode='a', header=False, index=False)
    return all_detail_keranjang_df