import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .connection import create_connection

def get_all_alamat_tokoDB():
    conn = create_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM alamat_toko"
        cursor.execute(query)
        data_alamat_toko = cursor.fetchall()
        
        list_alamat_toko = []
        for toko in data_alamat_toko:
            list_alamat_toko_dict = {
                'id_alamat_toko': toko[0],
                'nama_kecamatan': toko[1],
                'id_nama_jalan': toko[2],
                'id_nomor_bangunan': toko[3],
                'rt': toko[4],
                'rw': toko[5],
                'stok': toko[6],
                'kelurahan_desa': toko[7],
                'detail_lain': toko[8]
            }
            list_alamat_toko.append(list_alamat_toko_dict)
        return list_alamat_toko
    
    except Exception as e:  
        conn.rollback()
        print(f"Terjadi kesalahan saat mengambil data alamat toko: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def get_all_tokoDB():
    conn = create_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM toko"
        cursor.execute(query)
        data_toko = cursor.fetchall()
        
        list_toko = []
        for toko in data_toko:
            toko_dict = {
                'id_toko': toko[0],
                'id_alamat_toko': toko[1],
                'id_pengguna': toko[2],
                'nama_toko': toko[3],
                'deskripsi_toko': toko[4],
                'tanggal_mendaftar': toko[5],
                'status_toko' : toko[6],
            }
            list_toko.append(toko_dict)
        return list_toko
    
    except Exception as e:  
        conn.rollback()
        print(f"Terjadi kesalahan saat mengambil data pengguna: {e}")
        return []
    finally:
        cursor.close()
        conn.close()