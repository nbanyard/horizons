#
# Horizon Generator - Python
#
# Copyright (c) 2020 Nick Banyard
#
import math
import unittest
from unittest.mock import Mock, call

import filters

class TestFilters(unittest.TestCase):
    def test_add_height(self):
        points = [
            (None, 10050, 20000),
            (None, 10100, 20000),
            (None, 10150, 20000)
        ]

        dtm = Mock()
        dtm.get_height.side_effect=[40.3, 98.3, 73.1]

        results = list(filters.add_height(dtm, iter(points)))

        dtm.assert_has_calls([
            call.get_height(10050, 20000),
            call.get_height(10100, 20000),
            call.get_height(10150, 20000),
        ])

        self.assertEqual(
            results,
            [
                (None, 10050, 20000, 40.3),
                (None, 10100, 20000, 98.3),
                (None, 10150, 20000, 73.1)
            ]
        )

    def test_add_elevation(self):
        points = [
            (50, None, None, 40.3),
            (100, None, None, 98.3),
            (150, None, None, 73.1)
        ]

        results = list(filters.add_elevation(10.5, iter(points)))

        self.assertEqual(
            results,
            [
                (50, None, None, 40.3, math.atan((40.3 - 10.5) / 50)),
                (100, None, None, 98.3, math.atan((98.3 - 10.5) / 100)),
                (150, None, None, 73.1, math.atan((73.1 - 10.5) / 150))
            ]
        )

    def test_max_distance(self):
        points = [
            (50, None, None),
            (100, None, None),
            (120, None, None),
            (150, None, None),
            (110, None, None)
        ]

        results = list(filters.max_distance(125, iter(points)))

        self.assertEqual(
            results,
            [
                (50, None, None),
                (100, None, None),
                (120, None, None),
            ]
        )

    def test_remove_hidden(self):
        points = [
            (None, None, None, None, 0.1),
            (None, None, None, None, 0.3),
            (None, None, None, None, 0.2),
            (None, None, None, None, 0.2),
            (None, None, None, None, 0.3),
            (None, None, None, None, 0.5),
        ]

        results = list(filters.remove_hidden(iter(points)))

        self.assertEqual(
            results,
            [
                (None, None, None, None, 0.1),
                (None, None, None, None, 0.3),
                (None, None, None, None, 0.5),
            ]
        )
