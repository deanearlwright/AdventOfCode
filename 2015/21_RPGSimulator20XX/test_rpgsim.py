# ======================================================================
# RPG Simulator 20XX
#   Advent of Code 2015 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r p g s i m . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 21, RPG Simulator 20XX"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_21
import rpgsim

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ""
PART_ONE_TEXT = ""
PART_TWO_TEXT = ""

PART_ONE_RESULT = None
PART_TWO_RESULT = None

# ======================================================================
#                                                             TestRpgsim
# ======================================================================


class TestRpgsim(unittest.TestCase):  # pylint: disable=R0904
    "Test Rpgsim object"

    def test_empty_init(self):
        "Test the default Rpgsim creation"

        # 1. Create default Rpgsim object
        myobj = rpgsim.Rpgsim()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Rpgsim object creation from text"

        # 1. Create Rpgsim object from text
        myobj = rpgsim.Rpgsim(text=aoc_21.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 0)

    def test_part_one(self):
        "Test part one example of Rpgsim object"

        # 1. Create Rpgsim object from text
        myobj = rpgsim.Rpgsim(text=aoc_21.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Rpgsim object"

        # 1. Create Rpgsim object from text
        myobj = rpgsim.Rpgsim(part2=True, text=aoc_21.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ r p g s i m . p y                  end
# ======================================================================
