# ======================================================================
# Crab Combat
#   Advent of Code 2020 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ g a m e . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 22, Crab Combat"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_22
import game

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""
IGP_TEXT = """
Player 1:
43
19

Player 2:
2
29
14
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 306
PART_TWO_RESULT = 291

# ======================================================================
#                                                               TestGame
# ======================================================================


class TestGame(unittest.TestCase):  # pylint: disable=R0904
    "Test Game object"

    def test_empty_init(self):
        "Test the default Game creation"

        # 1. Create default Game object
        myobj = game.Game()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.players), 0)

    def test_text_init(self):
        "Test the Game object creation from text"

        # 1. Create Game object from text
        myobj = game.Game(text=aoc_22.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 12)
        self.assertEqual(len(myobj.players), 2)

    def test_part_one(self):
        "Test part one example of Game object"

        # 1. Create Game object from text
        myobj = game.Game(text=aoc_22.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two_infinite_game_prevention(self):
        "Test infinate game prevention for part two"

        # 1. Create Game object from text
        myobj = game.Game(part2=True, text=aoc_22.from_text(IGP_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False, limit=100), 86 + 19)

    def test_part_two(self):
        "Test part two example of Game object"

        # 1. Create Game object from text
        myobj = game.Game(part2=True, text=aoc_22.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False, limit=100), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      t e s t _ g a m e . p y                   end
# ======================================================================
