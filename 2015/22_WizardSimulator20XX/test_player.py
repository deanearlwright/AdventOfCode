# ======================================================================
# Wizard Simulator 20XX
#   Advent of Code 2015 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p l a y e r . p y
# ======================================================================
"Test Player for Advent of Code 2015 day 22, Wizard Simulator 20XX"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_22
import player

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
Hit Points: 10
Damage: 0
Armor: 0
Mana: 250
"""

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
        self.assertEqual(myobj.name, 'noone')
        self.assertEqual(len(myobj.attributes), 4)
        self.assertEqual(myobj.attributes['hitpoints'], 50)
        self.assertEqual(myobj.attributes['damage'], 0)
        self.assertEqual(myobj.attributes['armor'], 0)
        self.assertEqual(myobj.attributes['mana'], 500)

    def test_text_init(self):
        "Test the Player object creation from text"

        # 1. Create Player object from text
        myobj = player.Player(text=aoc_22.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(myobj.name, 'noone')
        self.assertEqual(len(myobj.attributes), 4)
        self.assertEqual(myobj.attributes['hitpoints'], 10)
        self.assertEqual(myobj.attributes['damage'], 7)
        self.assertEqual(myobj.attributes['armor'], 2)
        self.assertEqual(myobj.attributes['mana'], 250)

        # 3. Check methods
        self.assertEqual(myobj.is_dead(), False)
        self.assertEqual(myobj['hitpoints'], 12)
        self.assertEqual(myobj['damage'], 7)
        self.assertEqual(myobj['armor'], 2)
        myobj['hitpoints'] = 0
        self.assertEqual(myobj.attributes['hitpoints'], 0)
        self.assertEqual(myobj['hitpoints'], 0)
        self.assertEqual(myobj.is_dead(), True)
        myobj['hitpoints'] = 12
        myobj.defend(5)
        self.assertEqual(myobj['hitpoints'], 9)
        self.assertEqual(myobj.is_dead(), False)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ p l a y e r . p y                  end
# ======================================================================
