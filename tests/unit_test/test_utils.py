from io import StringIO
import unittest
from unittest.mock import patch

from src.utils.regex import (
    is_valid_name,
    contains_number,
    is_number,
    contains_special_characters,
)
from src.utils.time_validator import validate_hour_format
from src.utils import validate_file


class TestUtilsRegex(unittest.TestCase):
    def test_is_valid_name(self):
        # Test cases
        test_cases = [
            # Testing a valida name
            ("Marcos", True),
            # Testing name with number
            ("abc123def", False),
            # Testing empty string
            ("", False),
            # Testing string with only a number
            ("123", False),
            # Testing string with special characters
            ("abc!@#$%def", False),
        ]

        # Test the function for each test case
        for string, expected_result in test_cases:
            with self.subTest(string=string):
                self.assertEqual(is_valid_name(string), expected_result)

    def test_contains_number(self):
        # Test cases
        test_cases = [
            # Testing string with a number
            ("abc123def", True),
            # Testing string without a number
            ("abcdef", False),
            # Testing empty string
            ("", False),
            # Testing string with only a number
            ("123", True),
            # Testing string with special characters
            ("abc!@#$%def", False),
        ]

        # Test the function for each test case
        for string, expected_result in test_cases:
            with self.subTest(string=string):
                self.assertEqual(contains_number(string), expected_result)

    def test_is_number(self):
        test_cases = [
            # Positive integer
            ("1234", True),
            # Zero
            ("0", True),
            # Negative integer
            ("-1234", False),
            # Float
            ("12.34", False),
            # Negative float
            ("-12.34", False),
            # String with invalid characters
            ("abc", False),
            # Empty string
            ("", False),
            # Whitespace string
            ("   ", False),  # Whitespace string
        ]

        for string, expected_result in test_cases:
            with self.subTest(string=string):
                self.assertEqual(is_number(string), expected_result)

    def test_contains_special_characters(self):
        test_cases = [
            # String with no special characters
            ("hello123", False),
            # String with special characters
            ("hello!@#", True),
            # Empty string
            ("", False),
            # String with only special characters
            ("!@#", True),
            # String with special characters and numbers
            ("!@#123", True),
        ]

        for string, expected_result in test_cases:
            with self.subTest(string=string):
                self.assertEqual(contains_special_characters(string), expected_result)

    def test_validate_hour_format(self):
        """Test validate_hour_format function"""
        test_cases = [
            # string with valid format
            ("12:34", True),
            # string with invalid format
            ("1234", False),
            # empty string
            ("", False),
            # string with another time format
            ("12:34:56", False),
        ]

        for string, expected_result in test_cases:
            with self.subTest(string=string):
                self.assertEqual(
                    validate_hour_format(string),
                    expected_result,
                )

    @patch("sys.exit")
    def test_valid_file_extension(self, mock_exit):
        validate_file("test.txt")
        self.assertFalse(mock_exit.called)

    @patch("sys.exit")
    def test_invalid_file_extension(self, mock_exit):
        with patch("sys.stderr", new=StringIO()) as fake_stderr:
            validate_file("test.csv")
            self.assertEqual(fake_stderr.getvalue().strip(), "Invalid file extension")
        mock_exit.assert_called_with(1)


if __name__ == "__main__":
    unittest.main()
