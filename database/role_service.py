import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .connection import create_connection

def create_role_pembeli(id_pengguna, id_role = 1):
    conn = create_connection()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO pengguna_roles (id_pengguna, id_role)
        VALUES (%s, %s) RETURNING id_pengguna_role
        """
        cursor.execute(query, (id_pengguna, id_role))
        new_user_role_id = cursor.fetchone()[0]
        conn.commit()
        return new_user_role_id
    except Exception as e:
        conn.rollback()
        print(f"Terjadi kesalahan saat membuat role pembeli: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

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