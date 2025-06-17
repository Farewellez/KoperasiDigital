from database import *
import pandas as pd

def to_csv_allToko():
    all_toko = get_all_tokoDB()
    all_toko_df = pd.DataFrame(all_toko)
    all_toko_df.to_csv('all_toko.csv', mode='a', header=False, index=False)
    return all_toko_df