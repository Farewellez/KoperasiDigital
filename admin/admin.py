import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Data_export import export_produk_csv
# import sys
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from database.connection import get_db_connection
# conn = get_db_connection()

# if conn:
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM toko")
#     toko_aktif = cur.fetchall()

#     toko_aktif = [row[0] for row in toko_aktif]
#     for toko in toko_aktif:
#         print("toko masih kosong")

# ========== DATA DUMMY ==========
penjual_requests = [
    {"id": 1, "nama": "Toko Dua", "produk": ["Baju", "Sepatu"], "status": "pending"},
]

toko_aktif = [
    {"id": 1, "nama": "Toko Satu", "produk": ["Baju", "Sepatu"], "penjual": "User A"},
]

produk_list = [
    {"id": 1, "nama": "Baju", "kategori": "Fashion", "waktu": "2025-06-01", "status": "DITERIMA"},
    {"id": 2, "nama": "Laptop", "kategori": "Elektronik", "waktu": "2025-06-03", "status": "PENDING"},
    {"id": 3, "nama": "Sepatu", "kategori": "Fashion", "waktu": "2025-06-02", "status": "DITERIMA"},
]

feedback_data = [
    {"id_feedback": 1, "id_produk": 1, "id_user": 101, "nama_user": "Andi", "tanggal": "2025-06-05", "isi_feedback": "Produknya bagus dan sesuai gambar.", "rating": 5, "balasan": ""},
    {"id_feedback": 2, "id_produk": 3, "id_user": 102, "nama_user": "Budi", "tanggal": "2025-06-06", "isi_feedback": "Ukuran agak kecil, tapi oke.", "rating": 4, "balasan": ""},
    {"id_feedback": 3, "id_produk": 1, "id_user": 103, "nama_user": "Citra", "tanggal": "2025-06-07", "isi_feedback": "Pengiriman cepat, kualitas baik.", "rating": 5, "balasan": ""},
]

# ========== SORTING & SEARCHING ==========
def selection_sort_waktu(data, ascending=True):
    for i in range(len(data)):
        idx_extreme = i
        for j in range(i + 1, len(data)):
            if (ascending and data[j]["waktu"] < data[idx_extreme]["waktu"]) or \
               (not ascending and data[j]["waktu"] > data[idx_extreme]["waktu"]):
                idx_extreme = j
        data[i], data[idx_extreme] = data[idx_extreme], data[i]
    return data

def insertion_sort_feedback(data, ascending=True):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and ((data[j]["tanggal"] > key["tanggal"]) if ascending else (data[j]["tanggal"] < key["tanggal"])):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def binary_search_produk(data, nama):
    hasil = []
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid]['nama'].lower() == nama.lower():
            hasil.append(data[mid])
            break
        elif data[mid]['nama'].lower() < nama.lower():
            left = mid + 1
        else:
            right = mid - 1
    return hasil

# ========== FUNGSI TAMPILKAN ==========
def tampilkan_produk(produk):
    clear_screen()
    if not produk:
        print("Tidak ada produk untuk ditampilkan.")
        return
    for p in produk:
        print(f"ID {p['id']}: {p['nama']} ({p['kategori']}, {p['waktu']}, Status: {p['status']})")

def tampilkan_feedback(data):
    clear_screen()
    for f in data:
        print(f"ID: {f['id_feedback']}, Produk: {f['id_produk']}, User: {f['id_user']}")
        print(f"Tanggal: {f['tanggal']}")
        print(f"Isi: {f['isi_feedback']}")
        print(f"Rating: {f['rating']}")
        print(f"Balasan: {f['balasan'] if f['balasan'] else 'Belum ada balasan'}")
        print("-" * 40)


# ========== FITUR ADMIN ==========

