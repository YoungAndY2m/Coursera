def main():
    get_list()


def get_list():
    grocery = dict()
    while True:
        try:
            item = input()
            count = grocery.get(item.upper(), 0) + 1
            grocery[item.upper()] = count
        except EOFError:
            print()
            items = list(grocery.keys())
            items.sort()
            for item in items:
                print(grocery[item], item)
            break

main()
