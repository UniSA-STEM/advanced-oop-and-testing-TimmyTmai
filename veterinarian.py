'''
File: veterinarian.py
Description: Defines the Veterinarian class, a concrete Staff type.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Integrity Policy.
'''
from health_record import HealthRecord
from staff import Staff
from animal import Animal


class Veterinarian(Staff):
    """Veterinarian responsible for animal health, records, and treatment."""

    def __init__(self, name: str):
        """Create a veterinarian with the fixed role 'Veterinarian'."""
        super().__init__(name, "Veterinarian")
        # Map each animal to a list of its health records
        self.__records: dict[Animal, list[HealthRecord]] = {}

    def get_records(self, animal) -> list[HealthRecord]:
        """Return the list of health records for a given animal (create if absent)."""
        if not isinstance(animal, Animal):
            raise TypeError("'animal' must be an Animal class.")
        if animal not in self.__records:
            self.__records[animal] = []
        return self.__records[animal]

    def generate_record(self, animal: Animal) -> HealthRecord:
        """Interactively create a new health record for an assigned animal."""
        if animal not in self.assigned_animal:
            raise ValueError(f"{animal.name} is not assigned to {self.name}.")

        issue = input("Enter issue (injuries/illness/behavioral concerns): ").strip()
        severity = input("Enter severity (low/medium/high): ").strip()
        date = input("Enter date (dd/mm/yyyy): ").strip()
        notes = input("Enter treatment notes: ").strip()

        record = HealthRecord(
            animal=animal,
            issue=issue,
            severity=severity,
            date_reported=date,
            treatment_notes=notes,
            active=True,
        )
        self.get_records(animal).append(record)
        return record

    def health_check(self) -> None:
        """Go through all assigned animals and optionally create health records."""
        if not self.assigned_animal:
            print("No animals assigned for health check.")
            return

        for animal in self.assigned_animal:
            if animal.is_healthy:
                print(f"{animal.name} ({animal.species}) is healthy.")
            else:
                print(
                    f"{animal.name} ({animal.species}) is not healthy. "
                    "Do you want to create a record? (y/n)..."
                )
                choice = input().strip().lower()

                # Keep asking until user types y or n
                while choice not in ("y", "n"):
                    print("'choice' must be 'y' or 'n'.")
                    choice = input().strip().lower()

                if choice == "y":
                    self.generate_record(animal)
                # if 'n', simply continue to the next animal

    def record_report(self, animal: Animal | None = None) -> None:
        """
        Print health record reports.

        If no animal is given, prints reports for all assigned animals.
        """
        # Report for all assigned animals
        if animal is None:
            if not self.assigned_animal:
                print("No animals assigned to this veterinarian.")
                return

            for a in self.assigned_animal:
                print(f"\nAnimal: {a.name} ({a.species})")
                records = self.get_records(a)

                if not records:
                    print("  No health records found.")
                else:
                    for i, record in enumerate(records):
                        print(f"  Record [{i}]:")
                        for line in str(record).splitlines():
                            print("    " + line)
            return

        # Report for a specific animal
        if animal not in self.assigned_animal:
            raise ValueError(f"{animal.name} is not assigned to {self.name}.")

        records = self.get_records(animal)
        if not records:
            print("No health records found for this animal.\n")
            return

        for i, record in enumerate(records):
            print(f"\nRecord [{i}]:\n")
            print(record)

    def heal_animal(self, animal: Animal) -> None:
        """Heal a specific assigned animal and close any active records."""

        if animal not in self.assigned_animal:
            raise ValueError(f"{animal.name} is not assigned to {self.name}.")

        if animal.is_healthy:
            print(f"{animal.name} ({animal.species}) is healthy, no treatment needed.")
            return

        animal.heal()
        print(f"Performed treatment for {animal.name}.")

        records = self.get_records(animal)
        for record in records:
            if record.active:
                record.add_notes("Animal treated and condition resolved.")
                record.close_record()
                print(f"Record [{record.issue}] closed.")
        print(f"All active records for {animal.name} have been closed.")

    def perform_task(self, value: str) -> None:
        """Perform a task: 'health check', 'report', or 'heal'."""
        task = (value or "").strip().lower()
        if not task:
            raise ValueError("Please assign task.")
        if task not in ("health check", "report", "heal"):
            raise ValueError(
                f"Cannot perform task '{value}'. Options: 'health check', 'report', 'heal'."
            )

        if task == "health check":
            self.health_check()

        elif task == "report":
            self.record_report()

        elif task == "heal":
            # Filter assigned animals that are currently sick
            sick_animals = [a for a in self.assigned_animal if not a.is_healthy]
            if not sick_animals:
                print("All assigned animals are healthy. Nothing to heal.")
                return

            print("\n--- Sick Animals ---")
            for i, animal in enumerate(sick_animals, start=1):
                print(f"{i}. {animal.name} ({animal.species})")

            try:
                choice = int(input("Enter the number of the animal you want to heal: ").strip())
            except ValueError:
                print("Please enter a number.")
                return

            if choice < 1 or choice > len(sick_animals):
                print("Invalid number. Number is out of range.")
                return

            animal_to_heal = sick_animals[choice - 1]
            self.heal_animal(animal_to_heal)
