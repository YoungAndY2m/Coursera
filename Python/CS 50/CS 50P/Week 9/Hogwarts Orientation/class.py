'''
Class Student
:properties: name, gender, blood, description, house
'''
class Student:
    def __init__(self, name, gender, blood="Unknown", description="Unknown", house="Unknown") -> None:
        self.name = name
        self.gender = gender
        self.blood = blood
        self.description = description
        self.house = house
    
    def __str__(self) -> str:
        identity = "wizard" if self.gender == "male" else "witch"
        pronoun = "he" if self.gender == "male" else "she"
        return f"{self.name} is a young, {self.blood.lower()} {identity}. {pronoun.capitalize()} belongs to {self.house}. Description: {self.description}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        
    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, gender):
        self._gender = gender.lower()
        
    @property
    def blood(self):
        return self._blood
    
    @blood.setter
    def blood(self, blood):
        self._blood = blood
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        if description not in ["Bravery", "Loyalty", "Intelligence", "Ambition", "Disrespect", "Unknown"]:
            raise ValueError("Invalid Description")
        self._description = description
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "Azkaban", "Unknown"]:
            raise ValueError("Invalid house")
        self._house = house

print(Student("Yang", "female", "Half-blood", "Bravery", "Gryffindor"))
    
    