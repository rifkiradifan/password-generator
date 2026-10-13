import secrets  # sumber acak yang aman dari os
import string   # kumpulan karakter 
import argparse  # untuk parsing argumen baris perintah

def main() -> None:
    # 1. buat parser argumen
    parser = argparse.ArgumentParser(description="Generate secure random password.")
    # 2. daftarkan flag --length
    parser.add_argument("--length", type=int, default=16, help="Length of the password")
    # 3. baca flag dari command line
    args = parser.parse_args()
    
    
    charset =  string.ascii_lowercase
    password = "" # mulai dengan string kosong
    
    
    for _ in range(args.length):
        password += secrets.choice(charset) # tambahkan 1 karakter acak ke password

    print(password)
    
    
if __name__ == "__main__":
    main()