from abc import ABC, abstractmethod

# creating an abstract class with get_gender method
class Person(ABC):
    @abstractmethod
    def get_gender(self):
        return 0


class Male(Person):
    def __init__(self,name):
        self.name = name
        self.gender = "Male"
        
    def get_gender(self):
        print(self.gender)
        
        
class Female(Person):
    def __init__(self,name):
        self.name = name
        self.gender = "Female"
        
    def get_gender(self):
        print(self.gender)
        
per1 = Male("Rony")      #object of Male class
per2 = Female("Julia")   #object of Female class

# Display gender of objects created
per1.get_gender()

per2.get_gender()