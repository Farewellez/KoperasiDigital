import psycopg2

def connect_db():
    return psycopg2.connect(
        host="localhost",
        database="tokoku",
        user="postgres",
        password="123"
    )

def tambah_produk():
    nama = input("Nama produk: ")
    harga = int(input("Harga produk: "))
    stok = int(input("Stok: "))
    deskripsi = input("Deskripsi: ")

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO produk (nama, harga, stok, deskripsi) VALUES (%s, %s, %s, %s)",
                (nama, harga, stok, deskripsi))
    conn.commit()
    cur.close()
    conn.close()
    print("Produk berhasil ditambahkan.\n")

def lihat_produk():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM produk")
    rows = cur.fetchall()
    print("\n Daftar Produk:")
    for row in rows:
        print(f"ID: {row[0]} | Nama: {row[1]} | Harga: {row[2]} | Stok: {row[3]} | Deskripsi: {row[4]}")
    cur.close()
    conn.close()

def update_produk():
    lihat_produk()
    id_produk = int(input("\nMasukkan ID produk yang ingin diupdate: "))
    nama = input("Nama baru: ")
    harga = int(input("Harga baru: "))
    stok = int(input("Stok baru: "))
    deskripsi = input("Deskripsi baru: ")

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        UPDATE produk 
        SET nama = %s, harga = %s, stok = %s, deskripsi = %s 
        WHERE id = %s
    """, (nama, harga, stok, deskripsi, id_produk))
    conn.commit()
    cur.close()
    conn.close()
    print(" Produk berhasil diupdate.\n")

def hapus_produk():
    lihat_produk()
    id_produk = int(input("\nMasukkan ID produk yang ingin dihapus: "))
    konfirmasi = input("Yakin ingin menghapus produk ini? (y/n): ")
    if konfirmasi.lower() == "y":
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM produk WHERE id = %s", (id_produk,))
        conn.commit()
        cur.close()
        conn.close()
        print(" Produk berhasil dihapus.\n")
    else:
        print(" Penghapusan dibatalkan.\n")

def konfirmasi_pesanan():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT pesanan.id, produk.nama, pesanan.nama_pembeli, pesanan.status
        FROM pesanan 
        JOIN produk ON pesanan.produk_id = produk.id
    """)
    rows = cur.fetchall()
    print("\n Daftar Pesanan:")
    for row in rows:
        print(f"ID Pesanan: {row[0]} | Produk: {row[1]} | Pembeli: {row[2]} | Status: {row[3]}")

    id_pesanan = int(input("\nMasukkan ID pesanan yang ingin dikonfirmasi: "))
    cur.execute("UPDATE pesanan SET status = 'dikonfirmasi' WHERE id = %s", (id_pesanan,))
    conn.commit()
    cur.close()
    conn.close()
    print("Pesanan telah berhasil dikonfirmasi.\n")

def apply_kurir_terdekat():
    kota_penjual = input("Masukkan kota penjual: ")
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, nama, kota, jarak_km FROM kurir
        WHERE kota = %s
        ORDER BY jarak_km ASC
        LIMIT 1
    """, (kota_penjual,))
    kurir = cur.fetchone()
    if kurir:
        print(f"Kurir terdekat: ID: {kurir[0]} | Nama: {kurir[1]} | Kota: {kurir[2]} | Jarak: {kurir[3]} km")
    else:
        print("Tidak ditemukan kurir di kota yang dimaksud.")
    cur.close()
    conn.close()

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
""")
        pilihan = input("Pilih menu (1-7): ")

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
        else:
            print(" Pilihan tidak valid.\n")

if __name__ == "__main__":
    menu_penjual()
