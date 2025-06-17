import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .connection import create_connection
from .DBpengguna_roles import get_all_pengguna_rolesDB
from utils import clearTerminal

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

def check_role(id_pengguna):
    all_pengguna_role = get_all_pengguna_rolesDB()
    # print(all_pengguna_role)
    # input()
    for pengguna in all_pengguna_role:
        # print(pengguna['id_pengguna'], id_pengguna)
        if pengguna['id_pengguna'] == id_pengguna:
            if pengguna['id_role'] == 1: # pembeli
                clearTerminal()
                return "pembeli"
            elif pengguna['id_role'] == 2: # penjual
                clearTerminal()
                return "penjual"
            elif pengguna['id_role'] == 3: # kurir
                clearTerminal()
                return "kurir"
            else:
                clearTerminal()
                return "admin"
        else:
            continue
    print("error role pengguna tidak dapat ditemukan") # debugging sederhana
    return None