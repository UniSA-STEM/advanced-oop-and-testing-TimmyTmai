'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from abc import ABC, abstractmethod
import uuid

class Animal(ABC):
    def __init__(self, name,species, age, diet):
        self._id = uuid.uuid4()
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

    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self.__name
    @property
    def species(self):
        return self.__species
    @property
    def age(self):
        return self.__age
    @property
    def diet(self):
        return self.__diet

