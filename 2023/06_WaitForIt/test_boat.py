
# ======================================================================
# Wait For It
#   Advent of Code 2023 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ b o a t . p y
# ======================================================================
"Test Boat for Advent of Code 2023 day 06, Wait For It"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import boat

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ""

# ======================================================================
#                                                             TestBoat
# ======================================================================


class TestBoat(unittest.TestCase):  # pylint: disable=R0904
    "Test Boat object"

    def test_empty_init(self):
        "Test the default Boat creation"

        # 1. Create default Boat object
        myobj = boat.Boat()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)

        # 3. Check methods
        self.assertEqual(myobj.min_hold(time=7, distance=9), 2)
        self.assertEqual(myobj.max_hold(time=7, distance=9), 5)
        self.assertEqual(myobj.number_of_ways(time=7, distance=9), 4)

        self.assertEqual(myobj.min_hold(time=15, distance=40), 4)
        self.assertEqual(myobj.max_hold(time=15, distance=40), 11)
        self.assertEqual(myobj.number_of_ways(time=15, distance=40), 8)

        self.assertEqual(myobj.min_hold(time=30, distance=200), 11)
        self.assertEqual(myobj.max_hold(time=30, distance=200), 19)
        self.assertEqual(myobj.number_of_ways(time=30, distance=200), 9)

        self.assertEqual(myobj.min_hold(time=71530, distance=940200), 14)
        self.assertEqual(myobj.max_hold(time=71530, distance=940200), 71516)
        self.assertEqual(myobj.number_of_ways(time=71530, distance=940200),
                         71503)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ b o a t . p y                end
# ======================================================================
