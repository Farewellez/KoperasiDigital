from DB_Context import *
import pandas as pd

def to_csv_allRoles():
    all_role = get_all_roleDB()
    all_role_df = pd.DataFrame(all_role)
    all_role_df.to_csv('all_role.csv', mode='a', header=False, index=False)
    return all_role