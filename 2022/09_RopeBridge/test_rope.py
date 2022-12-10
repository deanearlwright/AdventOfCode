# ======================================================================
# Rope Bridge
#   Advent of Code 2022 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r o p e . p y
# ======================================================================
"Test Rope for Advent of Code 2022 day 09, Rope Bridge"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import rope

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                               TestRope
# ======================================================================


class TestRope(unittest.TestCase):  # pylint: disable=R0904
    "Test Rope object"

    def test_empty_init(self):
        "Test the default Rope creation"

        # 1. Create default Rope object
        myobj = rope.Rope()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.length, 2)
        self.assertEqual(len(myobj.knots), 2)
        self.assertEqual(myobj.knots[0], (0, 0))
        self.assertEqual(myobj.knots[1], (0, 0))
        self.assertEqual(len(myobj.visited), 1)

        # 3. Check methods
        myobj.move_head("R 4")
        self.assertEqual(myobj.head(), (4, 0))
        self.assertEqual(myobj.tail(), (3, 0))
        myobj.move_head("U 4")
        self.assertEqual(myobj.head(), (4, -4))
        myobj.move_head("L 3")
        self.assertEqual(myobj.head(), (1, -4))
        myobj.move_head("D 1")
        self.assertEqual(myobj.head(), (1, -3))
        myobj.move_head("R 4")
        self.assertEqual(myobj.head(), (5, -3))
        myobj.move_head("D 1")
        self.assertEqual(myobj.head(), (5, -2))
        myobj.move_head("L 5")
        self.assertEqual(myobj.head(), (0, -2))
        myobj.move_head("R 2")
        self.assertEqual(myobj.head(), (2, -2))
        self.assertEqual(myobj.tail(), (1, -2))
        self.assertEqual(len(myobj.visited), 13)
        self.assertEqual(myobj.tail_visited(), 13)

    def test_text_init(self):
        "Test the Rope object creation from text"

        # 1. Create Rope object from text
        myobj = rope.Rope(length=10)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.length, 10)
        self.assertEqual(len(myobj.knots), 10)
        self.assertEqual(myobj.knots[0], (0, 0))
        self.assertEqual(myobj.knots[1], (0, 0))
        self.assertEqual(len(myobj.visited), 1)

        # 3. Check methods
        myobj.move_head("R 4")
        self.assertEqual(myobj.head(), (4, 0))
        self.assertEqual(myobj.knots[1], (3, 0))
        self.assertEqual(myobj.knots[2], (2, 0))
        self.assertEqual(myobj.knots[3], (1, 0))
        self.assertEqual(myobj.knots[4], (0, 0))
        myobj.move_head("U 4")
        self.assertEqual(myobj.head(), (4, -4))
        self.assertEqual(myobj.knots[1], (4, -3))
        self.assertEqual(myobj.knots[2], (4, -2))
        self.assertEqual(myobj.knots[3], (3, -2))
        self.assertEqual(myobj.knots[4], (2, -2))
        self.assertEqual(myobj.knots[5], (1, -1))
        self.assertEqual(myobj.knots[6], (0, 0))
        myobj.move_head("L 3")
        self.assertEqual(myobj.head(), (1, -4))
        myobj.move_head("D 1")
        self.assertEqual(myobj.head(), (1, -3))
        myobj.move_head("R 4")
        self.assertEqual(myobj.head(), (5, -3))
        myobj.move_head("D 1")
        self.assertEqual(myobj.head(), (5, -2))
        myobj.move_head("L 5")
        self.assertEqual(myobj.head(), (0, -2))
        myobj.move_head("R 2")
        self.assertEqual(myobj.head(), (2, -2))
        self.assertEqual(myobj.tail(), (0, 0))
        self.assertEqual(len(myobj.visited), 1)
        self.assertEqual(myobj.tail_visited(), 1)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ r o p e . p y                    end
# ======================================================================
