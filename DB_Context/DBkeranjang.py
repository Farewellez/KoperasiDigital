import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .connection import create_connection

def get_all_keranjangDB():
    conn = create_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM keranjang"
        cursor.execute(query)
        dataKeranjang = cursor.fetchall()
        
        list_keranjang = []
        for keranjang in dataKeranjang:
            keranjang_dict = {
                'id_keranjang': keranjang[0],
                'id_pengguna': keranjang[1],
                'tanggal_dibuat': keranjang[2],
                'tanggal_terakhir_diperbarui': keranjang[3],
                'status_keranjang': keranjang[4]
            }
            list_keranjang.append(keranjang_dict)
        return list_keranjang
    
    except Exception as e:  
        conn.rollback()
        print(f"Terjadi kesalahan saat mengambil data pengguna: {e}")
        return []
    finally:
        cursor.close()
        conn.close()