
# ======================================================================
# Scratchcards
#   Advent of Code 2023 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s o l v e r . p y
# ======================================================================
"Test solver for Advent of Code 2023 day 04, Scratchcards"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_04
import solver

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 13
PART_TWO_RESULT = 30

# ======================================================================
#                                                             TestSolver
# ======================================================================


class TestSolver(unittest.TestCase):  # pylint: disable=R0904
    "Test Solver object"

    def test_empty_init(self):
        "Test the default Solver creation"

        # 1. Create default Solver object
        myobj = solver.Solver()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.cards), 0)

    def test_text_init(self):
        "Test the Solver object creation from text"

        # 1. Create Solver object from text
        myobj = solver.Solver(text=aoc_04.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(len(myobj.cards), 6)

        # 3. Check methods
        self.assertEqual(len(myobj.cards[0].matches()), 4)
        self.assertEqual(myobj.cards[0].score(), 8)
        self.assertEqual(len(myobj.cards[1].matches()), 2)
        self.assertEqual(myobj.cards[1].score(), 2)

        self.assertEqual(myobj.cards_for_card(5), 1)
        self.assertEqual(myobj.cards_for_card(4), 1)
        self.assertEqual(myobj.cards_for_card(3), 2)
        self.assertEqual(myobj.cards_for_card(2), 4)
        self.assertEqual(myobj.cards_for_card(1), 7)
        self.assertEqual(myobj.cards_for_card(0), 15)

    def test_part_one(self):
        "Test part one example of Solver object"

        # 1. Create Solver object from text
        text = aoc_04.from_text(PART_ONE_TEXT)
        myobj = solver.Solver(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Solver object"

        # 1. Create Solver object from text
        text = aoc_04.from_text(PART_TWO_TEXT)
        myobj = solver.Solver(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ s o l v e r . p y                end
# ======================================================================
