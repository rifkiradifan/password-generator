import string
import secrets

def main():
    print(secrets.choice(string.ascii_lowercase))
    
if __name__ == "__main__":
    main()
