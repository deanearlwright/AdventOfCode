# ======================================================================
# Operation Order
#   Advent of Code 2020 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ h o m e w o r k . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 18, Operation Order"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_18
import homework

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 26 + 437 + 12240 + 13632
PART_TWO_RESULT = 46 + 1445 + 669060 + 23340

# ======================================================================
#                                                           TestHomework
# ======================================================================


class TestHomework(unittest.TestCase):  # pylint: disable=R0904
    "Test Homework object"

    def test_empty_init(self):
        "Test the default Homework creation"

        # 1. Create default Homework object
        myobj = homework.Homework()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Homework object creation from text"

        # 1. Create Homework object from text
        myobj = homework.Homework(text=aoc_18.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)

    def test_part_one(self):
        "Test part one example of Homework object"

        # 1. Create Homework object from text
        myobj = homework.Homework(text=aoc_18.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Homework object"

        # 1. Create Homework object from text
        myobj = homework.Homework(part2=True, text=aoc_18.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ h o m e w o r k . p y                end
# ======================================================================
