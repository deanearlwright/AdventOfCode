# ======================================================================
# Balance Bots
#   Advent of Code 2016 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ b o t s . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 10, Balance Bots"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_10
import bots

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
"""

PART_ONE_TEXT = ""
PART_TWO_TEXT = ""

PART_ONE_RESULT = None
PART_TWO_RESULT = None

# ======================================================================
#                                                              TestBots
# ======================================================================


class TestBots(unittest.TestCase):  # pylint: disable=R0904
    "Test Bots object"

    def test_empty_init(self):
        "Test the default Bots creation"

        # 1. Create default Bots object
        myobj = bots.Bots()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.bots, {})
        self.assertEqual(myobj.outputs, {})
        self.assertEqual(myobj.twos, set())

    def test_text_init(self):
        "Test the Bots object creation from text"

        # 1. Create Bots object from text
        myobj = bots.Bots(text=aoc_10.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(len(myobj.bots), 3)
        self.assertEqual(len(myobj.outputs), 0)
        self.assertEqual(len(myobj.twos), 1)

        # 3. Check methods
        self.assertEqual(myobj.zooming_around(values=(5, 2)), 2)

    def test_part_one(self):
        "Test part one example of Bots object"

        # 1. Create Bots object from text
        myobj = bots.Bots(text=aoc_10.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Bots object"

        # 1. Create Bots object from text
        myobj = bots.Bots(part2=True, text=aoc_10.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ b o t s . p y                end
# ======================================================================
