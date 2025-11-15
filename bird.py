'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal

class Bird(Animal):
    def __init__(self, name, species, age, diet, environment,is_healthy, can_fly = True):
        super().__init__(name,species, age, diet, environment, is_healthy)
        self.__can_fly = can_fly

    def make_sound(self):
        return f"{self.__name} chirps or sings"

    @property
    def can_fly(self):
        return self.__can_fly

    def __str__(self):
        return super().__str__()