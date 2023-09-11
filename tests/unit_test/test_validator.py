import unittest
from src.utils.enums import Commands
from src.validators import Validator


class TestValidator(unittest.TestCase):
    def test_command(self):
        test_cases = [
            (Commands.Student, True),
            (Commands.Presence, True),
            ("InvalidCommand", False),
        ]
        for command, expected_result in test_cases:
            with self.subTest(command=command):
                self.assertEqual(Validator.command(command), expected_result)

    def test_day(self):
        test_cases = [
            # Valid day
            ("1", True),
            ("7", True),
            # Invalid day
            ("0", False),
            ("8", False),
            ("-1", False),
            ("10", False),
            # Invalid input
            ("Monday", False),
            ("3.5", False),
        ]

        for day, expected_result in test_cases:
            with self.subTest(day=day):
                self.assertEqual(Validator.day(day), expected_result)

    def test_name(self):
        test_cases = [
            ("Marco", True),
            ("Frank", True),
            ("David", True),
            ("123", False),
            ("!@#$", False),
            ("Marco David", False),
        ]

        for name, expected_result in test_cases:
            with self.subTest(name=name):
                self.assertEqual(Validator.name(name), expected_result)

    def test_time_interval(self):
        test_cases = [
            # Begin time before end time
            (
                "10:00",
                "12:00",
                True,
            ),
            # Begin time after end time
            (
                "10:00",
                "9:00",
                False,
            ),
            # Begin time equal to end time
            (
                "10:00",
                "10:00",
                False,
            ),
        ]

        for begin_time, end_time, expected_result in test_cases:
            self.assertEqual(
                Validator.time_interval(begin_time, end_time), expected_result
            )

    def test_validate_presence(self):
        test_cases = [
            ([], False),
            (["Presence", "marco", "invalid_day", "hour_begin", "hour_end"], False),
            (["Presence", "marco", "1", "invalid_hour_begin", "hour_end"], False),
            (["Presence", "marco", "2", "hour_begin", "invalid_hour_end"], False),
            (["Presence", "marco", "3", "10:00", "12:00"], True),
            (["Presence", "marco", "4", "09:00", "10:00", "B500"], True),
        ]

        for row, expected_result in test_cases:
            with self.subTest(row=row):
                self.assertEqual(Validator.validate_presence(row), expected_result)

    def test_rows(self):
        test_cases = [
            # Valid student row
            (["Student", "Fran"], True),
            # Valid presence row
            (["Presence", "Marco", "1", "09:02", "10:17", "R100"], True),
            # Invalid rows
            (["Delete"], False),
            (["Student"], False),
            (["Presence"], False),
            (["Student", "d90-"], False),
            (["Presence", "855"], False),
            (["Delete", "Marco"], False),
            (["Presence", "Marco"], False),
            (["Presence", "Marco", "D"], False),
            (["Presence", "Marco", "8"], False),
            (["Presence", "Marco", "5", "Hola"], False),
            (["Presence", "Marco", "5", "14:02"], False),
            (["Presence", "Marco", "5", "14:02", "Hola"], False),
        ]
        for row, expected_result in test_cases:
            with self.subTest(row=row):
                self.assertEqual(Validator.validate_row(row), expected_result)

    def test_hour_format(self):
        test_cases = [
            # Valid hour formats
            ("12:00", True),
            ("01:15", True),
            ("00:30", True),
            ("23:45", True),
            # Invalid hour formats
            ("25:00", False),
            ("13:60", False),
            ("100:30", False),
            ("-1:00", False),
            ("001:30", False),
        ]

        for hour, expected_output in test_cases:
            self.assertEqual(Validator.hour(hour), expected_output)


if __name__ == "__main__":
    unittest.main()
