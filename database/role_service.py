from . import connectDB

def create_role_pembeli(id_pengguna, id_role = 1):
    conn = connectDB()
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