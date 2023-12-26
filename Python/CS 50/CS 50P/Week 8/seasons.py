from datetime import date
import re, inflect, sys


def main():
    # inflect engine
    p = inflect.engine()

    # get user input
    format = input("Date of Birth: ")

    # calculate the difference in days
    birth = date.fromisoformat(input_date(format))
    current = date.today()
    difference = current - birth
    num_days = difference.days

    # calculate the difference in minutes
    num_mins = calculate_mins(num_days)

    # output the result using inflect p.number_to_words method
    output = p.number_to_words(num_mins, andword="") + " minutes"
    print(output.capitalize())


def input_date(format):
    matches = re.search(r"^\d{4}-\d{2}-\d{2}$", format)
    if matches:
        return matches.group()
    else:
        sys.exit("Invalid date")


def calculate_mins(days):
    return days * 1440


if __name__ == "__main__":
    main()
