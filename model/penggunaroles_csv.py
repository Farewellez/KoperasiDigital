from DB_Context import *
import pandas as pd

def to_csv_allPenggunaRolesDB():
    all_pengguna_roles = get_all_pengguna_rolesDB()
    all_pengguna_roles_df = pd.DataFrame(all_pengguna_roles)
    all_pengguna_roles_df.to_csv('allPengguna_roles.csv', mode='a', header=False, index=False)
    return all_pengguna_roles_df