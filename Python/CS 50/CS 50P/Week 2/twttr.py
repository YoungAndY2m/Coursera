def main():
    vowels = ["a", "e", "i", "o", "u"]
    msg = input("Input: ")
    check_vowels(msg, vowels)
    return 0

# def check_vowels(msg, vowels):
#     print("Output: ", end="")
#     for letter in msg:
#         if letter.lower() in vowels: print("", end="")
#         else: print(letter, end="")
#     print()

def check_vowels(msg, vowels):
    print("Output: ", end="")
    output= [x if not x.lower()in vowels else "" for x in msg]
    for x in output:
        print(x, end="")
    print()

main()