
# ======================================================================
# Not Enough Minerals
#   Advent of Code 2022 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r o b o t . p y
# ======================================================================
"Test Robot for Advent of Code 2022 day 19, Not Enough Minerals"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import robot

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "Each obsidian robot costs 3 ore and 14 clay."

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
        self.assertEqual(myobj.produces, None)
        self.assertEqual(myobj.costs, {})

    def test_text_init(self):
        "Test the Robot object creation from text"

        # 1. Create Robot object from text
        myobj = robot.Robot(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 44)
        self.assertEqual(myobj.produces, "obsidian")
        self.assertEqual(len(myobj.costs), 2)
        self.assertEqual(myobj.costs["ore"], 3)
        self.assertEqual(myobj.costs["clay"], 14)
        self.assertEqual(myobj.costs["obsidian"], 0)
        self.assertEqual(myobj.costs["geode"], 0)

        # 3. Check methods
        self.assertEqual(myobj.needs('ore'), 3)
        self.assertEqual(myobj.needs('clay'), 14)
        self.assertEqual(myobj.needs('obsidian'), 0)
        self.assertEqual(myobj.needs('geode'), 0)
        self.assertEqual(myobj.names(), ['ore', 'clay', 'obsidian', 'geode'])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ r o b o t . p y                   end
# ======================================================================
