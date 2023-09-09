from src.utils.enums import Commands
from src.utils.time_validator import string_to_datetime
from src.filters import Filters
from src.models import StudentAttendanceRegistry
from src.db import insert_attendance_registry, insert_student_registry


def input_pipeline(raw_data: list[list[str]]):
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
        attendace_object = StudentAttendanceRegistry(
            name=row[1],
            weekday=row[2],
            begin_time=string_to_datetime(row[3]),
            end_time=string_to_datetime(row[4]),
            classroom=row[5],
        )
        rows_by_student_name[row[1]].append(attendace_object)
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