def konfirmasi_daftar_penjual():
    clear_screen()
    print("=== Permintaan Daftar Penjual ===")
    pending = [req for req in penjual_requests if req["status"] == "pending"]
    if not pending:
        print("Tidak ada permintaan yang pending.")
        return

    for i, req in enumerate(pending):
        print(f"{i+1}. {req['nama']} - Produk: {', '.join(req['produk'])} - Status: {req['status']}")

    try:
        idx = int(input("Pilih nomor permintaan: ")) - 1
        if idx < 0 or idx >= len(pending):
            print("Nomor tidak valid.")
            return
    except ValueError:
        print("Input harus berupa angka.")
        return

    while True:
        pilihan = input("Setujui permintaan ini? (y/n): ").strip().lower()
        if pilihan in ('y', 'n'):
            break
        print("Input tidak valid. Masukkan hanya 'y' atau 'n'.")

    if pilihan == 'y':
        toko_aktif.append(pending[idx])
        pending[idx]["status"] = "disetujui"
        print("Penjual disetujui.")
    else:
        while True:
            alasan = input("Masukkan alasan penolakan: ").strip()
            if alasan:
                break
            print("Alasan tidak boleh kosong.")
        pending[idx]["status"] = f"ditolak - {alasan}"
        print("Permintaan ditolak.")


def nonaktifkan_toko():
    clear_screen()
    print("=== Daftar Toko Aktif ===")
    if not toko_aktif:
        print("Tidak ada toko aktif.")
        return

    for i, toko in enumerate(toko_aktif):
        print(f"{i+1}. {toko['nama']}")

    try:
        idx = int(input("Pilih toko yang ingin dinonaktifkan: ")) - 1
        if idx < 0 or idx >= len(toko_aktif):
            print("Nomor tidak valid.")
            return
    except ValueError:
        print("Input harus berupa angka.")
        return

    while True:
        konfirmasi = input("Nonaktifkan toko ini? (y/n): ").strip().lower()
        if konfirmasi in ('y', 'n'):
            break
        print("Input tidak valid. Masukkan hanya 'y' atau 'n'.")

    if konfirmasi == 'y':
        while True:
            alasan = input("Masukkan alasan penghapusan: ").strip()
            if alasan:
                break
            print("Alasan tidak boleh kosong.")
        toko = toko_aktif.pop(idx)
        print(f"Toko '{toko['nama']}' dihapus. Alasan: {alasan}")
    else:
        print("Batal.")

def konfirmasi_produk():
    clear_screen()
    while True:
        print("\n=== Konfirmasi Produk Jual ===")
        print("1. Tampilkan Semua Produk")
        print("2. Filter kategori")
        print("3. Urutkan berdasarkan waktu")
        print("4. Konfirmasi produk")
        print("0. Kembali")
        
        pilihan = input("Pilih opsi: ").strip()
        if pilihan not in ("0", "1", "2", "3", "4"):
            print("Pilihan tidak valid. Masukkan angka 0-4.")
            continue

        if pilihan == "0":
            break

        elif pilihan == "1":
            if not produk_list:
                print("Tidak ada produk dalam sistem.")
            else:
                tampilkan_produk(produk_list)

        elif pilihan == "2":
            kategori = input("Masukkan kategori: ").strip()
            if not kategori or kategori.isdigit():
                print("Kategori tidak boleh kosong atau berupa angka.")
                continue
            hasil = [p for p in produk_list if p["kategori"].lower() == kategori.lower()]
            if not hasil:
                print("Tidak ditemukan produk dengan kategori tersebut.")
            else:
                tampilkan_produk(hasil)

        elif pilihan == "3":
            while True:
                urut = input("Urutkan (1. Terbaru → Terlama | 2. Terlama → Terbaru): ").strip()
                if urut in ("1", "2"):
                    ascending = urut != "1"
                    hasil = selection_sort_waktu(produk_list.copy(), ascending)
                    tampilkan_produk(hasil)
                    break
                else:
                    print("Pilihan tidak valid. Masukkan hanya 1 atau 2.")

        elif pilihan == "4":
            pending_list = [p for p in produk_list if p["status"] == "PENDING"]
            if not pending_list:
                print("Tidak ada produk yang masih pending.")
                continue
            tampilkan_produk(pending_list)

            try:
                id_konfirm = int(input("Masukkan ID produk: "))
            except ValueError:
                print("Input harus berupa angka.")
                continue

            produk_terpilih = next((p for p in produk_list if p["id"] == id_konfirm and p["status"] == "PENDING"), None)
            if not produk_terpilih:
                print("ID tidak ditemukan atau produk sudah dikonfirmasi.")
                continue

            while True:
                aksi = input("Setujui produk ini? (y/n): ").strip().lower()
                if aksi in ('y', 'n'):
                    break
                print("Input tidak valid. Masukkan hanya 'y' atau 'n'.")

            produk_terpilih["status"] = "DITERIMA" if aksi == 'y' else "DITOLAK"
            print("Status produk diperbarui.")


