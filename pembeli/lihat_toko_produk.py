import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Data dummy
toko_list = [
    {"id": 1, "nama": "Toko Alpha", "produk": [
        {"id": 101, "nama": "Tamiya Biru", "harga": 50000},
        {"id": 102, "nama": "Dinamo Turbo", "harga": 75000}
    ]},
    {"id": 2, "nama": "Toko Beta", "produk": [
        {"id": 201, "nama": "Tamiya Merah", "harga": 55000},
        {"id": 202, "nama": "Ban Racing", "harga": 30000}
    ]}
]

keranjang = []

def tampilkan_daftar_produk_dan_toko():
    print("\n--- Daftar Produk dan Asal Toko ---")
    for toko in toko_list:
        print(f"\nToko: {toko['nama']}")
        for produk in toko['produk']:
            print(f"  - {produk['nama']} (ID: {produk['id']}, Harga: Rp{produk['harga']})")

def cari_produk_dari_id(id_produk):
    for toko in toko_list:
        for produk in toko['produk']:
            if produk['id'] == id_produk:
                return produk, toko['nama']
    return None, None

def tampilkan_info_produk():
    id_produk = int(input("\nMasukkan ID produk yang ingin dilihat: "))
    produk, asal_toko = cari_produk_dari_id(id_produk)
    if produk:
        print(f"\nNama Produk : {produk['nama']}")
        print(f"Harga       : Rp{produk['harga']}")
        print(f"Asal Toko   : {asal_toko}")
        beli = input("Ingin membeli produk ini? (y/n): ").lower()
        if beli == 'y':
            keranjang.append(produk)
            print("Produk ditambahkan ke keranjang.")
        else:
            print("Kembali ke pemilihan produk.")
    else:
        print("Produk tidak ditemukan.")

def tampilkan_info_toko():
    print("\n--- Daftar Toko ---")
    for toko in toko_list:
        print(f"{toko['id']}. {toko['nama']}")
    id_toko = int(input("Pilih ID toko: "))
    toko_terpilih = next((toko for toko in toko_list if toko['id'] == id_toko), None)
    if toko_terpilih:
        print(f"\nInformasi Toko: {toko_terpilih['nama']}")
        lanjut = input("Ingin melihat produk dari toko ini? (y/n): ").lower()
        if lanjut == 'y':
            print("\n--- Produk dari Toko Ini ---")
            for produk in toko_terpilih['produk']:
                print(f"  - {produk['nama']} (ID: {produk['id']}, Harga: Rp{produk['harga']})")
            tampilkan_info_produk()
        else:
            print("Kembali ke pemilihan toko/produk.")
    else:
        print("Toko tidak ditemukan.")

def fitur_melihat_toko_dan_produk():
    while True:
        clear_screen()
        # print("\n=== Fitur Lihat Toko & Produk ===")
        tampilkan_daftar_produk_dan_toko()
        print("\nPilih:")
        print("1. Lihat detail produk & beli")
        print("2. Lihat informasi toko")
        print("3. Kembali ke menu utama")
        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == '1':
            tampilkan_info_produk()
        elif pilihan == '2':
            tampilkan_info_toko()
        elif pilihan == '3':
            print("Kembali ke menu utama.")
            break
        else:
            print("Pilihan tidak valid.")
