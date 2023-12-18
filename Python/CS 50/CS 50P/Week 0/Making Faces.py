def main():
    msg = input("Hey, what's up!")
    print(face(msg))
    return 0

def face(msg):
    msg1 = msg.replace(":)", '')
    msg2 = msg1.replace(":(". '')
    return msg2

main()