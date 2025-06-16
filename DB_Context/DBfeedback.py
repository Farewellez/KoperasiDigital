import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .connection import create_connection

def get_all_feedbackDB():
    conn = create_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM feedback"
        cursor.execute(query)
        dataFeedback = cursor.fetchall()
        
        list_feedback = []
        for feedback in dataFeedback:
            feedback_dict = {
                'id_feedback': feedback[0],
                'id_produk': feedback[1],
                'id_pengguna': feedback[2],
                'id_toko': feedback[3],
                'rating': feedback[4],
                'tanggal_feedback': feedback[5],
                'isi_feedback' : feedback[6],
            }
            list_feedback.append(feedback_dict)
        return list_feedback
    
    except Exception as e:  
        conn.rollback()
        print(f"Terjadi kesalahan saat mengambil data pengguna: {e}")
        return []
    finally:
        cursor.close()
        conn.close()