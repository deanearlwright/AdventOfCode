# ======================================================================
# No Such Thing as Too Much
#   Advent of Code 2015 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ e g g n o g . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 17, No Such Thing as Too Much"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_17
import eggnog

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
20
15
10
5
5
"""
EXAMPLE_EGGNOG = 25

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 4
PART_TWO_RESULT = 3

# ======================================================================
#                                                             TestEggnog
# ======================================================================


class TestEggnog(unittest.TestCase):  # pylint: disable=R0904
    "Test Eggnog object"

    def test_empty_init(self):
        "Test the default Eggnog creation"

        # 1. Create default Eggnog object
        myobj = eggnog.Eggnog()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.containers, [])

    def test_text_init(self):
        "Test the Eggnog object creation from text"

        # 1. Create Eggnog object from text
        myobj = eggnog.Eggnog(text=aoc_17.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(len(myobj.containers), 5)

        # 3. Check methods
        self.assertEqual(myobj.num_combos(amount=EXAMPLE_EGGNOG), 4)

    def test_part_one(self):
        "Test part one example of Eggnog object"

        # 1. Create Eggnog object from text
        myobj = eggnog.Eggnog(text=aoc_17.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False, amount=EXAMPLE_EGGNOG), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Eggnog object"

        # 1. Create Eggnog object from text
        myobj = eggnog.Eggnog(part2=True, text=aoc_17.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False, amount=EXAMPLE_EGGNOG), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ e g g n o g . p y                  end
# ======================================================================
