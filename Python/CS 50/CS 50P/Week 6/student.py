import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
    writer2 = csv.DictWriter(file, fieldnames=["name", "home"])
    writer2.writerow({"name": name * 2, "home": home * 2})