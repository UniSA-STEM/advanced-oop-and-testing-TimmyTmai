'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name,species, age, diet):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet

    def eat(self):
        return f"{self.__name} is eating {self.__diet}."

    def sleep(self):
        return f"{self.__name} curls up and sleeps."

    @abstractmethod
    def make_sound(self):
        pass

