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

import helper
from enclosure import Enclosure

from animal import Animal
from enclosure import Enclosure
import helper

class Staff(ABC):
    def __init__(self, name: str, role: str):
        self._id = uuid.uuid4()
        self.__name = helper.validate_string(name, "Staff name")
        self.__role = role
        self.__active = True
        self._assigned_enclosure: list[Enclosure] = []
        self._assigned_animal: list[Animal] = []


    def assign_enclosure(self, enclosure):
        if not self.__active:
            raise RuntimeError("Cannot assign enclosure: staff member is inactive.")

        if not isinstance(enclosure, Enclosure):
            raise TypeError(f"{enclosure} must be an Enclosure instance.")

        if self.__role.lower().strip() != "zookeeper":
            raise PermissionError("Only staff with role 'zookeeper' can be assigned enclosures.")

        if enclosure not in self._assigned_enclosure:
            self._assigned_enclosure.append(enclosure)

    def assign_animal(self, animal):
        if not self.__active:
            raise RuntimeError("Cannot assign animal: staff member is inactive.")

        if not isinstance(animal, Animal):
            raise TypeError(f"{animal} must be an Animal instance.")

        if self.__role.lower().strip() != "veterinarian":
            raise PermissionError("Only staff with role 'veterinarian' can be assigned animals.")

        if animal not in self._assigned_animal:
            self._assigned_animal.append(animal)

    def deactivate(self) -> None:
        self.__active = False
        self._assigned_enclosure.clear()
        self._assigned_animal.clear()

    @abstractmethod
    def perform_task(self, task):
        pass

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

    def display_enclosure(self):
        for enc in self.assigned_enclosure:
            print(enc.environment)

    def display_animal(self):
        for animal in self.assigned_animal:
            print(animal.name)

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

