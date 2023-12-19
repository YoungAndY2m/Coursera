def main():
    ask_amount()

def ask_amount():
    n = 50
    while n > 0:
        print("Amount Due:", n)
        num = input("Insert Coin: ")
        if int(num) not in [5, 10, 25]: continue
        n = n - int(num)
    print(f"Change Owed: {abs(n)}")

main()
