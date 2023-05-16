
# ======================================================================
# Boiling Boulders
#   Advent of Code 2022 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c u b e . p y
# ======================================================================
"Test Cube for Advent of Code 2022 day 18, Boiling Boulders"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import cube

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "1,2,2"

# ======================================================================
#                                                               TestCube
# ======================================================================


class TestCube(unittest.TestCase):  # pylint: disable=R0904
    "Test Cube object"

    def test_empty_init(self):
        "Test the default Cube creation"

        # 1. Create default Cube object
        myobj = cube.Cube()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.loc, None)
        self.assertEqual(len(myobj.others), 0)

    def test_text_init(self):
        "Test the Cube object creation from text"

        # 1. Create Cube object from text
        myobj = cube.Cube(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(myobj.loc, (1, 2, 2))
        self.assertEqual(len(myobj.others), 0)

        # 3. Check methods
        self.assertEqual(myobj.unconnected_sides(), 6)
        near = cube.Cube(text="1,1,2")
        close = cube.Cube(text="1,1,6")
        far = cube.Cube(text="1,3,3")
        self.assertEqual(myobj.is_connected(near), True)
        self.assertEqual(myobj.is_connected(close), False)
        self.assertEqual(myobj.is_connected(far), False)
        self.assertEqual(myobj.unconnected_sides(), 5)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ c u b e . p y                    end
# ======================================================================
