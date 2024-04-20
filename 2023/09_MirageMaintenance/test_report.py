
# ======================================================================
# Mirage Maintenance
#   Advent of Code 2023 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r e p o r t . p y
# ======================================================================
"Test Report for Advent of Code 2023 day 09, Mirage Maintenance"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import report

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45",
]

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
        self.assertEqual(len(myobj.histories), 0)

    def test_text_init(self):
        "Test the Report object creation from text"

        # 1. Create Report object from text
        myobj = report.Report(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 3)
        self.assertEqual(len(myobj.histories), 3)

        # 3. Check methods
        self.assertEqual(myobj.histories[0].next_value(), 18)
        self.assertEqual(myobj.histories[1].next_value(), 28)
        self.assertEqual(myobj.histories[2].next_value(), 68)
        self.assertEqual(myobj.next_values(), 114)

        self.assertEqual(myobj.histories[0].prev_value(), -3)
        self.assertEqual(myobj.histories[1].prev_value(), 0)
        self.assertEqual(myobj.histories[2].prev_value(), 5)
        self.assertEqual(myobj.prev_values(), 2)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ r e p o r t . p y                  end
# ======================================================================
