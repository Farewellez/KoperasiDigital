import psycopg2 # Library python yang digunkan untuk koneksi ke database PostgreSQL
from dotenv import load_dotenv # Library python yang digunakan untuk memuat file .env
import os # Library python yang digunakan untuk mengakses variabel lingkungan

# Memuat file .env untuk mendapatkan variabel lingkungan
load_dotenv()

# Mendapatkan variabel lingkungan dari file .env
DB_HOST = os.getenv('PGHOST')
DB_PORT = os.getenv('PGPORT')
DB_NAME = os.getenv('PGDATABASE')
DB_USER = os.getenv('PGUSER')
DB_PASSWORD = os.getenv('PGPASSWORD')  

# Membuat koneksi ke database PostgreSQL
def create_connection():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        # print("Koneksi ke database berhasil!")
        return connection
    except Exception as e:
        print(f"Terjadi kesalahan saat menghubungkan ke database: {e}")
        return None