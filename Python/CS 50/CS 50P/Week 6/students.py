import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row) # still have white space problem in key & value
        students.append({"name": row["name"], "home":row["home"]})
    # for row in reader:
    #     students.append({"name":row[0], "home": row[1]})
    # for name, home in reader:
    #     students.append({"name": name, "home": home})

print(students)

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# def get_house(student):
#     return student["house"]

# sorted(key=func/lambda func)
# for student in sorted(students, key=get_house, reverse=True):
#     print(f"{student['name']} is in {student['house']}")
# for student in sorted(students, key=lambda student: student["name"], reverse=True):
#     print(f"{student['name']} is in {student['house']}")