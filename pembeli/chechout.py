from keranjang import fitur_keranjang
from data import checkout_history

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def konfirmasi_penerimaan():
    if not checkout_history:
        input("Tidak ada barang yang bisa dikonfirmasi. Tekan Enter...")
        return

    while True:
        clear_screen()
        print("=== Konfirmasi Penerimaan Barang ===")
        for idx, item in enumerate(checkout_history, 1):
            print(f"{idx}. {item['produk']} - {item['status']}")

        try:
            pilihan = int(input("Pilih nomor barang yang sudah diterima: "))
            if pilihan == 0:
                return
            elif 1 <= pilihan <= len(checkout_history):
                checkout_history[pilihan-1]['status'] = 'Selesai'
                print("Status diperbarui menjadi 'Selesai'.")
                feedback = input("Berikan feedback untuk produk ini: ")
                print(f"Terima kasih atas feedback: \"{feedback}\"")
                input("Tekan Enter untuk kembali...")
                return
            else:
                input("Nomor tidak valid. Tekan Enter untuk ulang...")
        except ValueError:
            input("Input harus berupa angka. Tekan Enter untuk ulang...")

def fitur_status_checkout():
    while True:
        clear_screen()
        print("=== Status Checkout Barang ===")
        if not checkout_history:
            print("Belum ada transaksi checkout.")
            input("Tekan Enter untuk kembali...")
            return

        for idx, item in enumerate(checkout_history, 1):
            print(f"{idx}. {item['produk']} - {item['jumlah']} pcs | Status: {item['status']} | Toko: {item['toko']}")

        print("\nPilihan:")
        print("1. Kembali ke Keranjang")
        print("2. Kembali ke Menu Utama")
        print("3. Konfirmasi Barang Diterima")

        pilihan = input("Pilih (1/2/3): ").strip()

        if pilihan == '1':
            fitur_keranjang()
            break
        elif pilihan == '2':
            break
        elif pilihan == '3':
            konfirmasi_penerimaan()
            break
        else:
            input("Pilihan tidak valid. Tekan Enter...")

if __name__ == "__main__":
    fitur_status_checkout