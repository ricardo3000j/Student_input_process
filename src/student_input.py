from src.data_wrangler import data_pipeline
from src.serializers import input_deserializer
from src.utils import validate_args, validate_file
import sys


class StudentInput:
    def __init__(self):
        self.input = self._get_input()
        self.raw_data = input_deserializer(self.input)

    def _get_input(self):
        """Get input from file"""
        validate_args()
        validate_file(sys.argv[1])
        return sys.argv[1]

    def get_processed_data(self):
        self.data = data_pipeline(self.raw_data)
        return self.data
