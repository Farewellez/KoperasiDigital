import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from string import ascii_letters
from . import check_account
from utils import *
from database import *
from utils.hashing import hash_password

# fungsi untuk membuat input data dari pengguna baru
def newUser():
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
     || <<<<<<<  🌟REGISTRASIKAN AKUN KAMU🌟   >>>>>>> ||
     ||           DAN BERGABUNG DENGAN KAMI            ||
     ||================================================||
     ||  📃 Registrasi nama pengguna                   ||
     ||  🔒 Buat password untuk akun kamu              ||
     ||  📧 Daftarkan email kamu                       ||
     ||  📲 Daftarkan juga nomor telepon kamu          ||
     ++================================================++''')

def regisNama():
    newUser() # dari file ini dengan function newuser
    global nama_pengguna
    nama_pengguna = input(f"{" "*4}😄 Masukkan nama pengguna: ")
    clearTerminal() # dari utils clear terminal
    loading_animation("memeriksa nama pengguna") # dari utils loading animation
    clearTerminal() # dari utils clear terminal
    if len(nama_pengguna.replace(' ', '')) < 9:
        invalidName() # dari utils invalid name
        clearTerminal() # dari utils clear terminal
        return None
    for char in nama_pengguna:
        if char not in ascii_letters + ' ':
            clearTerminal() # dari utils clear terminal
            invalidName() # dari utils invali name
            return None
    return nama_pengguna

def regisPassword():
    newUser() # dari file ini dengan function newuser
    global password
    password = input(f"{" "*4}🤐 Buat password untuk akun kamu: ")
    clearTerminal() # dari utils clear terminal
    loading_animation("memeriksa password") # dari utils loading animation
    clearTerminal() # dari utils clear terminal
    if len(password) < 8:
        invalidPW() # dari utils invalid input
        clearTerminal() # dari utils clear terminal
        return None
    return password

def regisEmail():
    newUser() # dari file ini dengan function newuser
    global email
    email = input(f"{" "*4}☺️ Daftarkan email kamu: ")
    clearTerminal() # dari utils clear terminal
    loading_animation("memeriksa email") # dari utils loading animation
    clearTerminal() # dari utils clear terminal
    if '@' not in email or '.' not in email.split('@')[-1]:
        invalidEmail() # dari utils invalid input
        clearTerminal() # dari utils clear terminal
        return None
    return email

def regisTelepon():
    newUser() # dari file ini dengan function newuser
    global telepon
    telepon = input(f"{" "*4}😉 Daftarkan nomor telepon kamu: ")
    clearTerminal() # dari utils clear terminal
    loading_animation("memeriksa nomor telepon") # dari utils loading animation
    clearTerminal() # dari utils clear terminal
    if not telepon.isdigit() or len(telepon) < 12:
        invalidTelepon() # dari utils invalid input
        clearTerminal() # dari utils clear terminal
        return None
    return telepon

def regisAkun():
    if name_f():
        # Cek apakah kombinasi email dan telepon sudah ada di database
        if not check_account.check_id_appearance(email, telepon):
            clearTerminal() # dari utils clear terminal
            print(f"{loading_animation('memuat halaman')}")
            clearTerminal() # dari utils clear terminal
            return False

        # Jika semua input valid, buat akun baru
        clearTerminal() # dari utils clear terminal
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
         || <<<<<<<   🌟AKUN BERHASIL DIBUAT🌟     >>>>>>> ||
         ||              🎉SELAMAT DATANG🎉                ||
         ||================================================||''')

        pengguna_baru = create_user_db(nama_pengguna, hashPW, email, telepon, id_alamat_pengguna=None) # dari database crud userDB
        print(f"{loading_animation('menambahkan role pengguna')}") # dari utils loading animation
        clearTerminal() # dari utils clear terminal
        create_role_pembeli(pengguna_baru, id_role=1)  # dari database crud role service
        return pengguna_baru # mengembalikkan id pengguna
    else:
        return False


def name_f():
    clearTerminal() # dari utils clear terminal
    while True:
        nama_pengguna = regisNama() # dari file ini dengan nama function regisNama
        if nama_pengguna is None:
            continue
        if password_f(): # dari file ini dengan nama function password_f
            return True
    
def password_f():
    clearTerminal() # dari utils clear terminal
    while True: 
        password = regisPassword() # dari file ini dengan nama function regisPassword
        if password is None:
            continue
        confirmPW = input("1. registrasi ulang nama\n2. lanjutkan\ninput pilihan: ")
        match confirmPW:
            case "1":
                name_f() # dari file ini dengan nama function name_f
            case "2":
                # password hasil di-hash sebelum disimpan
                global hashPW
                hashPW = hash_password(password) # dari utils hashing password
                if email_f(): # dari file ini dengan nama function email_f
                    return True
            case _:
                invalidInput() # dari utils invalid input
                continue
    
def email_f(): 
    clearTerminal() # dari utils clear terminal
    while True:
        email = regisEmail() # dari file ini dengan nama function regisEmail
        if email is None:
            continue
        confirmEmail = input("1. registrasi ulang password\n2. lanjutkan\ninput pilihan: ")
        match confirmEmail:
            case "1":
                password_f() # dari file ini dengan nama function password_f
            case "2":
                if telepon_f(): # dari file ini dengan nama function telepon_f
                    return True
            case _:
                invalidInput() # dari utils invalid input
                continue

def telepon_f():
    clearTerminal() # dari utils clear terminal
    while True:
        telepon = regisTelepon() # dari file ini dengan nama function regisTelepon
        if telepon is None:
            continue
        confirmTelepon = input("1. registrasi ulang email\n2. lanjutkan\ninput pilihan: ")
        match confirmTelepon:
            case "1":
                email_f() # dari file ini dengan nama function email_f
            case "2":
                return True
            case _:
                invalidInput() # dari utils invalid input
                continue 