'''
File: test_health_record.py
Description: Unit tests for the HealthRecord class.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
'''

import pytest
from health_record import HealthRecord, HealthRecordClosedError
from mammal import Mammal   # Uses your real Animal subclass


def make_lion(name="Simba", healthy=True):
    """Helper to create a valid Animal instance."""
    return Mammal(name, "Lion", 5, "Meat", "savannah", healthy)


# Constructor validation

def test_health_record_valid_creation():
    lion = make_lion()
    rec = HealthRecord(
        animal=lion,
        issue="injuries",
        severity="high",
        date_reported="25/12/2025",
        treatment_notes="Initial treatment.",
        active=True,
    )

    assert rec.issue == "injuries"
    assert rec.severity == "high"
    assert rec.active is True
    assert rec.date_reported == "25/12/2025"
    assert rec.treatment_notes == "Initial treatment."
    assert rec.animal is lion


def test_health_record_invalid_animal_type():
    with pytest.raises(TypeError):
        HealthRecord(
            animal="not an animal",
            issue="injuries",
            severity="high",
            date_reported="25/12/2025",
            treatment_notes="Test",
            active=True,
        )

def test_health_record_invalid_issue():
    lion = make_lion()
    with pytest.raises(ValueError):
        HealthRecord(
            lion,
            issue="broken wing",   # Not in VALID_ISSUES
            severity="high",
            date_reported="25/12/2025",
            treatment_notes="Test",
            active=True,
        )

def test_health_record_invalid_severity():
    lion = make_lion()
    with pytest.raises(ValueError):
        HealthRecord(
            lion,
            issue="injuries",
            severity="critical",  # Invalid
            date_reported="25/12/2025",
            treatment_notes="Test",
            active=True,
        )

def test_health_record_invalid_date():
    lion = make_lion()
    with pytest.raises(ValueError):
        HealthRecord(
            lion,
            issue="injuries",
            severity="high",
            date_reported="2025-12-25",  # Wrong format
            treatment_notes="Test",
            active=True,
        )

def test_health_record_invalid_active_flag():
    lion = make_lion()
    with pytest.raises(ValueError):
        HealthRecord(
            lion,
            issue="injuries",
            severity="high",
            date_reported="25/12/2025",
            treatment_notes="Test",
            active="yes",  # Must be bool
        )

def test_health_record_invalid_notes():
    lion = make_lion()
    with pytest.raises(ValueError):
        HealthRecord(
            lion,
            issue="injuries",
            severity="high",
            date_reported="25/12/2025",
            treatment_notes="   ",  # Empty
            active=True,
        )

# Closing records

def test_close_record_success():
    lion = make_lion()
    rec = HealthRecord(lion, "injuries", "medium", "12/11/2025", "Check-up", True)

    rec.close_record()
    assert rec.active is False


def test_close_record_twice_raises():
    lion = make_lion()
    rec = HealthRecord(lion, "injuries", "medium", "12/11/2025", "Check-up", True)

    rec.close_record()

    with pytest.raises(HealthRecordClosedError):
        rec.close_record()


# Adding notes

def test_add_notes_success():
    lion = make_lion()
    rec = HealthRecord(lion, "injuries", "low", "01/02/2025", "Initial check.", True)

    rec.add_notes("Second check.")
    assert "Second check." in rec.treatment_notes


def test_add_notes_invalid_string():
    lion = make_lion()
    rec = HealthRecord(lion, "injuries", "low", "01/02/2025", "Initial check.", True)

    with pytest.raises(ValueError):
        rec.add_notes("   ")   # Empty notes not allowed


def test_add_notes_to_closed_record_raises():
    lion = make_lion()
    rec = HealthRecord(lion, "injuries", "low", "01/02/2025", "Initial check.", True)

    rec.close_record()

    with pytest.raises(HealthRecordClosedError):
        rec.add_notes("Trying to modify closed record")


# String output

def test_health_record_str_output_contains_details():
    lion = make_lion()
    rec = HealthRecord(lion, "injuries", "medium", "01/01/2025", "Test notes", True)

    s = str(rec)
    assert "HEALTH RECORD" in s
    assert "Simba" in s
    assert "injuries" in s
    assert "medium" in s
    assert "01/01/2025" in s
    assert "Test notes" in s
