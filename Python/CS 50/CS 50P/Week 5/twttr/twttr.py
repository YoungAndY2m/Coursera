def main():
    msg = input("Input: ")
    print(shorten(msg))

def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    output = ""
    for letter in word:
        if letter.lower() in vowels: continue
        output += letter
    return output

if __name__ == "__main__":
    main()
