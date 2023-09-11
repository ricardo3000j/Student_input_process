import unittest
from unittest.mock import patch, mock_open
from src.serializers import input_deserializer, output_serializer
from src.models import OutputRecord


class TestSerializer(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    def test_input_deserializer(self, mock_open):
        test_cases = [
            # Test case for empty input file
            ("empty_input.txt", [[]]),
            # Test case for input with a single row
            ("single_row_input.txt", [["Student", "Marco"]]),
            # Test case for input with multiple rows
            ("multiple_rows_input.txt", [["row", "1"], ["row", "2"], ["row", "3"]]),
            # # Test case for input with empty rows
            ("empty_rows_input.txt", [["row", "1"], ["row", "2"], [], ["row", "3"]]),
        ]
        for input_file, expected_output in test_cases:
            mock_file = mock_open.return_value
            mock_file.read.return_value = get_file_content(input_file)
            self.assertEqual(input_deserializer(input_file), expected_output)

    def test_output_serializer(self):
        test_cases = [
            # Testing for empty records list
            ([], ""),
            # Testing for a single record
            ([OutputRecord("Marco", 60, 2)], "Marco: 60 minutes in 2 days \n"),
            # Testing for multiple records
            (
                [OutputRecord("Marco", 60, 2), OutputRecord("Frank", 30, 1)],
                "Marco: 60 minutes in 2 days \nFrank: 30 minutes in 1 days \n",
            ),
        ]

        for records, expected_output in test_cases:
            self.assertEqual(output_serializer(records), expected_output)


if __name__ == "__main__":
    unittest.main()


def get_file_content(input_file):
    # mock file content depending on input file
    if input_file == "empty_input.txt":
        return ""
    elif input_file == "single_row_input.txt":
        return "Student Marco"
    elif input_file == "multiple_rows_input.txt":
        return "row 1\nrow 2\nrow 3"
    elif input_file == "empty_rows_input.txt":
        return "row 1\nrow 2\n\nrow 3"
