import unittest
from unittest.mock import patch, mock_open

import main
from src.db import student_registry


class TestMainApp(unittest.TestCase):
    @patch("sys.argv", ["script_name", "input.txt"])
    @patch("builtins.open", new_callable=mock_open)
    def test_main_app(self, mock_open):
        mock_file = mock_open.return_value
        mock_file.read.return_value = get_file_content()
        output = main.app()
        self.assertEqual(output, get_expected_result())


if __name__ == "__main__":
    unittest.main()


def get_expected_result():
    """Expected result"""
    return """Marco: 142 minutes in 2 days
David: 104 minutes in 1 day
Fran: 0 minutes
"""


def get_file_content():
    """mock file input"""
    return """
Student Marco
Student David
Student Fran
Presence Marco 1 09:02 10:17 R100
Presence Marco 3 10:58 12:05 R205
Presence David 5 14:02 15:46 F505
Presence Mario 5 14:02 15:46

Delete
Student
Presence
Student d90-
Presence 855 
Delete Marco
Presence Marco D 10:58 12:05 R205
Presence Marco 8 10:58 12:05 R205
Presence Marco -5 10:58 12:05 R205
Presence Marco 0 10:58 12:05 R205
Presence Marco 0 25:58 12:70 R205
Presence Marco 5 Hola 12:70 R205
Presence Marco 5 14:02 13:70 R205
Presence Marco 5 14:05 10:25 R566
Presence Marco 5 14:02 Hola 

Presence Marco
Presence Marco D
Presence Marco 8
Presence Marco 5 Hola 
Presence Marco 5 14:02
Presence Marco 5 14:02 Hola

"""
