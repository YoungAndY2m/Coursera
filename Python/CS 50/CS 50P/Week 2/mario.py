def main():
    # print_column(3)
    # print_row(4)
    print_square(3)
    print()
    print_square_compact(3)


def print_column(height):
    # for _ in range(height):
    #     print("#")
    print("#\n" * height, end="")

def print_row(width):
    print("#" * width)

def print_square(size):
    # for each row in square
    for row in range(size):
        # for each brick in row
        for column in range(size):
            # print brick
            print("#", end="")
        # Every time finish a line, print a new line
        print()

def print_square_compact(size):
    for i in range(size):
        print("#" * size)

main()