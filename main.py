import secrets  # sumber acak yang aman dari os
import string   # kumpulan karakter 

def main() -> None:
    charset =  string.ascii_lowercase
    length = 16
    password = "" # mulai dengan string kosong
    
    for _ in range(length):
        password += secrets.choice(charset) # tambahkan 1 karakter acak ke password

    print(password)
    
    
if __name__ == "__main__":
    main()