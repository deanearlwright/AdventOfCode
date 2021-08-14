# ======================================================================
# Air Duct Spelunking
#   Advent of Code 2016 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r o b o t . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 24, Air Duct Spelunking"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_24
import robot

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
###########
#0.1.....2#
#.#######.#
#4.......3#
###########
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 14
PART_TWO_RESULT = 20

# ======================================================================
#                                                              TestRobot
# ======================================================================


class TestRobot(unittest.TestCase):  # pylint: disable=R0904
    "Test Robot object"

    def test_empty_init(self):
        "Test the default Robot creation"

        # 1. Create default Robot object
        myobj = robot.Robot()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.ducts, None)

    def test_text_init(self):
        "Test the Robot object creation from text"

        # 1. Create Robot object from text
        myobj = robot.Robot(text=aoc_24.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(len(myobj.ducts.text), 5)

        # 3. Check methods

    def test_part_one(self):
        "Test part one example of Robot object"

        # 1. Create Robot object from text
        myobj = robot.Robot(text=aoc_24.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Robot object"

        # 1. Create Robot object from text
        myobj = robot.Robot(part2=True, text=aoc_24.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ r o b o t . p y                   end
# ======================================================================
