import sys
import logging

logger = logging.getLogger(__name__)

def validate_args():
    if len(sys.argv) != 2:
        logger.error("Invalid number of arguments")
        sys.exit(1)

def validate_file(filename):
    if not filename.endswith(".txt"):
        logger.error("Invalid file extension")
        sys.exit(1)

def get_input():
    validate_args()
    validate_file(sys.argv[1])
    return sys.argv[1]