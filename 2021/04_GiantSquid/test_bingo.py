# ======================================================================
# Giant Squid
#   Advent of Code 2021 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ b i n g o . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 04, Giant Squid"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_04
import bingo

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 4512
PART_TWO_RESULT = 1924

# ======================================================================
#                                                              TestBingo
# ======================================================================


class TestBingo(unittest.TestCase):  # pylint: disable=R0904
    "Test Bingo object"

    def test_empty_init(self):
        "Test the default Bingo creation"

        # 1. Create default Bingo object
        myobj = bingo.Bingo()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.numbers), 0)
        self.assertEqual(len(myobj.cards), 0)

    def test_text_init(self):
        "Test the Bingo object creation from text"

        # 1. Create Bingo object from text
        myobj = bingo.Bingo(text=aoc_04.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 16)
        self.assertEqual(len(myobj.numbers), 27)
        self.assertEqual(len(myobj.cards), 3)

    def test_part_one(self):
        "Test part one example of Bingo object"

        # 1. Create Bingo object from text
        myobj = bingo.Bingo(text=aoc_04.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Bingo object"

        # 1. Create Bingo object from text
        myobj = bingo.Bingo(part2=True, text=aoc_04.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ b i n g o . p y                end
# ======================================================================
