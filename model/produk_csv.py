from DB_Context import *
import pandas as pd

def to_csv_allProductDB():
    all_produk = get_all_productDB()
    all_produk_df = pd.DataFrame(all_produk)
    all_produk_df.to_csv('allProduk.csv', mode='a', header=False, index=False)
    return all_produk_df