# ======================================================================
# Binary Boarding
#   Advent of Code 2020 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      t e s t _ b p a s s . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 05, Binary Boarding"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import bpass

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "FBFBBFFRLR"
EXAMPLES = [
    {'text': 'BFFFBBFRRR', 'row': 70, 'column': 7, 'seat': 567},
    {'text': 'FFFBBBFRRR', 'row': 14, 'column': 7, 'seat': 119},
    {'text': 'BBFFBBFRLL', 'row': 102, 'column': 4, 'seat': 820},
]

# ======================================================================
#                                                              TestBpass
# ======================================================================


class TestBpass(unittest.TestCase):  # pylint: disable=R0904
    "Test Boarding Pass object"

    def test_empty_init(self):
        "Test the default Bpass creation"

        # 1. Create default Boarding Pass object
        myobj = bpass.Bpass()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.row, None)
        self.assertEqual(myobj.column, None)
        self.assertEqual(myobj.seat, None)

    def test_text_init(self):
        "Test the Boarding Pass object creation from text"

        # 1. Create Boarding Pass object from text
        myobj = bpass.Bpass(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, EXAMPLE_TEXT)
        self.assertEqual(myobj.row, 44)
        self.assertEqual(myobj.column, 5)
        self.assertEqual(myobj.seat, 357)

    def test_part_one(self):
        "Test part one example of Boarding Pass object"

        # 1. Loop for all of the examples
        for example in EXAMPLES:

            # 2. Create Boarding Pass object from text
            myobj = bpass.Bpass(text=example['text'])

            # 3. Check the part one result
            self.assertEqual(myobj.row, example['row'])
            self.assertEqual(myobj.column, example['column'])
            self.assertEqual(myobj.seat, example['seat'])


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ b p a s s . p y                   end
# ======================================================================
