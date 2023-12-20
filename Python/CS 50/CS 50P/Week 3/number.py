def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("NOT interger")
#     else:
#         break
# print(f"x is {x}")
# else:
#     print(f"x is {x}")


# while True:
#     try:
#         x = int(input("What's x? "))
#         break
#     except ValueError:
#         print("NOT interger")
# print(f"x is {x}")


# while True:
#     try:
#         return int(input("What's x? "))
#     except ValueError:
#         print("NOT interger")

#     except ValueError:
#         pass