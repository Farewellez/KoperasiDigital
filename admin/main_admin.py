import os

from konfirmasi_penjual import konfirmasi_penjual
from nonaktifkan_toko import nonaktifkan_toko
from konfirmasi_produk import konfirmasi_produk
from feedback import menu_feedback_admin

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_admin():
    while True:
        clear_screen()
        print("=== MENU UTAMA ADMIN KOPERASI DIGITAL ===")
        print("1. Konfirmasi Permintaan Penjual")
        print("2. Nonaktifkan Toko")
        print("3. Konfirmasi Produk Jual")
        print("4. Kelola Feedback Pengguna")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            konfirmasi_penjual()
        elif pilihan == "2":
            nonaktifkan_toko()
        elif pilihan == "3":
            konfirmasi_produk()
        elif pilihan == "4":
            menu_feedback_admin()
        elif pilihan == "0":
            print("Keluar dari menu admin.")
            break
        else:
            print("Pilihan tidak valid. Tekan Enter untuk lanjut...")
            input()

if __name__ == "__main__":
    menu_admin()
