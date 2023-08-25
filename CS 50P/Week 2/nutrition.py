def main():
    fruits = [
        {"fruit" : "apple",
        "calories" : "130"},
        {"fruit" : "avocado",
        "calories" : "50"},
        {"fruit" : "banana",
        "calories" : "110"},
        {"fruit" : "cantaloupe",
        "calories" : "50"},
        {"fruit" : "grapefruit",
        "calories" : "60"}
    ]
    while True:
        msg = input("Item: ")
        for fruit in fruits:
            if msg == fruit["fruit"]:
                print(fruit["calories"]) 
                break

main()
