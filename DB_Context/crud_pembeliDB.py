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

def get_all_detail_pesanan():
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

def get_all_feedbackDB():
    conn = create_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM feedback"
        cursor.execute(query)
        dataFeedback = cursor.fetchall()
        
        list_feedback = []
        for feedback in dataFeedback:
            feedback_dict = {
                'id_feedback': feedback[0],
                'id_produk': feedback[1],
                'id_pengguna': feedback[2],
                'id_toko': feedback[3],
                'rating': feedback[4],
                'tanggal_feedback': feedback[5],
                'isi_feedback' : feedback[6],
            }
            list_feedback.append(feedback_dict)
        return list_feedback
    
    except Exception as e:  
        conn.rollback()
        print(f"Terjadi kesalahan saat mengambil data pengguna: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

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