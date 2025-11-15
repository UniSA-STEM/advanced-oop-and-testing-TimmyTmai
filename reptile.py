'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal

class Reptile(Animal):
    def __init__(self, name, species, age, diet, environment,is_healthy, is_venomous = True):
        super().__init__(name,species, age, diet, environment, is_healthy)
        self.__is_venomous = is_venomous

    def make_sound(self):
        return f"{self.name} hisses."

    @property
    def is_venomous(self):
        return self.__is_venomous

    def __str__(self):
        return super().__str__() + f"Is venomous: {self.__is_venomous}\n"