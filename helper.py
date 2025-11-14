from datetime import datetime

def validate_string(value, field_name):
    """Check if a string is valid (not empty, correct type)."""
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string.")
    value = value.strip()
    if not value:
        raise ValueError(f"{field_name} cannot be empty.")
    return True


def validate_level(value, field_name):
    levels = ["low", "medium", "high"]
    if validate_string(value, field_name):
        value = value.lower().strip()
        if value not in levels:
            raise ValueError(f"{field_name} must be one of {levels}")
    return True


def validate_date(value, field_name):
    """Check if a date is valid (not empty, correct type)."""
    if validate_string(value, field_name):
        try:
            # Try to convert the string to a date object
            date_object = datetime.strptime(value.strip(), '%d/%m/%Y').date()
            return True
        except ValueError:
            raise ValueError(f"{field_name} must be in format 'dd/mm/yyyy' (e.g., 05/10/2024).")
    return False

def validate_bool(value, field_name):
    """Ensure boolean fields are actually bool types."""
    if not isinstance(value, bool):
        raise TypeError(f"{field_name} must be a boolean (True/False).")
    return True

def validate_age(value):
    """Ensure age is a positive integer and within reasonable range."""
    if not isinstance(value, int):
        raise TypeError("Age must be an integer.")
    if value < 0:
        raise ValueError("Age cannot be negative.")
    if value > 250:
        raise ValueError("Age seems unrealistic (over 250).")
    return True
