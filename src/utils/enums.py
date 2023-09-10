from enum import Enum


class Commands(str, Enum):
    Student = "Student"
    Presence = "Presence"

    def __str__(self) -> str:
        return self.value


class SortBy(str, Enum):
    StudentName = "name"
    Days = "days"
    Time = "time"

    def __str__(self) -> str:
        return self.value


class SortType(str, Enum):
    Asc = "ascending"
    Des = "descending"

    def __str__(self) -> str:
        return self.value
