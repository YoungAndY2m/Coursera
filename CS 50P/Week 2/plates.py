import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6: return False
    elif s[0].isalpha() == False or s[1].isalpha() == False: return False
    elif not_number_require(s): return False
    elif have_marks(s): return False
    else: return True

def not_number_require(s):
    idx = []
    slist = list(s)
    print(slist.index("0"))
    for i in range(len(s)):
        if s[i].isdigit(): idx.append(i)
    if s[idx[0]] == '0': return True
    if not s[idx[0]:].isdigit(): return True


def have_marks(s):
    for letter in s:
        if letter in ['.', ' ', '?', '!']:
            return True
    return False

main()