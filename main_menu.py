from utils import * 
from auth import regisAkun
from database import *

# verifikasi awal apakah pengguna sudah punya akun
def MainMenu():
    while True:
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
             || <<<<<<< 🌟APAKAH SUDAH MEMILIKI AKUN🌟 >>>>>>> ||
             ||================================================||
             ||  1. Ya, saya sudah punya akun.                 ||
             ||  2. Tidak, saya belum punya akun.              ||
             ||  3. Keluar dari program.                       ||
             ++================================================++''')
        try:
            konfirmasiPengguna = int(input(f"{" "*13}> input pilihan anda [1/2/3]: "))
            match konfirmasiPengguna:
                case 1:
                    clearTerminal()
                    print(f"{loading_animation('memverifikasi akun')}")
                    clearTerminal()
                    break
                case 2:
                    clearTerminal()
                    print(f"{loading_animation('membuka pendaftaran akun')}")
                    clearTerminal()
                    if not regisAkun():  # Masuk ke fungsi pendaftaran akun baru
                        continue
                    print(f"{loading_animation('memuat halaman')}")
                    break 
                case 3:
                    clearTerminal()
                    print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
                    exit(0) # Keluar dari program
                case _:
                    clearTerminal()
                    invalidInput() # Input tidak valid
        except ValueError:
            clearTerminal()
            print(f"{loading_animation("verifikasi pilihan")}")
            clearTerminal()
            invalidInput()