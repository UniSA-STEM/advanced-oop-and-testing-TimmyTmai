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
from enclosure import Enclosure

from animal import Animal
from enclosure import Enclosure


class Staff(ABC):
    def __init__(self, name, role):
       self._id = uuid.uuid4()
       self.__name = name
       self.__role = role
       self.__active = True
       self._assigned_enclosure = []
       self._assigned_animal = []


    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self.__name
    @property
    def role(self):
        return self.__role
    @property
    def assigned_enclosure(self):
        return list(self._assigned_enclosure)
    @property
    def assigned_animal(self):
        return list(self._assigned_animal)

    def assign_enclosure(self, enclosure: Enclosure):
        if enclosure not in self._assigned_enclosure and self.__active == True:
            self._assigned_enclosure.append(enclosure)


    def assign_animal(self, animal: Animal):
        if animal not in self._assigned_animal and self.__active == True:
            self._assigned_animal.append(animal)

    def deactivate(self):
        self.__active = False
        for e in self._assigned_enclosure:
            self._assigned_enclosure.remove(e)
        for a in self._assigned_animal:
            self._assigned_animal.remove(a)

    ''''@abstractmethod
    def perform_task(self):
        pass'''

    def __str__(self):
        if self.__active:
            active = "Active"
        else:
            active = "Inactive"
        return (
            f"{self.__role} {self.__name} (ID: {self._id})\n"
            f"Assigned Enclosures: {[e.environment for e in self._assigned_enclosure]}\n"
            f"Assigned Animals: {[a.name for a in self._assigned_animal]}\n"
            f"Status: {active}\n\n"
        )

