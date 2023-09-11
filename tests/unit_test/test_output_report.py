import unittest
from datetime import datetime
from src.models import StudentAttendanceRegistry, OutputRecord
from src.report_output import OutputReport


class TestGenerateRecord(unittest.TestCase):
    def test_generate_record(self):
        test_cases = [
            # No attendances
            ("Frank", [], OutputRecord(name="Frank", time=0, days=0)),
            # Attendances with total time less than 5 minutes
            (
                "David",
                [
                    StudentAttendanceRegistry(
                        name="David",
                        weekday=1,
                        begin_time=datetime(2022, 1, 1, 9, 0, 0),
                        end_time=datetime(2022, 1, 1, 9, 2, 30),
                        classroom="D540",
                    ),
                    StudentAttendanceRegistry(
                        name="David",
                        weekday=2,
                        begin_time=datetime(2022, 1, 1, 10, 0, 0),
                        end_time=datetime(2022, 1, 1, 10, 3, 0),
                        classroom="D540",
                    ),
                ],
                OutputRecord(name="David", time=0, days=0),
            ),
            # Attendances with total time greater than 5 minutes
            (
                "Marcos",
                [
                    StudentAttendanceRegistry(
                        name="Marcos",
                        weekday=1,
                        begin_time=datetime(2022, 1, 1, 9, 0, 0),
                        end_time=datetime(2022, 1, 1, 9, 10, 0),
                        classroom="D540",
                    ),
                    StudentAttendanceRegistry(
                        name="Marcos",
                        weekday=2,
                        begin_time=datetime(2022, 1, 1, 10, 0, 0),
                        end_time=datetime(2022, 1, 1, 10, 5, 0),
                        classroom="D540",
                    ),
                    StudentAttendanceRegistry(
                        name="Marcos",
                        weekday=3,
                        begin_time=datetime(2022, 1, 1, 11, 0, 0),
                        end_time=datetime(2022, 1, 1, 11, 30, 0),
                        classroom="D540",
                    ),
                ],
                OutputRecord(name="Marcos", time=45, days=3),
            ),
        ]

        for student, attendances, expected_result in test_cases:
            record = OutputReport.generate_record(student, attendances)
            self.assertEqual(record.name, expected_result.name)
            self.assertEqual(record.time, expected_result.time)
            self.assertEqual(record.days, expected_result.days)


if __name__ == "__main__":
    unittest.main()
