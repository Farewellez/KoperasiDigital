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

# Pengurutan Merge Sort
def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    kiri = merge_sort(arr[:mid], key)
    kanan = merge_sort(arr[mid:], key)
    return merge(kiri, kanan, key)

def merge(left, right, key):
    hasil = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][key].lower() < right[j][key].lower():
            hasil.append(left[i])
            i += 1
        else:
            hasil.append(right[j])
            j += 1
    hasil.extend(left[i:])
    hasil.extend(right[j:])
    return hasil

# Binary Search
def binary_search(arr, target, key):
    low = 0
    high = len(arr) - 1
    result = []

    target = target.lower()
    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid][key].lower()

        if target == mid_val:
            # Temukan semua yang cocok di kiri dan kanan
            i = mid
            while i >= 0 and arr[i][key].lower() == target:
                result.insert(0, arr[i])
                i -= 1
                
            i = mid + 1
            while i < len(arr) and arr[i][key].lower() == target:
                result.append(arr[i])
                i += 1
            break
        elif target < mid_val:
            high = mid - 1
        else:
            low = mid + 1

    return result

def tampilkan_produk(produk_list):
    clear_screen()
    if not produk_list:
        print("Tidak ada produk ditemukan.")
        return
    print("=== Hasil Pencarian ===")
    for p in produk_list:
        print(f"- {p['nama']} (ID: {p['id']}, Harga: Rp{p['harga']}, Toko: {p['toko']})")

def fitur_searching():
    while True:
        clear_screen()
        print("=== Fitur Searching Produk / Toko ===")
        print("1. Cari Produk")
        print("2. Cari Toko")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Pilih jenis pencarian (1/2/3): ")

        if pilihan == '1':
            kata_kunci = input("Masukkan nama produk: ").strip().lower()
            produk_sorted = merge_sort(produk, 'nama')
            hasil = binary_search(produk_sorted, kata_kunci, 'nama')
            tampilkan_produk(hasil)

        elif pilihan == '2':
            kata_kunci = input("Masukkan nama toko: ").strip().lower()
            produk_sorted = merge_sort(produk, 'toko')
            hasil = binary_search(produk_sorted, kata_kunci, 'toko')
            tampilkan_produk(hasil)

        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid.")

        input("\nTekan Enter untuk kembali ke menu searching...")

fitur_searching()