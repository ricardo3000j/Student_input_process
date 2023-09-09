import sys
import logging

logger = logging.getLogger(__name__)


def validate_args():
    """Validate command line arguments only two arguments"""
    if len(sys.argv) != 2:
        logger.error("Invalid number of arguments")
        sys.exit(1)


def validate_file(filename):
    """Validate file extension only txt"""
    if not filename.endswith(".txt"):
        logger.error("Invalid file extension")
        sys.exit(1)
