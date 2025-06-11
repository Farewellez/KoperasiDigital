import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from database import get_all_productDB

def export_produk_csv(filename = "produk.csv"):
    all_produk_data = get_all_productDB()
    if not all_produk_data:
        print("Tidak ada data produk untuk diekspor.")
        return
    
    df = pd.DataFrame(all_produk_data)
    try:
        df.to_csv(filename, index=False)
        print(f"Data produk berhasil diekspor ke {filename}")
        return True
    except Exception as e:
        print(f"Terjadi kesalahan saat mengekspor data produk: {e}")
        return False