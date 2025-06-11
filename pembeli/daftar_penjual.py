import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def daftar_menjadi_penjual():
    clear_screen()
    print("=== Daftar Menjadi Penjual ===")
    konfirmasi = input("Apakah kamu yakin ingin mendaftar sebagai Penjual? (y/n): ").lower()

    if konfirmasi == 'y':
        print("\nSilakan isi data pendaftaran sebagai Penjual.")
        nama = input("Nama Lengkap: ")
        nik = input("NIK (Nomor Induk Kependudukan): ")
        nama_toko = input("Nama Toko: ")
        alamat_toko = input("Alamat Toko: ")
        no_hp = input("No. HP yang bisa dihubungi: ")

        # Simulasi penyimpanan ke database
        # Misal kita kirim data ini ke modul penyimpanan
        print("\nMendaftarkan sebagai Penjual...")
        print("Data telah disimpan. Anda sekarang terdaftar sebagai Penjual.")

        # Simulasi redirect ke fitur penjual
        input("\nTekan Enter untuk masuk ke fitur Penjual...")
        clear_screen()
        print(">> Fitur Penjual belum diimplementasikan pada bagian ini.")
    
    else:
        print("\nPendaftaran dibatalkan. Kembali ke menu utama.")
        input("Tekan Enter untuk melanjutkan...")

