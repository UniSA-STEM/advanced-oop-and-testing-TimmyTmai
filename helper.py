from datetime import datetime

def validate_string(value, field_name):
    """Check if a string is valid (not empty, correct type)."""
    try:
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string.")
        value = value.strip()
        if not value:
            raise ValueError(f"{field_name} cannot be empty.")
    except (TypeError, ValueError) as e:
        print(f"Validation Error: {e}")
        return False
    else:
        return True


def validate_level(value, field_name):
    """Ensure level is one of low/medium/high."""
    levels = ["low", "medium", "high"]
    try:
        if not validate_string(value, field_name):
            raise ValueError(f"{field_name} failed string validation.")
        value = value.lower().strip()
        if value not in levels:
            raise ValueError(f"{field_name} must be one of {levels}")
    except (TypeError, ValueError) as e:
        print(f"Validation Error: {e}")
        return False
    else:
        return True


def validate_date(value, field_name):
    """Check if a date is valid (not empty, correct type, correct format)."""
    try:
        if not validate_string(value, field_name):
            raise ValueError(f"{field_name} failed string validation.")
        datetime.strptime(value.strip(), "%d/%m/%Y").date()
    except (TypeError, ValueError) as e:
        print(f"Validation Error: {e}")
        return False
    else:
        return True


def validate_bool(value, field_name):
    """Ensure boolean fields are actually bool types."""
    try:
        if not isinstance(value, bool):
            raise TypeError(f"{field_name} must be a boolean (True/False).")
    except TypeError as e:
        print(f"Validation Error: {e}")
        return False
    else:
        return True


def validate_age(value):
    """Ensure age is a positive integer and within reasonable range."""
    try:
        if not isinstance(value, int):
            raise TypeError("Age must be an integer.")
        if value < 0:
            raise ValueError("Age cannot be negative.")
        if value > 250:
            raise ValueError("Age seems unrealistic (over 250).")
    except (TypeError, ValueError) as e:
        print(f"Validation Error: {e}")
        return False
    else:
        return True
