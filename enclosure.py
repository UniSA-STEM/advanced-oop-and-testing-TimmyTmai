'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal
import helper
from mammal import Mammal
from reptile import Reptile


class Enclosure:
    def __init__(self, size: int, environment: str):
        if not isinstance(size, int) or size <= 0:
            raise ValueError("size must be a positive integer.")

        self.__environment = helper.validate_environment(environment)
        self.__size = size
        self.__clean_level = 5
        self.__list_animal = []
        self.__enclosure_species = None
        self.__capacity = max(1, size // 100)

    # ---- Getters----
    @property
    def species(self) -> str | None:
        return self.__enclosure_species

    @property
    def animals(self) -> list[Animal]:
        return list(self.__list_animal)

    @property
    def clean_level(self) -> int:
        return self.__clean_level

    @property
    def environment(self) -> str:
        return self.__environment.lower()

    # ---- Helpers ----
    def _is_full(self) -> bool:
        return len(self.__list_animal) >= self.__capacity

    def is_compatible(self, animal: Animal) -> bool:
        same_environment = animal.environment.lower() == self.__environment.lower()
        same_species = (
                self.__enclosure_species is None
                or animal.species.lower() == self.__enclosure_species.lower()
        )
        return same_environment and same_species

    # ---- Core API ----
    def add_animal(self, animal) -> bool:
        """
        Returns True if added, False if rejected due to species/capacity.
        Raises TypeError if 'animal' isn't an Animal.
        """
        if not isinstance(animal, Animal):
            raise TypeError(f"{animal} must be an Animal class.")

        if self._is_full():
            print("Enclosure already full")
            return False

        if not self.is_compatible(animal):
            print("Enclosure not compatible (species or environment mismatch).")
            return False

        if self.__enclosure_species is None:
            self.__enclosure_species = animal.species

        self.__list_animal.append(animal)
        print(f"Added {animal.name} to the enclosure.")
        return True

    def remove_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("'animal' must be an Animal class.")
        if animal in self.__list_animal:
            self.__list_animal.remove(animal)
            if not self.__list_animal:
                self.__enclosure_species = None
            return True
        return False

    def clean_enclosure(self):
        self.__clean_level = 5
        print("Enclosure cleaned.")

    def animal_names(self) -> list[str]:
        return [a.name for a in self.__list_animal]

    def report_status(self) -> str:
        return (
            f"Clean level: {self.__clean_level}\n"
            f"List animal: {self.animal_names()}\n"
            f"Number of animals: {len(self.__list_animal)}\n"
            f"Capacity: {self.__capacity}\n"
        )

    def __str__(self):
        return (
            f"Enclosure type: {self.__environment}\n"
            f"Size: {self.__size}\n"
            f"Capacity: {self.__capacity}\n"
            f"Enclosure species: {self.__enclosure_species}\n"
            f"Clean level: {self.__clean_level}\n"
            f"List animal: {self.animal_names()}\n"
            f"Number of animals: {len(self.__list_animal)}\n"
        )
