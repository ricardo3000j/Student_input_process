from datetime import datetime
import unittest
from src.data_wrangler import (
    group_by_command,
    group_by_student_name,
    sort_by_param,
    input_pipeline,
    data_cleaner,
)
from src.models import StudentAttendanceRegistry, OutputRecord
from src.utils.enums import SortBy, SortType
from src.db import student_registry


class TestDataWrangler(unittest.TestCase):
    def test_group_by_command(self):
        test_cases = [
            # Grouping by command with multiple rows
            (
                [
                    ("Student", "data1"),
                    ("Presence", "data2"),
                    ("Student", "data3"),
                    ("Presence", "data4"),
                    ("Presence", "data5"),
                ],
                {
                    "Student": [("Student", "data1"), ("Student", "data3")],
                    "Presence": [
                        ("Presence", "data2"),
                        ("Presence", "data4"),
                        ("Presence", "data5"),
                    ],
                },
            ),
            # Empty input
            ([], {}),
            # Single row input
            ([("Presence", "data1")], {"Presence": [("Presence", "data1")]}),
            # Input with duplicate rows
            (
                [
                    ("Presence", "data1"),
                    ("Presence", "data1"),
                    ("Student", "data2"),
                    ("Student", "data2"),
                ],
                {
                    "Presence": [("Presence", "data1"), ("Presence", "data1")],
                    "Student": [("Student", "data2"), ("Student", "data2")],
                },
            ),
        ]

        for data, expected_result in test_cases:
            result = group_by_command(data)
            self.assertEqual(result, expected_result)

    def test_group_by_student_name(self):
        test_cases = [
            # Testing with data containing a single Presence
            (
                [["Presence", "Marco", "1", "09:00", "17:00", "D540"]],
                {
                    "Marco": [
                        StudentAttendanceRegistry(
                            name="Marco",
                            weekday=1,
                            begin_time=datetime.strptime("09:00", "%H:%M"),
                            end_time=datetime.strptime("17:00", "%H:%M"),
                            classroom="D540",
                        )
                    ]
                },
            ),
            # Testing with data containing multiple Presence for the same student
            (
                [
                    ["Presence", "Marco", "1", "09:00", "17:00", "D540"],
                    ["Presence", "Marco", "2", "09:00", "17:00", "D540"],
                    ["Presence", "Marco", "3", "09:00", "17:00", "D506"],
                ],
                {
                    "Marco": [
                        StudentAttendanceRegistry(
                            name="Marco",
                            weekday=1,
                            begin_time=datetime.strptime("09:00", "%H:%M"),
                            end_time=datetime.strptime("17:00", "%H:%M"),
                            classroom="D540",
                        ),
                        StudentAttendanceRegistry(
                            name="Marco",
                            weekday=3,
                            begin_time=datetime.strptime("09:00", "%H:%M"),
                            end_time=datetime.strptime("17:00", "%H:%M"),
                            classroom="D540",
                        ),
                        StudentAttendanceRegistry(
                            name="Marco",
                            weekday=2,
                            begin_time=datetime.strptime("09:00", "%H:%M"),
                            end_time=datetime.strptime("17:00", "%H:%M"),
                            classroom="D506",
                        ),
                    ]
                },
            ),
        ]

        for data, expected_output in test_cases:
            with self.subTest(data=data):
                result = group_by_student_name(data)
                self.assertEqual(
                    result["Marco"][0].name, expected_output["Marco"][0].name
                )
                self.assertEqual(
                    result["Marco"][0].classroom,
                    expected_output["Marco"][0].classroom,
                )
                self.assertEqual(
                    result["Marco"][0].begin_time,
                    expected_output["Marco"][0].begin_time,
                )

    def test_sort_by_param(self):
        test_cases = [
            (
                [
                    OutputRecord(name="Frank", time=30, days=1),
                    OutputRecord(name="Marco", time=60, days=2),
                    OutputRecord(name="David", time=45, days=3),
                ],
                SortBy.Time,
                SortType.Des,
                [
                    OutputRecord(name="Marco", time=60, days=2),
                    OutputRecord(name="David", time=45, days=3),
                    OutputRecord(name="Frank", time=30, days=1),
                ],
            ),
            (
                [
                    OutputRecord(name="Marco", time=60, days=2),
                    OutputRecord(name="Frank", time=30, days=1),
                    OutputRecord(name="David", time=45, days=3),
                ],
                SortBy.Time,
                SortType.Asc,
                [
                    OutputRecord(name="Frank", time=30, days=1),
                    OutputRecord(name="David", time=45, days=3),
                    OutputRecord(name="Marco", time=60, days=2),
                ],
            ),
        ]

        for records, sort_by, sort_type, expected_result in test_cases:
            result = sort_by_param(records, sort_by, sort_type)
            self.assertEqual(result[0].time, expected_result[0].time)
            self.assertEqual(result[1].time, expected_result[1].time)
            self.assertEqual(result[2].time, expected_result[2].time)

    def test_data_cleaner(self):
        # mock data with valid and invalid rows
        mock_data = [
            ["Student", "Fran"],
            ["Presence", "Marco", "1", "09:02", "10:17", "R100"],
            ["Delete"],
            ["Student"],
            ["Presence"],
            ["Student", "d90-"],
            ["Presence", "855"],
            ["Delete", "Marco"],
            ["Presence", "Marco"],
            ["Presence", "Marco", "D"],
            ["Presence", "Marco", "8"],
            ["Presence", "Marco", "5", "Hola"],
            ["Presence", "Marco", "5", "14:02"],
            ["Presence", "Marco", "5", "14:02", "Hola"],
        ]
        result = data_cleaner(mock_data)
        self.assertEqual(
            result,
            [["Student", "Fran"], ["Presence", "Marco", "1", "09:02", "10:17", "R100"]],
        )

    def test_data_pipeline(self):
        # mock data with valid and invalid rows
        mock_data = [
            ["Student", "Fran"],
            ["Student", "Marco"],
            ["Presence", "Marco", "1", "09:02", "10:17", "R100"],
            ["Delete"],
            ["Student"],
            ["Presence"],
            ["Student", "d90-"],
            ["Presence", "855"],
            ["Delete", "Marco"],
            ["Presence", "Marco"],
            ["Presence", "Marco", "D"],
            ["Presence", "Marco", "8"],
            ["Presence", "Marco", "5", "Hola"],
            ["Presence", "Marco", "5", "14:02"],
            ["Presence", "Marco", "5", "14:02", "Hola"],
        ]
        input_pipeline(mock_data)
        assert hasattr(student_registry, "Marco")
        assert hasattr(student_registry, "Fran")
        assert student_registry.__getattribute__("Fran") == []
        self.assertIsInstance(
            student_registry.__getattribute__("Marco")[0], StudentAttendanceRegistry
        )
        self.assertEqual(student_registry.__getattribute__("Marco")[0].name, "Marco")
        self.assertEqual(
            student_registry.__getattribute__("Marco")[0].end_time,
            datetime.strptime("10:17", "%H:%M"),
        )
