def main():
    msg = input("Input: ")
    remove_vowels(msg)

def remove_vowels(msg):
    vowels = ["a", "e", "i", "o", "u"]
    for letter in msg:
        if letter.lower() in vowels: continue
        print(letter, end="")

main()
