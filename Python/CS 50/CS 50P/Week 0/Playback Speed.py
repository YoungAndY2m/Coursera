def main():
    msg = input("What are you saying? ")
    print(playback(msg))
    return 0

def playback(msg):
    words = msg.split(' ')
    output = '...'.join(words)
    return output

main()