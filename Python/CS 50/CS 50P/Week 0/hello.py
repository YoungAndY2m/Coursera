''' 
    8/17 CS 50P
'''

def main():
    # Ask user for their name
    name = input("what's you name?\n").strip()

    # Say hello to the user
    print("okay,", name, sep=" fine ", end="\n\n")
    print("hello, " + name)
    print("Nice to meet you, ", end="")
    print(name.capitalize(), "\n")
    print(name.title())
    print(f"hello, {name}")
    hello()
    hello(name)

    # num = 78
    # print(f"Is num even? {True if num%2==0 else False}")

def hello(name="world"):
    print("hello,", name)

main()


