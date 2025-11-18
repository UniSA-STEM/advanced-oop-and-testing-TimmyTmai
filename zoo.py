'''
File: zoo.py
Description: Defines the Zoo class used to manage staff, animals, enclosures and health records.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Integrity Policy.
'''

import uuid

import helper
from animal import Animal
from mammal import Mammal
from reptile import Reptile
from staff import Staff
from zookeeper import Zookeeper
from veterinarian import Veterinarian
from enclosure import Enclosure
from health_record import HealthRecord


class Zoo:
    """Central class that manages staff, animals, enclosures and health records."""

    def __init__(self, name: str):
        if not helper.validate_string(name, "Zoo name"):
            raise ValueError("Invalid zoo name.")
        self.__name = name.strip()

        # Main collections
        self.__staff: list[Staff] = []
        self.__animals: list[Animal] = []
        self.__enclosures: list[Enclosure] = []

    # Basic getters
    @property
    def name(self):
        return self.__name

    @property
    def staff(self) -> list[Staff]:
        return list(self.__staff)

    @property
    def animals(self) -> list[Animal]:
        return list(self.__animals)

    @property
    def enclosures(self) -> list[Enclosure]:
        return list(self.__enclosures)

    # Add / remove methods
    def add_staff(self, staff_member: Staff) -> None:
        """Add a staff member (must be a Zookeeper or Veterinarian)."""
        from zookeeper import Zookeeper
        from veterinarian import Veterinarian

        if not isinstance(staff_member, (Zookeeper, Veterinarian)):
            raise TypeError("staff_member must be a Zookeeper or Veterinarian instance.")

        if staff_member not in self.__staff:
            self.__staff.append(staff_member)
            print(f"Added staff member {staff_member.name} ({staff_member.role}) to {self.__name}.")

    def remove_staff(self, staff_member: Staff) -> None:
        """Remove a staff member from the zoo."""
        if staff_member not in self.__staff:
            raise ValueError("Staff member does not belong to this zoo.")
        # Deactivate first to clear their assignments
        staff_member.deactivate()
        self.__staff.remove(staff_member)

    def add_animal(self, animal) -> None:
        """Add an animal to the zoo."""
        if not isinstance(animal, Animal):
            raise TypeError("animal must be an Animal instance.")
        if animal not in self.__animals:
            self.__animals.append(animal)
            print(f"Added animal {animal.name} to {self.__name}.")

    def remove_animal(self, animal: Animal) -> None:
        """Remove an animal from the zoo and from all enclosures."""
        if animal not in self.__animals:
            raise ValueError("Animal does not belong to this zoo.")
        # Remove from all enclosures that currently contain it
        for enclosure in self.__enclosures:
            enclosure.remove_animal(animal)
        self.__animals.remove(animal)

    def add_enclosure(self, enclosure) -> None:
        """Add an enclosure to the zoo."""
        if not isinstance(enclosure, Enclosure):
            raise TypeError("enclosure must be an Enclosure instance.")
        if enclosure not in self.__enclosures:
            self.__enclosures.append(enclosure)
            print(f"Added enclosure {enclosure.environment} to {self.__name}.")

    def remove_enclosure(self, enclosure: Enclosure) -> None:
        """Remove an enclosure if it is empty."""
        if enclosure not in self.__enclosures:
            raise ValueError("Enclosure does not belong to this zoo.")
        if enclosure.animals:
            raise RuntimeError("Cannot remove enclosure that still contains animals.")

        self.__enclosures.remove(enclosure)


    # Search helpers
    def find_staff_by_name(self, name: str) -> Staff | None:
        """Return all staff whose name matches (case-insensitive)."""
        name = (name or "").strip().lower()
        for s in self.__staff:
            if s.name.lower() == name:
                return s
        return None

    def find_staff_by_id(self, staff_id: uuid.UUID) -> Staff | None:
        """Return a staff member by UUID, or None if not found."""
        for s in self.__staff:
            if s.id == staff_id:
                return s
        return None

    def find_animal_by_name(self, name: str) -> list[Animal]:
        """Return all animals whose name matches (case-insensitive)."""
        name = (name or "").strip().lower()
        return [a for a in self.__animals if a.name.lower() == name]

    def find_enclosure_by_environment(self, environment: str) -> list[Enclosure]:
        """Return all enclosures with the given environment type."""
        env = (environment or "").strip().lower()
        return [e for e in self.__enclosures if e.environment.lower() == env]


    # Health record access
    def get_health_records_for_animal(self, animal: Animal) -> list[HealthRecord]:
        """
        Collect all health records for a given animal across all veterinarians.
        """
        if animal not in self.__animals:
            raise ValueError("Animal does not belong to this zoo.")

        all_records: list[HealthRecord] = []
        for staff_member in self.__staff:
            if isinstance(staff_member, Veterinarian):
                records = staff_member.get_records(animal)
                all_records.extend(records)

        if all_records is None:
            print("No records found.")

        for record in all_records:
            print(record)

        return all_records

    def animal_under_treatment(self):
        under_treatment = []
        for animal in self.__animals:
            records = self.get_health_records_for_animal(animal)
            if any(r.active for r in records):
                under_treatment.append(animal)
                print(f"{animal.name} ({animal.species}) is under treatment.")

        if not under_treatment:
            print("No animal is under treatment.")

        return under_treatment

    def __str__(self):
        """Return a simple text summary of the zoo."""
        return (
            f"--- ZOO SUMMARY: {self.__name} ---\n"
            f"Number of staff: {len(self.__staff)}\n"
            f"Number of animals: {len(self.__animals)}\n"
            f"Number of enclosures: {len(self.__enclosures)}\n"
        )


zoo = Zoo("Sydney Wildlife Park")

# Staff
zk = Zookeeper("Alice")
vet = Veterinarian("Dr. Sarah")
zoo.add_staff(zk)
zoo.add_staff(vet)

# Animals
lion = Mammal("Simba", "Lion", 5, "Meat", "savannah", True)
snake = Reptile("Serpant","Snake", 5, "egg", "jungle", False )
zoo.add_animal(lion)
zoo.add_animal(snake)

# Enclosure
sav = Enclosure(300, "savannah")
jungle = Enclosure(300, "jungle")
zoo.add_enclosure(sav)
sav.add_animal(lion)
zoo.add_enclosure(jungle)
jungle.add_animal(snake)


print(zoo)

# Assign staff
zk.assign_enclosure(sav)
vet.assign_animal(lion)
vet.assign_animal(snake)
vet.perform_task("health check")
zoo.get_health_records_for_animal(snake)