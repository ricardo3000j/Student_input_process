from src.data_wrangler import input_pipeline
from src.serializers import input_deserializer
from src.utils import validate_args, validate_file
import sys
import logging

logger = logging.getLogger(__name__)


class StudentInput:
    def __init__(self):
        self.input = self._get_input()
        self.raw_data = input_deserializer(self.input)

    def _get_input(self):
        """Get input from file"""
        logger.info("Getting input from file")
        validate_args()
        validate_file(sys.argv[1])
        return sys.argv[1]

    def insert_input_data(self):
        """Insert input data into registry"""
        logger.info("Inserting input data into registry")
        self.data = input_pipeline(self.raw_data)
