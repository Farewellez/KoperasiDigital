# import datasource yang dibuat dan library lain
import os
import sys
from database import KoperasiDigital

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Untuk cek apabila akun sudah ada atau belum
def alreadyAdd(id_pengguna):
    conn = KoperasiDigital()

    if conn:
        # print("fitur auth bisa connect")
        cur = conn.cursor()
        cur.execute("SELECT id_pengguna FROM pengguna")
        allID = cur.fetchall()

        allID = [row[0] for row in allID]

        if id_pengguna in allID:
            # print("akun sudah terdaftar")
            cur.close()
            conn.close()
            return True
        else:
            # print("akun belum terdaftar")
            return False
    else:
        print("Error")

def verifRole(role_pengguna = None):
    conn = KoperasiDigital()
    if conn:
        print("cek role dimulai")
        cur = conn.cursor()
        cur.execute("SELECT id_pengguna FROM pengguna")
        cur.fetchall
        cur.close()
        conn.close()
        return