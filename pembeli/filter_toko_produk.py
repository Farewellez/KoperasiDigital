import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Data dummy
produk = [
    {"id": 101, "nama": "Tamiya Biru", "harga": 50000, "toko": "Toko Alpha"},
    {"id": 102, "nama": "Tamiya Merah", "harga": 55000, "toko": "Toko Beta"},
    {"id": 103, "nama": "Mesin Jet", "harga": 75000, "toko": "Toko Alpha"},
    {"id": 104, "nama": "Ban Racing", "harga": 30000, "toko": "Toko Beta"},
    {"id": 105, "nama": "Body Transparan", "harga": 45000, "toko": "Toko Gamma"}
]

def tampilkan_produk(produk_list):
    clear_screen()
    if not produk_list:
        print("Tidak ada produk yang cocok dengan filter.")
        return
    print("=== Hasil Filter Produk ===")
    for p in produk_list:
        print(f"- {p['nama']} (ID: {p['id']}, Harga: Rp{p['harga']}, Toko: {p['toko']})")

def fitur_filtering_produk():
    while True:
        clear_screen()
        print("=== Fitur Filtering Produk ===")
        print("Filter berdasarkan:")
        print("1. Nama Toko")
        print("2. Harga Maksimum")
        print("3. Kata Kunci Nama Produk")
        print("4. Kembali ke Menu Utama")
        pilihan = input("Pilih jenis filter (1/2/3/4): ")

        if pilihan == '1':
            nama_toko = input("Masukkan nama toko: ").strip().lower()
            hasil = [p for p in produk if p['toko'].lower() == nama_toko]
            tampilkan_produk(hasil)

        elif pilihan == '2':
            try:
                harga_max = int(input("Masukkan harga maksimum: "))
                hasil = [p for p in produk if p['harga'] <= harga_max]
                tampilkan_produk(hasil)
            except ValueError:
                print("Input harus berupa angka.")

        elif pilihan == '3':
            kata_kunci = input("Masukkan kata kunci nama produk: ").strip().lower()
            hasil = [p for p in produk if kata_kunci in p['nama'].lower()]
            tampilkan_produk(hasil)

        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid.")

        input("\nTekan Enter untuk kembali ke menu filter...")


fitur_filtering_produk()