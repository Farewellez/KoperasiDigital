import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host = os.getenv("DB_HOST"),
            database = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            port = os.getenv('DB_PORT', 5432)
        )
        print("Koneksi ke database berhasil!")
        return conn
    except psycopg2.OperationalError as e:
        print(f"error saat koneksi ke database{e}")
        return None
    
# def connect():
#     print("connection di panggil...")
#     conn = get_db_connection()

#     if conn:
#         print("koneksi berhasil")
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM pengguna")
#         row = cur.fetchall()
#         print("Isi dari tabel saat ini adalah", len(row))
#         cur.close()
#         conn.close()