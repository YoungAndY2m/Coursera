# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(students[i])

# for i in range(len(students)):
#     print(i + 1, students[i])

# # Dictionary things
# students = {
#     "Hermione" : "Gryffindor", 
#     "Harry" : "Gryffindor", 
#     "Ron" : "Gryffindor", 
#     "Draco" : "Slytherin"
#     }
# # print(students["Hermione"])
# for student in students:
#     print(student)

# dictionary things with more categories
# List stores different dictionaries
students = [
    {"name" : "Hermione", 
    "house" : "Gryffindor", 
    "patronus" : "Gryffindor"},
    {"name" : "Harry", 
    "house" : "Gryffindor", 
    "patronus" : "Stag"},
    {"name" : "Ron", 
    "house" : "Gryffindor", 
    "patronus" : "Jack Russell terrier"},
    {"name" : "Draco", 
    "house" : "Slytherin", 
    "patronus" : None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=', ')
