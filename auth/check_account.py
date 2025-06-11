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