import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .connection import create_connection

def get_all_pengguna_rolesDB():
    conn = create_connection()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        query = """
        SELECT * FROM pengguna_roles
        """
        cursor.execute(query)
        data_pengguna_role = cursor.fetchall()

        list_role = []
        for pengguna_role in data_pengguna_role:
            pengguna_role_dict = {
                'id_pengguna_role': pengguna_role[0],
                'id_pengguna': pengguna_role[1],
                'id_role': pengguna_role[2]
            }
            list_role.append(pengguna_role_dict)
        return list_role
        
    except Exception as e:  
        conn.rollback()
        print(f"Terjadi kesalahan saat mengambil data pengguna: {e}")
        return []
    finally:
        cursor.close()
        conn.close()