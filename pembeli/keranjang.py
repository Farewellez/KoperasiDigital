import os
import pandas as pd
import csv

BASE_DIR = os.path.dirname(__file__)
KERANJANG_FILE = os.path.normpath(os.path.join(BASE_DIR, '..', 'dataCSV', 'keranjang.csv'))
PRODUK_FILE = os.path.normpath(os.path.join(BASE_DIR, '..', 'dataCSV', 'produk.csv'))
TOKO_FILE = os.path.normpath(os.path.join(BASE_DIR, '..', 'dataCSV', 'toko.csv'))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def baca_data_referensi():
    produk_df = pd.read_csv(PRODUK_FILE, dtype=str)
    produk_df['harga'] = produk_df['harga'].astype(int)
    toko_df = pd.read_csv(TOKO_FILE, dtype=str)
    produk_df = pd.merge(produk_df, toko_df, on='id_toko', how='left')
    return produk_df

def baca_keranjang():
    try:
        df = pd.read_csv(KERANJANG_FILE, dtype=str)
        df['jumlah'] = df['jumlah'].astype(int)
        return df.to_dict('records')
    except Exception as e:
        print(f"Gagal membaca file keranjang: {e}")
        return []

def tulis_keranjang(data):
    fieldnames = ['id_keranjang', 'pembeli', 'nama_produk', 'jumlah', 'status', 'feedback']
    with open(KERANJANG_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def cari_info_produk(nama_produk, produk_df):
    match = produk_df[produk_df['nama_produk'] == nama_produk]
    if not match.empty:
        return match.iloc[0]['harga'], match.iloc[0]['nama_toko']
    return 0, "Toko Tidak Diketahui"

def hapus_dari_keranjang():
    keranjang = baca_keranjang()
    produk_df = baca_data_referensi()

    if not keranjang:
        input("Keranjang kosong. Tekan Enter untuk kembali...")
        return

    while True:
        clear_screen()
        print("=== Hapus Produk dari Keranjang ===")
        for idx, item in enumerate(keranjang, 1):
            _, toko = cari_info_produk(item['nama_produk'], produk_df)
            print(f"{idx}. {item['nama_produk']} - {item['jumlah']} pcs (Toko: {toko})")

        try:
            pilihan = int(input("Pilih nomor produk yang ingin dihapus (0 untuk batal): "))
            if pilihan == 0:
                return
            elif 1 <= pilihan <= len(keranjang):
                konfirmasi = input(f"Yakin ingin menghapus '{keranjang[pilihan-1]['nama_produk']}'? (y/n): ").lower()
                if konfirmasi == 'y':
                    keranjang.pop(pilihan-1)
                    tulis_keranjang(keranjang)
                    print("Produk berhasil dihapus.")
                else:
                    print("Penghapusan dibatalkan.")
                input("Tekan Enter untuk kembali...")
                return
            else:
                input("Nomor tidak valid. Tekan Enter untuk ulang...")
        except ValueError:
            input("Input harus angka. Tekan Enter untuk ulang...")

def checkout():
    keranjang = baca_keranjang()
    if not keranjang:
        input("Keranjang kosong. Tidak bisa checkout. Tekan Enter...")
        return

    produk_df = baca_data_referensi()
    clear_screen()
    print("=== Checkout ===")

    total = 0
    for item in keranjang:
        if item.get('status', '') == '' or pd.isna(item.get('status')):
            harga, _ = cari_info_produk(item['nama_produk'], produk_df)
            subtotal = harga * item['jumlah']
            total += subtotal

    print(f"Total: Rp{total}")

    konfirmasi = input("Lanjutkan checkout? (y/n): ").lower()
    if konfirmasi == 'y':
        for item in keranjang:
            if item.get('status', '') == '' or pd.isna(item.get('status')):
                item['status'] = 'Diproses'
                item['feedback'] = ''
        tulis_keranjang(keranjang)
        print("Checkout berhasil! Barang sedang diproses.")
    else:
        print("Checkout dibatalkan.")
    input("Tekan Enter untuk kembali ke menu utama...")

def fitur_keranjang():
    while True:
        keranjang = baca_keranjang()
        produk_df = baca_data_referensi()

        keranjang_belum_checkout = [k for k in keranjang if k.get('status', '') == '' or pd.isna(k.get('status'))]
        clear_screen()
        print("=== Keranjang Belanja ===")

        if not keranjang_belum_checkout:
            print("Keranjang kosong.")
        else:
            total_harga = 0
            for idx, item in enumerate(keranjang_belum_checkout, 1):
                harga, toko = cari_info_produk(item['nama_produk'], produk_df)
                subtotal = harga * item['jumlah']
                total_harga += subtotal
                print(f"{idx}. {item['nama_produk']} - Rp{harga} x {item['jumlah']} = Rp{subtotal} (Toko: {toko})")
            print(f"\nTotal Belanja: Rp{total_harga}")

        print("\nPilihan:")
        print("1. Hapus Produk dari Keranjang")
        print("2. Checkout")
        print("3. Lihat Status & Beri Feedback")
        print("4. Kembali ke Menu Utama")

        pilihan = input("Pilih (1/2/3/4): ").strip()

        if pilihan == '1':
            hapus_dari_keranjang()
        elif pilihan == '2':
            checkout()
        elif pilihan == '3':
            lihat_status_dan_feedback()
        elif pilihan == '4':
            break
        else:
            input("Pilihan tidak valid. Tekan Enter untuk lanjut...")

def lihat_status_dan_feedback():
    keranjang = baca_keranjang()
    produk_df = baca_data_referensi()

    status_checkout = [item for item in keranjang if item.get('status') == 'Diproses']
    if not status_checkout:
        input("Belum ada pesanan yang diproses. Tekan Enter untuk kembali...")
        return

    while True:
        clear_screen()
        print("=== Status Pesanan & Feedback ===")
        for idx, item in enumerate(status_checkout, 1):
            harga, toko = cari_info_produk(item['nama_produk'], produk_df)
            subtotal = harga * item['jumlah']
            feedback_text = item['feedback'] if item['feedback'] else "-"
            print(f"{idx}. {item['nama_produk']} x{item['jumlah']} dari {toko} | Total: Rp{subtotal} | Feedback: {feedback_text}")

        print("\nPilihan:")
        print("1. Beri Feedback")
        print("2. Kembali ke Menu")

        pilihan = input("Pilih (1/2): ").strip()
        if pilihan == '1':
            try:
                no = int(input("Masukkan nomor pesanan yang ingin diberi feedback: "))
                if 1 <= no <= len(status_checkout):
                    feedback = input("Masukkan feedback Anda: ").strip()
                    id_target = status_checkout[no - 1]['id_keranjang']

                    for i in range(len(keranjang)):
                        if keranjang[i]['id_keranjang'] == id_target:
                            keranjang[i]['feedback'] = feedback
                            break

                    tulis_keranjang(keranjang)
                    input("Feedback berhasil disimpan. Tekan Enter...")
                else:
                    input("Nomor tidak valid. Tekan Enter untuk ulang...")
            except ValueError:
                input("Input harus berupa angka. Tekan Enter untuk ulang...")
        elif pilihan == '2':
            break
        else:
            input("Pilihan tidak valid. Tekan Enter untuk ulang...")

if __name__ == '__main__':
    fitur_keranjang()
