import inflect

# use mylist = p.join((words)) -> "word, word, and word" or "word and word"
p = inflect.engine()
names = []
# First: get all the names
while True:
    try:
        msg = input("Name: ")
        if len(msg) == 0: break
        names.append(msg)
    except EOFError:
        print()
        break
print("Adieu, adieu, to", p.join(names))
