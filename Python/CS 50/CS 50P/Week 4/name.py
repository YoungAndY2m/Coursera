import sys, random
while True:
    try:
        for arg in sys.argv[1:]:
            print("hello,", arg)
        break
    except (IndexError, ValueError):
        print("No input detected")
        sys.exit("exit here")

print(type(sys.argv))
print(type(random.choice))