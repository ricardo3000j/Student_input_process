from .serializers import output_serializer
from .db import student_registry
from .models import StudentAttendanceRegistry, OutputRecord
import logging
import sys

logger = logging.getLogger(__name__)


class OutputReport:
    """Model for report object"""

    """singleton pattern"""
    _instance = None

    def __new__(cls):
        logger.info("Creating OutputReport")
        if cls._instance is None:
            cls._instance = super(OutputReport, cls).__new__(cls)
        return cls._instance

    @property
    def serialized_output(self):
        """serialized report records"""
        logger.info("Getting serialized output")
        records = self.__dict__.values()
        return output_serializer(records)

    def generate_output(self):
        """Generate report output"""
        serialized_output = self.serialized_output
        logger.info("Generating output")
        with open("output.txt", "w") as file:
            file.write(serialized_output)
        print(serialized_output)
        logger.info("Output generated")

    def generate_report(self):
        """Generate report for all students"""
        for student, attendances in student_registry.__dict__.items():
            logger.info(f"Generating report for student: {student}")
            record = self.generate_record(student, attendances)
            self.__setattr__(student, record)

    def generate_record(
        self, student, attendances: list[StudentAttendanceRegistry]
    ) -> OutputRecord:
        """Generate student attendance entry"""
        time_counter = 0
        days_counter = 0

        for attendance in attendances:
            attendance_time = attendance.end_time - attendance.begin_time
            attendance_time = attendance_time.total_seconds()
            if attendance_time > 300:
                time_counter += attendance_time
                days_counter += 1

        time_minutes = int(time_counter / 60)

        return OutputRecord(name=student, time=time_minutes, days=days_counter)
