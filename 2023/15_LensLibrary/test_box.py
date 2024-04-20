
# ======================================================================
# Lens Library
#   Advent of Code 2023 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ b o x . p y
# ======================================================================
"Test Box for Advent of Code 2023 day 15, Lens Library"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import box

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                TestBox
# ======================================================================


class TestBox(unittest.TestCase):  # pylint: disable=R0904
    "Test Box object"

    def test_empty_init(self):
        "Test the default Box creation"

        # 1. Create default Box object
        myobj = box.Box()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.number, 0)
        self.assertEqual(len(myobj.lenses), 0)
        self.assertEqual(len(myobj.lengths), 0)

    def test_text_init(self):
        "Test the Box object creation from text"

        # 1. Create Box object from text
        myobj = box.Box(number=3)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.number, 3)
        self.assertEqual(len(myobj.lenses), 0)
        self.assertEqual(len(myobj.lengths), 0)

        # 3. Check methods
        myobj.operation("pc=4")
        myobj.operation("ot=9")
        myobj.operation("ab=5")
        myobj.operation("pc-")
        myobj.operation("pc=6")
        myobj.operation("ot=7")
        self.assertEqual(len(myobj.lenses), 3)
        self.assertEqual(len(myobj.lengths), 3)
        self.assertEqual(myobj.lenses, ["ot", "ab", "pc"])
        self.assertEqual(myobj.lengths, [7, 5, 6])

        self.assertEqual(myobj.power(), 140)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      t e s t _ b o x . p y                     end
# ======================================================================
