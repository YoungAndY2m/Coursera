class Student:
    def __init__(self, name, house) -> None:
        self.name = name
        self.house = house
    
    def __str__(self) -> str:
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    print(Student.get())

if __name__ == "__main__":
    main()