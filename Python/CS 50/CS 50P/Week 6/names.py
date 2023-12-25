name = input("What's your name? ")

# file = open("names.txt", 'a')
# file.write(name)
# file.close()

# automatically write the file and close it
# with open("names.txt", 'a') as file:
#     file.write(f"{name}\n")

with open("names.txt", 'r') as file:
    lines = file.readlines()
    for line in sorted(set(lines)):
        print("hello", line, end="")