def main():
    msg = input("Greeting: ")
    fine(msg)

def fine(msg):
    match msg.lower().strip():
        case msg if msg.startswith("hello"): print("$0")
        case msg if msg[0] == "h": print("$20")
        case _: print("$100")

main()
