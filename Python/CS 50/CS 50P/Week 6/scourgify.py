import csv, sys

def main():
    input, output = check_input()
    clean_format(input, output)

def check_input():
    length = len(sys.argv)
    if length < 3: sys.exit("Too few command-line arguments")
    elif length > 3: sys.exit("Too many command-line arguments")
    else:
        input_file_name = sys.argv[1]
        output_file_name = sys.argv[2]
        if input_file_name.find(".csv") == -1 or output_file_name.find(".csv") == -1: sys.exit("Not a CSV file")
        return input_file_name, output_file_name

def clean_format(input, output):
    names, houses = [], []
    try:
        with open(input, 'r') as file:
            reader = csv.DictReader(file)
            for line in reader:
                names.append(line["name"])
                houses.append(line["house"])
        with open(output, 'w') as csvfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            for idx, name in enumerate(names):
                last, first = name.split(",")
                writer.writerow({'first':first.strip(), 'last': last.strip(), 'house': houses[idx]})

    except FileNotFoundError: sys.exist(f"Could not read {input}")

if __name__ == "__main__":
    main()
