import os
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
data_produk = os.path.normpath(os.path.join(BASE_DIR, '..', 'dataCSV', 'produk.csv'))
data_toko = os.path.normpath(os.path.join(BASE_DIR, '..', 'dataCSV', 'toko.csv'))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_data():
    if not os.path.exists(data_produk) or not os.path.exists(data_toko):
        print("File produk.csv atau toko.csv tidak ditemukan.")
        return []

    produk_df = pd.read_csv(data_produk, dtype=str)
    toko_df = pd.read_csv(data_toko, dtype=str)

    produk_df['id_toko'] = produk_df['id_toko'].astype(str).str.strip()
    toko_df['id_toko'] = toko_df['id_toko'].astype(str).str.strip()

    merged_df = pd.merge(produk_df, toko_df[['id_toko', 'nama_toko']], on='id_toko', how='left')

    produk_list = []
    for _, row in merged_df.iterrows():
        produk_list.append({
            'id': row['id_produk'],
            'nama': row['nama_produk'],
            'harga': int(row['harga']),
            'toko': row['nama_toko']
        })

    return produk_list

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

def binary_search(arr, target, key):
    low = 0
    high = len(arr) - 1
    result = []

    target = target.lower()
    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid][key].lower()

        if target == mid_val:
            result.append(arr[mid])
            i = mid - 1
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
        input("\nTidak ada yang sesuai. Tekan enter untuk coba lagi...")
        return
    print("====== Hasil Pencarian ======\n")
    for p in produk_list:
        print(f"- {p['nama']} (ID: {p['id']}, Harga: Rp{p['harga']}, Toko: {p['toko']})")
    input("\nTekan enter untuk lanjut...")

def cari_produk(produk):
    kata_kunci = input("\nMasukkan nama produk: ").strip().lower()
    if not kata_kunci:
        input("\nInput tidak boleh kosong. Tekan Enter untuk coba lagi...")
        return
    produk_sorted = merge_sort(produk, 'nama')
    hasil = binary_search(produk_sorted, kata_kunci, 'nama')
    tampilkan_produk(hasil)

def cari_toko(produk):
    kata_kunci = input("\nMasukkan nama toko: ").strip().lower()
    if not kata_kunci:
        input("\nInput tidak boleh kosong. Tekan Enter untuk coba lagi...")
        return
    produk_sorted = merge_sort(produk, 'toko')
    hasil = binary_search(produk_sorted, kata_kunci, 'toko')
    tampilkan_produk(hasil)

def fitur_searching():
    produk = load_data()
    if not produk:
        input("\nData tidak tersedia. Tekan enter untuk keluar...")
        return

    while True:
        clear_screen()
        print("====== Searching Produk dan Toko ======")
        print("1. Cari Produk")
        print("2. Cari Toko")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Pilih jenis pencarian (1/2/3): ").strip()

        if pilihan == '1':
            cari_produk(produk)
        elif pilihan == '2':
            cari_toko(produk)
        elif pilihan == '3':
            input("\nTekan enter untuk ke menu utama...")
            break
        else:
            input("\nPilihan tidak valid. Tekan Enter untuk coba lagi...")

if __name__ == "__main__":
    fitur_searching()
