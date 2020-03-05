# ======================================================================
# Electromagnetic Moat
#   Advent of Code 2017 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        t e s t _ m o a t . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 24, Electromagnetic Moat"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_24
import moat

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ""
PART_ONE_TEXT = ""
PART_TWO_TEXT = ""

PART_ONE_RESULT = None
PART_TWO_RESULT = None

# ======================================================================
#                                                               TestMoat
# ======================================================================


class TestMoat(unittest.TestCase):  # pylint: disable=R0904
    "Test Moat object"

    def test_empty_init(self):
        "Test the default Moat creation"

        # 1. Create default Moat object
        myobj = moat.Moat()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Moat object creation from text"

        # 1. Create Moat object from text
        myobj = moat.Moat(text=aoc_24.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, EXAMPLE_TEXT)

    def test_part_one(self):
        "Test part one example of Moat object"

        # 1. Create Spinlock object from text
        myobj = moat.Moat(text=aoc_24.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Moat object"

        # 1. Create Spinlock object from text
        myobj = moat.Moat(part2=True, text=aoc_24.from_text(PART_TWO_TEXT))

        # 2. Check the part two
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ m o a t . p y                    end
# ======================================================================
