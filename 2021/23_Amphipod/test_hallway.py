# ======================================================================
# Amphipod
#   Advent of Code 2021 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ h a l l w a y . p y
# ======================================================================
"Test Hallway for Advent of Code 2021 day 23, Amphipod"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_23
import hallway

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
"""

# ======================================================================
#                                                            TestHallway
# ======================================================================


class TestHallway(unittest.TestCase):  # pylint: disable=R0904
    "Test Hallway object"

    def test_empty_init(self):
        "Test the default Hallway creation"

        # 1. Create default Hallway object
        myobj = hallway.Hallway()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.spaces, [])
        self.assertEqual(myobj.doorways, [])

    def test_text_init(self):
        "Test the Hallway object creation from text"

        # 1. Create Hallway object from text
        myobj = hallway.Hallway(text=aoc_23.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(len(myobj.spaces), 11)
        self.assertEqual(len(myobj.doorways), 4)
        self.assertEqual(myobj.doorways, [2, 4, 6, 8])

        # 3. Check methods
        self.assertEqual(str(myobj), "#...........#")


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ h a l l w a y . p y                 end
# ======================================================================
