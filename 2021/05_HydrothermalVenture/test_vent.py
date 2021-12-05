# ======================================================================
# Hydrothermal Venture
#   Advent of Code 2021 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ v e n t . p y
# ======================================================================
"Test Vent for Advent of Code 2021 day 05, Hydrothermal Venture"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import vent

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "9,4 -> 3,4"
EXAMPLE_TEXT2 = "7,0 -> 7,4"
EXAMPLE_TWO_ONE = "1,1 -> 3,3"
EXAMPLE_TWO_TWO = "9,7 -> 7,9"
EXAMPLE_TWO_THREE = "8,0 -> 0,8"

# ======================================================================
#                                                               TestVent
# ======================================================================


class TestVent(unittest.TestCase):  # pylint: disable=R0904
    "Test Vent object"

    def test_empty_init(self):
        "Test the default Vent creation"

        # 1. Create default Vent object
        myobj = vent.Vent()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.locs), 0)

    def test_text_init(self):
        "Test the Vent object creation from text"

        # 1. Create Vent object from text
        myobj = vent.Vent(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.locs), 7)

    def test_text2_init(self):
        "Test the Vent object creation from text"

        # 1. Create Vent object from text
        myobj = vent.Vent(text=EXAMPLE_TEXT2)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.locs), 5)

    def test_text_init_two_one(self):
        "Test the Vent object creation from for part two"

        # 1. Create Vent object from text
        myobj = vent.Vent(text=EXAMPLE_TWO_ONE, part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.locs), 3)

    def test_text_init_two_two(self):
        "Test the Vent object creation from for part two"

        # 1. Create Vent object from text
        myobj = vent.Vent(text=EXAMPLE_TWO_TWO, part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.locs), 3)

    def test_text_init_two_three(self):
        "Test the Vent object creation from for part two"

        # 1. Create Vent object from text
        myobj = vent.Vent(text=EXAMPLE_TWO_THREE, part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.locs), 9)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ v e n t . p y                end
# ======================================================================
