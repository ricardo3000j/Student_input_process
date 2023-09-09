from enum import Enum


class Commands(str, Enum):
    Student = "Student"
    Presence = "Presence"

    def __str__(self) -> str:
        return self.value
