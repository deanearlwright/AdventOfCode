# ======================================================================
# Memory Maneuver
#   Advent of Code 2018 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ l i c e n s e . p y
# ======================================================================
"Test solver for Advent of Code 2018 day 08, Memory Maneuver"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_08
import license

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 138
PART_TWO_RESULT = 66

# ======================================================================
#                                                            TestLicense
# ======================================================================


class TestLicense(unittest.TestCase):  # pylint: disable=R0904
    "Test License object"

    def test_empty_init(self):
        "Test the default License creation"

        # 1. Create default License object
        myobj = license.License()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the License object creation from text"

        # 1. Create License object from text
        myobj = license.License(text=aoc_08.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)

    def test_part_one(self):
        "Test part one example of License object"

        # 1. Create License object from text
        myobj = license.License(text=aoc_08.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of License object"

        # 1. Create License object from text
        myobj = license.License(part2=True, text=aoc_08.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ l i c e n s e . p y                end
# ======================================================================
