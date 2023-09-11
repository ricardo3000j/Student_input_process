import unittest
from unittest.mock import patch, mock_open
from mocks import mock_registry
from src.report_output import OutputReport
from src.utils.enums import SortBy, SortType


class TestOutput(unittest.TestCase):
    @patch("src.report_output.student_registry.__dict__", mock_registry)
    @patch("builtins.open", new_callable=mock_open)
    def test_output(self, mock_open):
        expected_result = "Marco: 45 minutes in 3 days\n"
        report_output = OutputReport()
        report_output.generate_report()
        output = report_output.generate_output(
            sort_by=SortBy.Time, sort_type=SortType.Des
        )
        self.assertEqual(output, expected_result)
