'''
File: enclosure.py
Description: Defines the Enclosure class for housing animals in the zoo.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
import helper


class Enclosure:
    """Represents an animal enclosure with a specific environment and capacity."""

    def __init__(self, size: int, environment: str):
        """Create an enclosure with a given size and environment."""
        if not isinstance(size, int) or size <= 0:
            raise ValueError("size must be a positive integer.")

        # Validate and normalise environment (e.g., 'aquatic', 'savannah')
        self.__environment = helper.validate_environment(environment)
        self.__size = size

        # Clean level ranges from 0 to 5 (start fully clean)
        self.__clean_level = 5

        # Animals currently in this enclosure
        self.__list_animal: list[Animal] = []

        # Species restriction: once the first animal is added, only that species allowed
        self.__enclosure_species: str | None = None

        # Capacity based on size (e.g., 100 sqm = 1 animal, 300 sqm = 3)
        self.__capacity = max(1, size // 100)

    #property
    @property
    def species(self) -> str | None:
        return self.__enclosure_species

    @property
    def animals(self) -> list[Animal]:
        # Return a copy to protect the internal list
        return list(self.__list_animal)

    @property
    def clean_level(self) -> int:
        return self.__clean_level

    @property
    def environment(self) -> str:
        return self.__environment.lower()

    # helpers
    def _is_full(self) -> bool:
        """Internal check if enclosure has reached its capacity."""
        return len(self.__list_animal) >= self.__capacity

    def is_compatible(self, animal: Animal) -> bool:
        """
        Check if an animal can be housed here based on environment and species.
        """
        same_environment = animal.environment.lower() == self.__environment.lower()
        same_species = (
            self.__enclosure_species is None
            or animal.species.lower() == self.__enclosure_species.lower()
        )
        return same_environment and same_species

    # ---- Core API ----
    def add_animal(self, animal) -> bool:
        """
        Try to add an animal to the enclosure.

        Returns:
            True if added successfully, False if rejected due to
            capacity or compatibility. Raises TypeError for wrong type.
        """
        if not isinstance(animal, Animal):
            raise TypeError(f"{animal} must be an Animal class.")

        if self._is_full():
            print("Enclosure already full.")
            return False

        if not self.is_compatible(animal):
            print("Enclosure not compatible (species or environment mismatch).")
            return False

        # First animal determines the species allowed in this enclosure
        if self.__enclosure_species is None:
            self.__enclosure_species = animal.species

        self.__list_animal.append(animal)
        print(f"Added {animal.name} to the enclosure.")
        return True

    def remove_animal(self, animal):
        """Remove an animal if present. Return True if removed, False otherwise."""
        if not isinstance(animal, Animal):
            raise TypeError("'animal' must be an Animal class.")

        if animal in self.__list_animal:
            self.__list_animal.remove(animal)

            # If enclosure becomes empty, clear species restriction
            if not self.__list_animal:
                self.__enclosure_species = None
            return True

        return False

    def clean_enclosure(self):
        """Restore the enclosure to maximum cleanliness."""
        self.__clean_level = 5
        print("Enclosure cleaned.")

    def decrease_cleanliness(self):
        """
        Reduce cleanliness by one step.

        If cleanliness drops to 2 or below, all animals become unhealthy.
        """
        self.__clean_level -= 1
        print("Enclosure getting dirty.")

        if self.__clean_level <= 2:
            for animal in self.__list_animal:
                animal.is_healthy = False
                print(f"{animal.name} has become sick due to dirty enclosure.")

    def animal_names(self) -> list[str]:
        """Return a list of names of all animals in this enclosure."""
        return [a.name for a in self.__list_animal]

    def report_status(self) -> str:
        """Return a short text report about this enclosure."""
        return (
            f"Clean level: {self.__clean_level}\n"
            f"List animal: {self.animal_names()}\n"
            f"Number of animals: {len(self.__list_animal)}\n"
            f"Capacity: {self.__capacity}\n"
        )

    def __str__(self):
        """Formatted string representation of this enclosure."""
        return (
            f"--- ENCLOSURE INFORMATION ---\n"
            f"Enclosure type: {self.__environment}\n"
            f"Size: {self.__size}\n"
            f"Capacity: {self.__capacity}\n"
            f"Enclosure species: {self.__enclosure_species}\n"
            f"Clean level: {self.__clean_level}\n"
            f"List animal: {self.animal_names()}\n"
            f"Number of animals: {len(self.__list_animal)}\n"
        )
