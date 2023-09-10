from src.utils.regex import is_valid_name, is_number
from src.utils.enums import Commands
from src.utils.time_validator import string_to_datetime, validate_hour_format


class Validator:
    @classmethod
    def command(cls, command):
        return command in [Commands.Student, Commands.Presence]

    @classmethod
    def name(cls, name):
        return is_valid_name(name)

    @classmethod
    def hour(cls, hour):
        return validate_hour_format(hour)

    @classmethod
    def day(cls, day):
        return is_number(day) and int(day) > 0 and int(day) < 8

    @classmethod
    def time_interval(cls, begin_time, end_time):
        begin_time = string_to_datetime(begin_time)
        end_time = string_to_datetime(end_time)
        return begin_time < end_time

    @classmethod
    def validate_presence(cls, row):
        row_len = len(row)
        # removing row with len < 5,
        # minminum lenght for a valid row for presence is 5
        if row_len < 5:
            return False
        # validate day of week
        if row_len > 2 and not Validator.day(row[2]):
            return False

        # validate begin time
        if row_len > 3 and not Validator.hour(row[3]):
            return False

        # validate end time
        if row_len > 4 and not Validator.hour(row[4]):
            return False
        # validate end time must be greater than begin time

        if not Validator.time_interval(row[3], row[4]):
            return False
        # validate classroom and fill it with default string
        if row[0] == Commands.Presence and row_len == 5:
            row.append("default classroom")

        return True

    @classmethod
    def validate_row(cls, row):
        # remove empty rows
        if not row:
            return False
        row_len = len(row)
        # remove row with only 1 element
        if row_len == 1:
            return False
        # minimun lenght for a valid row is 2
        # Validate command filter
        if not cls.command(row[0]):
            return False
        # validate student name
        if not cls.name(row[1]):
            return False
        if row[0] == Commands.Presence:
            return cls.validate_presence(row)
        return True
