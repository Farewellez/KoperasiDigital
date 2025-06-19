import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_tidak_kosong(prompt):
    while True:
        data = input(prompt).strip()
        if data:
            return data
        print("Input tidak boleh kosong. Silakan coba lagi.")

def input_nik(prompt):
    while True:
        nik = input(prompt).strip()
        try:
            if len(nik) == 16 and int(nik):
                return nik
            else:
                print("NIK harus 16 digit. Silakan coba lagi.")
        except ValueError:
            print("NIK harus berupa angka. Silakan coba lagi.")

def input_nomor_hp(prompt):
    while True:
        no_hp = input(prompt).strip()
        try:
            if 12 <= len(no_hp) <= 13 and int(no_hp):
                return no_hp
            else:
                print("Nomor HP harus 12 sampai 13 digit angka. Silakan coba lagi.")
        except ValueError:
            print("Nomor HP harus berupa angka. Silakan coba lagi.")

def input_konfirmasi(prompt):
    while True:
        jawab = input(prompt).strip().lower()
        if jawab in ['y', 'n']:
            return jawab
        input("\nInput tidak valid. Tekan enter untuk coba lagi...")
        clear_screen()

def daftar_menjadi_penjual():
    clear_screen()

    konfirmasi = input_konfirmasi("Apakah kamu yakin ingin mendaftar sebagai Penjual? (y/n): ")

    if konfirmasi == 'y':
        clear_screen()
        print("====== Silakan isi data pendaftaran sebagai Penjual ======\n")
        nama = input_tidak_kosong("Nama Lengkap: ")
        nik = input_nik("NIK (Nomor Induk Kependudukan): ")
        nama_toko = input_tidak_kosong("Nama Toko: ")
        alamat_toko = input_tidak_kosong("Alamat Toko: ")
        no_hp = input_nomor_hp("No. HP yang bisa dihubungi: ")
        input("\nSilakan tunggu konfirmasi dari admin. Tekan enter untuk lanjut... ")
        clear_screen()

    else:
        input("\nPendaftaran dibatalkan. Tekan enter untuk lanjut...")
        clear_screen()

if __name__ == "__main__":
    daftar_menjadi_penjual()
