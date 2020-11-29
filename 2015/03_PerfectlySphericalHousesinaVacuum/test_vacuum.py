# ======================================================================
# Perfectly Spherical Houses in a Vacuum
#   Advent of Code 2015 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ v a c u u m . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 03, Perfectly Spherical Houses in a Vacuum"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_03
import vacuum

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ""
PART_ONE_TEXT = ""
PART_TWO_TEXT = ""

PART_ONE_RESULT = None
PART_TWO_RESULT = None

# ======================================================================
#                                                              TestVacuum
# ======================================================================


class TestVacuum(unittest.TestCase):  # pylint: disable=R0904
    "Test Vacuum object"

    def test_empty_init(self):
        "Test the default Vacuum creation"

        # 1. Create default Vacuum object
        myobj = vacuum.Vacuum()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Vacuum object creation from text"

        # 1. Create Vacuum object from text
        myobj = vacuum.Vacuum(text=aoc_03.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 0)

    def test_part_one(self):
        "Test part one example of Vacuum object"

        # 1. Create Vacuum object from text
        myobj = vacuum.Vacuum(text=aoc_03.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Vacuum object"

        # 1. Create Vacuum object from text
        myobj = vacuum.Vacuum(part2=True, text=aoc_03.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ v a c u u m . p y                end
# ======================================================================
