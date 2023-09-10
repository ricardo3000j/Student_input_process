from .models import StudentAttendanceRegistry
import logging

logger = logging.getLogger(__name__)

"""Datastructure to store students"""

class StudentsRegistry:
    """object to store students"""

    """Singleton pattern"""
    _instance = None

    def __new__(cls):
        logger.info("Creating StudentsRegistry")
        if cls._instance is None:
            cls._instance = super(StudentsRegistry, cls).__new__(cls)
        return cls._instance


student_registry = StudentsRegistry()


def insert_student_registry(students: list[list[str]]):
    """Insert students into registry."""
    for student in students:
        logger.info(f"Inserting student: {student[1]}")
        student_registry.__setattr__(student[1], [])


def insert_attendance_registry(
    student_attendance: dict[str, list[StudentAttendanceRegistry]]
):
    """Insert students attendance into registry."""
    for student, attendance in student_attendance.items():
        logger.info(f"Inserting attendance for student: {student}")
        update_student_registry(student, attendance)


def update_student_registry(
    student_name: str, attendances: list[StudentAttendanceRegistry]
):
    """batch insert attendance to student records."""
    student = hasattr(student_registry, student_name)
    if student:
        student_registry.__getattribute__(student_name).extend(attendances)
    else:
        logger.info(f"Student not found: {student_name}")
