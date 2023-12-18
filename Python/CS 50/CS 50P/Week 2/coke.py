def main():
    accepted = [25, 10, 5]
    due = 50
    while due != 0:
        inserted = check_amount(accepted, due)
        due = insert_money(inserted, due)
    print("Change Owed:", due)
    return 0

def check_amount(accepted, due):
    while True:
        print("Amount due:", due)
        inserted = int(input("Insert Coin: "))
        if inserted in accepted: break
    return inserted

def insert_money(inserted, due):
    due = due - inserted
    return due

main()