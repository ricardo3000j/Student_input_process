from src.utils.enums import Commands
from src.filters import Filters
from src.models import StudentAttendanceRegistry
from src.db import student_registry


def data_pipeline(raw_data: list[list[str]]):

    sorted_data = sort_by_command(raw_data)
    insert_student_registry(sorted_data[Commands.Student])
    sorted_attendance = sort_by_student_name(sorted_data[Commands.Presence])
    insert_attendance_registry(sorted_attendance)

    

def sort_by_command(data):
    """Create a dict to group by command"""
    rows_by_command = {}
    for row in data:
        if not Filters.valid_command(row[0]):
            continue
        if not row[0] in rows_by_command:
            rows_by_command[row[0]] = []
        rows_by_command[row[0]].append(row)
    return rows_by_command


def sort_by_student_name(data):
    """Create a dict to group by student name"""
    rows_by_student_name = {}
    for row in data:
        if not Filters.valid_name(row[1]):
            continue
        if not row[1] in rows_by_student_name:
            rows_by_student_name[row[1]] = []
        rows_by_student_name[row[1]].append(row)
    return rows_by_student_name




def data_cleaner(raw_data):
    """Remove invalid rows."""
    clean_data = []
    for row in raw_data:
        # Filters to remove invalid rows

        # Valid command filter
        if not Filters.valid_command(row[0]):
            continue

        # validate student name
        if not Filters.valid_name(row[1]):
            continue

        # validate day of week
        # if is_number(row[2]) and

        clean_data.append(row)
    return clean_data


def insert_student_registry(students: list[list[str]]):
    """Insert students into registry."""
    for student in students:
        student_registry.__setattr__(student[1], [])


def insert_attendance_registry(
    student_attendance: dict[str, list[StudentAttendanceRegistry]]
):
    """Insert students attendance into registry."""
    for student, attendance in student_attendance.items():
        update_student_registry(student, attendance)




def update_student_registry(
    student_name: str, attendances: list[StudentAttendanceRegistry]
):
    """batch insert attendance to student records."""
    student_registry.__getattribute__(student_name).extend(attendances)
