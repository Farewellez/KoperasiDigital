import os
from data import produk

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_produk(produk_list):
    clear_screen()
    if not produk_list:
        input("\nTidak ada yang sesuai. Tekan enter untuk coba lagi...")
        return
    print("====== Hasil Pencarian ======\n")
    for p in produk_list:
        print(f"- {p['nama']} (ID: {p['id']}, Harga: Rp{p['harga']}, Toko: {p['toko']})")
    input("\nTekan enter untuk lanjut...")


def filter_berdasarkan_toko():
    kata_kunci_toko = input("\nMasukkan nama toko: ").strip().lower()
    if not kata_kunci_toko:
        input("Input tidak boleh kosong. Tekan enter untuk coba lagi...")
        return
    hasil = [p for p in produk if kata_kunci_toko in p['toko'].lower()]
    tampilkan_produk(hasil)

def filter_berdasarkan_harga():
    try:
        harga_max = int(input("\nMasukkan harga maksimum: "))
        hasil = [p for p in produk if p['harga'] <= harga_max]
        tampilkan_produk(hasil)
    except ValueError:
        input("Input harus berupa angka. Tekan enter untuk coba lagi...")

def filter_berdasarkan_produk():
    kata_kunci_produk = input("\nMasukkan kata kunci nama produk: ").strip().lower()
    if not kata_kunci_produk:
        input("Input tidak boleh kosong. Tekan enter untuk coba lagi...")
        return
    hasil = [p for p in produk if kata_kunci_produk in p['nama'].lower()]
    tampilkan_produk(hasil)

def fitur_filtering_produk():
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
            filter_berdasarkan_toko()
        elif pilihan == '2':
            filter_berdasarkan_harga()
        elif pilihan == '3':
            filter_berdasarkan_produk()
        elif pilihan == '4':
            input("\nTekan enter untuk ke menu utama...")
            break
        else:
            input("\nInput tidak valid. Tekan enter untuk coba lagi...")

if __name__ == "__main__":
    fitur_filtering_produk