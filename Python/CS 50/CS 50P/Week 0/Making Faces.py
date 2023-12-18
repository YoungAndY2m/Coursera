def main():
    msg = input()
    result = convert(msg)
    print(result)

def convert(msg):
    msg = msg.replace(":)", "🙂")
    msg = msg.replace(":(", "🙁")
    return msg

main()
