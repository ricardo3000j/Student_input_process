import unittest
from unittest.mock import patch, mock_open
from mocks import expected_result, file_content
import main


class TestMainApp(unittest.TestCase):
    @patch("sys.argv", ["script_name", "input.txt"])
    @patch("builtins.open", new_callable=mock_open)
    def test_main_app(self, mock_open):
        mock_file = mock_open.return_value
        mock_file.read.return_value = file_content
        output = main.app()
        self.assertEqual(output, expected_result)


if __name__ == "__main__":
    unittest.main()
