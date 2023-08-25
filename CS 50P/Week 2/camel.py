def main():
    while True:
        msg = input("camelCase: ")
        if len(msg) != 0: break
    snake_case(msg)
    return 0

def snake_case(msg):
    print("snake_case: ", end="")
    for letter in msg:
        if letter.islower(): print(letter, end="")
        else: print("_" + letter.lower(), end="")
    print()

main()