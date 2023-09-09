from src.utils.regex import is_valid_name, is_number
from src.utils.enums import Commands
from src.utils.time_validator import validate_hour_format


class Filters():
    @staticmethod
    def valid_command(command):
        return command in [Commands.Student, Commands.Presence]

    @staticmethod
    def valid_name(name):
        return is_valid_name(name)

    @staticmethod
    def valid_hour(hour):
        return validate_hour_format(hour)
