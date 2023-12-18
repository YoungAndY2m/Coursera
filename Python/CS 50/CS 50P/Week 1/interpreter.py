def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    math_expr(x, y, z)

def math_expr(x, y, z):
    match y:
        case "+": print(float(x) + float(z))
        case "-": print(float(x) - float(z))
        case "*": print(float(x) * float(z))
        case "/": print(float(x) / float(z))

main()
