# ======================================================================
# Two-Factor Authentication
#   Advent of Code 2016 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d i s p l a y . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 08, Two-Factor Authentication"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_08
import display

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1
"""

DISPLAY_START = """.......
.......
......."""

DISPLAY_ONE = """###....
###....
......."""

DISPLAY_TWO = """#.#....
###....
.#....."""

DISPLAY_THREE = """....#.#
###....
.#....."""

DISPLAY_FOUR = """.#..#.#
#.#....
.#....."""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 6
PART_TWO_RESULT = DISPLAY_FOUR

# ======================================================================
#                                                            TestDisplay
# ======================================================================


class TestDisplay(unittest.TestCase):  # pylint: disable=R0904
    "Test Display object"

    def test_empty_init(self):
        "Test the default Display creation"

        # 1. Create default Display object
        myobj = display.Display()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.tall, 6)
        self.assertEqual(myobj.wide, 50)
        self.assertEqual(len(myobj.pixels), 6)
        self.assertEqual(myobj.inst, 0)

    def test_text_init(self):
        "Test the Display object creation from text"

        # 1. Create Display object from text
        myobj = display.Display(text=aoc_08.from_text(EXAMPLE_TEXT), wide=7, tall=3)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(myobj.tall, 3)
        self.assertEqual(myobj.wide, 7)
        self.assertEqual(len(myobj.pixels), 3)
        self.assertEqual(myobj.inst, 0)

        # 3. Check methods
        self.assertEqual(myobj.lit(), 0)
        self.assertEqual(str(myobj), DISPLAY_START)
        self.assertEqual(myobj.one_inst(), True)
        self.assertEqual(myobj.inst, 1)
        self.assertEqual(str(myobj), DISPLAY_ONE)
        self.assertEqual(myobj.lit(), 6)
        self.assertEqual(myobj.one_inst(), True)
        self.assertEqual(myobj.inst, 2)
        self.assertEqual(str(myobj), DISPLAY_TWO)
        self.assertEqual(myobj.lit(), 6)
        self.assertEqual(myobj.one_inst(), True)
        self.assertEqual(myobj.inst, 3)
        self.assertEqual(str(myobj), DISPLAY_THREE)
        self.assertEqual(myobj.lit(), 6)
        self.assertEqual(myobj.one_inst(), True)
        self.assertEqual(myobj.inst, 4)
        self.assertEqual(str(myobj), DISPLAY_FOUR)
        self.assertEqual(myobj.lit(), 6)
        self.assertEqual(myobj.one_inst(), False)
        self.assertEqual(myobj.inst, 4)
        self.assertEqual(str(myobj), DISPLAY_FOUR)
        self.assertEqual(myobj.lit(), 6)

    def test_part_one(self):
        "Test part one example of Display object"

        # 1. Create Display object from text
        myobj = display.Display(text=aoc_08.from_text(PART_ONE_TEXT), wide=7, tall=3)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Display object"

        # 1. Create Display object from text
        myobj = display.Display(part2=True, text=aoc_08.from_text(PART_TWO_TEXT), wide=7, tall=3)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ d i s p l a y . p y                 end
# ======================================================================
