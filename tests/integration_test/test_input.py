import unittest
from unittest.mock import patch, mock_open
from mocks import file_content
from src.student_input import StudentInput
from src.db import student_registry


class TestInput(unittest.TestCase):
    @patch("sys.argv", ["script_name", "input.txt"])
    @patch("builtins.open", new_callable=mock_open)
    def test_main_app(self, mock_open):
        mock_file = mock_open.return_value
        mock_file.read.return_value = file_content
        student_input = StudentInput()
        student_input.insert_input_data()
        assert hasattr(student_registry, "Marco")
        assert hasattr(student_registry, "Fran")