# ======================================================================
# Report Repair
#   Advent of Code 2020 Day 01 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r e p o r t . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 01, Report Repair"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_01
import report

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
1721
979
366
299
675
1456
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 514579
PART_TWO_RESULT = 241861950

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
        self.assertEqual(len(myobj.numbers), 0)

    def test_text_init(self):
        "Test the Report object creation from text"

        # 1. Create Report object from text
        myobj = report.Report(text=aoc_01.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(len(myobj.numbers), 6)

    def test_part_one(self):
        "Test part one example of Report object"

        # 1. Create Report object from text
        myobj = report.Report(text=aoc_01.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Report object"

        # 1. Create Report object from text
        myobj = report.Report(part2=True, text=aoc_01.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ r e p o r t . p y                 end
# ======================================================================
