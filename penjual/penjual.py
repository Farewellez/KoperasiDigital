produk_list = []
pesanan_list = []

kurir_list = [
    {"id": 1, "nama": "Kurir A", "kota": "Jember", "jarak_km": 5},
    {"id": 2, "nama": "Kurir B", "kota": "Banyuwangi", "jarak_km": 10},
    {"id": 3, "nama": "Kurir C", "kota": "Jember", "jarak_km": 3},
]

id_counter = 1
pesanan_counter = 1


def tambah_produk():
    global id_counter
    nama = input("Nama produk: ")
    harga = int(input("Harga produk: "))
    stok = int(input("Stok: "))
    deskripsi = input("Deskripsi: ")

    produk_list.append({
        "id": id_counter,
        "nama": nama,
        "harga": harga,
        "stok": stok,
        "deskripsi": deskripsi
    })

    id_counter += 1
    print("Produk berhasil ditambahkan.\n")


def lihat_produk():
    if not produk_list:
        print("Belum ada produk.")
    else:
        print("\nDaftar Produk:")
        for p in produk_list:
            print(f"ID: {p['id']} | Nama: {p['nama']} | Harga: {p['harga']} | "
                  f"Stok: {p['stok']} | Deskripsi: {p['deskripsi']}")


def update_produk():
    lihat_produk()
    id_produk = int(input("\nMasukkan ID produk yang ingin diupdate: "))

    for p in produk_list:
        if p['id'] == id_produk:
            p['nama'] = input("Nama baru: ")
            p['harga'] = int(input("Harga baru: "))
            p['stok'] = int(input("Stok baru: "))
            p['deskripsi'] = input("Deskripsi baru: ")
            print("Produk berhasil diupdate.\n")
            return

    print("Produk tidak ditemukan.\n")

def hapus_produk():
    lihat_produk()
    id_produk = int(input("\nMasukkan ID produk yang ingin dihapus: "))

    global produk_list
    produk_list = [p for p in produk_list if p['id'] != id_produk]

    print("Produk berhasil dihapus.\n")


def konfirmasi_pesanan():
    global pesanan_list

    if not pesanan_list:
        print("Belum ada pesanan.")
        return

    print("\nDaftar Pesanan:")
    for p in pesanan_list:
        print(f"ID: {p['id']} | Produk: {p['produk']} | Pembeli: {p['pembeli']} | Status: {p['status']}")

    id_pesanan = int(input("Masukkan ID pesanan yang ingin dikonfirmasi: "))

    for p in pesanan_list:
        if p['id'] == id_pesanan:
            p['status'] = 'dikonfirmasi'
            print("Pesanan berhasil dikonfirmasi.\n")
            return

    print("Pesanan tidak ditemukan.\n")


def apply_kurir_terdekat():
    kota = input("Masukkan kota penjual: ")
    kurir_di_kota = [k for k in kurir_list if k['kota'].lower() == kota.lower()]

    if kurir_di_kota:
        kurir_terdekat = sorted(kurir_di_kota, key=lambda x: x['jarak_km'])[0]
        print(f"Kurir terdekat: ID: {kurir_terdekat['id']} | Nama: {kurir_terdekat['nama']} | "
              f"Kota: {kurir_terdekat['kota']} | Jarak: {kurir_terdekat['jarak_km']} km")
    else:
        print("Tidak ada kurir di kota tersebut.")


def binary_search_produk(data, keyword):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        nama_produk = data[mid]['nama'].lower()

        if keyword == nama_produk:
            return data[mid]
        elif keyword < nama_produk:
            right = mid - 1
        else:
            left = mid + 1

    return None


def cari_produk():
    if not produk_list:
        print("Belum ada produk.")
        return

    keyword = input("Masukkan nama lengkap produk (huruf kecil semua): ").lower()
    sorted_produk = sorted(produk_list, key=lambda x: x['nama'].lower())
    hasil = binary_search_produk(sorted_produk, keyword)

    if hasil:
        print("\nProduk ditemukan:")
        print(f"ID: {hasil['id']} | Nama: {hasil['nama']} | Harga: {hasil['harga']} | "
              f"Stok: {hasil['stok']} | Deskripsi: {hasil['deskripsi']}")
    else:
        print("Produk tidak ditemukan.")


def merge_sort_produk(data, ascending=True):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left_half = merge_sort_produk(data[:mid], ascending)
    right_half = merge_sort_produk(data[mid:], ascending)

    return merge(left_half, right_half, ascending)


def merge(left, right, ascending):
    result = []

    while left and right:
        if ascending:
            if left[0]['harga'] <= right[0]['harga']:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        else:
            if left[0]['harga'] >= right[0]['harga']:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

    result.extend(left or right)
    return result


def urutkan_produk():
    if not produk_list:
        print("Belum ada produk.")
        return

    print("\nUrutkan berdasarkan harga:")
    print("1. Termurah ke Termahal")
    print("2. Termahal ke Termurah")
    pilihan = input("Pilih (1/2): ")

    if pilihan == "1":
        sorted_data = merge_sort_produk(produk_list, ascending=True)
    elif pilihan == "2":
        sorted_data = merge_sort_produk(produk_list, ascending=False)
    else:
        print("Pilihan tidak valid.")
        return

    print("\nHasil Pengurutan:")
    for p in sorted_data:
        print(f"ID: {p['id']} | Nama: {p['nama']} | Harga: {p['harga']} | "
              f"Stok: {p['stok']} | Deskripsi: {p['deskripsi']}")


def menu_penjual():
    while True:
        print("""
=== MENU PENJUAL ===
1. Tambah Produk
2. Lihat Produk
3. Update Produk
4. Hapus Produk
5. Konfirmasi Pesanan
6. Apply Kurir Terdekat
7. Keluar
8. Cari Produk
9. Urutkan Produk
""")
        pilihan = input("Pilih menu (1-9): ")

        if pilihan == "1":
            tambah_produk()
        elif pilihan == "2":
            lihat_produk()
        elif pilihan == "3":
            update_produk()
        elif pilihan == "4":
            hapus_produk()
        elif pilihan == "5":
            konfirmasi_pesanan()
        elif pilihan == "6":
            apply_kurir_terdekat()
        elif pilihan == "7":
            print("Keluar dari menu penjual.")
            break
        elif pilihan == "8":
            cari_produk()
        elif pilihan == "9":
            urutkan_produk()
        else:
            print("Pilihan tidak valid.\n")


if __name__ == "__main__":
    menu_penjual()
