import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from DB_Context import *

def to_csv_alldetail_pesanan():
    all_detail_pesanan = get_all_detail_pesananDB()
    all_detail_pesanan_df = pd.DataFrame(all_detail_pesanan)
    all_detail_pesanan_df.to_csv('allDetail_Pesanan.csv', mode='a', header=False, index=False)
    return all_detail_pesanan_df