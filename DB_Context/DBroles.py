import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .connection import create_connection

def get_all_roleDB():
    conn = create_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM roles"
        cursor.execute(query)
        data_role = cursor.fetchall()
        
        list_role = []
        for role in data_role:
            role_dict = {
                'id_role': role[0],
                'nama_role': role[1]
            }
            list_role.append(role_dict)
        return list_role
    
    except Exception as e:  
        conn.rollback()
        print(f"Terjadi kesalahan saat mengambil data pengguna: {e}")
        return []
    finally:
        cursor.close()
        conn.close()