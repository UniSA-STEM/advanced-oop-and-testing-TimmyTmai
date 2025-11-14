'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from abc import ABC, abstractmethod
import uuid


class Animal(ABC):
    def __init__(self, name: str, species: str, age: int, diet: str, environment: str, is_healthy = True):
        self._id = uuid.uuid4()
        self.__name = self._validate_string(name, "name")
        self.__species = self._validate_string(species, "species")
        self.__age = self._validate_age(age)
        self.__diet = self._validate_string(diet, "diet")
        self.__environment = self._validate_string(environment, "environment")
        self.__healthy = self._validate_bool(is_healthy, "is_healthy")

    def _validate_string(self, value, field_name):
        """Check if a string is valid (not empty, correct type)."""
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string.")
        value = value.strip()
        if not value:
            raise ValueError(f"{field_name} cannot be empty.")
        return value

    def _validate_age(self, value):
        """Ensure age is a positive integer and within reasonable range."""
        if not isinstance(value, int):
            raise TypeError("Age must be an integer.")
        if value < 0:
            raise ValueError("Age cannot be negative.")
        if value > 250:
            raise ValueError("Age seems unrealistic (over 250).")
        return value

    def _validate_bool(self, value, field_name):
        """Ensure boolean fields are actually bool types."""
        if not isinstance(value, bool):
            raise TypeError(f"{field_name} must be a boolean (True/False).")
        return value

    def eat(self):
        return f"{self.__name} is eating {self.__diet}."

    def sleep(self):
        return f"{self.__name} curls up and sleeps."

    @abstractmethod
    def make_sound(self):
        pass

    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self.__name
    @property
    def species(self):
        return self.__species
    @property
    def age(self):
        return self.__age
    @property
    def diet(self):
        return self.__diet
    @property
    def is_healthy(self):
        return self.__healthy
    @property
    def environment(self):
        return self.__environment