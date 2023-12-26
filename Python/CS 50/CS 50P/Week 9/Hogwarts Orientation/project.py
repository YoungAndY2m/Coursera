import sys, re, csv

GENDER = ["male", "female"]
HOUSES = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "Azkaban", "Unknown"]
DESCRIPTION = ["Bravery", "Loyalty", "Intelligence", "Ambition", "Disrespect", "Unknown"]
BLOOD = ["muggle-born", "half-blood", "pure-blood"]

def main():
    ...


"""
First part: receive the Hogwarts Acceptance Letter
Input student's information for future reference
"""
def accepting_invitation():
    """
    Ask for student's name, gender, blood, and description
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
    
def ask_property(p):
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

"""
Third part: sort roommates
Based on the student's gender and/or personal choice, sort the roommates
"""


if __name__ == "__main__":
    main()