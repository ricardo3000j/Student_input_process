import re


def is_number(string: str) -> bool:
    """Check if string is a number"""
    return bool(re.match(r"^[0-9]+$", string))


def contains_number(string: str) -> bool:
    """Check if string contains a number"""
    return bool(re.search(r"[0-9]", string))


def contains_special_characters(string: str) -> bool:
    """Check if string contains special characters"""
    return bool(re.search(r"[^a-zA-Z0-9]", string))


def is_valid_name(string: str) -> bool:
    """Check if string is a valid name"""
    valid_name = (
        not is_number(string)
        and not contains_number(string)
        and len(string) > 0
        and not contains_special_characters(string)
    )
    return valid_name
