
# ======================================================================
# Cube Conundrum
#   Advent of Code 2023 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ g a m e . p y
# ======================================================================
"Test Game for Advent of Code 2023 day 02, Cube Conundrum"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import game

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

# ======================================================================
#                                                             TestGame
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
        self.assertEqual(myobj.id, 0)
        self.assertEqual(len(myobj.pulls), 0)
        self.assertEqual(len(myobj.max), 3)

    def test_text_init(self):
        "Test the Game object creation from text"

        # 1. Create Game object from text
        myobj = game.Game(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 54)
        self.assertEqual(myobj.id, 1)
        self.assertEqual(len(myobj.pulls), 3)
        self.assertEqual(len(myobj.max), 3)
        self.assertEqual(myobj.max["red"], 4)
        self.assertEqual(myobj.max["green"], 2)
        self.assertEqual(myobj.max["blue"], 6)

        # 3. Check methods
        self.assertEqual(myobj.possible(12, 13, 14), True)
        self.assertEqual(myobj.possible(5, 5, 5), False)
        self.assertEqual(myobj.power_set(), 48)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ g a m e . p y                end
# ======================================================================
