from datetime import datetime


class StudentAttendanceRegistry:
    """Model for student attendance"""

    def __init__(
        self,
        name: str,
        weekday: int,
        begin_time: datetime,
        end_time: datetime,
        classroom: str,
    ):
        self.name: str = name
        self.weekday: int = weekday
        self.begin_time: datetime = begin_time
        self.end_time: datetime = end_time
        self.classroom: str = classroom


class OutputRecord:
    """Model for report record"""

    def __init__(self, name: str, time: int, days: int):
        self.name: str = name
        self.time: int = time
        self.days: int = days