def detail_feedback(feedback_id):
    clear_screen()
    for f in feedback_data:
        if f["id_feedback"] == feedback_id:
            print("Detail Feedback:")
            print(f"Tanggal: {f['tanggal']}")
            print(f"Isi: {f['isi_feedback']}")
            print(f"Rating: {f['rating']}")
            print(f"Balasan: {f['balasan']}")
            return f
    print("Feedback tidak ditemukan.")
    return None

# Balas feedback
def balas_feedback(feedback_id, balasan):
    clear_screen()
    for f in feedback_data:
        if f["id_feedback"] == feedback_id:
            f["balasan"] = balasan
            print("Balasan berhasil ditambahkan.")
            return

# Hapus feedback
def hapus_feedback(feedback_id):
    clear_screen()
    global feedback_data
    feedback_data = [f for f in feedback_data if f["id_feedback"] != feedback_id]
    print("Feedback berhasil dihapus.")

# Simpan feedback (dummy)
def simpan_feedback():
    print("Feedback disimpan ke database admin.")

def menu_feedback_admin():
    clear_screen()
    while True:
        print("\n=== MENU FEEDBACK ADMIN ===")
        print("1. Tampilkan semua feedback user")
        print("2. Tampilkan feedback dari terbaru ke terlama")
        print("3. Tampilkan feedback dari terlama ke terbaru")
        print("4. Lihat detail feedback")
        print("0. Kembali ke menu admin")
        pilihan = input("Pilih menu: ")

        if pilihan == "0":
            break

        elif pilihan == "1":
            print("\n--- Semua Feedback User ---")
            tampilkan_feedback(feedback_data)

        elif pilihan == "2":
            print("\n--- Feedback Terbaru ke Terlama ---")
            sorted_data = insertion_sort_feedback(feedback_data.copy(), ascending=False)
            tampilkan_feedback(sorted_data)

        elif pilihan == "3":
            print("\n--- Feedback Terlama ke Terbaru ---")
            sorted_data = insertion_sort_feedback(feedback_data.copy(), ascending=True)
            tampilkan_feedback(sorted_data)

        elif pilihan == "4":
            try:
                feedback_id = int(input("Masukkan ID feedback yang ingin dilihat: "))
                feedback = detail_feedback(feedback_id)
                if feedback:
                    while True:
                        print("\nAksi pada Feedback:")
                        print("1. Balas feedback")
                        print("2. Hapus feedback")
                        print("3. Simpan feedback")
                        print("0. Kembali")
                        aksi = input("Pilih aksi: ")

                        if aksi == "1":
                            while True:
                                balasan = input("Masukkan balasan: ").strip()
                                if balasan:
                                    balas_feedback(feedback_id, balasan)
                                    print("Balasan tersimpan di database feedback.")
                                    break
                                else:
                                    print("Balasan tidak boleh kosong.")

                        elif aksi == "2":
                            hapus_feedback(feedback_id)
                            break

                        elif aksi == "3":
                            simpan_feedback(feedback_id)
                            break

                        elif aksi == "0":
                            break

                        else:
                            print("Pilihan tidak valid.")
            except ValueError:
                print("Input ID harus berupa angka.")
        else:
            print("Pilihan tidak valid.")

def menu_admin():
    clear_screen()
    while True:
        print("\n=== Menu Admin ===")
        print("1. Konfirmasi Daftar Penjual")
        print("2. Nonaktifkan Toko")
        print("3. Konfirmasi Produk Jual")
        print("4. Lihat Feedback Produk")
        print("0. Keluar")

        pilihan = input("Pilih fitur: ")

        if not pilihan.isdigit():
            print("Input harus berupa angka.")
            continue

        pilihan = int(pilihan)

        if pilihan == 1:
            konfirmasi_daftar_penjual()
        elif pilihan == 2:
            nonaktifkan_toko()
        elif pilihan == 3:
            konfirmasi_produk()
        elif pilihan == 4:
            menu_feedback_admin()
        elif pilihan == 0:
            print("Keluar dari menu admin.")
            break
        else:
            print("Pilihan tidak tersedia. Silakan masukkan angka 0 - 4.")


menu_admin()