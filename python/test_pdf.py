#
# Horizon Generator - Python
#
# Copyright (c) 2020 Nick Banyard
#
import unittest

import pdf

class TestPdf(unittest.TestCase):
    def test_outline(self):
        """
        Creates outline document, no assertions, manual check required
        """
        document = pdf.Document('test_horizon.pdf', 'Outline Only', 4)
        document.save()
