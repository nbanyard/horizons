#
# Horizon Generator - Python
#
# Copyright (c) 2020 Nick Banyard
#
import itertools
import math
import unittest
from unittest.mock import patch

import generators


BASE_EASTINGS = 513950
BASE_NORTHINGS = 143150
OVER_HORIZON = 50000
STEP = 50

class TestGenerateByNorthings(unittest.TestCase):
    """
    Test the northings generator, first walk cardinal points, then diagnonals
    """
    def test_north(self):
        """
        By northing generator walks due North.
        """
        by_northings = generators.generate_by_northings(BASE_EASTINGS, BASE_NORTHINGS, 0, STEP)

        self.assertEqual(next(by_northings), (1 * STEP, BASE_EASTINGS, BASE_NORTHINGS + 1 * STEP))
        self.assertEqual(next(by_northings), (2 * STEP, BASE_EASTINGS, BASE_NORTHINGS + 2 * STEP))
        self.assertEqual(next(by_northings), (3 * STEP, BASE_EASTINGS, BASE_NORTHINGS + 3 * STEP))
        self.assertEqual(next(by_northings), (4 * STEP, BASE_EASTINGS, BASE_NORTHINGS + 4 * STEP))

    def test_south(self):
        """
        By northing generator walks due South.
        """
        by_northings = generators.generate_by_northings(BASE_EASTINGS, BASE_NORTHINGS, math.pi, STEP)

        self.assertEqual(next(by_northings), (1 * STEP, BASE_EASTINGS, BASE_NORTHINGS - 1 * STEP))
        self.assertEqual(next(by_northings), (2 * STEP, BASE_EASTINGS, BASE_NORTHINGS - 2 * STEP))
        self.assertEqual(next(by_northings), (3 * STEP, BASE_EASTINGS, BASE_NORTHINGS - 3 * STEP))
        self.assertEqual(next(by_northings), (4 * STEP, BASE_EASTINGS, BASE_NORTHINGS - 4 * STEP))

    def test_east(self):
        """
        By northing generator takes one step East.
        """
        by_northings = generators.generate_by_northings(BASE_EASTINGS, BASE_NORTHINGS, math.pi / 2, STEP)

        first_step = next(by_northings)

        self.assertGreater(first_step[0], OVER_HORIZON)

    def test_west(self):
        """
        By northing generator takes one step West.
        """
        by_northings = generators.generate_by_northings(BASE_EASTINGS, BASE_NORTHINGS, 3 * math.pi / 2, STEP)

        first_step = next(by_northings)

        self.assertGreater(first_step[0], OVER_HORIZON)

    def test_north_east(self):
        """
        By northing generator walks due North East.
        """
        by_northings = generators.generate_by_northings(BASE_EASTINGS, BASE_NORTHINGS, math.pi / 4, STEP)

        self.assertEqual(next(by_northings), (int(1 * STEP * math.sqrt(2)), BASE_EASTINGS + 1 * STEP, BASE_NORTHINGS + 1 * STEP))
        self.assertEqual(next(by_northings), (int(2 * STEP * math.sqrt(2)), BASE_EASTINGS + 2 * STEP, BASE_NORTHINGS + 2 * STEP))
        self.assertEqual(next(by_northings), (int(3 * STEP * math.sqrt(2)), BASE_EASTINGS + 3 * STEP, BASE_NORTHINGS + 3 * STEP))
        self.assertEqual(next(by_northings), (int(4 * STEP * math.sqrt(2)), BASE_EASTINGS + 4 * STEP, BASE_NORTHINGS + 4 * STEP))

    def test_south_east(self):
        """
        By northing generator walks due South East.
        """
        by_northings = generators.generate_by_northings(BASE_EASTINGS, BASE_NORTHINGS, 3 * math.pi / 4, STEP)

        self.assertEqual(next(by_northings), (int(1 * STEP * math.sqrt(2)), BASE_EASTINGS + 1 * STEP, BASE_NORTHINGS - 1 * STEP))
        self.assertEqual(next(by_northings), (int(2 * STEP * math.sqrt(2)), BASE_EASTINGS + 2 * STEP, BASE_NORTHINGS - 2 * STEP))
        self.assertEqual(next(by_northings), (int(3 * STEP * math.sqrt(2)), BASE_EASTINGS + 3 * STEP, BASE_NORTHINGS - 3 * STEP))
        self.assertEqual(next(by_northings), (int(4 * STEP * math.sqrt(2)), BASE_EASTINGS + 4 * STEP, BASE_NORTHINGS - 4 * STEP))

    def test_south_west(self):
        """
        By northing generator walks 3-4-5 South Westish.
        """
        # South plus acos(4/5) goes 3 steps west for 4 south
        by_northings = generators.generate_by_northings(BASE_EASTINGS, BASE_NORTHINGS, math.pi + math.acos(4/5), STEP)

        next(by_northings)
        next(by_northings)
        next(by_northings)
        distance, eastings, northings = next(by_northings)
        self.assertLessEqual(abs(distance - 5 * STEP), 1)
        self.assertLessEqual(abs(eastings - (BASE_EASTINGS - 3 * STEP)), 1)
        self.assertLessEqual(abs(northings - (BASE_NORTHINGS - 4 * STEP)), 1)

    def test_north_west(self):
        """
        By northing generator walks 3-4-5 North Westish.
        """
        # West plus acos(4/5) goes 4 steps west for 3 north
        by_northings = generators.generate_by_northings(BASE_EASTINGS, BASE_NORTHINGS, 3 * math.pi / 2 + math.acos(4/5), STEP)

        next(by_northings)
        next(by_northings)
        distance, eastings, northings = next(by_northings)
        self.assertLessEqual(abs(distance - 5 * STEP), 1)
        self.assertLessEqual(abs(eastings - (BASE_EASTINGS - 4 * STEP)), 1)
        self.assertLessEqual(abs(northings - (BASE_NORTHINGS + 3 * STEP)), 1)

