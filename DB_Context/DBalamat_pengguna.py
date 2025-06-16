import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .connection import create_connection

def get_all_alamatpenggunaDB():
    conn = create_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM alamat_pengguna"
        cursor.execute(query)
        dataPengguna = cursor.fetchall()
        
        list_pengguna = []
        for pengguna in dataPengguna:
            user_dict = {
                'id_alamat_pengguna': pengguna[0],
                'id_kecamatan': pengguna[1],
                'nama_jalan': pengguna[2],
                'nomor_bangunan': pengguna[3],
                'rt': pengguna[4],
                'rw': pengguna[5],
                'kelurahan_desa' : pengguna[6],
                'detail_lain': pengguna[7],
                'kode_pos': pengguna[8]
            }
            list_pengguna.append(user_dict)
        return list_pengguna
    
    except Exception as e:  
        conn.rollback()
        print(f"Terjadi kesalahan saat mengambil data alamat pengguna: {e}")
        return []
    finally:
        cursor.close()
        conn.close()