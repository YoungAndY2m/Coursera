import random
print(random.choice(["heads", "tails"]))
print(random.randint(1, 10))
cards = [1, 2, 3]
random.shuffle(cards)
print(cards)

# from random import choice
# print(choice(["heads", "tails"]))

import statistics
print(statistics.mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))