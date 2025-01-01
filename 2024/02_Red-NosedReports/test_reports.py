
# ======================================================================
# Red-Nosed Reports
#   Advent of Code 2024 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r e p o r t s . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 02, Red-Nosed Reports"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_02
import reports

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 2
PART_TWO_RESULT = 4

# ======================================================================
#                                                            TestReports
# ======================================================================


class TestReports(unittest.TestCase):  # pylint: disable=R0904
    "Test Reports object"

    def test_empty_init(self):
        "Test the default Reports creation"

        # 1. Create default Reports object
        myobj = reports.Reports()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.reports), 0)

    def test_text_init(self):
        "Test the Reports object creation from text"

        # 1. Create Reports object from text
        myobj = reports.Reports(text=aoc_02.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(len(myobj.reports), 6)

        # 3. Check methods
        self.assertTrue(myobj.reports[0].is_safe())
        self.assertFalse(myobj.reports[1].is_safe())
        self.assertFalse(myobj.reports[2].is_safe())
        self.assertFalse(myobj.reports[3].is_safe())
        self.assertFalse(myobj.reports[4].is_safe())
        self.assertTrue(myobj.reports[5].is_safe())

    def test_part_one(self):
        "Test part one example of Reports object"

        # 1. Create Reports object from text
        text = aoc_02.from_text(PART_ONE_TEXT)
        myobj = reports.Reports(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Reports object"

        # 1. Create Reports object from text
        text = aoc_02.from_text(PART_TWO_TEXT)
        myobj = reports.Reports(part2=True, text=text)

        # 2. Check methods
        self.assertTrue(myobj.reports[0].is_safe())
        self.assertFalse(myobj.reports[1].is_safe_two())
        self.assertFalse(myobj.reports[2].is_safe_two())
        self.assertTrue(myobj.reports[3].is_safe_two())
        self.assertTrue(myobj.reports[4].is_safe_two())
        self.assertTrue(myobj.reports[5].is_safe_two())

        # 3. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ r e p o r t s . p y                 end
# ======================================================================
