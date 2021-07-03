# ======================================================================
# Timing is Everything
#   Advent of Code 2016 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d i s c s . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 15, Timing is Everything"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_15
import discs

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = ""

PART_ONE_RESULT = 5
PART_TWO_RESULT = None

# ======================================================================
#                                                              TestDiscs
# ======================================================================


class TestDiscs(unittest.TestCase):  # pylint: disable=R0904
    "Test Discs object"

    def test_empty_init(self):
        "Test the default Discs creation"

        # 1. Create default Discs object
        myobj = discs.Discs()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.sizes, [])
        self.assertEqual(myobj.positions, [])

    def test_text_init(self):
        "Test the Discs object creation from text"

        # 1. Create Discs object from text
        myobj = discs.Discs(text=aoc_15.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 2)
        self.assertEqual(myobj.sizes, [5, 2])
        self.assertEqual(myobj.positions, [4, 1])

        # 3. Check methods
        self.assertEqual(myobj.useCRT(), 5)

    def test_part_one(self):
        "Test part one example of Discs object"

        # 1. Create Discs object from text
        myobj = discs.Discs(text=aoc_15.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Discs object"

        # 1. Create Discs object from text
        myobj = discs.Discs(part2=True, text=aoc_15.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ d i s c s . p y                end
# ======================================================================
