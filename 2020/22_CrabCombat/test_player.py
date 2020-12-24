# ======================================================================
# Crab Combat
#   Advent of Code 2020 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p l a y e r . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 22, Crab Combat"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import player

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE = {'number': 1, 'cards': [9, 2, 6, 3, 1]}

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
        self.assertEqual(myobj.number, 0)
        self.assertEqual(len(myobj.cards), 0)

    def test_text_init(self):
        "Test the Player object creation from text"

        # 1. Create Player object from text
        myobj = player.Player(number=EXAMPLE['number'], cards=EXAMPLE['cards'])

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.number, 1)
        self.assertEqual(len(myobj.cards), 5)

        # 3. Test methods
        self.assertEqual(myobj.score(), 45 + 8 + 18 + 6 + 1)
        self.assertEqual(myobj.get_top_card(), 9)
        self.assertEqual(len(myobj.cards), 4)
        myobj.keep(9, 5)
        self.assertEqual(len(myobj.cards), 6)
        self.assertEqual(myobj.score(), 12 + 30 + 12 + 3 + 18 + 5)
        self.assertEqual(myobj.lost(), False)
        self.assertEqual(myobj.get_top_card(), 2)
        self.assertEqual(myobj.get_top_card(), 6)
        self.assertEqual(myobj.get_top_card(), 3)
        self.assertEqual(myobj.get_top_card(), 1)
        self.assertEqual(myobj.get_top_card(), 9)
        self.assertEqual(myobj.get_top_card(), 5)
        self.assertEqual(myobj.get_top_card(), None)
        self.assertEqual(myobj.get_top_card(), None)
        self.assertEqual(myobj.lost(), True)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ p l a y e r . py                 end
# ======================================================================
