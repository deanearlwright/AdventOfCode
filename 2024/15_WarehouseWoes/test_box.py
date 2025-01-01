
# ======================================================================
# Warehouse Woes
#   Advent of Code 2024 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ b o x . p y
# ======================================================================
"Test Box for Advent of Code 2024 day 15, Warehouse Woes"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import box

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ""

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
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.loc, (0, 0))

    def test_text_init(self):
        "Test the Box object creation from text"

        # 1. Create Box object from text
        myobj = box.Box(loc=(1, 4))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.loc, (1, 4))

        # 3. Check methods
        self.assertEqual(myobj.gps(), 104)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      t e s t _ b o x . p y                     end
# ======================================================================
