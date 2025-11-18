'''
File: test_staff.py
Description: Unit tests for the Staff abstract base class.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest

from staff import Staff
from enclosure import Enclosure
from mammal import Mammal


class DummyZookeeper(Staff):
    """Concrete Staff used for testing zookeeper behaviour."""

    def __init__(self, name: str):
        super().__init__(name, "zookeeper")

    def perform_task(self, task: str):
        pass


class DummyVeterinarian(Staff):
    """Concrete Staff used for testing veterinarian behaviour."""

    def __init__(self, name: str):
        super().__init__(name, "veterinarian")

    def perform_task(self, task: str):
        pass


def make_enclosure():
    return Enclosure(size=200, environment="savannah")


def make_lion(name="Simba"):
    return Mammal(name, "Lion", 5, "Meat", "savannah", True)

# Constructor validation

def test_staff_valid_creation():
    zk = DummyZookeeper(" Alice ")
    assert zk.name == "Alice"
    assert zk.role == "zookeeper"
    assert zk.id is not None


def test_staff_invalid_name_raises():
    with pytest.raises(ValueError):
        DummyZookeeper("   ")  # invalid staff name


def test_staff_invalid_role_raises():
    # Use a one-off subclass specifying an invalid role
    class BadRoleStaff(Staff):
        def __init__(self):
            super().__init__("Bob", "   ")  # invalid role

        def perform_task(self, task: str):
            pass

    with pytest.raises(ValueError):
        BadRoleStaff()

# assign_enclosure

def test_zookeeper_assign_enclosure_success():
    zk = DummyZookeeper("Alice")
    enc = make_enclosure()

    zk.assign_enclosure(enc)

    assert enc in zk.assigned_enclosure
    # internal list should contain exactly one enclosure
    assert len(zk.assigned_enclosure) == 1


def test_assign_enclosure_wrong_type_raises():
    zk = DummyZookeeper("Alice")

    with pytest.raises(TypeError):
        zk.assign_enclosure("not an enclosure")


def test_veterinarian_cannot_be_assigned_enclosure():
    vet = DummyVeterinarian("Dr. Bob")
    enc = make_enclosure()

    with pytest.raises(PermissionError):
        vet.assign_enclosure(enc)


def test_inactive_staff_cannot_be_assigned_enclosure():
    zk = DummyZookeeper("Alice")
    enc = make_enclosure()

    zk.deactivate()

    with pytest.raises(RuntimeError):
        zk.assign_enclosure(enc)


# assign_animal

def test_veterinarian_assign_animal_success():
    vet = DummyVeterinarian("Dr. Bob")
    lion = make_lion()

    vet.assign_animal(lion)

    assert lion in vet.assigned_animal
    assert len(vet.assigned_animal) == 1


def test_assign_animal_wrong_type_raises():
    vet = DummyVeterinarian("Dr. Bob")

    with pytest.raises(TypeError):
        vet.assign_animal("not an animal")


def test_zookeeper_cannot_be_assigned_animal():
    zk = DummyZookeeper("Alice")
    lion = make_lion()

    with pytest.raises(PermissionError):
        zk.assign_animal(lion)


def test_inactive_staff_cannot_be_assigned_animal():
    vet = DummyVeterinarian("Dr. Bob")
    lion = make_lion()

    vet.deactivate()

    with pytest.raises(RuntimeError):
        vet.assign_animal(lion)


# Deactivate behaviour

def test_deactivate_clears_assignments():
    zk = DummyZookeeper("Alice")
    vet = DummyVeterinarian("Dr. Bob")
    enc = make_enclosure()
    lion = make_lion()

    zk.assign_enclosure(enc)
    vet.assign_animal(lion)

    assert len(zk.assigned_enclosure) == 1
    assert len(vet.assigned_animal) == 1

    zk.deactivate()
    vet.deactivate()

    assert zk.assigned_enclosure == []
    assert vet.assigned_animal == []


# Defensive copies from properties

def test_assigned_enclosure_returns_copy():
    zk = DummyZookeeper("Alice")
    enc = make_enclosure()
    zk.assign_enclosure(enc)

    enclosures = zk.assigned_enclosure
    enclosures.clear()   # modify the copy

    # Internal list should remain unchanged
    assert len(zk.assigned_enclosure) == 1


def test_assigned_animal_returns_copy():
    vet = DummyVeterinarian("Dr. Bob")
    lion = make_lion()
    vet.assign_animal(lion)

    animals = vet.assigned_animal
    animals.clear()   # modify the copy

    assert len(vet.assigned_animal) == 1


# Display helpers & __str__

def test_display_enclosure_prints_environment(capsys):
    zk = DummyZookeeper("Alice")
    enc = make_enclosure()
    zk.assign_enclosure(enc)

    zk.display_enclosure()
    captured = capsys.readouterr()

    assert "savannah" in captured.out.lower()


def test_display_animal_prints_name(capsys):
    vet = DummyVeterinarian("Dr. Bob")
    lion = make_lion()
    vet.assign_animal(lion)

    vet.display_animal()
    captured = capsys.readouterr()

    assert "Simba" in captured.out


def test_staff_str_contains_core_info():
    zk = DummyZookeeper("Alice")
    enc = make_enclosure()
    zk.assign_enclosure(enc)

    s = str(zk)
    assert "--- STAFF INFORMATION ---" in s
    assert "Alice" in s
    assert "zookeeper" in s.lower()
    assert "Assigned Enclosures" in s
