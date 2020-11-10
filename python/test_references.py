#
# Horizon Generator - Python
#
# Copyright (c) 2020 Nick Banyard
#
import unittest

import references

class TestReferenes(unittest.TestCase):
    """
    Test OS reference conversion
    """
    def test_odd_digits(self):
        with self.assertRaises(references.InvalidReferenceError):
            references.to_osref('TQ32812', 6)

    def test_too_many_digits(self):
        with self.assertRaises(references.InvalidReferenceError):
            references.to_osref('TQ123456123456', 6)

    def test_wrong_order(self):
        with self.assertRaises(references.InvalidReferenceError):
            references.to_osref('123123TQ', 6)

    def test_wrong_type(self):
        with self.assertRaises(references.InvalidCoordinatesError):
            references.to_osref(True, 6)

    def test_ten_to_six(self):
        self.assertEqual(references.to_osref('SU1234554321', 6), 'SU123543')

    def test_ten_to_six_with_spaces(self):
        self.assertEqual(references.to_osref('SU 12345 54321', 6), 'SU123543')

    def test_four_to_six_with_spaces(self):
        self.assertEqual(references.to_osref('SU 12 54', 6), 'SU120540')

    def test_fix_case_six(self):
        self.assertEqual(references.to_osref('s u123123', 6), 'SU123123')

    def test_fix_case_to_four(self):
        self.assertEqual(references.to_osref('s u123123', 4), 'SU1212')

    def test_eastings_and_northings_su(self):
        self.assertEqual(references.to_osref((472847, 127395), 2), 'SU72')

    def test_eastings_and_northings_ny(self):
        self.assertEqual(references.to_osref((372847, 527395), 8), 'NY72842739')

    def test_eastings_and_northings_hp(self):
        self.assertEqual(references.to_osref((472847, 1227395), 4), 'HP7227')

    def test_eastings_and_northings_tg(self):
        self.assertEqual(references.to_osref((672847, 327395), 10), 'TG7284727395')

    def test_eastings_and_northings_bad_figures(self):
        with self.assertRaises(references.InvalidFigureReferenceRequest):
            self.assertEqual(references.to_osref((672847, 327395), 9), 'TG7284727395')

