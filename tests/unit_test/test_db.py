import unittest
from unittest.mock import patch
from src.db import (
    insert_student_registry,
    insert_attendance_registry,
    student_registry,
)
from src.models import StudentAttendanceRegistry


class TestInsertStudentRegistry(unittest.TestCase):
    def test_insert_student_registry(self):
        students = ["student", "Marcos"], ["student", "Frank"]
        insert_student_registry(students)
        assert hasattr(student_registry, "Marcos")
        assert hasattr(student_registry, "Frank")
        assert student_registry.__getattribute__("Marcos") == []
        assert student_registry.__getattribute__("Frank") == []


class TestInsertAttendanceRegistry(unittest.TestCase):
    def test_insert_attendance_registry(self):
        students = [["student", "Marcos"]]
        insert_student_registry(students)
        student_attendance = {
            "Marcos": [
                StudentAttendanceRegistry(
                    name="Marcos",
                    weekday=1,
                    begin_time="10:00",
                    end_time="11:00",
                    classroom="default classroom",
                )
            ]
        }
        insert_attendance_registry(student_attendance)
        self.assertIsInstance(student_registry.__getattribute__("Marcos"), list)
        self.assertIsInstance(
            student_registry.__getattribute__("Marcos")[0],
            StudentAttendanceRegistry
        )


if __name__ == "__main__":
    unittest.main()
