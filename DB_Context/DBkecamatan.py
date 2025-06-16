import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .connection import create_connection

def get_all_kecamatanDB():
    conn = create_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM kecamatan"
        cursor.execute(query)
        data_kecamatan = cursor.fetchall()
        
        list_kecamatan = []
        for kecamatan in data_kecamatan:
            kecamatan_dict = {
                'id_kecamatan': kecamatan[0],
                'nama_kecamatan': kecamatan[1],
            }
            list_kecamatan.append(kecamatan_dict)
        return list_kecamatan
    
    except Exception as e:  
        conn.rollback()
        print(f"Terjadi kesalahan saat mengambil data pengguna: {e}")
        return []
    finally:
        cursor.close()
        conn.close()