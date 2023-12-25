import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    output = ""
    matches = re.findall(r"(\d{1,2}):?(\d{2})? (AM|PM)", s)
    if matches:
        for time in matches:
            time_list = list(time)
            length = len(time_list)
            if length == 3:
                if int(time_list[0]) > 11 or int(time_list[1]) > 59: raise ValueError

            elif length == 2:

        return output
    else:
        return False

def am_pm(time):
    if time[-1] == "AM":
        return f"{}"

if __name__ == "__main__":
    main()
