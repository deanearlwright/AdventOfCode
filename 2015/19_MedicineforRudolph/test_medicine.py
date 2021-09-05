# ======================================================================
# Medicine for Rudolph
#   Advent of Code 2015 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ m e d i c i n e . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 19, Medicine for Rudolph"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_19
import medicine

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
H => HO
H => OH
O => HH

HOHOHO
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = ""

PART_ONE_RESULT = 7
PART_TWO_RESULT = None

# ======================================================================
#                                                           TestMedicine
# ======================================================================


class TestMedicine(unittest.TestCase):  # pylint: disable=R0904
    "Test Medicine object"

    def test_empty_init(self):
        "Test the default Medicine creation"

        # 1. Create default Medicine object
        myobj = medicine.Medicine()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Medicine object creation from text"

        # 1. Create Medicine object from text
        myobj = medicine.Medicine(text=aoc_19.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(len(myobj.transformations), 3)
        self.assertEqual(myobj.calibrate, "HOHOHO")

        # 3. check methods
        self.assertEqual(myobj.expand('O'), set(['HH']))
        self.assertEqual(myobj.expand('H'), set(['HO', 'OH']))
        self.assertEqual(myobj.expand('HOH'), set(['HOOH', 'HOHO', 'OHOH', 'HHHH']))
        self.assertEqual(len(myobj.expand('HOHOHO')), 7)

    def test_part_one(self):
        "Test part one example of Medicine object"

        # 1. Create Medicine object from text
        myobj = medicine.Medicine(text=aoc_19.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Medicine object"

        # 1. Create Medicine object from text
        myobj = medicine.Medicine(part2=True, text=aoc_19.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ m e d i c i n e . p y                end
# ======================================================================
