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
        "calories" : "60"},
        {"fruit" : "pear",
        "calories" : "100"},
        {"fruit" : "honeydew melon",
        "calories" : "50"},
        {"fruit" : "kiwifruit",
        "calories" : "90"},
        {"fruit" : "lemon",
        "calories" : "15"},
        {"fruit" : "lime",
        "calories" : "20"},
        {"fruit" : "sweet cherries",
        "calories" : "100"}
    ]

    ask_fruit = input("Item: ").lower().strip()
    for fruit in fruits:
        if ask_fruit == fruit["fruit"]:
            print("Calories: ", fruit["calories"])

main()
