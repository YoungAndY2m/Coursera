students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)

"""
List comprehension & Lambda functions
Filter (similar to map)
"""

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

# gryffindors = filter(is_gryffindor, students)
gryffindors = filter(lambda s:s["house"] == "Gryffindor", students)
for gryffindor in sorted(gryffindors, key=lambda s:s["name"]):
    print(gryffindor["name"])


"""
Dictionary Comprehension
"""
new_students = ["Hermione", "Harry", "Ron"]
gryffindors = [{"name":student, "house":"Gryffindor"} for student in new_students]
gryffindor_name = {student:"Gryffindor" for student in new_students}

print(gryffindor_name)

"""
enumerate
"""
for i, student in enumerate(new_students):
    print(i+1, student)
