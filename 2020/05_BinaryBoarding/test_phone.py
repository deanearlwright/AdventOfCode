# ======================================================================
# Binary Boarding
#   Advent of Code 2020 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p h o n e . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 05, Binary Boarding"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_05
import phone

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 820
PART_TWO_RESULT = 120

# ======================================================================
#                                                              TestPhone
# ======================================================================


class TestPhone(unittest.TestCase):  # pylint: disable=R0904
    "Test Phone object"

    def test_empty_init(self):
        "Test the default Phone creation"

        # 1. Create default Phone object
        myobj = phone.Phone()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.passes), 0)

    def test_text_init(self):
        "Test the Phone object creation from text"

        # 1. Create Phone object from text
        myobj = phone.Phone(text=aoc_05.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(len(myobj.passes), 4)

    def test_part_one(self):
        "Test part one example of Phone object"

        # 1. Create Phone object from text
        myobj = phone.Phone(text=aoc_05.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Phone object"

        # 1. Create Phone object from text
        myobj = phone.Phone(part2=True, text=aoc_05.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ p h o n e . p y                   end
# ======================================================================
