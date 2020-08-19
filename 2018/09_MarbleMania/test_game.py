# ======================================================================
# Marble Mania
#   Advent of Code 2018 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ g a m e . p y
# ======================================================================
"Test solver for Advent of Code 2018 day 09, Marble Mania"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_09
import game

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
9 players; last marble is worth 25 points
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 32
PART_TWO_RESULT = 22563

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
        self.assertEqual(myobj.num_players, 0)
        self.assertEqual(myobj.last_marble, 0)
        self.assertEqual(myobj.current_marble, 0)
        self.assertEqual(myobj.current_player, None)
        self.assertEqual(len(myobj.circle), 1)
        self.assertEqual(myobj.circle[0], 0)
        self.assertEqual(len(myobj.players), 0)
        self.assertEqual(myobj.highest_score(), 0)


    def test_text_init(self):
        "Test the Game object creation from text"

        # 1. Create Game object from text
        myobj = game.Game(text=aoc_09.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(myobj.num_players, 9)
        self.assertEqual(myobj.last_marble, 25)
        self.assertEqual(myobj.current_marble, 0)
        self.assertEqual(myobj.current_player, None)
        self.assertEqual(len(myobj.circle), 1)
        self.assertEqual(myobj.circle[0], 0)
        self.assertEqual(len(myobj.players), 9)
        self.assertEqual(myobj.highest_score(), 0)

        # 3. Walk through the example
        self.assertEqual(myobj.next_marble(), 1)
        self.assertEqual(myobj.current_marble, 1)
        self.assertEqual(myobj.next_player(), 0)
        myobj.place_marble()
        self.assertEqual(len(myobj.circle), 2)
        self.assertEqual(list(myobj.circle), [0, 1])

        self.assertEqual(myobj.next_marble(), 2)
        self.assertEqual(myobj.current_marble, 2)
        self.assertEqual(myobj.next_player(), 1)
        myobj.place_marble()
        self.assertEqual(len(myobj.circle), 3)
        self.assertEqual(list(myobj.circle), [1, 0, 2])

        self.assertEqual(myobj.next_marble(), 3)
        self.assertEqual(myobj.current_marble, 3)
        self.assertEqual(myobj.next_player(), 2)
        myobj.place_marble()
        self.assertEqual(len(myobj.circle), 4)
        self.assertEqual(list(myobj.circle), [0, 2, 1, 3])

        self.assertEqual(myobj.next_marble(), 4)
        self.assertEqual(myobj.current_marble, 4)
        self.assertEqual(myobj.next_player(), 3)
        myobj.place_marble()
        self.assertEqual(len(myobj.circle), 5)
        self.assertEqual(list(myobj.circle), [2, 1, 3, 0, 4])

        self.assertEqual(myobj.next_marble(), 5)
        self.assertEqual(myobj.current_marble, 5)
        self.assertEqual(myobj.next_player(), 4)
        myobj.place_marble()
        self.assertEqual(len(myobj.circle), 6)
        self.assertEqual(list(myobj.circle), [1, 3, 0, 4, 2, 5])

        self.assertEqual(myobj.next_marble(), 6)
        self.assertEqual(myobj.current_marble, 6)
        self.assertEqual(myobj.next_player(), 5)
        myobj.place_marble()
        self.assertEqual(len(myobj.circle), 7)
        self.assertEqual(list(myobj.circle), [3, 0, 4, 2, 5, 1, 6])

        self.assertEqual(myobj.next_marble(), 7)
        self.assertEqual(myobj.current_marble, 7)
        self.assertEqual(myobj.next_player(), 6)
        myobj.place_marble()
        self.assertEqual(len(myobj.circle), 8)
        self.assertEqual(list(myobj.circle), [0, 4, 2, 5, 1, 6, 3, 7])

        myobj.game_turn()
        myobj.game_turn()
        myobj.game_turn()
        myobj.game_turn()
        myobj.game_turn()
        myobj.game_turn()
        myobj.game_turn()
        myobj.game_turn()
        myobj.game_turn()
        myobj.game_turn()
        self.assertEqual(myobj.current_marble, 17)
        self.assertEqual(len(myobj.circle), 18)
        self.assertEqual(list(myobj.circle), [4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15, 0, 16, 8, 17])
        self.assertEqual(myobj.highest_score(), 0)

        myobj.game_turn()
        myobj.game_turn()
        myobj.game_turn()
        myobj.game_turn()
        myobj.game_turn()
        self.assertEqual(myobj.current_marble, 22)
        self.assertEqual(len(myobj.circle), 23)
        self.assertEqual(list(myobj.circle), [11, 1, 12, 6, 13, 3, 14, 7, 15, 0, 16, 8, 17, 4, 18, 9, 19, 2, 20, 10, 21, 5, 22])
        self.assertEqual(myobj.highest_score(), 0)

        myobj.game_turn()
        self.assertEqual(myobj.current_marble, 23)
        self.assertEqual(len(myobj.circle), 22)
        self.assertEqual(list(myobj.circle), [2, 20, 10, 21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15, 0, 16, 8, 17, 4, 18, 19])
        self.assertEqual(myobj.highest_score(), 32)

        myobj.game_turn()
        myobj.game_turn()
        self.assertEqual(myobj.current_marble, 25)
        self.assertEqual(len(myobj.circle), 24)
        self.assertEqual(list(myobj.circle), [10, 21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15, 0, 16, 8, 17, 4, 18, 19, 2, 24, 20, 25])
        self.assertEqual(myobj.highest_score(), 32)
        self.assertEqual(myobj.players[4], 32)
        self.assertEqual(myobj.game_turn(), None)


    def test_example_30_35_40(self):
        "Test the part one example but let the game go a little longer"
        myobj = game.Game(text=["9 players; last marble is worth 30 points"])
        self.assertEqual(myobj.num_players, 9)
        self.assertEqual(myobj.last_marble, 30)
        self.assertEqual(myobj.part_one(verbose=False), 32)
        self.assertEqual(myobj.current_marble, 30)
        self.assertEqual(len(myobj.circle), 29)
        #self.assertEqual(myobj.circle, [0, 16, 8, 17, 4, 18, 19, 2, 24, 20, 25, 10, 21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15])

        myobj = game.Game(text=["9 players; last marble is worth 35 points"])
        self.assertEqual(myobj.num_players, 9)
        self.assertEqual(myobj.last_marble, 35)
        self.assertEqual(myobj.part_one(verbose=False), 32)
        self.assertEqual(myobj.current_marble, 35)
        self.assertEqual(len(myobj.circle), 34)

        myobj = game.Game(text=["9 players; last marble is worth 38 points"])
        self.assertEqual(myobj.num_players, 9)
        self.assertEqual(myobj.last_marble, 38)
        self.assertEqual(myobj.part_one(verbose=False), 32)
        self.assertEqual(myobj.current_marble, 38)
        self.assertEqual(len(myobj.circle), 37)
        self.assertEqual(list(myobj.circle), [0, 16, 8, 17, 4, 18, 19, 2, 24, 20, 25, 10, 26, 21, 27, 5, 28, 22, 29, 11, 30, 1, 31, 12, 32, 6, 33, 13, 34, 3, 35, 14, 36, 7, 37, 15, 38])

    def test_examples(self):
        "Test several example games"
        #   - 10 players; last marble is worth 1618 points: high score is 8317
        #   - 13 players; last marble is worth 7999 points: high score is 146373
        #   - 17 players; last marble is worth 1104 points: high score is 2764
        #   - 21 players; last marble is worth 6111 points: high score is 54718
        #   - 30 players; last marble is worth 5807 points: high score is 37305
        myobj = game.Game(text=["10 players; last marble is worth 1618 points"])
        self.assertEqual(myobj.num_players, 10)
        self.assertEqual(myobj.last_marble, 1618)
        self.assertEqual(myobj.part_one(verbose=False), 8317)
        myobj = game.Game(text=["13 players; last marble is worth 7999 points"])
        self.assertEqual(myobj.part_one(verbose=False), 146373)
        myobj = game.Game(text=["17 players; last marble is worth 1104 points"])
        self.assertEqual(myobj.part_one(verbose=False), 2764)
        myobj = game.Game(text=["21 players; last marble is worth 6111 points"])
        self.assertEqual(myobj.part_one(verbose=False), 54718)
        myobj = game.Game(text=["30 players; last marble is worth 5807 points"])
        self.assertEqual(myobj.part_one(verbose=False), 37305)

    def test_part_one(self):
        "Test part one example of Game object"

        # 1. Create Game object from text
        myobj = game.Game(text=aoc_09.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Game object"

        # 1. Create Game object from text
        myobj = game.Game(part2=True, text=aoc_09.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      t e s t _ g a m e . p y                   end
# ======================================================================
