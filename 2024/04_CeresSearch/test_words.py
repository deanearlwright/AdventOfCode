
# ======================================================================
# Ceres Search
#   Advent of Code 2024 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ w o r d s . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 04, Ceres Search"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_04
import words

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 18
PART_TWO_RESULT = 9

# ======================================================================
#                                                              TestWords
# ======================================================================


class TestWords(unittest.TestCase):  # pylint: disable=R0904
    "Test Words object"

    def test_empty_init(self):
        "Test the default Words creation"

        # 1. Create default Words object
        myobj = words.Words()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.letters), 0)

    def test_text_init(self):
        "Test the Words object creation from text"

        # 1. Create Words object from text
        myobj = words.Words(text=aoc_04.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.letters), 4)
        self.assertEqual(len(myobj.letters["X"]), 19)
        self.assertEqual(len(myobj.letters["M"]), 38)
        self.assertEqual(len(myobj.letters["A"]), 24)
        self.assertEqual(len(myobj.letters["S"]), 19)

        # 3. Check methods
        self.assertEqual(myobj.find_all_directions("XMAS"), 18)

    def test_part_one(self):
        "Test part one example of Words object"

        # 1. Create Words object from text
        text = aoc_04.from_text(PART_ONE_TEXT)
        myobj = words.Words(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Words object"

        # 1. Create Words object from text
        text = aoc_04.from_text(PART_TWO_TEXT)
        myobj = words.Words(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ w o r d s . p y                end
# ======================================================================
