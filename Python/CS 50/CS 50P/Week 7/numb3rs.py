import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    if matches:
        for i in range(1, 5):
            try:
                num = int(matches.group(i))
                if num > 255: return False
            except ValueError:
                return False
        return True
    else:
        print("here")
        return False


if __name__ == "__main__":
    main()
