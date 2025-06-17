import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .connection import create_connection

def get_all_pesananDB():
    conn = create_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM pesanan"
        cursor.execute(query)
        dataPesanan = cursor.fetchall()
        
        list_pesanan = []
        for pesanan in dataPesanan:
            pesanan_dict = {
                'id_pesanan': pesanan[0],
                'id_pengguna': pesanan[1],
                'tanggal_pesanan': pesanan[2],
                'status_pesanan': pesanan[3],
                'total_harga_pesanan': pesanan[4],
                'id_alamat_pengiriman': pesanan[5],
                'metode_pembayaran' : pesanan[6],
                'nomor_resi' : pesanan[7],
            }
            list_pesanan.append(pesanan_dict)
        return list_pesanan
    
    except Exception as e:  
        conn.rollback()
        print(f"Terjadi kesalahan saat mengambil data pengguna: {e}")
        return []
    finally:
        cursor.close()
        conn.close()