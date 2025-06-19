import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_tidak_kosong(prompt):
    while True:
        data = input(prompt).strip()
        if data:
            return data
        print("Input tidak boleh kosong. Silakan coba lagi.")

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

def daftar_menjadi_kurir():
    clear_screen()

    konfirmasi = input_konfirmasi("Apakah Anda ingin mendaftar sebagai kurir? (y/n): ")

    if konfirmasi == 'y':
        clear_screen()
        print("====== Silakan isi data pendaftaran sebagai Kurir ======\n")
        nama = input_tidak_kosong("Nama Lengkap: ")
        alamat = input_tidak_kosong("Alamat: ")
        nomor_hp = input_nomor_hp("Nomor HP: ")
        wilayah = input_tidak_kosong("Wilayah Operasi: ")
        input("\nSilakan tunggu konfirmasi dari admin. Tekan enter untuk lanjut... ")
        clear_screen()
    else:
        input("\nPendaftaran dibatalkan. Tekan enter untuk lanjut...")
        clear_screen()

if __name__ == "__main__":
    daftar_menjadi_kurir()
