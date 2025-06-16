import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .connection import create_connection

def get_all_PenggunaDB():
    conn = create_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM pengguna"
        cursor.execute(query)
        dataPengguna = cursor.fetchall()
        
        list_pengguna = []
        for pengguna in dataPengguna:
            user_dict = {
                'id_pengguna': pengguna[0],
                'id_alamat_pengguna': pengguna[1],
                'nama_pengguna': pengguna[2],
                'password_hash': pengguna[3],
                'tanggal_registrasi': pengguna[4],
                'email': pengguna[5],
                'telepon' : pengguna[6],
            }
            list_pengguna.append(user_dict)
        return list_pengguna
    
    except Exception as e:  
        conn.rollback()
        print(f"Terjadi kesalahan saat mengambil data pengguna: {e}")
        return []
    finally:
        cursor.close()
        conn.close()