class TestGenerateByEastings(unittest.TestCase):
    """
    Test eastings generator, based on northings generator so skip easy cardinals
    """
    def test_north_east(self):
        """
        By eastings generator walks due North East.
        """
        by_eastings = generators.generate_by_eastings(BASE_EASTINGS, BASE_NORTHINGS, math.pi / 4, STEP)

        self.assertEqual(next(by_eastings), (int(1 * STEP * math.sqrt(2)), BASE_EASTINGS + 1 * STEP, BASE_NORTHINGS + 1 * STEP))
        self.assertEqual(next(by_eastings), (int(2 * STEP * math.sqrt(2)), BASE_EASTINGS + 2 * STEP, BASE_NORTHINGS + 2 * STEP))
        self.assertEqual(next(by_eastings), (int(3 * STEP * math.sqrt(2)), BASE_EASTINGS + 3 * STEP, BASE_NORTHINGS + 3 * STEP))
        self.assertEqual(next(by_eastings), (int(4 * STEP * math.sqrt(2)), BASE_EASTINGS + 4 * STEP, BASE_NORTHINGS + 4 * STEP))

    def test_south_east(self):
        """
        By eastings generator walks due South East.
        """
        by_eastings = generators.generate_by_eastings(BASE_EASTINGS, BASE_NORTHINGS, 3 * math.pi / 4, STEP)

        self.assertEqual(next(by_eastings), (int(1 * STEP * math.sqrt(2)), BASE_EASTINGS + 1 * STEP, BASE_NORTHINGS - 1 * STEP))
        self.assertEqual(next(by_eastings), (int(2 * STEP * math.sqrt(2)), BASE_EASTINGS + 2 * STEP, BASE_NORTHINGS - 2 * STEP))
        self.assertEqual(next(by_eastings), (int(3 * STEP * math.sqrt(2)), BASE_EASTINGS + 3 * STEP, BASE_NORTHINGS - 3 * STEP))
        self.assertEqual(next(by_eastings), (int(4 * STEP * math.sqrt(2)), BASE_EASTINGS + 4 * STEP, BASE_NORTHINGS - 4 * STEP))

    def test_south_west(self):
        """
        By eastings generator walks 3-4-5 South Westish.
        """
        # South plus acos(4/5) goes 4 steps south for 3 west
        by_eastings = generators.generate_by_eastings(BASE_EASTINGS, BASE_NORTHINGS, math.pi + math.acos(4/5), STEP)

        next(by_eastings)
        next(by_eastings)
        distance, eastings, northings = next(by_eastings)
        self.assertLessEqual(abs(distance - 5 * STEP), 1)
        self.assertLessEqual(abs(eastings - (BASE_EASTINGS - 3 * STEP)), 1)
        self.assertLessEqual(abs(northings - (BASE_NORTHINGS - 4 * STEP)), 1)

    def test_north_west(self):
        """
        By northing generator walks 3-4-5 North Westish.
        """
        # West plus acos(4/5) goes 3 steps north for 4 west
        by_eastings = generators.generate_by_eastings(BASE_EASTINGS, BASE_NORTHINGS, 3 * math.pi / 2 + math.acos(4/5), STEP)

        next(by_eastings)
        next(by_eastings)
        next(by_eastings)
        distance, eastings, northings = next(by_eastings)
        self.assertLessEqual(abs(distance - 5 * STEP), 1)
        self.assertLessEqual(abs(eastings - (BASE_EASTINGS - 4 * STEP)), 1)
        self.assertLessEqual(abs(northings - (BASE_NORTHINGS + 3 * STEP)), 1)

class TestGenerateOnBearing(unittest.TestCase):
    """
    Test bearing generator

    Mock the northing and easting generators.
    Walk the 3-4-5 triangle North-North-East

    Base coorindates are passed in, but ignored in the mock for ease of use
    """
    # North plus acos(4/5) goes 3 steps east for 4 north (and visa versa)
    by_northing_sequence = [
        (int(i * STEP * 5 / 4), int(i * STEP * 3 / 4), i * STEP)
        for i in range(1, 10)
    ]
    by_easting_sequence = [
        (int(i * STEP * 5 / 3), i * STEP, int(i * STEP * 4 / 3))
        for i in range(1, 10)
    ]

    @patch('generators.generate_by_eastings')
    @patch('generators.generate_by_northings')
    def test_on_bearing(self, northings_mock, eastings_mock):
        northings_mock.return_value = iter(self.by_northing_sequence)
        eastings_mock.return_value = iter(self.by_easting_sequence)

        on_bearing = generators.generate_on_bearing(BASE_EASTINGS, BASE_NORTHINGS, math.acos(4/5), STEP)

        # While the cardinal generators walk the gaps between the TDM posts
        # The bearing generator tries to get close to the posts
        merged_expectation = sorted(self.by_northing_sequence + self.by_easting_sequence)
        centered_expectation = [
            tuple(int((c + d)/2) for c, d in zip(a, b))
            for a, b in zip(merged_expectation[:-1], merged_expectation[1:])
        ]

        # The real consumer stops when distance reaches a given value
        # We will stop after 10 steps
        self.assertEqual(
            list(itertools.islice(on_bearing, 10)),
            centered_expectation[:10]
        )

        northings_mock.assert_called_once_with(BASE_EASTINGS, BASE_NORTHINGS, math.acos(4/5), STEP)
