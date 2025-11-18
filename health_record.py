'''
File: health_record.py
Description: Defines the HealthRecord class for tracking animal health issues.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Integrity Policy.
'''

import uuid
import helper
from animal import Animal


class HealthRecordClosedError(Exception):
    """Raised when trying to modify a closed health record."""
    pass


class HealthRecord:
    """Represents a single health record entry for an animal."""

    def __init__(
        self,
        animal,
        issue: str,
        severity: str,
        date_reported: str,
        treatment_notes: str,
        active: bool
    ):
        """Create a new health record for a given animal."""
        self._id = uuid.uuid4()

        # Ensure we are always linked to a valid Animal instance
        if not isinstance(animal, Animal):
            raise TypeError("HealthRecord must be associated with an Animal instance.")

        # Validate all provided fields before assigning them
        if not (
            helper.validate_issue(issue, "issue")
            and helper.validate_level(severity, "severity")
            and helper.validate_date(date_reported, "date_reported")
            and helper.validate_bool(active, "active")
            and helper.validate_string(treatment_notes, "treatment_notes")
        ):
            raise ValueError("Invalid input provided when creating HealthRecord.")

        self.__animal = animal
        self.__issue = issue.strip()
        self.__severity = severity.lower().strip()
        self.__date_reported = date_reported.strip()
        self.__treatment_notes = treatment_notes.strip()
        self.__active = active

    @property
    def id(self):
        return self._id

    @property
    def animal(self):
        return self.__animal

    @property
    def issue(self):
        return self.__issue

    @property
    def severity(self):
        return self.__severity

    @property
    def active(self):
        return self.__active

    @property
    def date_reported(self):
        return self.__date_reported

    @property
    def treatment_notes(self):
        return self.__treatment_notes

    def close_record(self):
        """Mark this record as closed. Further changes will not be allowed."""
        if not self.__active:
            raise HealthRecordClosedError(
                f"Health record '{self.__issue}' is already closed."
            )
        self.__active = False

    def add_notes(self, notes: str):
        """Append additional notes if the record is still active."""
        if not self.__active:
            raise HealthRecordClosedError(
                f"Cannot add notes. Health record '{self.__issue}' is already closed."
            )

        if not helper.validate_string(notes, "notes"):
            raise ValueError("Notes must be a non-empty string.")

        # Append new notes on a new line to keep a running history
        self.__treatment_notes += f"\n{notes.strip()}"

    def __str__(self):
        """Return a formatted string representation of the health record."""
        status = "Active" if self.__active else "Closed"
        return (
            f"--- HEALTH RECORD ---\n"
            f"Animal name: {self.__animal.name}\n"
            f"Status: {status}\n"
            f"Issue: {self.__issue}\n"
            f"Severity: {self.__severity}\n"
            f"Date Reported: {self.__date_reported}\n"
            f"Treatment Notes:\n{self.__treatment_notes}\n"
        )
