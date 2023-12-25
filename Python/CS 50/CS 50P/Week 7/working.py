import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(\d{1,2})(:\d{2})? (AM|PM) to (\d{1,2})(:\d{2})? (AM|PM)$", s)
    if matches:
        hr1, min1, am_pm1, hr2, min2, am_pm2 = matches.groups()
        min1 = min1 or ":00"
        min2 = min2 or ":00"
        if int(hr1) > 12 or int(hr2) > 12 or int(min1[1:]) > 59 or int(min2[1:]) > 59:
            raise ValueError
        if am_pm1 == 'PM' and hr1 != '12':
            hr1 = str(int(hr1) + 12)
        elif am_pm1 == 'AM' and hr1 == '12':
            hr1 = '00'
        if am_pm2 == 'PM' and hr2 != '12':
            hr2 = str(int(hr2) + 12)
        elif am_pm2 == 'AM' and hr2 == '12':
            hr2 = '00'

        return f"{int(hr1):02}{min1} to {int(hr2):02}{min2}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
