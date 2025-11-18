'''
File: helper.py
Description: Validation helper functions for the zoo management system.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
'''

from datetime import datetime


def validate_string(value, field_name):
    """
    Basic string validation: check type and make sure it's not empty.
    """
    try:
        # Must be a string type
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string.")

        # Remove leading/trailing spaces and ensure something remains
        if not value.strip():
            raise ValueError(f"{field_name} cannot be empty.")

        return True

    except (TypeError, ValueError) as e:
        print(f"Validation Error: {e}")
        return False


def validate_level(value, field_name):
    """
    Validate severity level (low, medium, high).
    """
    allowed = ["low", "medium", "high"]

    try:
        # First check if it's a valid string
        if not validate_string(value, field_name):
            raise ValueError(f"{field_name} failed string validation.")

        # Standardise for comparison
        level = value.strip().lower()

        # Check if it is one of the allowed choices
        if level not in allowed:
            raise ValueError(f"{field_name} must be one of {allowed}")

        return True

    except (TypeError, ValueError) as e:
        print(f"Validation Error: {e}")
        return False


def validate_date(value, field_name):
    """
    Check if the date string is valid and matches DD/MM/YYYY format.
    """
    try:
        # Must be a proper string
        if not validate_string(value, field_name):
            raise ValueError(f"{field_name} failed string validation.")

        # Try converting the string into a real datetime object
        datetime.strptime(value.strip(), "%d/%m/%Y").date()
        return True

    except ValueError:
        print(f"Validation Error: {field_name} must be in format DD/MM/YYYY (e.g., 25/12/2024).")
        return False

    except TypeError:
        print(f"Validation Error: {field_name} must be a string representing a date.")
        return False


def validate_bool(value, field_name):
    """
    Ensure a field is strictly a boolean (True/False).
    """
    try:
        # Python is strict here: only real booleans allowed
        if not isinstance(value, bool):
            raise TypeError(f"{field_name} must be a boolean.")
        return True

    except TypeError as e:
        print(f"Validation Error: {e}")
        return False


def validate_age(value):
    """
    Validate age: must be an integer, non-negative, and realistic.
    """
    try:
        # Age must be a number (int specifically)
        if not isinstance(value, int):
            raise TypeError("Age must be an integer.")

        # No negative ages
        if value < 0:
            raise ValueError("Age cannot be negative.")

        # Extremely large ages are unrealistic for animals
        if value > 250:
            raise ValueError("Age seems unrealistic (over 250).")

        return True

    except (TypeError, ValueError) as e:
        print(f"Validation Error: {e}")
        return False


# List of environments allowed for animal classes
VALID_ENVIRONMENTS = [
    "aquatic", "savannah", "jungle", "arctic",
    "desert", "forest", "mountain", "grassland"
]


def validate_environment(value, field_name="environment"):
    """
    Check that the environment is one of the allowed choices.
    """
    # Must be a string because environment names are text
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string.")

    env = value.strip().lower()

    # Check if environment exists in the predefined list
    if env not in VALID_ENVIRONMENTS:
        raise ValueError(f"{field_name} must be one of {VALID_ENVIRONMENTS}")

    return env

VALID_ISSUES = ["injuries", "illness", "behavioral concerns"]

def validate_issue(value, field_name="issue"):
    """
    Check that the environment is one of the allowed choices.
    """
    # Must be a string because environment names are text
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string.")

    iss = value.strip().lower()

    # Check if environment exists in the predefined list
    if iss not in VALID_ISSUES:
        raise ValueError(f"{field_name} must be one of {VALID_ISSUES}")

    return iss