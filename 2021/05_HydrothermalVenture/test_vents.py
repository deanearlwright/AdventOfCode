# ======================================================================
# Hydrothermal Venture
#   Advent of Code 2021 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ v e n t s . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 05, Hydrothermal Venture"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_05
import vents

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 5
PART_TWO_RESULT = 12

# ======================================================================
#                                                              TestVents
# ======================================================================


class TestVents(unittest.TestCase):  # pylint: disable=R0904
    "Test Vents object"

    def test_empty_init(self):
        "Test the default Vents creation"

        # 1. Create default Vents object
        myobj = vents.Vents()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Vents object creation from text"

        # 1. Create Vents object from text
        myobj = vents.Vents(text=aoc_05.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)

    def test_part_one(self):
        "Test part one example of Vents object"

        # 1. Create Vents object from text
        myobj = vents.Vents(text=aoc_05.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Vents object"

        # 1. Create Vents object from text
        myobj = vents.Vents(part2=True, text=aoc_05.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ v e n t s . p y                   end
# ======================================================================
