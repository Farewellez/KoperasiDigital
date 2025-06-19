import os
from data import keranjang

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hapus_dari_keranjang():
    if not keranjang:
        input("Keranjang kosong. Tekan Enter untuk kembali...")
        return

    while True:
        clear_screen()
        print("=== Hapus Produk dari Keranjang ===")
        for idx, item in enumerate(keranjang, start=1):
            print(f"{idx}. {item['nama']} - {item['jumlah']} pcs (Toko: {item['toko']})")

        try:
            pilihan = int(input("Pilih nomor produk yang ingin dihapus (0 untuk batal): "))
            if pilihan == 0:
                return
            elif 1 <= pilihan <= len(keranjang):
                konfirmasi = input(f"Yakin ingin menghapus '{keranjang[pilihan-1]['nama']}'? (y/n): ").lower()
                if konfirmasi == 'y':
                    keranjang.pop(pilihan-1)
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
    global checkout_history
    if not keranjang:
        input("Keranjang kosong. Tidak bisa checkout. Tekan Enter...")
        return

    clear_screen()
    print("=== Checkout ===")
    total = sum(item['harga'] * item['jumlah'] for item in keranjang)
    print(f"Total: Rp{total}")

    konfirmasi = input("Lanjutkan checkout? (y/n): ").lower()
    if konfirmasi == 'y':
        for item in keranjang:
            checkout_history.append({
                'produk': item['nama'],
                'jumlah': item['jumlah'],
                'status': 'Diproses',
                'toko': item['toko']
            })
        keranjang.clear()
        print("Checkout berhasil! Barang sedang diproses.")
    else:
        print("Checkout dibatalkan.")
    input("Tekan Enter untuk kembali ke menu utama...")

def fitur_keranjang():
    while True:
        clear_screen()
        print("=== Keranjang Belanja ===")
        if not keranjang:
            print("Keranjang kosong.")
        else:
            total_harga = 0
            for idx, item in enumerate(keranjang, start=1):
                subtotal = item['harga'] * item['jumlah']
                total_harga += subtotal
                print(f"{idx}. {item['nama']} - Rp{item['harga']} x {item['jumlah']} = Rp{subtotal} (Toko: {item['toko']})")
            print(f"\nTotal Belanja: Rp{total_harga}")

        print("\nPilihan:")
        print("1. Hapus Produk dari Keranjang")
        print("2. Checkout")
        print("3. Kembali ke Menu Utama")

        pilihan = input("Pilih (1/2/3): ").strip()

        if pilihan == '1':
            hapus_dari_keranjang()
        elif pilihan == '2':
            checkout()
            break
        elif pilihan == '3':
            break
        else:
            input("Pilihan tidak valid. Tekan Enter untuk lanjut...")

if __name__ == "__main__":
    fitur_keranjang