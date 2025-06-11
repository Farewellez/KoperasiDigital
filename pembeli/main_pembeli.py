import os
from daftar_penjual import *
from filter_toko_produk import *
from keranjang import *
from lihat_toko_produk import *
from searching_toko_produk import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    while True:
        clear_screen()
        print("=== Selamat Datang di Aplikasi Koperasi Digital ===")
        print("Anda login sebagai: Pembeli")
        print("\n--- Menu Utama Pembeli ---")
        print("1. Melihat daftar toko dan produk")
        print("2. Cari berdasarkan toko atau produk")
        print("3. Cari toko dan produk")
        print("8. Keluar aplikasi")
        pilihan = input("Pilih fitur (1 / 8): ")

        if pilihan == '1':
            fitur_melihat_toko_dan_produk()
        if pilihan == '2':
            fitur_filtering_produk
        if pilihan == '3':
            fitur_searching
        elif pilihan == '8':
            print("Terima kasih! Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

