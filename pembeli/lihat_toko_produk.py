import os
import csv
import pandas as pd
# from dataCSV import *

# ==============================

# Muat data produk & toko
def muat_data():
    path_produk = os.path.join(os.path.dirname(__file__), '..', 'produk.csv')
    path_toko = os.path.join(os.path.dirname(__file__), '..', 'toko.csv')

    if not os.path.exists(path_produk) or not os.path.exists(path_toko):
        print("File CSV tidak ditemukan.")
        return None, None

    produk_df = pd.read_csv(path_produk, dtype=str)
    toko_df = pd.read_csv(path_toko, dtype=str)

    # Gabungkan untuk dapatkan nama toko pada data produk
    merged_df = produk_df.merge(toko_df[['id_toko', 'nama_toko']], on='id_toko', how='left')

    return merged_df, toko_df


def simpan_ke_keranjang_csv(data):
    path_keranjang = os.path.join(os.path.dirname(__file__), '..', 'keranjang.csv')

    # Jika file belum ada, tulis header
    file_ada = os.path.exists(path_keranjang)
    with open(path_keranjang, mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ['id_keranjang', 'id_produk', 'nama_produk', 'harga', 'id_toko', 'nama_toko']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_ada:
            writer.writeheader()

        # Hitung id_keranjang otomatis (berdasarkan isi file)
        id_keranjang = 1
        if file_ada:
            with open(path_keranjang, mode='r', encoding='utf-8') as readfile:
                reader = csv.DictReader(readfile)
                id_keranjang = sum(1 for _ in reader) + 1

        # Siapkan data
        baris = {
            'id_keranjang': id_keranjang,
            'id_produk': data['id_produk'],
            'nama_produk': data['nama_produk'],
            'harga': data['harga'],
            'id_toko': data['id_toko'],
            'nama_toko': data['nama_toko']
        }

        writer.writerow(baris)

# ===============================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_daftar_produk_dan_toko(produk_df):
    print("\n====== Daftar Produk dan Asal Toko ======")
    for _, row in produk_df.iterrows():
        print(f"  - {row['nama_produk']} (ID: {row['id_produk']}, Harga: Rp{row['harga']}, Toko: {row['nama_toko']})")

def cari_produk_dari_id(produk_df, id_produk):
    return produk_df[produk_df['id_produk'] == id_produk]

def tampilkan_info_produk(produk_df):
    id_produk = input("\nMasukkan ID produk yang ingin dilihat: ").strip()
    hasil = cari_produk_dari_id(produk_df, id_produk)

    if not hasil.empty:
        row = hasil.iloc[0]
        print(f"\nNama Produk : {row['nama_produk']}")
        print(f"Harga       : Rp{row['harga']}")
        print(f"Asal Toko   : {row['nama_toko']}")

        beli = input("Ingin membeli produk ini? (y/n): ").strip().lower()
        if beli == 'y':
            keranjang.append(row.to_dict())
            input("\nProduk ditambahkan ke keranjang. Tekan enter untuk lanjut...")
        elif beli == 'n':
            input("\nTekan enter untuk kembali...")
        else:
            input("\nInput tidak valid. Tekan enter untuk kembali...")
    else:
        input("\nID produk tidak ditemukan. Tekan enter untuk kembali...")

def tampilkan_info_toko(produk_df):
    toko_unik = produk_df[['id_toko', 'nama_toko']].drop_duplicates().reset_index(drop=True)

    print("\n====== Daftar Toko ======")
    for idx, row in toko_unik.iterrows():
        print(f"{idx + 1}. {row['nama_toko']} (ID: {row['id_toko']})")

    try:
        pilihan = int(input("Pilih nomor toko: "))
        selected_toko = toko_unik.iloc[pilihan - 1]
    except (ValueError, IndexError):
        input("\nPilihan tidak valid. Tekan enter untuk kembali...")
        return

    print(f"\nInformasi Toko: {selected_toko['nama_toko']}")
    lanjut = input("Ingin melihat produk dari toko ini? (y/n): ").strip().lower()
    if lanjut == 'y':
        print(f"\n====== Produk dari {selected_toko['nama_toko']} ======")
        filter_df = produk_df[produk_df['id_toko'] == selected_toko['id_toko']]
        for _, row in filter_df.iterrows():
            print(f"  - {row['nama_produk']} (ID: {row['id_produk']}, Harga: Rp{row['harga']})")
        tampilkan_info_produk(produk_df)
    else:
        input("\nTekan enter untuk kembali...")

def fitur_melihat_toko_dan_produk():
    produk_df, toko_df = muat_data()
    if produk_df is None or toko_df is None:
        return

    while True:
        clear_screen()
        tampilkan_daftar_produk_dan_toko(produk_df)
        print("\nPilih:")
        print("1. Lihat detail produk & beli")
        print("2. Lihat informasi toko")
        print("3. Kembali ke menu utama")

        pilihan = input("Masukkan pilihan (1/2/3): ").strip()
        if pilihan == '1':
            tampilkan_info_produk(produk_df)
        elif pilihan == '2':
            tampilkan_info_toko(produk_df)
        elif pilihan == '3':
            input("\nTekan enter untuk ke menu utama...")
            break
        else:
            input("\nInput tidak valid. Tekan enter untuk coba lagi...")

if __name__ == "__main__":
    fitur_melihat_toko_dan_produk()
