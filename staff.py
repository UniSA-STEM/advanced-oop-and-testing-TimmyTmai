'''
File: staff.py
Description: Defines the abstract Staff class used in the zoo management system.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod
import uuid

from animal import Animal
from enclosure import Enclosure
import helper


class Staff(ABC):
    """Abstract base class for staff members in the zoo."""

    def __init__(self, name: str, role: str):
        """Create a staff member with a name, role, and default active status."""
        self._id = uuid.uuid4()

        # Validate name and role before assigning them
        if helper.validate_string(name, "Staff name") and helper.validate_string(role, "Staff role"):
            self.__name = name.strip()
            self.__role = role.strip()
        else:
            raise ValueError("Invalid staff name or role provided.")

        # Staff start as active by default
        self.__active = True

        # Lists used to track what this staff member is responsible for
        self._assigned_enclosure: list[Enclosure] = []
        self._assigned_animal: list[Animal] = []

    def assign_enclosure(self, enclosure) -> None:
        """
        Assign an enclosure to this staff member.

        Only active staff with role 'zookeeper' are allowed to take enclosures.
        """
        if not self.__active:
            raise RuntimeError("Cannot assign enclosure: staff member is inactive.")

        if not isinstance(enclosure, Enclosure):
            raise TypeError("Assigned enclosure must be an Enclosure instance.")

        # Only zookeepers can be assigned to enclosures
        if self.__role.lower() != "zookeeper":
            raise PermissionError("Only staff with role 'zookeeper' can be assigned enclosures.")

        if enclosure not in self._assigned_enclosure:
            self._assigned_enclosure.append(enclosure)

    def assign_animal(self, animal) -> None:
        """
        Assign an animal to this staff member.

        Only active staff with role 'veterinarian' are allowed to take animals.
        """
        if not self.__active:
            raise RuntimeError("Cannot assign animal: staff member is inactive.")

        if not isinstance(animal, Animal):
            raise TypeError("Assigned animal must be an Animal instance.")

        # Only veterinarians can be assigned animals
        if self.__role.lower() != "veterinarian":
            raise PermissionError("Only staff with role 'veterinarian' can be assigned animals.")

        if animal not in self._assigned_animal:
            self._assigned_animal.append(animal)

    def deactivate(self) -> None:
        """
        Deactivate this staff member.

        Clears any current assignments so they are no longer responsible
        for animals or enclosures.
        """
        self.__active = False
        self._assigned_enclosure.clear()
        self._assigned_animal.clear()

    @abstractmethod
    def perform_task(self, task: str):
        """
        Each concrete staff type must define what 'perform_task' means.

        For example: Zookeeper might 'clean enclosure', Veterinarian might
        'check health record'.
        """
        pass

    # Properties

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
        # Return a copy so the caller cannot modify the internal list directly
        return list(self._assigned_enclosure)

    @property
    def assigned_animal(self):
        # Same idea: protect internal list from external modification
        return list(self._assigned_animal)

    # Helper display methods

    def display_enclosure(self) -> None:
        """Print environments of all enclosures assigned to this staff member."""
        for enc in self.assigned_enclosure:
            print(enc.environment)

    def display_animal(self) -> None:
        """Print names of all animals assigned to this staff member."""
        for animal in self.assigned_animal:
            print(animal.name)

    def __str__(self) -> str:
        """Readable summary of the staff member and their assignments."""
        active = "Active" if self.__active else "Inactive"
        return (
            f"--- STAFF INFORMATION ---\n"
            f"{self.__role} {self.__name} (ID: {self._id})\n"
            f"Assigned Enclosures: {[e.environment for e in self._assigned_enclosure]}\n"
            f"Assigned Animals: {[a.name for a in self._assigned_animal]}\n"
            f"Status: {active}\n\n"
        )
