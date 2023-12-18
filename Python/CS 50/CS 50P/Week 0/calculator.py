# x = int(input("What's x?"))
# y = int(input("What's y?"))
# z = x + y
# print(z)

# print(f"{2/3:.2f}")
# print(round(2/3, 2))

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
    print(x ** 2)
    print(pow(x, 2))

def square(n):
    ans = n * n
    return ans

main()