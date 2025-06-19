import pandas as pd
import os
from tampilan import clear_screen, tampilkan_feedback
from algoritma import insertion_sort_feedback

# Path ke file csv
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RATING_PATH = os.path.join(BASE_DIR, 'dataCSV', 'rating.csv')

# Load data feedback dari CSV
try:
    feedback_df = pd.read_csv(RATING_PATH)
    if 'balasan' not in feedback_df.columns:
        feedback_df['balasan'] = ""
except FileNotFoundError:
    print("File rating.csv tidak ditemukan.")
    feedback_df = pd.DataFrame(columns=[
        "id_rating", "nama_pembeli", "nama_toko", "nilai",
        "komentar", "tanggal", "balasan"
    ])

feedback_data = feedback_df.to_dict(orient="records")

def detail_feedback(feedback_id):
    clear_screen()
    for f in feedback_data:
        if f["id_rating"] == feedback_id:
            print("Detail Feedback:")
            print(f"Tanggal : {f['tanggal']}")
            print(f"Pembeli : {f['nama_pembeli']}")
            print(f"Toko    : {f['nama_toko']}")
            print(f"Rating  : {f['nilai']}")
            print(f"Komentar: {f['komentar']}")
            print(f"Balasan : {f['balasan'] if f['balasan'] else 'Belum ada balasan'}")
            return f
    print("Feedback tidak ditemukan.")
    return None

def balas_feedback(feedback_id, balasan):
    for f in feedback_data:
        if f["id_rating"] == feedback_id:
            f["balasan"] = balasan
            print("\nBalasan berhasil ditambahkan.")
            return

def hapus_feedback(feedback_id):
    global feedback_data
    feedback_data = [f for f in feedback_data if f["id_rating"] != feedback_id]
    simpan_feedback(silent=True)  # panggil tanpa pesan
    print("Feedback berhasil dihapus dari database.")

def simpan_feedback(silent=False):
    df = pd.DataFrame(feedback_data)
    df.to_csv(RATING_PATH, index=False)
    if not silent:
        print("Perubahan disimpan ke file rating.csv.\n")


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
            tampilkan_feedback(feedback_data)

        elif pilihan == "2":
            sorted_data = insertion_sort_feedback(feedback_data.copy(), ascending=False)
            tampilkan_feedback(sorted_data)

        elif pilihan == "3":
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
                                    break
                                else:
                                    print("Balasan tidak boleh kosong.")

                        elif aksi == "2":
                            hapus_feedback(feedback_id)
                            break

                        elif aksi == "3":
                            simpan_feedback()
                            break

                        elif aksi == "0":
                            break

                        else:
                            print("Pilihan tidak valid.")
            except ValueError:
                print("Input ID harus berupa angka.")
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu_feedback_admin()
