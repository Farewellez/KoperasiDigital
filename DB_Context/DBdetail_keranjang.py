import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .connection import create_connection

def get_all_detail_keranjangDB():
    conn = create_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM detail_keranjang"
        cursor.execute(query)
        data_detail_keranjang = cursor.fetchall()
        
        list_detail_keranjang = []
        for detail_keranjang in data_detail_keranjang:
            detail_keranjang_dict = {
                'id_detail_keranjang': detail_keranjang[0],
                'id_keranjang': detail_keranjang[1],
                'id_produk': detail_keranjang[2],
                'jumlah_produk': detail_keranjang[3],
                'harga_saat_ditambahkan': detail_keranjang[4],
                'tanggal_ditambahkan': detail_keranjang[5],
            }
            list_detail_keranjang.append(detail_keranjang_dict)
        return list_detail_keranjang
    
    except Exception as e:  
        conn.rollback()
        print(f"Terjadi kesalahan saat mengambil data pengguna: {e}")
        return []
    finally:
        cursor.close()
        conn.close()
