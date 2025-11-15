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

import helper


class Animal(ABC):
    def __init__(self, name, species, age, diet, environment, is_healthy):
        self._id = uuid.uuid4()
        try:
            if (
                    helper.validate_string(name, "name")
                    and helper.validate_string(species, "species")
                    and helper.validate_age(age)
                    and helper.validate_string(diet, "diet")
                    and helper.validate_string(environment, "environment")
                    and helper.validate_bool(is_healthy, "is_healthy")
            ):
                # only assign if all validations succeed
                self.__name = name.strip()
                self.__species = species.strip()
                self.__age = age
                self.__diet = diet.strip()
                self.__environment = environment.strip()
                self.__is_healthy = is_healthy
            else:
                raise ValueError("Invalid attribute values for Animal.")
        except Exception as e:
            print(f"Error creating Animal: {e}")

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
        return self.__is_healthy
    @property
    def environment(self):
        return self.__environment

    @is_healthy.setter
    def is_healthy(self, value):
        if not isinstance(value, bool):
            raise TypeError("is_healthy must be a boolean value.")
        self.__is_healthy = value

    def __str__(self):
        return (f"--- ANIMAL INFORMATION ---\n"
                f"Animal name: {self.__name}\n"
                f"Animal species: {self.__species}\n"
                f"Animal age: {self.__age}\n"
                f"Animal diet: {self.__diet}\n"
                f"Animal environment: {self.__environment}\n"
                f"Animal is healthy: {self.__is_healthy}\n"
                )