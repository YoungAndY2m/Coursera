import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r"^<iframe .*src=\"(https?://(?:www\.)?youtube\.com/embed/\w+)\".*</iframe>$", s)
    if matches:
        link = re.sub(r"^https?://(www\.)?youtube\.com/embed/", "https://youtu.be/", matches.group(1))
        return link
    else:
        return "None"

if __name__ == "__main__":
    main()
