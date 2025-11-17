'''
File: zookeeper.py
Description: Defines the Zookeeper class, a concrete Staff type.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff


class Zookeeper(Staff):
    """Zookeeper responsible for cleaning and feeding enclosures."""

    def __init__(self, name):
        super().__init__(name, "Zookeeper")

    def perform_task(self, value):
        """Perform a task such as 'clean' or 'feed'."""
        task = (value or "").strip().lower()

        if not task:
            raise ValueError("Please assign task.")

        if task not in ("clean", "feed"):
            raise ValueError(f"Cannot perform task '{value}'.")

        # Edge case: no enclosures assigned
        if not self.assigned_enclosure:
            raise RuntimeError("No enclosures assigned to this zookeeper.")

        if task == "clean":
            for enc in self.assigned_enclosure:
                enc.clean_enclosure()
                print(f"Cleaned {enc.environment} enclosure.")
            return

        if task == "feed":
            for enc in self.assigned_enclosure:
                for animal in enc.animals:
                    print(f"Feeding {animal.name}...")
                enc.decrease_cleanliness()
            print("Fed all assigned enclosures.")
