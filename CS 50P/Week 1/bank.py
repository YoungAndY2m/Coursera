def hello_detection(msg):
    match msg:
        case "Hello" | "hello":
            print("$0")
        case msg if (msg[0] == 'H') | (msg[0] == 'h'):
            print("$20")
        case _:
            print("$100")

def main():
    msg = input("Greeting: ")
    hello_detection(msg)
    return 0

main()