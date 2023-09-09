from datetime import datetime


class StudentAttendanceRegistry:
    """Model for student attendance"""

    def __init__(self, **kwargs):
        self.name: str = kwargs.get("name")
        self.weekday: int = kwargs.get("weekday")
        self.begin_time: datetime = kwargs.get("begin_time")
        self.end_time: datetime = kwargs.get("end_time")
        self.classroom: str = kwargs.get("classroom")


class OutputRecord:
    """Model for report record"""

    def __init__(self, **kwargs):
        self.name: str = kwargs.get("name")
        self.time: int = kwargs.get("time")
        self.days: int = kwargs.get("days")
