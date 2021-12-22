# ======================================================================
# Dirac Dice
#   Advent of Code 2021 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ g a m e . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 21, Dirac Dice"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_21
import game

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
Player 1 starting position: 4
Player 2 starting position: 8
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 739785
PART_TWO_RESULT = 444356092776315

# ======================================================================
#                                                              TestGame
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
        self.assertEqual(len(myobj.track), 10)
        self.assertEqual(myobj.track[0], 1)
        self.assertEqual(myobj.track[-1], 10)
        self.assertEqual(myobj.players, [])
        self.assertEqual(myobj.die, None)
        self.assertEqual(myobj.goal, 1000)
        self.assertEqual(myobj.times, 3)

    def test_text_init(self):
        "Test the Game object creation from text"

        # 1. Create Game object from text
        myobj = game.Game(text=aoc_21.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 2)
        self.assertEqual(len(myobj.track), 10)
        self.assertEqual(myobj.track[0], 1)
        self.assertEqual(myobj.track[-1], 10)
        self.assertEqual(len(myobj.players), 2)
        self.assertEqual(myobj.players[0].number, 1)
        self.assertEqual(myobj.players[0].position, 3)
        self.assertEqual(myobj.players[0].score, 0)
        self.assertEqual(myobj.players[1].number, 2)
        self.assertEqual(myobj.players[1].position, 7)
        self.assertEqual(myobj.players[1].score, 0)
        self.assertEqual(myobj.die.sides, 100)
        self.assertEqual(myobj.goal, 1000)
        self.assertEqual(myobj.times, 3)

        # 3. Check methods
        myobj.full_turn()
        self.assertEqual(myobj.players[0].number, 1)
        self.assertEqual(myobj.players[0].position, 9)
        self.assertEqual(myobj.players[0].score, 10)
        self.assertEqual(myobj.players[1].number, 2)
        self.assertEqual(myobj.players[1].position, 2)
        self.assertEqual(myobj.players[1].score, 3)
        myobj.full_turn()
        self.assertEqual(myobj.players[0].number, 1)
        self.assertEqual(myobj.players[0].position, 3)
        self.assertEqual(myobj.players[0].score, 14)
        self.assertEqual(myobj.players[1].number, 2)
        self.assertEqual(myobj.players[1].position, 5)
        self.assertEqual(myobj.players[1].score, 9)

    def test_part_one(self):
        "Test part one example of Game object"

        # 1. Create Game object from text
        myobj = game.Game(text=aoc_21.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Game object"

        # 1. Create Game object from text
        myobj = game.Game(part2=True, text=aoc_21.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ g a m e . p y                end
# ======================================================================
