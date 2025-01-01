
# ======================================================================
# Restroom Redoubt
#   Advent of Code 2024 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r o b o t . p y
# ======================================================================
"Test Robot for Advent of Code 2024 day 14, Restroom Redoubt"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import robot

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
TEST_SIZE = (11, 7) # cols, rows
EXAMPLE_TEXT = "p=2,4 v=2,-3"

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
        self.assertEqual(myobj.position, (0, 0))
        self.assertEqual(myobj.velocity, (0, 0))
        self.assertEqual(myobj.size, None)
        self.assertEqual(myobj.middle, None)

    def test_text_init(self):
        "Test the Robot object creation from text"

        # 1. Create Robot object from text
        myobj = robot.Robot(text=EXAMPLE_TEXT, size=TEST_SIZE)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 12)
        self.assertEqual(myobj.position, (2, 4))
        self.assertEqual(myobj.velocity, (2, -3))
        self.assertEqual(myobj.size, (11, 7))
        self.assertEqual(myobj.middle, (5, 3))

        # 3. Check methods
        self.assertEqual(myobj.quadrant(), 3)
        self.assertEqual(myobj.move(), (4, 1))  # After 1 second
        self.assertEqual(myobj.quadrant(), 1)
        self.assertEqual(myobj.move(), (6, 5))  # After 2 seconds
        self.assertEqual(myobj.quadrant(), 4)
        self.assertEqual(myobj.move(), (8, 2))  # After 3 seconds
        self.assertEqual(myobj.quadrant(), 2)
        self.assertEqual(myobj.move(), (10, 6)) # After 4 seconds
        self.assertEqual(myobj.quadrant(), 4)
        self.assertEqual(myobj.move(), (1, 3))  # After 5 seconds
        self.assertEqual(myobj.quadrant(), 0)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ r o b o t . p y                   end
# ======================================================================
