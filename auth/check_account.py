import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DB_Context import *
from utils import *

def check_id_appearance(email, telepon):
    # Ambil semua data pengguna dari database
    all_users = get_all_alamatpenggunaDB()
    
    for user in all_users:
        if user['email'] == email and user['id_pengguna'] and user['telepon'] == telepon:
            clearTerminal()
            invalidAkun()
            return False
    return True  # Tidak ada masalah, ID unik

def verif_akun(email, password):
    all_users = get_all_alamatpenggunaDB() # dari database crud useDB
    
    for user in all_users:
        # print(user)
        # input()
        if user['email'] == email and user['id_pengguna'] and bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
            # print(user['email'])
            # print(user['id_pengguna'])
            # print(bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')))
            # input()
            # clearTerminal()
            return user['id_pengguna']
        else:
            # input()
            continue