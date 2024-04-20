
# ======================================================================
# Sand Slabs
#   Advent of Code 2023 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ b r i c k . p y
# ======================================================================
"Test Brick for Advent of Code 2023 day 22, Sand Slabs"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import brick

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "1,0,1~1,2,1"

# ======================================================================
#                                                             TestBrick
# ======================================================================


class TestBrick(unittest.TestCase):  # pylint: disable=R0904
    "Test Brick object"

    def test_empty_init(self):
        "Test the default Brick creation"

        # 1. Create default Brick object
        myobj = brick.Brick()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.corners, None)

    def test_text_init(self):
        "Test the Brick object creation from text"

        # 1. Create Brick object from text
        myobj = brick.Brick(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 11)
        self.assertNotEqual(myobj.corners, None)
        self.assertEqual(myobj.corners, ((1, 0, 1), (1, 2, 1)))

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ b r i c k . p y                end
# ======================================================================
