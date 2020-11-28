# ======================================================================
# I Was Told There Would Be No Math
#   Advent of Code 2015 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ m a t h . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 02, I Was Told There Would Be No Math"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_02
import math

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ""
PART_ONE_TEXT = ""
PART_TWO_TEXT = ""

PART_ONE_RESULT = None
PART_TWO_RESULT = None

# ======================================================================
#                                                              TestMath
# ======================================================================


class TestMath(unittest.TestCase):  # pylint: disable=R0904
    "Test Math object"

    def test_empty_init(self):
        "Test the default Math creation"

        # 1. Create default Math object
        myobj = math.Math()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Math object creation from text"

        # 1. Create Math object from text
        myobj = math.Math(text=aoc_02.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 0)

    def test_part_one(self):
        "Test part one example of Math object"

        # 1. Create Math object from text
        myobj = math.Math(text=aoc_02.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Math object"

        # 1. Create Math object from text
        myobj = math.Math(part2=True, text=aoc_02.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ m a t h . p y                end
# ======================================================================
