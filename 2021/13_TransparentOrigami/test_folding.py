# ======================================================================
# Transparent Origami
#   Advent of Code 2021 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ f o l d i n g . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 13, Transparent Origami"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_13
import folding

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 17
PART_TWO_RESULT = 16

PART_TWO_IMAGE = """
#####
#...#
#...#
#...#
#####
"""

# ======================================================================
#                                                            TestFolding
# ======================================================================


class TestFolding(unittest.TestCase):  # pylint: disable=R0904
    "Test Folding object"

    def test_empty_init(self):
        "Test the default Folding creation"

        # 1. Create default Folding object
        myobj = folding.Folding()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.dots), 0)
        self.assertEqual(len(myobj.instructions), 0)

    def test_text_init(self):
        "Test the Folding object creation from text"

        # 1. Create Folding object from text
        myobj = folding.Folding(text=aoc_13.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 20)
        self.assertEqual(len(myobj.dots), 18)
        self.assertEqual(len(myobj.instructions), 2)

        self.assertEqual(myobj.instructions[0], ('y', 7))
        self.assertEqual(myobj.instructions[1], ('x', 5))

        # 3. Check methods
        self.assertEqual(myobj.fold_up(7), 17)
        self.assertEqual(myobj.fold_left(5), 16)

    def test_text_init_two(self):
        "Test the Folding object creation from text for part 2"

        # 1. Create Folding object from text
        myobj = folding.Folding(text=aoc_13.from_text(EXAMPLE_TEXT), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 20)
        self.assertEqual(len(myobj.dots), 18)
        self.assertEqual(len(myobj.instructions), 2)

        self.assertEqual(myobj.instructions[0], ('y', 7))
        self.assertEqual(myobj.instructions[1], ('x', 5))

        # 3. Check methods
        self.assertEqual(myobj.fold_all(), 16)
        self.assertEqual(PART_TWO_IMAGE.strip(), str(myobj))

    def test_part_one(self):
        "Test part one example of Folding object"

        # 1. Create Folding object from text
        myobj = folding.Folding(text=aoc_13.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Folding object"

        # 1. Create Folding object from text
        myobj = folding.Folding(part2=True, text=aoc_13.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ f o l d i n g . p y                 end
# ======================================================================
