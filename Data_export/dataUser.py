import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from database import get_all_userDB 

def to_csv_allUser():
    all_user = get_all_userDB()
    all_user_df = pd.DataFrame(all_user)
    all_user_df.to_csv('allPengguna.csv', mode='a', header=False, index=False)
    return all_user_df