import pandas as pd
import os
from datetime import datetime
#path file CSV
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUESTS_PATH = os.path.join(BASE_DIR, 'dataCSV', 'penjual_requests.csv')
TOKO_PATH = os.path.join(BASE_DIR, 'dataCSV', 'toko.csv')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_request_penjual():
    try:
        return pd.read_csv(REQUESTS_PATH)
    except FileNotFoundError:
        print("File tidak ditemukan:", REQUESTS_PATH)
        return pd.DataFrame(columns=["id", "nama", "produk", "status"])

def simpan_request_penjual(df):
    df.to_csv(REQUESTS_PATH, index=False)

def load_toko():
    try:
        return pd.read_csv(TOKO_PATH)
    except FileNotFoundError:
        return pd.DataFrame(columns=["id_toko", "nama_toko", "deskripsi_toko", "tanggal_mendaftar", "status_toko"])

def simpan_toko(df):
    df.to_csv(TOKO_PATH, index=False)

def tampilkan_request_pending():
    df = load_request_penjual()
    pending = df[df['status'].str.lower().str.strip() == 'menunggu verifikasi']

    if pending.empty:
        print("Tidak ada permintaan pendaftaran penjual yang menunggu verifikasi.")
        return None

    pending_list = pending.to_dict('records')

    print("=" * 95)
    print(f"{'ID':<5} {'Nama Toko':<25} {'Produk':<30} {'Status':<30}")
    print("-" * 95)
    for p in pending_list:
        produk_bersih = p['produk'].replace(';', ', ')
        print(f"{p['id']:<5} {p['nama']:<25} {produk_bersih:<30} {p['status']:<30}")
    print("=" * 95)

    return pending

def konfirmasi_penjual():
    clear_screen()
    pending_df = tampilkan_request_pending()
    if pending_df is None or pending_df.empty:
        return

    try:
        id_input = int(input("\nMasukkan ID penjual yang ingin dikonfirmasi/ditolak: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    df = load_request_penjual()
    if id_input not in df['id'].values:
        print("ID penjual tidak ditemukan.")
        return

    selected = df[df['id'] == id_input].iloc[0]

    while True:
        konfirmasi = input(f"Setujui pendaftaran penjual '{selected['nama']}'? (y/n): ").strip().lower()
        if konfirmasi in ('y', 'n'):
            break
        print("Input tidak valid. Masukkan hanya 'y' atau 'n'.")

    if konfirmasi == 'y':
        df.loc[df['id'] == id_input, 'status'] = 'disetujui'
        toko_df = load_toko()
        toko_df['id_toko'] = toko_df['id_toko'].astype(int) if not toko_df.empty else pd.Series(dtype=int)

        if id_input in toko_df['id_toko'].values:
            print("Toko sudah ada dalam daftar.")
        else:
            toko_baru = {
                "id_toko": id_input,
                "nama_toko": selected['nama'],
                "deskripsi_toko": "Belum ada deskripsi",
                "tanggal_mendaftar": datetime.now().strftime("%Y-%m-%d"),
                "status_toko": "aktif"
            }
            toko_df = pd.concat([toko_df, pd.DataFrame([toko_baru])], ignore_index=True)
            simpan_toko(toko_df)
            print("Penjual disetujui dan ditambahkan ke daftar toko.")
    else:
        while True:
            alasan = input("Masukkan alasan penolakan: ").strip()
            if alasan:
                break
            print("Alasan tidak boleh kosong.")
        df.loc[df['id'] == id_input, 'status'] = f'ditolak - {alasan}'
        print("Permintaan ditolak.")

    simpan_request_penjual(df)

if __name__ == "__main__":
    konfirmasi_penjual()