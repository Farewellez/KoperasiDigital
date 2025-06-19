import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# ========== FUNGSI TAMPILKAN ==========
def tampilkan_produk(produk):
    clear_screen()
    if not produk:
        print("Tidak ada produk untuk ditampilkan.")
        return

    print("=" * 80)
    print(f"{'ID':<5} {'Nama Produk':<25} {'Kategori':<15} {'Tanggal':<12} {'Status':<20}")
    print("-" * 80)
    
    for p in produk:
        status_bersih = p['status'].split(" - ")[0].strip()
        print(f"{p['id']:<5} {p['nama']:<25} {p['kategori']:<15} {p['waktu']:<12} {status_bersih:<20}")
    
    print("=" * 80)


def tampilkan_feedback(data):
    clear_screen()
    for f in data:
        print(f"ID       : {f['id_rating']}")
        print(f"Pembeli  : {f['nama_pembeli']}")
        print(f"Toko     : {f['nama_toko']}")
        print(f"Rating   : {f['nilai']}")
        print(f"Komentar : {f['komentar']}")
        print(f"Tanggal  : {f['tanggal']}")
        print(f"Balasan  : {f.get('balasan', 'Belum ada balasan')}")
        print("-" * 40)
