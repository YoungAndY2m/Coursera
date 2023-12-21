import random


def main():
    level = get_level()
    score = generate_integer(level)
    print("Score:", score)



# Prompt user for a level
def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            choose_level = input("Level: ")
            if int(choose_level) in levels: return int(choose_level)
        except ValueError: pass

# Prompt user to solve 10 math problems
def generate_integer(level):
    multiplication = [0, 10, 100, 9, 99, 999]
    count = 0
    for i in range(10):
        x = random.randint(multiplication[level-1], multiplication[level+2])
        y = random.randint(multiplication[level-1], multiplication[level+2])
        ans = x + y
        # check for error up to three times
        error = 0
        while error != 3:
            result = input(f"{x} + {y} = ")
            try:
                if int(result) == ans:
                    count += 1
                    break
            except ValueError: pass
            print("EEE")
            error += 1
        if error == 3: print(f"{x} + {y} = {ans}")
    return count

if __name__ == "__main__":
    main()
