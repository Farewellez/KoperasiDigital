import pandas as pd
import os

#path file CSV
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKO_PATH = os.path.join(BASE_DIR, 'dataCSV', 'toko.csv')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_toko():
    try:
        return pd.read_csv(TOKO_PATH)
    except FileNotFoundError:
        print(" File toko.csv tidak ditemukan.")
        return pd.DataFrame(columns=["id_toko", "nama_toko", "deskripsi_toko", "tanggal_mendaftar", "status_toko"])

def simpan_toko(df):
    df.to_csv(TOKO_PATH, index=False)

def tampilkan_toko_aktif():
    df = load_toko()
    aktif_df = df[df['status_toko'].str.lower().str.strip() == 'aktif']

    if aktif_df.empty:
        print("Tidak ada toko yang aktif.")
        return None

    print("\n=== Daftar Toko Aktif ===\n")
    print(f"{'ID':<5} {'Nama Toko':<20} {'Deskripsi Toko':<30} {'Tanggal Daftar':<15}")
    print("-" * 75)

    for _, row in aktif_df.iterrows():
        print(f"{row['id_toko']:<5} {row['nama_toko']:<20} {row['deskripsi_toko']:<30} {row['tanggal_mendaftar']:<15}")
    return aktif_df

def nonaktifkan_toko():
    clear_screen()
    aktif_df = tampilkan_toko_aktif()
    if aktif_df is None or aktif_df.empty:
        return

    try:
        id_input = int(input("\nMasukkan ID toko yang ingin dinonaktifkan: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    df = load_toko()
    if id_input not in df['id_toko'].values:
        print("ID toko tidak ditemukan.")
        return

    status_sekarang = df.loc[df['id_toko'] == id_input, 'status_toko'].values[0].lower()
    if status_sekarang.startswith('nonaktif'):
        print("Toko ini sudah dalam status nonaktif.")
        return

    nama_toko = df[df['id_toko'] == id_input]['nama_toko'].values[0]

    while True:
        konfirmasi = input(f"Nonaktifkan toko '{nama_toko}'? (y/n): ").lower()
        if konfirmasi in ('y', 'n'):
            break
        print("Input tidak valid. Masukkan hanya 'y' atau 'n'.")

    if konfirmasi == 'y':
        while True:
            alasan = input("Masukkan alasan penonaktifan toko: ").strip()
            if alasan:
                break
            print("Alasan tidak boleh kosong.")
        df.loc[df['id_toko'] == id_input, 'status_toko'] = f"nonaktif - {alasan}"
        simpan_toko(df)
        print("Toko berhasil dinonaktifkan.")
    else:
        print("Aksi dibatalkan.")

if __name__ == "__main__":
    nonaktifkan_toko()