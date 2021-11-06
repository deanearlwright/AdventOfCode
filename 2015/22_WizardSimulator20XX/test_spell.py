# ======================================================================
# Wizard Simulator 20XX
#   Advent of Code 2015 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s p e l l . p y
# ======================================================================
"Test Spell for Advent of Code 2015 day 22, Wizard Simulator 20XX"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import spell
import player

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "Shield, 113, 6, 6, 0, 7, 0"

# ======================================================================
#                                                              TestSpell
# ======================================================================


class TestSpell(unittest.TestCase):  # pylint: disable=R0904
    "Test Spell object"

    def test_empty_init(self):
        "Test the default Spell creation"

        # 1. Create default Shop object
        myobj = spell.Spell()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.name, "None")
        self.assertEqual(myobj.cost, 9999)
        self.assertEqual(myobj.turns, 0)
        self.assertEqual(myobj.damage, 0)
        self.assertEqual(myobj.heal, 0)
        self.assertEqual(myobj.armor, 0)
        self.assertEqual(myobj.mana, 0)

        # 3. Check methods
        self.assertEqual(str(myobj), "None, 9999, 0, 0, 0, 0, 0")

    def test_text_init(self):
        "Test Spell creation from text"

        # 1. Create default Shop object
        myobj = spell.Spell(text=EXAMPLE_TEXT)

        # 2. Make sure it has the default values
        self.assertEqual(myobj.name, "Shield")
        self.assertEqual(myobj.cost, 113)
        self.assertEqual(myobj.turns, 6)
        self.assertEqual(myobj.damage, 6)
        self.assertEqual(myobj.heal, 0)
        self.assertEqual(myobj.armor, 7)
        self.assertEqual(myobj.mana, 0)

        # 3. Check methods
        self.assertEqual(str(myobj), "Shield, 113, 6, 6, 0, 7, 0")
        player_1 = player.Player(name="P1")
        player_2 = player.Player(name="P2")
        act = myobj.cast(player_1, player_2)
        self.assertEqual(player_1["used"], 113)
        self.assertNotEqual(act, None)
        self.assertEqual(act.name, myobj.name)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ s p e l l . p y                   end
# ======================================================================
