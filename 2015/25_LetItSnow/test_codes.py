# ======================================================================
# Let It Snow
#   Advent of Code 2015 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c o d e s . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 25, Let It Snow"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_25
import codes

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
To continue, please consult the code grid in the manual.  Enter the code at row 4, column 6.
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = ""

PART_ONE_RESULT = 31527494
PART_TWO_RESULT = None

# ======================================================================
#                                                              TestCodes
# ======================================================================


class TestCodes(unittest.TestCase):  # pylint: disable=R0904
    "Test Codes object"

    def test_empty_init(self):
        "Test the default Codes creation"

        # 1. Create default Codes object
        myobj = codes.Codes()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.row, 0)
        self.assertEqual(myobj.col, 0)

        # 3. Check methods
        self.assertEqual(myobj.next_code(20151125), 31916031)
        self.assertEqual(myobj.next_code(31916031), 18749137)
        self.assertEqual(myobj.next_code(18749137), 16080970)

        self.assertEqual(myobj.first_order(1), 1)
        self.assertEqual(myobj.first_order(2), 2)
        self.assertEqual(myobj.first_order(3), 4)
        self.assertEqual(myobj.first_order(4), 7)
        self.assertEqual(myobj.first_order(5), 11)
        self.assertEqual(myobj.first_order(6), 16)

        self.assertEqual(myobj.order(1, 1), 1)
        self.assertEqual(myobj.order(2, 1), 2)
        self.assertEqual(myobj.order(3, 1), 4)
        self.assertEqual(myobj.order(1, 2), 3)
        self.assertEqual(myobj.order(4, 3), 18)
        self.assertEqual(myobj.order(1, 6), 21)

        self.assertEqual(myobj.code(1, 1), 20151125)
        self.assertEqual(myobj.code(2, 1), 31916031)
        self.assertEqual(myobj.code(3, 1), 16080970)
        self.assertEqual(myobj.code(1, 2), 18749137)
        self.assertEqual(myobj.code(4, 3), 21345942)
        self.assertEqual(myobj.code(1, 6), 33511524)

    def test_text_init(self):
        "Test the Codes object creation from text"

        # 1. Create Codes object from text
        myobj = codes.Codes(text=aoc_25.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(myobj.row, 4)
        self.assertEqual(myobj.col, 6)

    def test_part_one(self):
        "Test part one example of Codes object"

        # 1. Create Codes object from text
        myobj = codes.Codes(text=aoc_25.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Codes object"

        # 1. Create Codes object from text
        myobj = codes.Codes(part2=True, text=aoc_25.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ c o d e s . p y                   end
# ======================================================================
