import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .connection import create_connection

def get_all_detail_pesananDB():
    conn = create_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM detail_pesanan"
        cursor.execute(query)
        data_detail_pesanan = cursor.fetchall()
        
        list_detail_pesanan = []
        for detail_pesanan in data_detail_pesanan:
            detail_pesanan_dict = {
                'id_detail_pesanan': detail_pesanan[0],
                'id_pesanan': detail_pesanan[1],
                'id_produk': detail_pesanan[2],
                'kuantitas': detail_pesanan[3],
                'harga_saat_pesan': detail_pesanan[4],
                'diskon_per_item': detail_pesanan[5],
                'subtotal_item' : detail_pesanan[6],
            }
            list_detail_pesanan.append(detail_pesanan_dict)
        return list_detail_pesanan
    
    except Exception as e:  
        conn.rollback()
        print(f"Terjadi kesalahan saat mengambil data pengguna: {e}")
        return []
    finally:
        cursor.close()
        conn.close()