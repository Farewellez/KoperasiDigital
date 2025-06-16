import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .connection import create_connection

def get_all_productDB():
    conn = create_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM produk"
        cursor.execute(query)
        dataProduk = cursor.fetchall()
        
        list_produk = []
        for produk in dataProduk:
            product_dict = {
                'id_produk': produk[0],
                'nama_produk': produk[1],
                'id_kategori': produk[2],
                'id_toko': produk[3],
                'deskripsi_produk': produk[4],
                'harga_dasar': produk[5],
                'stok': produk[6],
                'satuan': produk[7],
                'status_produk': produk[8]
            }
            list_produk.append(product_dict)
        return list_produk
    
    except Exception as e:  
        conn.rollback()
        print(f"Terjadi kesalahan saat mengambil data produk: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def get_all_kategoriDB():
    conn = create_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM kategori"
        cursor.execute(query)
        dataKategori = cursor.fetchall()
        
        list_kategori = []
        for kategori in dataKategori:
            kategori_dict = {
                'id_kategori': kategori[0],
                'nama_kategori': kategori[1],
                'deskripsi': kategori[2]
            }
            list_kategori.append(kategori_dict)
        return list_kategori
    
    except Exception as e:  
        conn.rollback()
        print(f"Terjadi kesalahan saat mengambil data pengguna: {e}")
        return []
    finally:
        cursor.close()
        conn.close()