import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    flag = True
    # start with at least two letters
    if len(s) < 2 or not s[0:2].isalpha(): flag = False
    # maximum of 6 characters and a minimum of 2 characters
    if len(s) > 6: flag = False
    # numbers must come at end, first number cannot be a zero
    s_list = list(s)
    idx = []
    for i in range(len(s)):
        if s_list[i].isdigit(): idx.append(i)
    if len(idx) > 0:
        if s[idx[0]] == "0": flag = False
        if not s[idx[0]:].isdigit(): return False
    # No periods, spaces, or punctuation marks
    for letter in s:
        if letter.isspace() or letter == "." or letter in string.punctuation: flag = False
    return flag


if __name__ == "__main__":
    main()
