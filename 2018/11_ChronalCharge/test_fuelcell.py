# ======================================================================
# Chronal Charge
#   Advent of Code 2018 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ f u e l c e l l . p y
# ======================================================================
"Test solver for Advent of Code 2018 day 11, Chronal Charge"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_11
import fuelcell

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
8
"""
PART_ONE_TEXT = """
18
"""
PART_TWO_TEXT = PART_ONE_TEXT

PART_ONE_RESULT = (33, 45)
PART_TWO_RESULT = (90, 269, 16)

# ======================================================================
#                                                           TestFuelcell
# ======================================================================


class TestFuelcell(unittest.TestCase):  # pylint: disable=R0904
    "Test Fuelcell object"

    def test_empty_init(self):
        "Test the default Fuelcell creation"

        # 1. Create default Fuelcell object
        myobj = fuelcell.Fuelcell()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.width, 300)
        self.assertEqual(myobj.height, 300)
        self.assertEqual(myobj.serial, None)
        self.assertEqual(myobj.cells, None)


    def test_text_init(self):
        "Test the Fuelcell object creation from text"

        # 1. Create Fuelcell object from text
        myobj = fuelcell.Fuelcell(text=aoc_11.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(myobj.width, 300)
        self.assertEqual(myobj.height, 300)
        self.assertEqual(myobj.serial, 8)
        self.assertEqual(len(myobj.cells), myobj.width * myobj.height)
        self.assertEqual(myobj.cell_at(3, 5), 4)

    def test_levels(self):
        "Test the Fuelcell levels with various serial numbers"

        # 1. Test levels
        myobj = fuelcell.Fuelcell(text=["57"])
        self.assertEqual(myobj.cell_at(122,  79), -5)
        myobj = fuelcell.Fuelcell(text=["39"])
        self.assertEqual(myobj.cell_at(217, 196),  0)
        myobj = fuelcell.Fuelcell(text=["71"])
        self.assertEqual(myobj.cell_at(101, 153),  4)

    def test_grid_sum(self):
        "Test the Fuelcell 3x3 grid sum with various serial numbers"

        # 1. Test levels
        myobj = fuelcell.Fuelcell(text=["18"])
        self.assertEqual(myobj.grid_sum(33, 45), 29)
        myobj = fuelcell.Fuelcell(text=["42"])
        self.assertEqual(myobj.grid_sum(21, 61), 30)

    def test_max_grid(self):
        "Find the maximum Fuelcell 3x3 grid with various serial numbers"

        # 1. Test levels
        myobj = fuelcell.Fuelcell(text=["18"])
        self.assertEqual(myobj.max_grid(), (33, 45))
        myobj = fuelcell.Fuelcell(text=["42"])
        self.assertEqual(myobj.max_grid(), (21, 61))

    def test_part_one(self):
        "Test part one example of Fuelcell object"

        # 1. Create Fuelcell object from text
        myobj = fuelcell.Fuelcell(text=aoc_11.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part2_grid_sum(self):
        "Test the Fuelcell 3x3 grid sum with various serial numbers"

        # 1. Test levels
        myobj = fuelcell.Fuelcell(text=["18"])
        self.assertEqual(myobj.part2_grid_sum(90, 269, 16), 113)
        myobj = fuelcell.Fuelcell(text=["42"])
        self.assertEqual(myobj.part2_grid_sum(232, 251, 12), 119)

    def test_part2_max_grid(self):
        "Find the maximum Fuelcell 3x3 grid with various serial numbers"

        # 1. Test levels
        myobj = fuelcell.Fuelcell(text=["18"])
        self.assertEqual(myobj.part2_max_grid(), (90, 269, 16))
        myobj = fuelcell.Fuelcell(text=["42"])
        self.assertEqual(myobj.part2_max_grid(), (232, 251, 12))

    def test_part_two(self):
        "Test part two example of Fuelcell object"

        # 1. Create Fuelcell object from text
        myobj = fuelcell.Fuelcell(part2=True, text=aoc_11.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ f u e l c e l l . p y                end
# ======================================================================
