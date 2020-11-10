#
# Horizon Generator - Python
#
# Copyright (c) 2020 Nick Banyard
#
import unittest

import calcs

class TestCalcs(unittest.TestCase):

    def test_distance_colour_far(self):
        result = calcs.distance_colour(30000, 30000, (0.2, 0.4, 0.6), (0.9, 0.9, 0.9))
        expectation = (0.9, 0.9, 0.9)

        for r, e in zip(result, expectation):
            self.assertAlmostEqual(r, e)

    def test_distance_colour_half(self):
        result = calcs.distance_colour(15000, 30000, (0.2, 0.4, 0.6), (0.9, 0.9, 0.9))
        expectation = (0.55, 0.65, 0.75)

        for r, e in zip(result, expectation):
            self.assertAlmostEqual(r, e)

    def test_distance_colour_tenth(self):
        result = calcs.distance_colour(3000, 30000, (0.2, 0.4, 0.6), (0.9, 0.9, 0.9))
        expectation = (0.27, 0.45, 0.63)

        for r, e in zip(result, expectation):
            self.assertAlmostEqual(r, e)
