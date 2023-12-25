import validators

def main():
    response = validators.email(input("What's your email address? "))
    if response:
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
