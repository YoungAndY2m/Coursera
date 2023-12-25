import csv, sys
from tabulate import tabulate

def main():
    csv_name = check_input()
    headers, pizza = grid_format(csv_name)
    print(headers)
    print(pizza)
    print(tabulate(pizza, headers, tablefmt="grid"))

def check_input():
    length = len(sys.argv)
    if length < 2: sys.exit("Too few command-line arguments")
    elif length > 2: sys.exit("Too many command-line arguments")
    else:
        file_name = sys.argv[1]
        if file_name.find(".csv") == -1: sys.exit("Not a CSV file")
        return file_name

# Usage of enumerated for row_number and nested expression
def grid_format(csv_name):
    pizza = list()
    keys = list()
    try:
        with open(csv_name, 'r') as file:
            reader = csv.reader(file)
            for row_number, line in enumerate(reader):
                if row_number == 0:
                    keys = line
                else:
                    pizza.append(line)
                    # pizza.append({keys[i]:value for i, value in enumerate(line)})

        # print(pizza)
        return keys, pizza
    except FileNotFoundError: sys.exist("File does not exist")

if __name__ == "__main__":
    main()
