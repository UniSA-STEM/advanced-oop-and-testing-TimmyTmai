'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from enclosure import Enclosure
from reptile import Reptile
from staff import Staff
from abc import ABC, abstractmethod

class Zookeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "Zookeeper")

    def perform_task(self, value):
        tasks = ["clean", "feed"]
        value = value.lower().strip()
        if not value:
            raise ValueError(f"Please assign task.")
        if value.lower() not in tasks:
            raise ValueError(f"Cannot perform task {value}.")

        for value in tasks:
            if value == "clean":
                for enclosure in self._assigned_enclosure:
                    enclosure.clean_enclosure()
                print("Cleaned all enclosures.")

            if value == "feed":
                for animal in self._assigned_animal:
                    animal.eat()
                print("Fed all animals.")

tom = Zookeeper("Tom")

enclosure1 = Enclosure(500,"Aquatic")
tom.assign_enclosure(enclosure1)
alligator = Reptile("Mr.A","Alligator",20, "meat", "Aquatic")
tom.assign_enclosure(enclosure1)
enclosure1.add_animal(alligator)
tom.perform_task("feed")