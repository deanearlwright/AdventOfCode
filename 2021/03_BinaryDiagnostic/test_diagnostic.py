# ======================================================================
# Binary Diagnostic
#   Advent of Code 2021 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                  t e s t _ d i a g n o s t i c . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 03, Binary Diagnostic"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_03
import diagnostic

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 198
PART_TWO_RESULT = 230

# ======================================================================
#                                                         TestDiagnostic
# ======================================================================


class TestDiagnostic(unittest.TestCase):  # pylint: disable=R0904
    "Test Diagnostic object"

    def test_empty_init(self):
        "Test the default Diagnostic creation"

        # 1. Create default Diagnostic object
        myobj = diagnostic.Diagnostic()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Diagnostic object creation from text"

        # 1. Create Diagnostic object from text
        myobj = diagnostic.Diagnostic(text=aoc_03.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 12)

        # 3. Check methods
        self.assertEqual(myobj.get_bits(), 22)
        self.assertEqual(myobj.get_bits(False), 9)

        self.assertEqual(myobj.most(myobj.text, 0), '1')
        self.assertEqual(myobj.most(myobj.text, 1), '0')
        self.assertEqual(myobj.most(myobj.text, 2), '1')
        self.assertEqual(myobj.most(myobj.text, 3), '1')
        self.assertEqual(myobj.most(myobj.text, 4), '0')

        self.assertEqual(myobj.handle_ties('0', '1'), '0')
        self.assertEqual(myobj.handle_ties('=', '1'), '1')
        self.assertEqual(myobj.handle_ties('1', '1'), '1')

        self.assertEqual(len(myobj.keep(myobj.text, '1', 0)), 7)
        self.assertEqual(len(myobj.keep(myobj.text, '0', 0)), 5)

        self.assertEqual(myobj.keep_one(), 23)
        self.assertEqual(myobj.keep_one(False), 10)

    def test_part_one(self):
        "Test part one example of Diagnostic object"

        # 1. Create Diagnostic object from text
        myobj = diagnostic.Diagnostic(text=aoc_03.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Diagnostic object"

        # 1. Create Diagnostic object from text
        myobj = diagnostic.Diagnostic(part2=True, text=aoc_03.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end               t e s t _ d i a g n o s t i c . p y              end
# ======================================================================
