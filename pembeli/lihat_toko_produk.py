import os
import csv
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
data_produk = os.path.normpath(os.path.join(BASE_DIR, '..', 'dataCSV', 'produk.csv'))
data_toko = os.path.normpath(os.path.join(BASE_DIR, '..', 'dataCSV', 'toko.csv'))
data_keranjang = os.path.normpath(os.path.join(BASE_DIR, '..', 'dataCSV', 'keranjang.csv'))

def load_data():
    if not os.path.exists(data_produk) or not os.path.exists(data_toko):
        print("File produk.csv atau toko.csv tidak ditemukan.")
        return pd.DataFrame()

    produk_df = pd.read_csv(data_produk, dtype=str)
    toko_df = pd.read_csv(data_toko, dtype=str)

    produk_df['id_toko'] = produk_df['id_toko'].astype(str).str.strip()
    toko_df['id_toko'] = toko_df['id_toko'].astype(str).str.strip()

    merged_df = pd.merge(produk_df, toko_df[['id_toko', 'nama_toko']], on='id_toko', how='left')

    return merged_df

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_daftar_produk_dan_toko(produk_df):
    print("\n====== Daftar Produk dan Asal Toko ======")
    for _, p in produk_df.iterrows():
        print(f"  - {p['nama_produk']} (ID: {p['id_produk']}, Harga: Rp{p['harga']}, Toko: {p['nama_toko']})")

def cari_produk_dari_id(produk_df, id_produk):
    return produk_df[produk_df['id_produk'].astype(str).str.strip() == str(id_produk).strip()]

def tambah_ke_keranjang(pembeli, nama_produk, jumlah):
    keranjang_list = []

    if os.path.exists(data_keranjang):
        with open(data_keranjang, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            keranjang_list = list(reader)

    last_id = int(keranjang_list[-1]['id_keranjang']) if keranjang_list else 0

    new_entry = {
        'id_keranjang': str(last_id + 1),
        'pembeli': pembeli,
        'nama_produk': nama_produk,
        'jumlah': str(jumlah)
    }

    file_exists = os.path.isfile(data_keranjang)
    with open(data_keranjang, 'a', newline='', encoding='utf-8') as f:
        fieldnames = ['id_keranjang', 'pembeli', 'nama_produk', 'jumlah']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists or os.stat(data_keranjang).st_size == 0:
            writer.writeheader()
        writer.writerow(new_entry)

def tampilkan_info_produk(produk_df):
    try:
        id_produk = input("\nMasukkan ID produk yang ingin dilihat: ")
    except ValueError:
        input("\nID produk harus berupa angka. Silakan coba lagi...")
        return

    p = cari_produk_dari_id(produk_df, id_produk)
    if not p.empty:
        data = p.iloc[0]
        print(f"\nNama Produk : {data['nama_produk']}")
        print(f"Harga       : Rp{data['harga']}")
        print(f"Asal Toko   : {data['nama_toko']}")

        beli = input("Ingin membeli produk ini? (y/n): ").strip().lower()
        if beli == 'y':
            try:
                jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
                pembeli = input("Masukkan nama pembeli: ").strip()
                tambah_ke_keranjang(pembeli, data['nama_produk'], jumlah)
                input("\n✅ Produk berhasil ditambahkan ke keranjang. Tekan enter untuk lanjut...")
            except ValueError:
                input("\nJumlah harus berupa angka. Tekan enter untuk kembali...")
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
        nama_toko = toko_unik.iloc[pilihan - 1]['nama_toko']
    except (ValueError, IndexError):
        input("\nPilihan tidak valid. Tekan enter untuk kembali...")
        return

    print(f"\nInformasi Toko: {nama_toko}")
    lanjut = input("Ingin melihat produk dari toko ini? (y/n): ").strip().lower()
    if lanjut == 'y':
        print(f"\n====== Produk dari Toko: {nama_toko} ======")
        for _, p in produk_df.iterrows():
            if p['nama_toko'] == nama_toko:
                print(f"  - {p['nama_produk']} (ID: {p['id_produk']}, Harga: Rp{p['harga']})")
        tampilkan_info_produk(produk_df)
    else:
        input("\nTekan enter untuk kembali...")

def fitur_melihat_toko_dan_produk():
    produk_df = load_data()
    if produk_df.empty:
        input("\nTidak ada data untuk ditampilkan. Tekan enter untuk keluar...")
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
