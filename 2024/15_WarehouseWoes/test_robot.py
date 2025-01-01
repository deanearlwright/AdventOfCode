
# ======================================================================
# Warehouse Woes
#   Advent of Code 2024 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r o b o t . p y
# ======================================================================
"Test Robot for Advent of Code 2024 day 15, Warehouse Woes"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import robot

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ""

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

    def test_text_init(self):
        "Test the Robot object creation from text"

        # 1. Create Robot object from text
        myobj = robot.Robot(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 0)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ r o b o t . p y                   end
# ======================================================================
