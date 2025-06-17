from DB_Context import *
import pandas as pd

def to_csv_allPesananDB():
    all_pesanan = get_all_pesananDB()
    all_pesanan_df = pd.DataFrame(all_pesanan)
    all_pesanan_df.to_csv('allpesanan.csv', mode='a', header=False, index=False)
    return all_pesanan_df