class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

class Student(Wizard):
    def __init__(self, name, house) -> None:
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject) -> None:
        super().__init__(name)
        self.subject = subject
    
    def __str__(self) -> str:
        output = super().__str__()
        return output + f" - {self.subject}"

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")

print(Professor("someone", "somejob"))
print(professor)