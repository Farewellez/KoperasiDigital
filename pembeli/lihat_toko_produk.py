import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from data import produk, keranjang

from DB_Context import get_all_productDB

data_produk = get_all_productDB()
print(data_produk)
for char in data_produk:
    print(char)

# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def tampilkan_daftar_produk_dan_toko():
#     print("\n====== Daftar Produk dan Asal Toko ======")
#     for p in produk.keys():
#         print (p)

# def cari_produk_dari_id(id_produk):
#     for p in produk:
#         if p['id'] == id_produk:
#             return p
#     return None

# def tampilkan_info_produk():
#     try:
#         id_produk = int(input("\nMasukkan ID produk yang ingin dilihat: "))
#     except ValueError:
#         input("\nID produk harus berupa angka. Silakan coba lagi...")
#         return

#     p = cari_produk_dari_id(id_produk)
#     if p:
#         print(f"\nNama Produk : {p['nama']}")
#         print(f"Harga       : Rp{p['harga']}")
#         print(f"Asal Toko   : {p['toko']}")
        
#         beli = input("Ingin membeli produk ini? (y/n): ").strip().lower()
#         if beli == 'y':
#             keranjang.append(p)
#             input("\nProduk ditambahkan ke keranjang. Tekan enter untuk lanjut...")
#         elif beli == 'n':
#             input("\nTekan enter untuk kembali...")
#         else:
#             input("\nInput tidak valid. Tekan enter untuk kembali...")
#     else:
#         input("\nID produk tidak ditemukan. Tekan enter untuk kembali...")

# def tampilkan_info_toko():
#     toko_unik = sorted(set(p['toko'] for p in produk))
#     print("\n====== Daftar Toko ======")
#     for idx, toko in enumerate(toko_unik, start=1):
#         print(f"{idx}. {toko}")
#     try:
#         pilihan = int(input("Pilih nomor toko: "))
#         nama_toko = toko_unik[pilihan - 1]
#     except (ValueError, IndexError):
#         input("\nPilihan tidak valid. Tekan enter untuk kembali...")
#         return

#     print(f"\nInformasi Toko: {nama_toko}")
#     lanjut = input("Ingin melihat produk dari toko ini? (y/n): ").strip().lower()
#     if lanjut == 'y':
#         print("\n====== Produk dari Toko Ini ======")
#         for p in produk:
#             if p['toko'] == nama_toko:
#                 print(f"  - {p['nama']} (ID: {p['id']}, Harga: Rp{p['harga']})")
#         tampilkan_info_produk()
#     elif lanjut == 'n':
#         input("\nTekan enter untuk kembali...")
#     else:
#         input("\nInput tidak valid. Tekan enter untuk kembali...")

# def fitur_melihat_toko_dan_produk():
#     while True:
#         clear_screen()
#         tampilkan_daftar_produk_dan_toko()
#         print("\nPilih:")
#         print("1. Lihat detail produk & beli")
#         print("2. Lihat informasi toko")
#         print("3. Kembali ke menu utama")
        
#         pilihan = input("Masukkan pilihan (1/2/3): ").strip()
#         if pilihan == '1':
#             tampilkan_info_produk()
#         elif pilihan == '2':
#             tampilkan_info_toko()
#         elif pilihan == '3':
#             input("\nTekan enter untuk ke menu utama...")
#             break
#         else:
#             input("\nInput tidak valid. Tekan enter untuk coba lagi...")

# if __name__ == "__main__":
#     fitur_melihat_toko_dan_produk()