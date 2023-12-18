def karatsuba(x, y):
    # base case
    if x < 10 or y < 10:
        return x * y
    
    # Calculate the number of digits in the input numbers
    num_digits = max(len(str(x)), len(str(y)))
    n = num_digits // 2

    # get a, b, c, d
    a = x // 10**n
    b = x % 10**n
    c = y // 10**n
    d = y % 10**n

    # Recursively compute ac
    ac = karatsuba(a, c)
    # Recursively compute bd
    bd = karatsuba(b, d)
    # Recursively compute (a+b)(c+d) = ac+bd+ad+bc
    add = karatsuba(a + b, c + d) - ac - bd

    return ac * 10**(n*2) + add * 10**n + bd


print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))