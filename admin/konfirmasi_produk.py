import pandas as pd
import os
from algoritma import selection_sort_waktu, selection_sort_nama, binary_search_produk
from tampilan import clear_screen, tampilkan_produk

#path file CSV
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRODUK_PATH = os.path.join(BASE_DIR, 'dataCSV', 'produk.csv')

# Load produk dari CSV
def load_produk_csv():
    try:
        return pd.read_csv(PRODUK_PATH)
    except FileNotFoundError:
        print("File produk.csv tidak ditemukan.")
        return pd.DataFrame(columns=[
            "id_produk", "nama_produk", "harga", "id_toko",
            "kategori", "tanggal_ditambahkan", "status_produk"
        ])

def simpan_produk_csv(df):
    df.to_csv(PRODUK_PATH, index=False)

# Ubah DataFrame menjadi list of dict
def df_to_dict_list(df):
    return [
        {
            "id": int(row["id_produk"]),
            "nama": row["nama_produk"],
            "kategori": row["kategori"],
            "waktu": row["tanggal_ditambahkan"],
            "status": row["status_produk"]
        }
        for _, row in df.iterrows()
    ]

def konfirmasi_produk():
    produk_df = load_produk_csv()
    produk_list = df_to_dict_list(produk_df)

    while True:
        print("\n=== Konfirmasi Produk Jual ===")
        print("1. Tampilkan Semua Produk")
        print("2. Filter kategori")
        print("3. Urutkan berdasarkan waktu")
        print("4. Konfirmasi produk")
        print("5. Cari produk berdasarkan nama")
        print("0. Kembali")

        pilihan = input("Pilih opsi: ").strip()
        if pilihan not in ("0", "1", "2", "3", "4", "5"):
            print("Pilihan tidak valid. Masukkan angka 0-5.")
            continue

        if pilihan == "0":
            break

        elif pilihan == "1":
            if not produk_list:
                print("Tidak ada produk dalam sistem.")
            else:
                tampilkan_produk(produk_list)

        elif pilihan == "2":
            kategori = input("Masukkan kategori: ").strip()
            if not kategori or kategori.isdigit():
                print("Kategori tidak boleh kosong atau berupa angka.")
                continue
            hasil = [p for p in produk_list if p["kategori"].lower() == kategori.lower()]
            if not hasil:
                print("Tidak ditemukan produk dengan kategori tersebut.")
            else:
                tampilkan_produk(hasil)

        elif pilihan == "3":
            while True:
                urut = input("Urutkan (1. Terbaru → Terlama | 2. Terlama → Terbaru): ").strip()
                if urut in ("1", "2"):
                    ascending = urut != "1"
                    hasil = selection_sort_waktu(produk_list.copy(), ascending)
                    tampilkan_produk(hasil)
                    break
                else:
                    print("Pilihan tidak valid. Masukkan hanya 1 atau 2.")

        elif pilihan == "4":
            verifikasi_list = [p for p in produk_list if p["status"].lower().startswith("menunggu")]
            if not verifikasi_list:
                print("Tidak ada produk yang masih menunggu verifikasi.")
                continue
            tampilkan_produk(verifikasi_list)

            try:
                id_konfirm = int(input("Masukkan ID produk: "))
            except ValueError:
                print("Input harus berupa angka.")
                continue

            produk_terpilih = next(
                (p for p in produk_list if p["id"] == id_konfirm and p["status"].lower().startswith("menunggu")),
                None
            )
            if not produk_terpilih:
                print("ID tidak ditemukan atau produk sudah dikonfirmasi.")
                continue

            while True:
                aksi = input("Setujui produk ini? (y/n): ").strip().lower()
                if aksi in ('y', 'n'):
                    break
                print("Input tidak valid. Masukkan hanya 'y' atau 'n'.")

            if aksi == 'y':
                produk_df.loc[produk_df['id_produk'] == id_konfirm, 'status_produk'] = "Disetujui"
                print("✅ Produk disetujui.")
            else:
                while True:
                    alasan = input("Masukkan alasan penolakan produk: ").strip()
                    if alasan:
                        break
                    print("Alasan tidak boleh kosong.")
                produk_df.loc[produk_df['id_produk'] == id_konfirm, 'status_produk'] = f"Ditolak - {alasan}"
                print("❌ Produk ditolak dan alasan dicatat.")

            simpan_produk_csv(produk_df)
            produk_list = df_to_dict_list(produk_df)

        elif pilihan == "5":
            nama_cari = input("Masukkan nama produk yang dicari: ").strip()
            if not nama_cari:
                print("Nama produk tidak boleh kosong.")
                continue

            produk_sorted = selection_sort_nama(produk_list.copy())
            hasil = binary_search_produk(produk_sorted, nama_cari)

            if hasil:
                tampilkan_produk(hasil)
            else:
                print("Produk tidak ditemukan.")

if __name__ == "__main__":
    konfirmasi_produk()