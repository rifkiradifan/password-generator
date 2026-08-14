import string
import secrets
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=int, default=12)
    args = parser.parse_args()
    
    print("".join(secrets.choice(string.ascii_lowercase) for _ in range(args.length)))
    
if __name__ == "__main__":
    main()
