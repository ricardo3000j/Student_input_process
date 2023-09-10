import logging
from src.student_input import StudentInput
from src.report_output import OutputReport
from src.utils.enums import SortBy, SortType

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logger.info("Starting program")
    student_input = StudentInput()
    student_input.insert_input_data()
    report_output = OutputReport()
    report_output.generate_report()
    report_output.generate_output(sort_by=SortBy.Time, sort_type=SortType.Des)
    logger.info("Finished program")
