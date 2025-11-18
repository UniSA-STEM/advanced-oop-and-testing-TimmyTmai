'''
File: test_enclosure.py
Description: Tests for the Enclosure class.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest

from enclosure import Enclosure
from mammal import Mammal


def make_lion(name="Simba"):
    """Helper to create a valid savannah mammal."""
    return Mammal(name, "Lion", 5, "Meat", "savannah", True)


# Constructor validation

def test_enclosure_valid_creation():
    enc = Enclosure(size=200, environment="Savannah")

    # size and environment
    assert enc.environment == "savannah"
    assert enc.clean_level == 5
    # 200 // 100 = 2
    assert "Capacity: 2" in enc.report_status()


def test_enclosure_invalid_size_raises():
    with pytest.raises(ValueError):
        Enclosure(size=0, environment="savannah")

    with pytest.raises(ValueError):
        Enclosure(size=-10, environment="savannah")


def test_enclosure_invalid_environment_raises():
    # helper.validate_environment should raise ValueError for invalid env
    with pytest.raises(ValueError):
        Enclosure(size=100, environment="ocean")


# Adding animals

def test_add_compatible_animal_success():
    enc = Enclosure(size=200, environment="savannah")
    lion = make_lion()

    added = enc.add_animal(lion)

    assert added is True
    assert lion in enc.animals
    assert enc.species == "Lion"


def test_add_animal_wrong_type_raises():
    enc = Enclosure(size=200, environment="savannah")

    with pytest.raises(TypeError):
        enc.add_animal("not an animal")


def test_add_incompatible_environment_rejected():
    enc = Enclosure(size=200, environment="aquatic")
    lion = make_lion()

    added = enc.add_animal(lion)

    assert added is False
    assert lion not in enc.animals


def test_enclosure_capacity_limit():
    # size=100 -> capacity = 1
    enc = Enclosure(size=100, environment="savannah")
    lion1 = make_lion("Simba")
    lion2 = make_lion("Nala")

    assert enc.add_animal(lion1) is True
    assert enc.add_animal(lion2) is False
    assert len(enc.animals) == 1


def test_species_restriction_after_first_animal():
    enc = Enclosure(size=300, environment="savannah")
    lion = make_lion("Simba")
    tiger = Mammal("Sheru", "Tiger", 4, "Meat", "savannah", True)

    assert enc.add_animal(lion) is True
    # Different species, same environment → should be rejected
    assert enc.add_animal(tiger) is False
    assert tiger not in enc.animals
    assert enc.species == "Lion"


# Removing animals

def test_remove_animal_success_and_clear_species_when_empty():
    enc = Enclosure(size=200, environment="savannah")
    lion = make_lion()

    enc.add_animal(lion)
    removed = enc.remove_animal(lion)

    assert removed is True
    assert lion not in enc.animals
    # enclosure should reset species when empty
    assert enc.species is None


def test_remove_animal_not_present_returns_false():
    enc = Enclosure(size=200, environment="savannah")
    lion = make_lion()
    # never added
    removed = enc.remove_animal(lion)
    assert removed is False


def test_remove_animal_wrong_type_raises():
    enc = Enclosure(size=200, environment="savannah")
    with pytest.raises(TypeError):
        enc.remove_animal("not an animal")


# Cleanliness and health effects

def test_clean_enclosure_resets_clean_level():
    enc = Enclosure(size=200, environment="savannah")
    lion = make_lion()
    enc.add_animal(lion)

    enc.decrease_cleanliness()
    assert enc.clean_level == 4

    enc.clean_enclosure()
    assert enc.clean_level == 5


def test_decrease_cleanliness_makes_animals_sick_when_low():
    enc = Enclosure(size=200, environment="savannah")
    lion = make_lion()
    enc.add_animal(lion)

    # Clean level starts at 5. After 3 decreases => 2 => sickness trigger.
    enc.decrease_cleanliness()  # 4
    enc.decrease_cleanliness()  # 3
    enc.decrease_cleanliness()  # 2  -> should make lion sick

    assert enc.clean_level == 2
    assert lion.is_healthy is False


# Reporting helpers

def test_animal_names_and_report_status():
    enc = Enclosure(size=200, environment="savannah")
    lion = make_lion()
    enc.add_animal(lion)

    names = enc.animal_names()
    assert names == ["Simba"]

    status = enc.report_status()
    assert "Clean level:" in status
    assert "Number of animals: 1" in status


def test_enclosure_str_contains_core_info():
    enc = Enclosure(size=200, environment="savannah")
    lion = make_lion()
    enc.add_animal(lion)

    s = str(enc)

    assert "--- ENCLOSURE INFORMATION ---" in s
    assert "savannah" in s
    assert "Size: 200" in s
    assert "Capacity:" in s
    assert "Simba" in s
