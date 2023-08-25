def main():
    msg = input("What are you saying? ")
    print(lowercase(msg))
    return 0

def lowercase(input):
    output = input.lower()
    return output

main()