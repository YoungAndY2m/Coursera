import re, csv, random
import inflect
from model import Student

GENDER = ["male", "female"]
HOUSES = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "Unknown"]
DESCRIPTION = ["bravery", "loyalty", "intelligence", "ambition","unknown"]
BLOOD = ["muggle-born", "half-blood", "pure-blood"]
ROSTER = "roster.csv"
P = inflect.engine()

def main():
    """
    First part: receive the Hogwarts Acceptance Letter
    """
    # accept invitation
    new_student = accepting_invitation()
    """
    Second part: sorting hat
    """
    # sorting hat sort the house
    selected_house = sorting_hat(new_student)
    change_house(new_student, selected_house)
    # add the student to the roster
    write_coster(new_student, ROSTER)
    """
    Third part: sort roommates
    """
    roommates = sort_roommates(new_student)
    roommates_list(roommates, new_student)

"""
First part: receive the Hogwarts Acceptance Letter
Input student's information for future reference
"""
def accepting_invitation() -> Student:
    """
    Ask for student's name, gender, blood, and description
    Return the new_student
    """
    # narratives
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

"""
Second part: sorting hat
Based on the student's information, sort the houses
"""
def sorting_hat(student: Student) -> str:
    """
    Sorting hat picks a house for the student
    P.S. Like Harry Potter, the student can say no!
    Extra P.S. The student is automatically sorted to the last house left.
    """
    # narratives
    print("(OvO): Let's go to Hogwarts~~~")
    print("After the train......boat.....You are standing in front of the sorting hat")
    print(f"🎩: Hello, {student.name}! Let me see what's inside you...")
    # get preference from previous student information
    advice = preference(student)
    idx = 0
    while idx < len(advice):
        accept_or_not = input(f"Better be... {advice[idx]}! Do you accept it? (yes or no?)\n")
        yes_matches = re.search("^(yes|yeah|y).*", accept_or_not, re.IGNORECASE)
        if yes_matches: return advice[idx]
        else: 
            idx += 1
            continue
    print(f"I'm afraid you have to go to {advice[-1]} since no option left...")
    return advice[-1]

def preference(student: Student) -> list:
    """
    Provide sorting hat with house preferences 
    based on student's blood status and description
    """
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    preference = dict.fromkeys(houses, 0)
    match student.blood.lower():
        case "pure-blood": preference["Slytherin"] += 1
        case _: 
            preference["Gryffindor"] += 1
            preference["Hufflepuff"] += 1
            preference["Ravenclaw"] += 1
    match student.description.lower():
        case "bravery": preference["Gryffindor"] += 1
        case "loyalty": preference["Hufflepuff"] += 1
        case "intelligence": preference["Ravenclaw"] += 1
        case "ambition": preference["Slytherin"] += 1
    # sort the preference based on counting values
    preference_list = sorted([(value, key) for key, value in preference.items()], reverse=True)
    # return the sorted houses name for sorting hat to make the decision
    return [item[1] for item in preference_list]

def change_house(student: Student, house: str) -> None:
    student.house = house

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
Third part: sort roommates
Based on the student's gender, sort the roommates
"""
def sort_roommates(student: Student) -> list:
    """
    Roommates must have the same gender & house
    """
    students = []
    with open(ROSTER, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["house"] != student.house or row["gender"] != student.gender: continue
            else:
                students.append(Student(f"{row['first']} {row['last']}", row['gender'], row['blood'], row['description'], row['house']))
    return students

def roommates_list(students: list, current_student: Student) -> None:
    """
    Maximum number is 4
    """
    names = [student.name for student in students if student.name != current_student.name]
    if len(students) == 0:
        print("I'm afraid you won't have any roommates. Enjoy your single room!")
    elif len(students) < 4:
        output = P.join(names)
        print(f"Your roommates are going to be - {output}")
    else:
        random.shuffle(names)
        output = P.join(names[0:3])
        print(f"Your roommates are going to be - {output}")


if __name__ == "__main__":
    main()