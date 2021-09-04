# ======================================================================
# Aunt Sue
#   Advent of Code 2015 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d e t e c t i v e . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 16, Aunt Sue"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_16
import detective

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------


EXAMPLE_TEXT = """
Sue 1: children: 1, cars: 8, vizslas: 7
Sue 2: akitas: 10, perfumes: 10, children: 5
Sue 3: cars: 5, pomeranians: 4, vizslas: 1
Sue 4: goldfish: 5, children: 8, perfumes: 3
Sue 5: vizslas: 2, akitas: 7, perfumes: 6
Sue 6: children: 3, goldfish: 5, vizslas: 0
Sue 7: perfumes: 8, cars: 4, goldfish: 10
Sue 8: perfumes: 1, trees: 6, goldfish: 0
Sue 9: pomeranians: 3, goldfish: 10, trees: 10
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 6
PART_TWO_RESULT = 8

# ======================================================================
#                                                          TestDetective
# ======================================================================


class TestDetective(unittest.TestCase):  # pylint: disable=R0904
    "Test Detective object"

    def test_empty_init(self):
        "Test the default Detective creation"

        # 1. Create default Detective object
        myobj = detective.Detective()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.csi.text), 10)
        self.assertEqual(len(myobj.aunts), 0)

    def test_text_init(self):
        "Test the Detective object creation from text"

        # 1. Create Detective object from text
        myobj = detective.Detective(text=aoc_16.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 9)
        self.assertEqual(len(myobj.csi.text), 10)
        self.assertEqual(len(myobj.aunts), 9)

    def test_part_one(self):
        "Test part one example of Detective object"

        # 1. Create Detective object from text
        myobj = detective.Detective(text=aoc_16.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Detective object"

        # 1. Create Detective object from text
        myobj = detective.Detective(part2=True, text=aoc_16.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                t e s t _ d e t e c t i v e . p y               end
# ======================================================================
