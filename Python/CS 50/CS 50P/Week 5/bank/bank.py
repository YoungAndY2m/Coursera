def main():
    msg = input("Greeting: ")
    print(value(msg))

def value(greeting):
    output = 0
    match greeting.lower().strip():
        case greeting if greeting.startswith("hello"): output = 0
        case greeting if greeting[0] == "h": output = 20
        case _: output = 100
    return output

if __name__ == "__main__":
    main()
