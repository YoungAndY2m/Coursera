'''
Class Student
:properties: name, gender, blood, description, house
'''
class Student:
    def __init__(self, name: str, gender: str, blood: str ="Unknown", description: str ="Unknown", house: str ="Unknown") -> None:
        self.name = name
        self.gender = gender
        self.blood = blood
        self.description = description
        self.house = house
    
    def __str__(self) -> str:
        identity = "witch" if self.gender == "female" else "wizard"
        pronoun = "she" if self.gender == "female" else "he"
        return f"{self.name.title()} is a young, {self.blood.lower()} {identity}. {pronoun.capitalize()} belongs to {self.house}. Description: {self.description.capitalize()}"
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name) -> None:
        self._name = name
        
    @property
    def gender(self) -> str:
        return self._gender
    
    @gender.setter
    def gender(self, gender) -> None:
        self._gender = gender.lower()
        
    @property
    def blood(self) -> str:
        return self._blood
    
    @blood.setter
    def blood(self, blood) -> None:
        self._blood = blood
    
    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, description) -> None:
        self._description = description
    
    @property
    def house(self) -> str:
        return self._house
    
    @house.setter
    def house(self, house) -> None:
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "Azkaban", "Unknown"]:
            raise ValueError("Invalid house")
        self._house = house

# print(Student("Yang", "female", "Half-blood", "Bravery", "Gryffindor"))
    
    