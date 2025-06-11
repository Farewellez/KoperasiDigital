import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database import *
from utils import *

def check_id_appearance(email, telepon):
    # Ambil semua data pengguna dari database
    all_users = get_all_userDB()
    
    for user in all_users:
        if user['email'] == email and user['id_pengguna'] and user['telepon'] == telepon:
            clearTerminal()
            invalidAkun()
            return False
    return True  # Tidak ada masalah, ID unik

def verif_akun(email, password):
    all_users = get_all_userDB()
    
    for user in all_users:
        if user['email'] == email and user['id_pengguna'] and bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
            clearTerminal()
            return user['id_pengguna']
        else:
            return False