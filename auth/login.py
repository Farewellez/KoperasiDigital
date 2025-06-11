import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import *
from check_account import *

def login():   
    print('''
     ++================================================++
     ||       _   ___   _____ ______       ____        ||
     ||      | | /  /  //   \\\ |   \\\     //  ||       ||
     ||      | |/  /  //     \\\|    \\\   //---||       ||
     ||      |  _  \  \\\     //|    //  //    ||       ||
     ||      |_|  \_\  \\\___//_|___//__//     ||       ||
     ||                                                ||
     ||                                                ||
     ||            KOPERASI DIGITAL DESA               ||
     ++------------------------------------------------++
     || <<<<<<<     🌟MASUKKAN AKUN KAMU🌟     >>>>>>> ||
     ||                                                ||
     ||================================================||
     ||  📃 Input email kamu                           ||
     ||  🔒 Input password akunmu                      ||
     ++================================================++''')

def login_pengguna():
    while True:
        clearTerminal()
        login()
        email = input(f"{" "*5}Email: ")
        clearTerminal()
        loading_animation("memeriksa email")
        clearTerminal()
        if '@' not in email or '.' not in email.split('@')[-1]:
            invalidEmail()
            clearTerminal()
            continue
        
        password = input(f"{" "*5}Password: ")
        clearTerminal()
        loading_animation("memeriksa password")
        clearTerminal()
        if len(password) < 8:
            invalidPW()
            clearTerminal()
            continue

        clearTerminal()
        loading_animation('memverifikasi akun')
        
        get_id_pengguna = verif_akun(email, password)
        if get_id_pengguna:
            clearTerminal()
            print(f"{loading_animation('memuat halaman')}")
            wellcomeback()
            check_role(get_id_pengguna)
        else:
            clearTerminal()
            print(f"{loading_animation('memuat halaman')}")
            invalidEmailOrPw()
            back_home = input("Apakah ingin kembali ke homepage? (y/n): ")
            if back_home.lower() == 'y':
                return False
            elif back_home.lower() == 'n':
                continue
            else:
                clearTerminal()
                invalidInput()
                continue

def check_role(id_pengguna):
    all_pengguna_role = get_all_pengguna_rolesDB()
    for pengguna in all_pengguna_role:
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
            print("error role pengguna tidak dapat ditemukan") # debugging sederhana
            return None