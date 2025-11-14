'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.a
'''
from animal import Animal

class Mammal(Animal):
    def __init__(self, name, species, age, diet, environment, is_healthy, is_nocturnal = False):
        super().__init__(name,species, age, diet, environment, is_healthy)
        self.__is_nocturnal = is_nocturnal

    def make_sound(self):
        return f"{self.__name} makes a mammal-like sound."

    @property
    def is_nocturnal(self):
        return self.__is_nocturnal

    def __str__(self):
        return super().__str__()

leo = Mammal("Leo", "Lion", 20, "meat", "Safari", True, False)
print(leo)