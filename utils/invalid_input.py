from .clear_terminal import clearTerminal
from .loading import loading_animation

def invalidInput():
    input('''
          ++================================================++
          ||            ⚠️  INPUT TIDAK VALID ⚠️              ||
          ||                                                ||
          ||    Silakan masukkan input yang sesuai dengan   ||
          ||            pilihan yang tersedia               ||
          ||                                                ||
          ||  Tekan enter untuk melanjutkan...              ||
          ++================================================++''')
    clearTerminal()
    loading_animation("memuat ulang")
    clearTerminal()

def invalidName():
    input('''
          ++================================================++
          ||            ⚠️  INPUT TIDAK VALID ⚠️              ||
          ||                                                ||
          ||   NAMA HANYA BOLEH MENGANDUNG HURUF DAN SPASI  ||
          ||   MINIMAL 9 KARAKTER (TANPA ANGKA ATAU TANDA)  ||
          ||                                                ||
          ||         Tekan enter untuk melanjutkan...       ||
          ++================================================++''')
    clearTerminal()
    loading_animation("memuat ulang")
    clearTerminal()

def invalidPW():
    input('''
          ++================================================++
          ||            ⚠️  INPUT TIDAK VALID ⚠️              ||
          ||                                                ||
          ||       PASSWORD MINIMAL BERISI 8 KARAKTER       ||
          ||                                                ||
          ||         Tekan enter untuk melanjutkan...       ||
          ++================================================++''')
    clearTerminal()
    loading_animation("memuat ulang")
    clearTerminal()

def invalidEmail():
    input('''
          ++================================================++
          ||            ⚠️  INPUT TIDAK VALID ⚠️              ||
          ||                                                ||
          ||          PASTIKAN FORMAT EMAIL SESUAI          ||
          ||                                                ||
          ||            CONTOH: elliot@gmail.com            ||  
          ||         Tekan enter untuk melanjutkan...       ||
          ++================================================++''')
    clearTerminal()
    loading_animation("memuat ulang")
    clearTerminal()

def invalidTelepon():
    input('''
          ++================================================++
          ||            ⚠️  INPUT TIDAK VALID ⚠️              ||
          ||                                                ||
          ||   NOMOR TELEPON HANYA BOLEH MENGANDUNG ANGKA   ||
          ||    MINIMAL 12 DIGIT (TANPA SPASI ATAU TANDA)   ||
          ||                                                ||
          ||         Tekan enter untuk melanjutkan...       ||
          ++================================================++''')
    clearTerminal()
    loading_animation("memuat ulang")
    clearTerminal()