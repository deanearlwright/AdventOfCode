
# ======================================================================
# Never Tell Me The Odds
#   Advent of Code 2023 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                   t e s t _ h a i l s t o n e s . p y
# ======================================================================
"Test Hailstones for Advent of Code 2023 day 24, Never Tell Me The Odds"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import hailstones

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "19, 13, 30 @ -2,  1, -2",
    "18, 19, 22 @ -1, -1, -2",
    "20, 25, 34 @ -2, -2, -4",
    "12, 31, 28 @ -1, -2, -1",
    "20, 19, 15 @  1, -5, -3",
]

# ======================================================================
#                                                         TestHailstones
# ======================================================================


class TestHailstones(unittest.TestCase):  # pylint: disable=R0904
    "Test Hailstones object"

    def test_empty_init(self):
        "Test the default Hailstones creation"

        # 1. Create default Hailstones object
        myobj = hailstones.Hailstones()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.hailstones), 0)

    def test_text_init(self):
        "Test the Hailstones object creation from text"

        # 1. Create Hailstones object from text
        myobj = hailstones.Hailstones(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(len(myobj.hailstones), 5)
        self.assertEqual(myobj.hailstones[0].pos, (19, 13, 30))
        self.assertEqual(myobj.hailstones[4].vel, (1, -5, -3))

        # 3. Check methods
        self.assertEqual(myobj.xyintersections(), 2)
        self.assertEqual(myobj.xyzintersections(), 47)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end               t e s t _ h a i l s t o n e s . p y              end
# ======================================================================
