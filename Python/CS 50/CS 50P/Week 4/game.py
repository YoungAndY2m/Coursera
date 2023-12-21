import random, sys

# Reprompt if not an int or less than 1
while True:
    try:
        # prompt for a level
        num = input("Level: ")
        guess = random.randint(1, int(num))
        break
    except ValueError:
        pass

# Prompt the user to guess the number
while True:
    try:
        user_guess = input("Guess: ")
        user_int = int(user_guess)
    except ValueError:
        pass
    else:
        if user_int < guess: print("Too small!")
        elif user_int > guess: print("Too large!")
        else:
            print("Just right!")
            sys.exit()
