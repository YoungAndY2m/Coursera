import sys

def main():
    file = check_file()
    print(line_count(file))

def check_file():
    if len(sys.argv) == 1: sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2: sys.exit("Too many command-line arguments")
    else:
        file_name = sys.argv[1]
        if file_name.find(".py") == -1: sys.exit("Not a Python file")
        return file_name

def line_count(file):
    count = 0
    try:
        with open(file, 'r') as fh:
            for line in fh:
                line = line.strip()
                if line.startswith("#") or len(line) == 0: continue
                count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    return count

if __name__ == "__main__":
    main()
