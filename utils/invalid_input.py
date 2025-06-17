import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

def invalidAkun(): 
      input('''
              ++================================================++
              ||            ⚠️  INPUT TIDAK VALID ⚠️              ||
              ||                                                ||
              ||   AKUN SUDAH TERDAFTAR, SILAKAN GUNAKAN AKUN   ||
              ||                YANG LAIN ATAU LOGIN             ||
              ||                                                ||
              ||         Tekan enter untuk melanjutkan...       ||
              ++================================================++''')
      clearTerminal()
      loading_animation("memuat ulang")
      clearTerminal()

def invalidEmailAkun():
    input('''
          ++================================================++
          ||            ⚠️  INPUT TIDAK VALID ⚠️              ||
          ||                                                ||
          ||   EMAIL SUDAH TERDAFTAR, SILAKAN GUNAKAN EMAIL  ||
          ||                YANG LAIN ATAU LOGIN             ||
          ||                                                ||
          ||         Tekan enter untuk melanjutkan...       ||
          ++================================================++''')
    clearTerminal()
    loading_animation("memuat ulang")
    clearTerminal()

# invalid email or pw
def invalidEmailOrPw():
    input('''
          ++================================================++
          ||            ⚠️  INPUT TIDAK VALID ⚠️              ||
          ||                                                ||
          ||   EMAIL ATAU PASSWORD TIDAK SESUAI, SILAKAN    ||
          ||   PERIKSA KEMBALI ATAU KONTAK ADMIN            ||
          ||                                                ||
          ||         Tekan enter untuk melanjutkan...       ||
          ++================================================++''')