<h1 align = "center">Koperasi Digital Desa</h1> 

### Alur kode program
1. mulai dengan menjalankan script dari main.py
```
python ./main.py
```

2. ketika sudah dijalankan maka akan masuk ke isi dari filenya
```
from main_menu import MainMenu
from utils import clearTerminal

def main():
    clearTerminal() # dari utils clear terminal
    MainMenu() # dari . main menu

if __name__ == "__main__":
    main()
```
3. kode eksekusi dilanjutkan ke MainMenu() dengan isi sebagai berikut
```
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 

from utils import *
from auth import *
from database import *

# verifikasi awal apakah pengguna sudah punya akun
def MainMenu():
    clearTerminal() # Dari utils clear terminal
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
                    print(f"{loading_animation('memuat halaman')}") # dari utils loading
                    clearTerminal() # dari  clear terminal
                    match login_pengguna(): # dari auth login
                        case False:
                            continue
                        case None:
                            continue
                        case "pembeli":
                            clearTerminal() # dari utils clear terminal
                            return
                        case "penjual":
                            clearTerminal() # dari utils clear terminal
                            return
                        case "kurir":
                            clearTerminal() # dari utils clear terminal
                            return
                        case "admin":
                            clearTerminal() # dari utils clear terminal
                            return
                        case _:
                            continue
                case 2:
                    clearTerminal() # dari utils clear terminal
                    print(f"{loading_animation('membuka pendaftaran akun')}") # dari utils loading
                    clearTerminal() # dari utils clear terminal
                    if not regisAkun():  # dari auth newuser
                        continue
                    print(f"{loading_animation('memuat halaman')}") # dari auth loading
                    continue
                case 3:
                    clearTerminal() # dari utils clear terminal
                    print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
                    exit(0) # Keluar dari program
                case _:
                    clearTerminal() # dari utils clear terminal
                    invalidInput() # dari utils invalid input
                    continue

        except ValueError:
            clearTerminal() # dari utils clear terminal
            print(f"{loading_animation("verifikasi pilihan")}") # dari utils loading
            clearTerminal() # dari utils clear terminal
            invalidInput() # dari utils invalid input
```
