import sys, re, csv
from model import Student

GENDER = ["male", "female"]
HOUSES = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "Azkaban", "Unknown"]
DESCRIPTION = ["bravery", "loyalty", "intelligence", "ambition", "disrespect", "unknown"]
BLOOD = ["muggle-born", "half-blood", "pure-blood"]
ROSTER = "roster.csv"

def main():
    """
    First part: receive the Hogwarts Acceptance Letter
    """
    # accept invitation
    new_student = accepting_invitation()
    # add the student to the roster
    write_coster(new_student, ROSTER)


"""
First part: receive the Hogwarts Acceptance Letter
Input student's information for future reference
"""
def accepting_invitation() -> Student:
    """
    Ask for student's name, gender, blood, and description
    Return the new_student
    """
    print("An owl just landed and tapped on your window.")
    # ask for name
    name = ask_property("name")
    # ask for gender
    gender = ask_property("gender") 
    # ask for blood
    blood = ask_property("blood")
    # ask for description
    description = ask_property("description")

    return Student(name, gender, blood, description)
    
    
def ask_property(p: str) -> str:
    """
    Ask for student's name, gender, blood, and description
    accepting_invitation()'s sub-function
    """
    while True:
        match p:
            case "name":
                name = input("(OvO): Hi~ What's your name?\n")
                if not name: continue
                else: return name.strip()
            case "gender":
                gender = input("(OvO): Great! What's your gender? [male, female, or rather not say?]\n")
                if gender.lower().strip() not in GENDER: return "unknown"
                else: return gender.lower().strip()
            case "blood":
                blood = input("(OvO): How about your blood status? [pure-blood, half-blood, or muggle-born?]\n")
                if blood.lower().strip() not in BLOOD: continue
                else: return blood.lower().strip()
            case "description":
                description = input("(OvO): Final question, how would you describe yourself? [Bravery, Loyalty, Intelligence, or Ambition?]\n")
                if description.lower().strip() not in DESCRIPTION: continue
                else: return description.lower().strip()

def write_coster(student: Student, file_path: str) -> None:
    """
    Add the student information to roster.csv
    """
    # separate first and last name
    name = student.name
    try:
        first, last = name.split(" ")
    except ValueError:
        first, last = name, "Unknown"
    gender = student.gender
    blood = student.blood
    description = student.description
    house = student.house
    with open(file_path, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=["first","last","house","gender","blood","description"])
        writer.writerow({"first":first.capitalize(), "last":last.capitalize(), "house":house, "gender":gender, "blood":blood, "description":description})

def read_last_line(file_path):
    """
    Return the last line of the file (for csv testing & return new_student)
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if lines:
            return lines[-1].strip()
        else:
            return None

"""
Second part: sorting hat
Based on the student's information, sort the houses
"""


"""
Third part: sort roommates
Based on the student's gender and/or personal choice, sort the roommates
"""


if __name__ == "__main__":
    main()