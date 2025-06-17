# from authentikasi import CheckAkun, CheckRole
from authentikasi.auth import alreadyAdd,verifRole
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


# function main awal dari segalanya 😈
def main():
    username = str(input("input username anda:\n"))
    password = str(input("input password anda:\n"))
    
    # dummy role
    # if CheckAkun(username) == True:
    #     print("akun sudah terdaftar")
    #     CheckRole()
    if alreadyAdd(username) == True:
        print("akun sudah terdaftar")
        verifRole()
            
    else:
        print("akun belum terdaftar")
        verifRole()



# idiom untuk fungsi main
if __name__ == "__main__":
    main()