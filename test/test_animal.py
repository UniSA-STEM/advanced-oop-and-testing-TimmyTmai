'''
File: test_animal.py
Description: Tests for the abstract Animal base class.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
'''

import pytest
from animal import Animal


# A small concrete subclass so we can instantiate Animal
class DummyAnimal(Animal):
    def make_sound(self):
        return "dummy sound"


def test_animal_valid_creation():
    """Animal with valid data should be created successfully."""
    a = DummyAnimal("Simba", "Lion", 5, "Meat", "savannah", True)

    assert a.name == "Simba"
    assert a.species == "Lion"
    assert a.age == 5
    assert a.diet == "Meat"
    assert a.environment == "savannah"
    assert a.is_healthy is True
    assert a.id is not None  # UUID generated


def test_animal_invalid_name_raises_value_error():
    """Empty name should cause constructor to raise ValueError."""
    with pytest.raises(ValueError):
        DummyAnimal("", "Lion", 5, "Meat", "savannah", True)


def test_animal_invalid_age_raises_value_error():
    """Negative age should cause constructor to raise ValueError."""
    with pytest.raises(ValueError):
        DummyAnimal("Simba", "Lion", -1, "Meat", "savannah", True)


def test_animal_invalid_environment_raises_value_error():
    """Environment not in VALID_ENVIRONMENTS should raise ValueError."""
    with pytest.raises(ValueError):
        DummyAnimal("Simba", "Lion", 5, "Meat", "ocean", True)


def test_animal_invalid_is_healthy_type_raises_value_error():
    """
    Non-boolean is_healthy should fail validation and cause ValueError
    at construction time.
    """
    with pytest.raises(ValueError):
        DummyAnimal("Simba", "Lion", 5, "Meat", "savannah", "yes")


def test_animal_heal_sets_is_healthy_true():
    """Calling heal() should mark the animal as healthy."""
    a = DummyAnimal("Simba", "Lion", 5, "Meat", "savannah", False)
    a.heal()
    assert a.is_healthy is True


def test_animal_is_healthy_setter_rejects_non_bool():
    """Setter for is_healthy should raise TypeError on non-boolean values."""
    a = DummyAnimal("Simba", "Lion", 5, "Meat", "savannah", True)

    with pytest.raises(TypeError):
        a.is_healthy = "yes"  # invalid

    # still accepts valid boolean values
    a.is_healthy = False
    assert a.is_healthy is False


def test_animal_eat_message():
    """eat() should include the animal name and diet."""
    a = DummyAnimal("Simba", "Lion", 5, "Meat", "savannah", True)
    msg = a.eat()
    assert "Simba" in msg
    assert "Meat" in msg


def test_animal_sleep_message():
    """sleep() should include the animal name."""
    a = DummyAnimal("Simba", "Lion", 5, "Meat", "savannah", True)
    msg = a.sleep()
    assert "Simba" in msg
    assert "sleeps" in msg or "curls up" in msg


def test_animal_str_contains_core_fields():
    """__str__ output should include key details."""
    a = DummyAnimal("Simba", "Lion", 5, "Meat", "savannah", True)
    s = str(a)

    assert "--- ANIMAL INFORMATION ---" in s
    assert "Simba" in s
    assert "Lion" in s
    assert "5" in s
    assert "Meat" in s
    assert "savannah" in s
    assert "True" in s
