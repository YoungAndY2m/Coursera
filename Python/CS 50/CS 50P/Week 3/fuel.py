def main():
    fuel = round(prompt(), 2) * 100
    if fuel <=1 : print("E")
    elif fuel >=99 : print("F")
    else: print(int(fuel), "%", sep="")

def prompt():
    while True:
        try:
            msg = input("Fraction: ")
            x, y = msg.split("/")
            if int(x) > int(y):
                continue
            return int(x)/int(y)
        except (ValueError, ZeroDivisionError):
            pass


main()
