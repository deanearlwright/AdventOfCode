# ======================================================================
# Infinite Elves and Infinite Houses
#   Advent of Code 2015 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ f e d e l f . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 20, Infinite Elves and Infinite Houses"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_20
import fedelf

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "140"
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = ""

PART_ONE_RESULT = 8
PART_TWO_RESULT = None

# ======================================================================
#                                                             TestFedelf
# ======================================================================


class TestFedelf(unittest.TestCase):  # pylint: disable=R0904
    "Test Fedelf object"

    def test_empty_init(self):
        "Test the default Fedelf creation"

        # 1. Create default Fedelf object
        myobj = fedelf.Fedelf()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.goal, 0)

    def test_text_init(self):
        "Test the Fedelf object creation from text"

        # 1. Create Fedelf object from text
        myobj = fedelf.Fedelf(text=aoc_20.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(myobj.goal, 140)

        # 3. Check mothods
        self.assertEqual(myobj.slow_deliver(), 8)
        self.assertEqual(myobj.fast_deliver(), 8)
        self.assertEqual(myobj.deliver2(), 8)

    def test_part_one(self):
        "Test part one example of Fedelf object"

        # 1. Create Fedelf object from text
        myobj = fedelf.Fedelf(text=aoc_20.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Fedelf object"

        # 1. Create Fedelf object from text
        myobj = fedelf.Fedelf(part2=True, text=aoc_20.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ f e d e l f . p y                  end
# ======================================================================
