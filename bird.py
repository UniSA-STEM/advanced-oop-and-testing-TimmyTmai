'''
File: bird.py
Description: Defines the Bird subclass of Animal.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal


class Bird(Animal):
    """Represents a bird in the zoo system."""

    def __init__(self, name, species, age, diet, environment, is_healthy, can_fly=True):
        """Create a Bird with an optional flying ability."""
        # Initialise shared animal attributes
        super().__init__(name, species, age, diet, environment, is_healthy)

        # Bird-specific trait
        self.__can_fly = can_fly

    def make_sound(self):
        """Return a generic bird sound."""
        return f"{self.name} chirps or sings."

    @property
    def can_fly(self):
        return self.__can_fly

    def __str__(self):
        """Extend base animal output with flying ability."""
        return super().__str__() + f"Can fly: {self.__can_fly}\n"
