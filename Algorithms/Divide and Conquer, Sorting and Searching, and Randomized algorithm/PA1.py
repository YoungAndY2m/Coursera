def karatsuba(x, y):
    # Base case: If the numbers are small, use standard multiplication
    if x < 10 or y < 10:
        return x * y

    # Calculate the number of digits in the input numbers
    num_digits = max(len(str(x)), len(str(y)))
    m = num_digits // 2

    # Split the numbers into two halves
    a = x // 10**m
    b = x % 10**m
    c = y // 10**m
    d = y % 10**m

    # Recursive calls for sub-problems
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    # Combine the results
    result = ac * 10**(2*m) + ad_bc * 10**m + bd

    return result

# Example usage
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
result = karatsuba(x, y)
print("Result:", result)
