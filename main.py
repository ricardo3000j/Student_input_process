import logging
from src.student_input import StudentInput
from src.db import student_registry
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    student_input = StudentInput()
    student_input.get_processed_data()
    print(student_registry.__dict__)