
# ======================================================================
# Boiling Boulders
#   Advent of Code 2022 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c u b e s . p y
# ======================================================================
"Test Cubes for Advent of Code 2022 day 18, Boiling Boulders"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import cubes

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "2,2,2",
    "1,2,2",
    "3,2,2",
    "2,1,2",
    "2,3,2",
    "2,2,1",
    "2,2,3",
    "2,2,4",
    "2,2,6",
    "1,2,5",
    "3,2,5",
    "2,1,5",
    "2,3,5"
]

# ======================================================================
#                                                              TestCubes
# ======================================================================


class TestCubes(unittest.TestCase):  # pylint: disable=R0904
    "Test Cubes object"

    def test_empty_init(self):
        "Test the default Cubes creation"

        # 1. Create default Cubes object
        myobj = cubes.Cubes()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.cubes), 0)

    def test_text_init(self):
        "Test the Cubes object creation from text"

        # 1. Create Cubes object from text
        myobj = cubes.Cubes(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 13)
        self.assertEqual(len(myobj.cubes), 13)

        # 3. Check the methods
        self.assertEqual(myobj.total_unconnected_sides(), 64)
        self.assertEqual(myobj.total_cooled_sides(), 58)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ c u b e s . p y                   end
# ======================================================================
