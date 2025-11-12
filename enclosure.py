'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal

class Enclosure:
    def __init__(self, size: int, environment: str):
        self.__size = size
        self.__environment = environment
        self.__clean_level = 5
        self.__list_animal: list[Animal] = []
        self.__enclosure_species: str | None = None
        self.__capacity = max(1, size // 100) #1 animal per 100 area units

    # ---- Getters----
    @property
    def species(self) -> str | None:
        return self.__enclosure_species

    @property
    def animals(self) -> list[Animal]:
        return list(self.__list_animal)  # copy to protect internals

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
        same_species = (self.__enclosure_species == animal.species() or self.__enclosure_species is None)
        same_environment = animal.environment().lower() == self.__environment.lower()
        return same_species and same_environment

    # ---- Core API ----
    def add_animal(self, animal) -> bool:
        """
        Returns True if added, False if rejected due to species/capacity.
        Raises TypeError if 'animal' isn't an Animal.
        """
        if not isinstance(animal, Animal):
            raise TypeError("'animal' must be an Animal class.")

        if self._is_full():
            print("Enclosure already full")
            return False

        if self.is_compatible(animal):
            self.__list_animal += [animal]
            return True
        else:
            print("Enclosure not compatible")
            return False


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

