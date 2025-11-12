'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
import uuid
class HealthRecordClosedError(Exception):
    """Raised when trying to modify or access a closed health record."""
    pass

class HealthRecord:
    def __init__(self,issue: str, severity: str, date_reported: str, treatment_notes: str, active = True):
        self._id = uuid.uuid4()
        self.__issue = issue
        self.__severity = severity
        self.__date_reported = date_reported
        self.__treatment_notes = treatment_notes
        self.__active = active

    @property
    def id(self):
        return self._id
    @property
    def issue(self):
        return self.__issue
    @property
    def severity(self):
        return self.__severity
    @property
    def active(self):
        return self.__active

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
        return f"[{status}] {self.__issue} (Severity: {self.__severity})"



