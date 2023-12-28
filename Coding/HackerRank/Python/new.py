# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():
    N, M = map(int, input().split())
    half_rows = []
    num_half = N // 2
    for i in range(1, N // 2 + 1):
        num_line = 2 * i - 1
        num_dot = num_line * 2
        num_hy = M - num_line - num_dot

        output = "-"*int(num_hy/2) + ".|"
        if num_line != 1: 
            output += "..|"*(num_line-1)
        output += "." + "-"*int(num_hy/2)
        
        half_rows.append(output)
    
    for row in half_rows:
        print(row)
    print("-"*int(((M-7)/2)), end="")
    print("WELCOME", end="")
    print("-"*int(((M-7)/2)))
    half_rows.reverse()
    for row in half_rows:
        print(row)


if __name__ == "__main__":
    main()
