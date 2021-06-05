# ======================================================================
# Explosives in Cyberspace
#   Advent of Code 2016 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d e c o m p r e s s . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 09, Explosives in Cyberspace"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_09
import decompress

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
X(8x2)(3x3)ABCY
"""
EXAMPLE_EXPAND = "X(3x3)ABC(3x3)ABCY"

EXAMPLES_ONE = {
  "ADVENT": "ADVENT",
  "A(1x5)BC": "ABBBBBC",
  "(3x3)XYZ": "XYZXYZXYZ",
  "A(2x2)BCD(2x2)EFG": "ABCBCDEFEFG",
  "(6x1)(1x3)A": "(1x3)A",
  "X(8x2)(3x3)ABCY": "X(3x3)ABC(3x3)ABCY",
}
EXAMPLES_TWO = {
  "ADVENT": 6,
  "A(1x5)BC": 7,
  "(3x3)XYZ": 9,
  "A(2x2)BCD(2x2)EFG": 11,
  "(6x1)(1x3)A": 3,
  "X(8x2)(3x3)ABCY": 20,
  "(27x12)(20x12)(13x14)(7x10)(1x12)A": 241920,
  "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN": 445,
}
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 18
PART_TWO_RESULT = 20

# ======================================================================
#                                                         TestDecompress
# ======================================================================


class TestDecompress(unittest.TestCase):  # pylint: disable=R0904
    "Test Decompress object"

    def test_empty_init(self):
        "Test the default Decompress creation"

        # 1. Create default Decompress object
        myobj = decompress.Decompress()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

        # 3. Check methods
        self.assertEqual(myobj.expand(), '')

    def test_text_init(self):
        "Test the Decompress object creation from text"

        # 1. Create Decompress object from text
        myobj = decompress.Decompress(text=aoc_09.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)

        # 3. Check methods
        self.assertEqual(myobj.expand(), EXAMPLE_EXPAND)

    def test_examples_one(self):
        "Test the part one examples"

        # 1. Loop for the examples
        for text, expanded in EXAMPLES_ONE.items():

            # 1. Create Decompress object from text
            myobj = decompress.Decompress(text=[text])

            # 2. Make sure it has the expected values
            self.assertEqual(myobj.part2, False)
            self.assertEqual(len(myobj.text), 1)

            # 3. Check methods
            self.assertEqual(myobj.expand(), expanded)

    def test_examples_two(self):
        "Test the part two examples"

        # 1. Loop for the examples
        for text, expanded in EXAMPLES_TWO.items():

            # 1. Create Decompress object from text
            # print(text, expanded)
            myobj = decompress.Decompress(text=[text], part2=True)

            # 2. Make sure it has the expected values
            self.assertEqual(myobj.part2, True)
            self.assertEqual(len(myobj.text), 1)

            # 3. Check methods
            self.assertEqual(myobj.expanded(), expanded)

    def test_part_one(self):
        "Test part two example of Decompress object"

        # 1. Create Decompress object from text
        myobj = decompress.Decompress(text=aoc_09.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Decompress object"

        # 1. Create Decompress object from text
        myobj = decompress.Decompress(part2=True, text=aoc_09.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end               t e s t _ d e c o m p r e s s . p y              end
# ======================================================================
