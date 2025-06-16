import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import *
from .check_account import *
from database import check_role

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

        clearTerminal()
        login()
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
        
        get_id_pengguna = verif_akun(email, password) # dari . checkaccount
        if get_id_pengguna:
            clearTerminal() # dari utils clear terminal
            print(f"{loading_animation('memuat halaman')}") # dari utils loading animation
            clearTerminal()
            wellcomeback() # dari utils valid input
            role_pengguna = check_role(get_id_pengguna) # dari database role service
            return role_pengguna
        else:
            clearTerminal() # dari utils clear terminal
            print(f"{loading_animation('memuat halaman')}") # dari utils loading animation
            invalidEmailOrPw() # dari utils invalid input
            back_home = input("Apakah ingin kembali ke homepage? (y/n): ") 
            if back_home.lower() == 'y':
                return False
            elif back_home.lower() == 'n':
                continue
            else:
                clearTerminal()
                invalidInput()
                continue