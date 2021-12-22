# ======================================================================
# Dirac Dice
#   Advent of Code 2021 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p l a y e r . p y
# ======================================================================
"Test Player for Advent of Code 2021 day 21, Dirac Dice"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import player

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "Player 1 starting position: 4"

# ======================================================================
#                                                             TestPlayer
# ======================================================================


class TestPlayer(unittest.TestCase):  # pylint: disable=R0904
    "Test Player object"

    def test_empty_init(self):
        "Test the default Player creation"

        # 1. Create default Player object
        myobj = player.Player()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.number, 0)
        self.assertEqual(myobj.position, 0)
        self.assertEqual(myobj.score, 0)
        self.assertEqual(myobj.wins, 0)

    def test_text_init(self):
        "Test the Player object creation from text"

        # 1. Create Player object from text
        myobj = player.Player(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 29)
        self.assertEqual(myobj.number, 1)
        self.assertEqual(myobj.position, 3)
        self.assertEqual(myobj.score, 0)
        self.assertEqual(myobj.wins, 0)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ p l a y e r . p y                  end
# ======================================================================
