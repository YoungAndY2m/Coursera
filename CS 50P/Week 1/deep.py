def ask_question():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    match ans:
        case "42": print('Yes')
        case "forty-two": print('Yes')
        case "forty two": print('Yes')
        case _: print('No')

def main():
    ask_question()
    return 0

main()