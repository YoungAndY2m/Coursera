def main():
    yell("This", "is", "CS50")
    cs = ["This", "is", "CS50"]
    print(*[word.upper() for word in cs])

def yell(*words):
    uppercase = map(str.upper, words)
    print(*uppercase)


if __name__ == "__main__":
    main()