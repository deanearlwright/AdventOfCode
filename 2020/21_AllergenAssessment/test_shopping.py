# ======================================================================
# Allergen Assessment
#   Advent of Code 2020 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s h o p p i n g . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 21, Allergen Assessment"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_21
import shopping

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 5
PART_TWO_RESULT = 'mxmxvkd,sqjhc,fvjkl'

# ======================================================================
#                                                           TestShopping
# ======================================================================


class TestShopping(unittest.TestCase):  # pylint: disable=R0904
    "Test Shopping object"

    def test_empty_init(self):
        "Test the default Shopping creation"

        # 1. Create default Shopping object
        myobj = shopping.Shopping()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.labels, [])
        self.assertEqual(len(myobj.ingredients), 0)
        self.assertEqual(len(myobj.allergens), 0)
        self.assertEqual(len(myobj.mapping), 0)

    def test_text_init(self):
        "Test the Shopping object creation from text"

        # 1. Create Shopping object from text
        myobj = shopping.Shopping(text=aoc_21.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(len(myobj.labels), 4)
        self.assertEqual(len(myobj.mapping), 3)
        self.assertEqual(myobj.mapping['soy'], set(['sqjhc', 'fvjkl']))

    def test_part_one(self):
        "Test part one example of Shopping object"

        # 1. Create Shopping object from text
        myobj = shopping.Shopping(text=aoc_21.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Shopping object"

        # 1. Create Shopping object from text
        myobj = shopping.Shopping(part2=True, text=aoc_21.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ s h o p p i n g . p y                end
# ======================================================================
