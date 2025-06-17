import os
from lihat_toko_produk import fitur_melihat_toko_dan_produk
from filter_toko_produk import fitur_filtering_produk
from searching_toko_produk import fitur_searching
from keranjang import fitur_keranjang
from daftar_penjual import daftar_menjadi_penjual
from daftar_kurir import daftar_menjadi_kurir

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("DEBUG: Sampai sini OK") 

def menu_pembeli():
    while True:
        clear_screen()
        print("===== MENU PEMBELI =====\n")
        print("1. Lihat Produk dan Toko")
        print("2. Filter Produk")
        print("3. Search Produk dan Toko")
        print("4. Keranjang & Checkout")
        print("5. Daftar Penjual")
        print("6. Daftar Kurir")
        print("7. Keluar")

        pilihan = input("\nPilih menu (1-5): ").strip()
        if pilihan == '1':
            fitur_melihat_toko_dan_produk()
        elif pilihan == '2':
            fitur_filtering_produk()
        elif pilihan == '3':
            fitur_searching()
        elif pilihan == '4':
            fitur_keranjang()
        elif pilihan == '5':
            daftar_menjadi_penjual()
        elif pilihan == '6':
            daftar_menjadi_kurir()
        elif pilihan == '7':
            print("Terima kasih telah menggunakan aplikasi.")
            break
        else:
            input("Pilihan tidak valid. Tekan enter untuk coba lagi...")

if __name__ == "__main__":
    menu_pembeli()
