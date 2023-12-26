# class Cat:
#     MEOWS = 3

#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")

# cat = Cat()
# cat.meow()

# def meow(n: int) -> str:
#     """
#     Meow n times.

#     :param n: Number of times to meow
#     :type n: int
#     :raise TypeError: If n is not an int
#     :return: A string of n meows, one per line
#     :rtype: str
#     """
#     return "meow\n" * n

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-n", help="number of times to meow")
parser.add_argument("-a", help="some explanation")
args = parser.parse_args()

if args.n:
    print(args.n)
    for _ in range(int(args.n)):
        print("meow")
if args.a:
    print(args.a)