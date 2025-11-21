'''
File: animal.py
Description: Defines the abstract Animal class used in the zoo management system.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod
import uuid

import helper


class Animal(ABC):
    """
    Base class for all animals in the zoo.

    Holds shared attributes such as name, species, age, diet, environment
    and basic behaviours like eating and sleeping.
    """

    def __init__(self, name, species, age, diet, environment, is_healthy):
        """
        Create a new Animal after validating the input values.
        Raises ValueError if any value is invalid.
        """
        # Each animal gets a unique ID so it can be tracked in the system.
        self._id = uuid.uuid4()

        # Validate inputs before assigning them.
        if (
            helper.validate_string(name, "name")
            and helper.validate_string(species, "species")
            and helper.validate_age(age)
            and helper.validate_string(diet, "diet")
            and helper.validate_environment(environment, "environment")
            and helper.validate_bool(is_healthy, "is_healthy")
        ):
            # Use stripped versions of string values to avoid extra spaces.
            self.__name = name.strip()
            self.__species = species.strip()
            self.__age = age
            self.__diet = diet.strip()
            self.__environment = environment.strip()
            self.__is_healthy = is_healthy
        else:
            # If any validation failed, do not create a half-valid object.
            raise ValueError("Invalid attribute values provided when creating Animal.")

    def eat(self):
        """Return a message describing the animal eating."""
        return f"{self.__name} is eating {self.__diet}."

    def sleep(self):
        """Return a message describing the animal sleeping."""
        return f"{self.__name} curls up and sleeps."

    def heal(self):
        """Mark the animal as healthy again."""
        self.__is_healthy = True

    @abstractmethod
    def make_sound(self):
        """
        Force subclasses to define their own sound (e.g., roar, bark, chirp).
        """
        pass

    # Property getters

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
        return self.__is_healthy

    @property
    def environment(self):
        return self.__environment

    @is_healthy.setter
    def is_healthy(self, value):
        """
        Update the health status of the animal.

        Raises TypeError if the new value is not a boolean.
        """
        if not isinstance(value, bool):
            raise TypeError("is_healthy must be a boolean value.")
        self.__is_healthy = value

    def __str__(self):
        """
        Nicely formatted string showing key details about the animal.
        """
        return (
            f"--- ANIMAL INFORMATION ---\n"
            f"Animal name: {self.__name}\n"
            f"Animal species: {self.__species}\n"
            f"Animal age: {self.__age}\n"
            f"Animal diet: {self.__diet}\n"
            f"Animal environment: {self.__environment}\n"
            f"Animal is healthy: {self.__is_healthy}\n"
        )