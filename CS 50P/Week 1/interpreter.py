def interpret(expr):
    x, y, z = expr.split()
    print(x, y, z)
    if (y == '/') and (z == '0'):
        print("You cannot divide zero")
    elif y == '+':
        print(int(x) + int(z))
    elif y == '-':
        print(int(x) - int(z))
    elif y == '*':
        print(int(x) * int(z))
    elif y == '/':
        print(int(x) / int(z))


def main():
    expr = str(input("Expression: "))
    print(isinstance(expr, str))
    print(expr.split())
    # interpret(expr)
    return 0

main()