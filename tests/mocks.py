from datetime import datetime
from src.models import StudentAttendanceRegistry


expected_result = """Marco: 142 minutes in 2 days
David: 104 minutes in 1 day
Fran: 0 minutes
"""


file_content = """
Student Marco
Student David
Student Fran
Presence Marco 1 09:02 10:17 R100
Presence Marco 3 10:58 12:05 R205
Presence David 5 14:02 15:46 F505
Presence Mario 5 14:02 15:46

Delete
Student
Presence
Student d90-
Presence 855 
Delete Marco
Presence Marco D 10:58 12:05 R205
Presence Marco 8 10:58 12:05 R205
Presence Marco -5 10:58 12:05 R205
Presence Marco 0 10:58 12:05 R205
Presence Marco 0 25:58 12:70 R205
Presence Marco 5 Hola 12:70 R205
Presence Marco 5 14:02 13:70 R205
Presence Marco 5 14:05 10:25 R566
Presence Marco 5 14:02 Hola 

Presence Marco
Presence Marco D
Presence Marco 8
Presence Marco 5 Hola 
Presence Marco 5 14:02
Presence Marco 5 14:02 Hola

"""
mock_registry = {
    "Marco": [
        StudentAttendanceRegistry(
            name="Marcos",
            weekday=1,
            begin_time=datetime(2022, 1, 1, 9, 0, 0),
            end_time=datetime(2022, 1, 1, 9, 10, 0),
            classroom="D540",
        ),
        StudentAttendanceRegistry(
            name="Marcos",
            weekday=2,
            begin_time=datetime(2022, 1, 1, 10, 0, 0),
            end_time=datetime(2022, 1, 1, 10, 5, 0),
            classroom="D540",
        ),
        StudentAttendanceRegistry(
            name="Marcos",
            weekday=3,
            begin_time=datetime(2022, 1, 1, 11, 0, 0),
            end_time=datetime(2022, 1, 1, 11, 30, 0),
            classroom="D540",
        ),
    ]
}
