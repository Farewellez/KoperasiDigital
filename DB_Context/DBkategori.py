import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .connection import create_connection

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