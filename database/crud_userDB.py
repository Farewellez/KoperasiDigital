import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from . import connectDB

def create_user_db(nama_pengguna, password, email, telepon, id_alamat_pengguna=None):
    connection = connectDB()
    if connection is None:
        return False
    
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO pengguna (nama_pengguna, password_hash, email, telepon, id_alamat_pengguna)
        VALUES (%s, %s, %s, %s, %s) RETURNING id_pengguna 
        """
        cursor.execute(query, (nama_pengguna, password, email, telepon, id_alamat_pengguna))
        new_user_id = cursor.fetchone()[0]
        connection.commit()
        return new_user_id
    
    except Exception as e:
        connection.rollback()  # Rollback jika terjadi kesalahan
        print(f"Terjadi kesalahan saat membuat akun: {e}")
        return False
    
    finally:
        cursor.close()
        connection.close()

def get_all_userDB():
    conn = connectDB()
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

def get_all_alamatpenggunaDB():
    conn = connectDB()
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

def get_all_kecamatanDB():
    conn = create_user_db()
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