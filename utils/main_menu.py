from .invalid_input import invalidInput
from .clear_terminal import clearTerminal
from .loading import loading_animation
from auth import regisAkun

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
                    pass # Isi nanti dengan logika untuk verifikasi akun
                case 2:
                    clearTerminal()
                    print(f"{loading_animation('membuka pendaftaran akun')}")
                    clearTerminal()
                    regisAkun() # Masuk ke fungsi pendaftaran akun baru
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