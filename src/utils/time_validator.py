from datetime import datetime


def validate_hour_format(hour):
    """Validate hour format"""
    try:
        datetime.strptime(hour, "%H:%M")
    except ValueError:
        return False
    return True


def string_to_datetime(string):
    """Convert string to datetime"""
    return datetime.strptime(string, "%H:%M")
