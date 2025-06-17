from DB_Context import *
import pandas as pd

def to_csv_allProductDB():
    all_produk = get_all_productDB()
    if not all_produk:
        return []
    
    df = pd.DataFrame(all_produk)
    df.to_csv('allProduk.csv', mode='w', header=True, index=False)  # overwrite file
    return all_produk  # kembalikan sebagai list of dict