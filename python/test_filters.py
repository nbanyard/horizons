import math
import unittest
from unittest.mock import Mock, call

from filters import max_distance, add_height, add_elevation

class TestFilters(unittest.TestCase):
    def test_add_height(self):
        points = [
            (50, 10050, 20000),
            (100, 10100, 20000),
            (150, 10150, 20000)
        ]

        dtm = Mock()
        dtm.get_height.side_effect=[40.3, 98.3, 73.1]

        results = list(add_height(dtm, iter(points)))

        dtm.assert_has_calls([
            call.get_height(10050, 20000),
            call.get_height(10100, 20000),
            call.get_height(10150, 20000),
        ])

        self.assertEqual(
            results,
            [
                (50, 10050, 20000, 40.3),
                (100, 10100, 20000, 98.3),
                (150, 10150, 20000, 73.1)
            ]
        )

    def test_add_elevation(self):
        points = [
            (50, 10050, 20000, 40.3),
            (100, 10100, 20000, 98.3),
            (150, 10150, 20000, 73.1)
        ]

        results = list(add_elevation(10.5, iter(points)))

        self.assertEqual(
            results,
            [
                (50, 10050, 20000, 40.3, math.atan((40.3 - 10.5) / 50)),
                (100, 10100, 20000, 98.3, math.atan((98.3 - 10.5) / 100)),
                (150, 10150, 20000, 73.1, math.atan((73.1 - 10.5) / 150))
            ]
        )

    def test_max_distance(self):
        points = [
            (50, 10050, 20000),
            (100, 10100, 20000),
            (120, 10120, 20000),
            (150, 10150, 20000),
            (110, 10110, 20000)
        ]

        results = list(max_distance(125, iter(points)))

        self.assertEqual(
            results,
            [
                (50, 10050, 20000),
                (100, 10100, 20000),
                (120, 10120, 20000),
            ]
        )
