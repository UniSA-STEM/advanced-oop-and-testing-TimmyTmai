'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff

class Zookeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "Zookeeper")

    def perform_task(self, value):
        task = (value or "").strip().lower()
        if not task:
            raise ValueError("Please assign task.")
        if task not in ("clean", "feed"):
            raise ValueError(f"Cannot perform task '{value}'.")

        if task == "clean":
            for enc in self.assigned_enclosure:
                enc.clean_enclosure()
                print(f"Cleaned {enc.environment} enclosures.")
                return

        if value == "feed":
            for enc in self.assigned_enclosure:
                for animal in enc.animals:  # read-only copy
                    print(f"feeding {animal.name}...")
                enc.decrease_cleanliness()
            print("Feed all enclosures.")

