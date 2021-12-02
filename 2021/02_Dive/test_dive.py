# ======================================================================
# Dive
#   Advent of Code 2021 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d i v e . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 02, Dive"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_02
import dive

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 150
PART_TWO_RESULT = 900

# ======================================================================
#                                                               TestDive
# ======================================================================


class TestDive(unittest.TestCase):  # pylint: disable=R0904
    "Test Dive object"

    def test_empty_init(self):
        "Test the default Dive creation"

        # 1. Create default Dive object
        myobj = dive.Dive()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.hor, 0)
        self.assertEqual(myobj.depth, 0)
        self.assertEqual(myobj.aim, 0)

    def test_text_init(self):
        "Test the Dive object creation from text"

        # 1. Create Dive object from text
        myobj = dive.Dive(text=aoc_02.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(myobj.hor, 0)
        self.assertEqual(myobj.depth, 0)
        self.assertEqual(myobj.aim, 0)

        # 3. Check methods

    def test_part_one(self):
        "Test part one example of Dive object"

        # 1. Create Dive object from text
        myobj = dive.Dive(text=aoc_02.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Dive object"

        # 1. Create Dive object from text
        myobj = dive.Dive(part2=True, text=aoc_02.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ d i v e . p y                    end
# ======================================================================
