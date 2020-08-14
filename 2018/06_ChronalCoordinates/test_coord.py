# ======================================================================
# Chronal Coordinates
#   Advent of Code 2018 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      t e s t _ c o o r d . p y
# ======================================================================
"Test solver for Advent of Code 2018 day 06, Chronal Coordinates"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import coord

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                              TestCoord
# ======================================================================


class TestCoord(unittest.TestCase):  # pylint: disable=R0904
    "Test Coord object"

    def test_empty_init(self):
        "Test the default Coord creation"

        # 1. Create default Area object
        myobj = coord.Coord()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.x, None)
        self.assertEqual(myobj.y, None)
        self.assertEqual(myobj.isInfinite, None)
        self.assertEqual(myobj.minX, None)
        self.assertEqual(myobj.maxX, None)
        self.assertEqual(myobj.minY, None)
        self.assertEqual(myobj.maxY, None)
        self.assertEqual(myobj.area, None)
        self.assertEqual(myobj.closest, None)


    def test_loc_init(self):
        "Test the Coord object creation with loc"

        # 1. Create Area object from text
        myobj = coord.Coord(x=1, y=5)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.x, 1)
        self.assertEqual(myobj.y, 5)
        self.assertEqual(myobj.isInfinite, None)
        self.assertEqual(myobj.minX, None)
        self.assertEqual(myobj.maxX, None)
        self.assertEqual(myobj.minY, None)
        self.assertEqual(myobj.maxY, None)
        self.assertEqual(myobj.area, None)
        self.assertEqual(myobj.closest, None)

        # 3. Test the distance method
        self.assertEqual(myobj.distance(1, 5), 0)
        self.assertEqual(myobj.distance(3, 5), 2)
        self.assertEqual(myobj.distance(0, 5), 1)
        self.assertEqual(myobj.distance(1, 7), 2)
        self.assertEqual(myobj.distance(1, 4), 1)
        self.assertEqual(myobj.distance(0, 0), 6)
        self.assertEqual(myobj.distance(9, 9), 12)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ c o o r d . p y                   end
# ======================================================================
