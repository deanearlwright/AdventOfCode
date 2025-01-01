
# ======================================================================
# Red-Nosed Reports
#   Advent of Code 2024 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r e p o r t . p y
# ======================================================================
"Test Report for Advent of Code 2024 day 02, Red-Nosed Reports"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import report

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "7 6 4 2 1"

# ======================================================================
#                                                             TestReport
# ======================================================================


class TestReport(unittest.TestCase):  # pylint: disable=R0904
    "Test Report object"

    def test_empty_init(self):
        "Test the default Report creation"

        # 1. Create default Report object
        myobj = report.Report()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.levels), 0)

    def test_text_init(self):
        "Test the Report object creation from text"

        # 1. Create Report object from text
        myobj = report.Report(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 9)
        self.assertEqual(len(myobj.levels), 5)
        self.assertEqual(myobj.levels[0], 7)
        self.assertEqual(myobj.levels[4], 1)

        # 3. Check methods
        self.assertTrue(myobj.is_safe())

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ r e p o r t . p y                  end
# ======================================================================
