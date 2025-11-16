'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
import uuid
import helper
from animal import Animal

class HealthRecordClosedError(Exception):
    """Raised when trying to modify or access a closed health record."""
    pass

class HealthRecord:
    def __init__(self,animal: Animal, issue, severity, date_reported, treatment_notes, active):
        self._id = uuid.uuid4()
        try:
            helper.validate_string(issue, "issue")
            helper.validate_level(severity, "severity")
            helper.validate_date(date_reported, "date_reported")
            helper.validate_bool(active, "active")
            helper.validate_string(treatment_notes, "treatment_notes")
        except Exception as e:
            raise ValueError(f"Invalid input for HealthRecord: {e}")
        else:
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
        if not self.__active:
            raise HealthRecordClosedError(
                f"Health record '{self.__issue}' is already closed."
            )
        self.__active = False


    def add_notes(self, notes):
        if not self.__active:
            raise HealthRecordClosedError(
                f"Cannot add notes. Health record '{self.__issue}' is already closed."
            )
        if not isinstance(notes, str) or notes.strip() == "":
            raise ValueError("Notes must be a non-empty string.")

        self.__treatment_notes += f"\n{notes}"

    def __str__(self):
        status = "Active" if self.__active else "Closed"
        return (f"--- HEALTH RECORD ---\n"
                f"Animal name: {self.__animal}\n"
                f"Status: {status}\n"
                f"Issue: {self.__issue}\n"
                f"Severity: {self.__severity}\n"
                f"Date Reported: {self.__date_reported}\n"
                f"Treatment Notes:\n{self.__treatment_notes}\n")


