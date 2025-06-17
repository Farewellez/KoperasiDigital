import os
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
data_produk = os.path.normpath(os.path.join(BASE_DIR, '..', 'dataCSV', 'produk.csv'))
data_toko = os.path.normpath(os.path.join(BASE_DIR, '..', 'dataCSV', 'toko.csv'))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_data():
    if not os.path.exists(data_produk) or not os.path.exists(data_toko):
        print("File produk.csv atau toko.csv tidak ditemukan.")
        return []

    produk_df = pd.read_csv(data_produk, dtype=str)
    toko_df = pd.read_csv(data_toko, dtype=str)

    produk_df['id_toko'] = produk_df['id_toko'].astype(str).str.strip()
    toko_df['id_toko'] = toko_df['id_toko'].astype(str).str.strip()

    merged_df = pd.merge(produk_df, toko_df[['id_toko', 'nama_toko']], on='id_toko', how='left')
    
    # Ubah ke list of dict agar sama seperti data dummy sebelumnya
    produk_list = []
    for _, row in merged_df.iterrows():
        produk_list.append({
            'id': row['id_produk'],
            'nama': row['nama_produk'],
            'harga': int(row['harga']),
            'toko': row['nama_toko']
        })

    return produk_list

def tampilkan_produk(produk_list):
    clear_screen()
    if not produk_list:
        input("\nTidak ada yang sesuai. Tekan enter untuk coba lagi...")
        return
    print("====== Hasil Pencarian ======\n")
    for p in produk_list:
        print(f"- {p['nama']} (ID: {p['id']}, Harga: Rp{p['harga']}, Toko: {p['toko']})")
    input("\nTekan enter untuk lanjut...")

def filter_berdasarkan_toko(produk):
    kata_kunci_toko = input("\nMasukkan nama toko: ").strip().lower()
    if not kata_kunci_toko:
        input("Input tidak boleh kosong. Tekan enter untuk coba lagi...")
        return
    hasil = [p for p in produk if kata_kunci_toko in p['toko'].lower()]
    tampilkan_produk(hasil)

def filter_berdasarkan_harga(produk):
    try:
        harga_max = int(input("\nMasukkan harga maksimum: "))
        hasil = [p for p in produk if p['harga'] <= harga_max]
        tampilkan_produk(hasil)
    except ValueError:
        input("Input harus berupa angka. Tekan enter untuk coba lagi...")

def filter_berdasarkan_produk(produk):
    kata_kunci_produk = input("\nMasukkan kata kunci nama produk: ").strip().lower()
    if not kata_kunci_produk:
        input("Input tidak boleh kosong. Tekan enter untuk coba lagi...")
        return
    hasil = [p for p in produk if kata_kunci_produk in p['nama'].lower()]
    tampilkan_produk(hasil)

def fitur_filtering_produk():
    produk = load_data()
    if not produk:
        input("\nData tidak ditemukan atau kosong. Tekan enter untuk keluar...")
        return

    while True:
        clear_screen()
        print("====== Fitur Filtering Produk ======\n")
        print("Filter berdasarkan:")
        print("1. Nama Toko")
        print("2. Harga Maksimum")
        print("3. Kata Kunci Nama Produk")
        print("4. Kembali ke Menu Utama")
        pilihan = input("Pilih jenis filter (1/2/3/4): ").strip()

        if pilihan == '1':
            filter_berdasarkan_toko(produk)
        elif pilihan == '2':
            filter_berdasarkan_harga(produk)
        elif pilihan == '3':
            filter_berdasarkan_produk(produk)
        elif pilihan == '4':
            input("\nTekan enter untuk ke menu utama...")
            break
        else:
            input("\nInput tidak valid. Tekan enter untuk coba lagi...")

if __name__ == "__main__":
    fitur_filtering_produk()
