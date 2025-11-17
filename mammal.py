'''
File: mammal.py
Description: Defines the Mammal subclass of Animal.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal


class Mammal(Animal):
    """Represents a mammal in the zoo system."""

    def __init__(self, name, species, age, diet, environment, is_healthy, is_nocturnal=False):
        """Create a Mammal with an optional nocturnal trait."""
        # Initialise all shared animal attributes
        super().__init__(name, species, age, diet, environment, is_healthy)

        # Mammal-specific attribute
        self.__is_nocturnal = is_nocturnal

    def make_sound(self):
        """Return a generic mammal sound."""
        return f"{self.name} makes a mammal-like sound."

    @property
    def is_nocturnal(self):
        return self.__is_nocturnal

    def __str__(self):
        """Extend base string representation with mammal details."""
        return super().__str__() + f"Is nocturnal: {self.__is_nocturnal}\n"
