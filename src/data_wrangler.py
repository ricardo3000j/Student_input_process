from src.utils.enums import Commands
from src.utils.time_validator import string_to_datetime
from src.filters import Filters
from src.models import StudentAttendanceRegistry
from src.db import insert_attendance_registry, insert_student_registry
from .utils.enums import SortBy, SortType


def input_pipeline(raw_data: list[list[str]]):
    """pipeline to insert data into registry."""
    cleaned_data = data_cleaner(raw_data)
    sorted_data = group_by_command(cleaned_data)
    insert_student_registry(sorted_data[Commands.Student])
    sorted_attendance = group_by_student_name(sorted_data[Commands.Presence])
    insert_attendance_registry(sorted_attendance)


def group_by_command(data):
    """Create a dict to group by command"""
    rows_by_command = {}
    for row in data:
        if not Filters.valid_command(row[0]):
            continue
        if not row[0] in rows_by_command:
            rows_by_command[row[0]] = []
        rows_by_command[row[0]].append(row)
    return rows_by_command


def group_by_student_name(data):
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
        if not row:  # remover entradas vacias
            continue
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


def sort_by_param(records, sort_by: SortBy, sort_type: SortType):
    """quick sort algorithm to sort records by element and sort_type"""
    if len(records) <= 1:
        return records
    pivot = records[len(records) // 2].__getattribute__(sort_by)
    lower, equal, upper = [], [], []

    for record in records:
        record_element = record.__getattribute__(sort_by)
        if record_element > pivot:
            upper.append(record)
        elif record_element == pivot:
            equal.append(record)
        else:
            lower.append(record)
    if sort_type == SortType.Asc:
        sorted_records = (
            sort_by_param(lower, sort_by, sort_type)
            + equal
            + sort_by_param(upper, sort_by, sort_type)
        )
    elif sort_type == SortType.Des:
        sorted_records = (
            sort_by_param(upper, sort_by, sort_type)
            + equal
            + sort_by_param(lower, sort_by, sort_type)
        )

    return sorted_records
