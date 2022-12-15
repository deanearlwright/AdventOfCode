
# ======================================================================
# Regolith Reservoir
#   Advent of Code 2022 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s c a n . p y
# ======================================================================
"Test Scan for Advent of Code 2022 day 14, Regolith Reservoir"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import scan

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "500,0"

# ======================================================================
#                                                               TestScan
# ======================================================================


class TestScan(unittest.TestCase):  # pylint: disable=R0904
    "Test Scan object"

    def test_empty_init(self):
        "Test the default Scan creation"

        # 1. Create default Scan object
        myobj = scan.Scan()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.source, None)
        self.assertEqual(myobj.slice, {})
        self.assertEqual(myobj.rocks, 0)
        self.assertEqual(myobj.sand, 0)
        self.assertEqual(myobj.lowest, 0)

    def test_text_init(self):
        "Test the Scan object creation from text"

        # 1. Create Scan object from text
        myobj = scan.Scan(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(myobj.source, (500, 0))
        self.assertEqual(myobj.slice, {})
        self.assertEqual(myobj.rocks, 0)
        self.assertEqual(myobj.sand, 0)
        self.assertEqual(myobj.lowest, 0)

        # 3. Add some rock
        myobj.add_path("498,4 -> 498,6 -> 496,6")
        self.assertEqual(myobj.rocks, 5)
        self.assertEqual(len(myobj.slice), 5)
        myobj.add_path("503,4 -> 502,4 -> 502,9 -> 494,9")
        self.assertEqual(myobj.rocks, 20)
        self.assertEqual(len(myobj.slice), 20)

        myobj.find_lowest()
        self.assertEqual(myobj.lowest, 9)

        self.assertEqual(myobj.drop(), (500, 8))
        self.assertEqual(myobj.sand, 1)
        self.assertEqual(myobj.drop(), (499, 8))
        self.assertEqual(myobj.sand, 2)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ s c a n . p y                    end
# ======================================================================
