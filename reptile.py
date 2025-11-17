'''
File: reptile.py
Description: Defines the Reptile subclass of Animal.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal


class Reptile(Animal):
    """Represents a reptile in the zoo system."""

    def __init__(self, name, species, age, diet, environment, is_healthy, is_venomous=True):
        """Create a Reptile with an optional venomous trait."""
        # Initialise shared animal attributes
        super().__init__(name, species, age, diet, environment, is_healthy)

        # Reptile-specific trait
        self.__is_venomous = is_venomous

    def make_sound(self):
        """Return the typical sound associated with reptiles."""
        return f"{self.name} hisses."

    @property
    def is_venomous(self):
        return self.__is_venomous

    def __str__(self):
        """Extend base animal details with venom status."""
        return super().__str__() + f"Is venomous: {self.__is_venomous}\n"
