class Student:
    def __init__(self, name, house, patronus) -> None:
        self.name = name
        self.house = house # also call the setter method
        self.patronus = patronus

    def __str__(self) -> str:
        return f"{self.name} is in {self.house}, {self.patronus}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name: 
            raise ValueError("Missing name")
        self._name = name
    
    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "stag~"
            case "Otter":
                return "otter~"
            case "Jack Russell terrier":
                return "terrier~"
            case _:
                return "/"

def main():
    student = get_student()
    # print(f"{student.name} from {student.house}")
    print(student)
    try:
        print("Expecto Patronum!")
        print(student.charm())
    except AttributeError:
        print("No student exist!")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

        
if __name__ == "__main__":
    main()