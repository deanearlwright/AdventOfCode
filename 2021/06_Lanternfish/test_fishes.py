# ======================================================================
# Lanternfish
#   Advent of Code 2021 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ f i s h e s . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 06, Lanternfish"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_06
import fishes

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
3,4,3,1,2
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 5934
PART_TWO_RESULT = 26984457539

# ======================================================================
#                                                             TestFishes
# ======================================================================


class TestFishes(unittest.TestCase):  # pylint: disable=R0904
    "Test Fishes object"

    def test_empty_init(self):
        "Test the default Fishes creation"

        # 1. Create default Fishes object
        myobj = fishes.Fishes()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.fishes), 0)
        self.assertEqual(myobj.day, 0)
        self.assertEqual(len(myobj.fish_timer), 9)

    def test_text_init(self):
        "Test the Fishes object creation from text"

        # 1. Create Fishes object from text
        myobj = fishes.Fishes(text=aoc_06.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(len(myobj.fishes), 5)
        self.assertEqual(myobj.day, 0)
        self.assertEqual(len(myobj.fish_timer), 9)

        # 3. Check methods
        self.assertEqual(myobj.go_until(18), 26)
        self.assertEqual(myobj.go_until(80), 5934)

    def test_text_init_two(self):
        "Test the Fishes object creation from text"

        # 1. Create Fishes object from text
        myobj = fishes.Fishes(text=aoc_06.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(len(myobj.fishes), 5)
        self.assertEqual(myobj.day, 0)
        self.assertEqual(len(myobj.fish_timer), 9)

        # 3. Check methods
        self.assertEqual(myobj.go_until_two(18), 26)
        self.assertEqual(myobj.go_until_two(80), 5934)

    def test_part_one(self):
        "Test part one example of Fishes object"

        # 1. Create Fishes object from text
        myobj = fishes.Fishes(text=aoc_06.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Fishes object"

        # 1. Create Fishes object from text
        myobj = fishes.Fishes(part2=True, text=aoc_06.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ f i s h e s . p y                  end
# ======================================================================
