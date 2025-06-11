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
    newUser()
    nama_pengguna = input(f"{" "*4}😄 Masukkan nama pengguna: ")
    clearTerminal()
    loading_animation("memeriksa nama pengguna")
    clearTerminal()
    if len(nama_pengguna.replace(' ', '')) < 9:
        invalidName()
        clearTerminal()
        return None
    for char in nama_pengguna:
        if char not in ascii_letters + ' ':
            clearTerminal()
            invalidName()
            return None
    return nama_pengguna

def regisPassword():
    newUser()
    password = input(f"{" "*4}🤐 Buat password untuk akun kamu: ")
    clearTerminal()
    loading_animation("memeriksa password")
    clearTerminal()
    if len(password) < 8:
        invalidPW()
        clearTerminal()
        return None
    return password

def regisEmail():
    newUser()
    email = input(f"{" "*4}☺️ Daftarkan email kamu: ")
    clearTerminal()
    loading_animation("memeriksa email")
    clearTerminal()
    if '@' not in email or '.' not in email.split('@')[-1]:
        invalidEmail()
        clearTerminal()
        return None
    return email

def regisTelepon():
    newUser()
    telepon = input(f"{" "*4}😉 Daftarkan nomor telepon kamu: ")
    clearTerminal()
    loading_animation("memeriksa nomor telepon")
    clearTerminal()
    if not telepon.isdigit() or len(telepon) < 12:
        invalidTelepon()
        clearTerminal()
        return None
    return telepon

def regisAkun():
    while True:
        nama_pengguna = regisNama()
        if nama_pengguna is None:
            continue
        break
    
    while True:
        password = regisPassword()
        if password is None:
            continue
        # password hasil di-hash sebelum disimpan
        hashPW = hash_password(password)
        break
    
    while True:
        email = regisEmail()
        if email is None:
            continue
        break

    while True:
        telepon = regisTelepon()
        if telepon is None:
            continue
        break
    
    # Cek apakah kombinasi email dan telepon sudah ada di database
    if not check_account.check_id_appearance(email, telepon):
        clearTerminal()
        print(f"{loading_animation('memuat halaman')}")
        clearTerminal()
        return None
    
    # Jika semua input valid, buat akun baru
    clearTerminal()
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
    
    pengguna_baru = create_user_db(nama_pengguna, hashPW, email, telepon, id_alamat_pengguna=None)
    print(f"{loading_animation('menambahkan role pengguna')}")
    create_role_pembeli(pengguna_baru, id_role=1)  
    return pengguna_baru