
# ======================================================================
# Monkey Market
#   Advent of Code 2024 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ m a r k e t . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 22, Monkey Market"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_22
import market

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
1
10
100
2024
"""
EXAMPLE_TWO = """
1
2
3
2024
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TWO

PART_ONE_RESULT = 37327623
PART_TWO_RESULT = 23

# ======================================================================
#                                                             TestMarket
# ======================================================================


class TestMarket(unittest.TestCase):  # pylint: disable=R0904
    "Test Market object"

    def test_empty_init(self):
        "Test the default Market creation"

        # 1. Create default Market object
        myobj = market.Market()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Market object creation from text"

        # 1. Create Market object from text
        myobj = market.Market(text=aoc_22.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)

        # 3. Check methods
        myobj.evolve_all()
        self.assertEqual(myobj.secret_sum(), 37327623)

    def test_text_Two(self):
        "Test the Market object creation from text"

        # 1. Create Market object from text
        myobj = market.Market(text=aoc_22.from_text(EXAMPLE_TWO), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 4)

        # 3. Check methods
        myobj.evolve_all()
        self.assertEqual(myobj.secret_sum(), 37990510)
        self.assertEqual(myobj.total_bananas((-2, 1, -1, 3)), 23)
        self.assertEqual(myobj.best_delta(), (-2, 1, -1, 3))

    def test_part_one(self):
        "Test part one example of Market object"

        # 1. Create Market object from text
        text = aoc_22.from_text(PART_ONE_TEXT)
        myobj = market.Market(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Market object"

        # 1. Create Market object from text
        text = aoc_22.from_text(PART_TWO_TEXT)
        myobj = market.Market(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ m a r k e t . p y                  end
# ======================================================================
