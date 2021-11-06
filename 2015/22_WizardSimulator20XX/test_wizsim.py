# ======================================================================
# Wizard Simulator 20XX
#   Advent of Code 2015 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ w i z s i m . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 22, Wizard Simulator 20XX"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import wizsim
import spells

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
WIZARD_TEXT = [
    "Hit Points: 50",
    "Mana: 500",
]

DEMO_WIZARD_TEXT = [
    "Hit Points: 10",
    "Mana: 250",
]

BOSS13_TEXT = [
    "Hit Points: 13",
    "Damage: 8",
]

BOSS14_TEXT = [
    "Hit Points: 14",
    "Damage: 8",
]

PART_ONE_TEXT = ""
PART_TWO_TEXT = ""

PART_ONE_RESULT = 212
PART_TWO_RESULT = 212

# ======================================================================
#                                                             TestWizsim
# ======================================================================


class TestWizsim(unittest.TestCase):  # pylint: disable=R0904
    "Test Wizsim object"

    def test_empty_init(self):
        "Test the default Wizsim creation"

        # 1. Create default Wizsim object
        myobj = wizsim.Wizsim()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.spells), 5)
        self.assertEqual(len(myobj.states), 0)

    def test_text_init(self):
        "Test the Wizsim object creation from text"

        # 1. Create Wizsim object from text
        myobj = wizsim.Wizsim(text=BOSS13_TEXT)
        myobj.initial_state(wizard_text=WIZARD_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 2)
        self.assertEqual(len(myobj.spells), 5)
        self.assertEqual(len(myobj.states), 1)
        self.assertEqual(myobj.states[0].wizard.name, "Wizard")
        self.assertEqual(myobj.states[0].wizard['hitpoints'], 50)
        self.assertEqual(myobj.states[0].wizard['damage'], 0)
        self.assertEqual(myobj.states[0].wizard['mana'], 500)
        self.assertEqual(myobj.states[0].wizard['used'], 0)
        self.assertEqual(myobj.states[0].boss.name, "Boss")
        self.assertEqual(myobj.states[0].boss['hitpoints'], 13)
        self.assertEqual(myobj.states[0].boss['damage'], 8)

        # 3. Reset using demo player
        myobj.initial_state(wizard_text=DEMO_WIZARD_TEXT, boss_text=BOSS13_TEXT)
        self.assertEqual(myobj.states[0].wizard.name, "Wizard")
        self.assertEqual(myobj.states[0].wizard['hitpoints'], 10)
        self.assertEqual(myobj.states[0].wizard['damage'], 0)
        self.assertEqual(myobj.states[0].wizard['mana'], 250)
        self.assertEqual(myobj.states[0].wizard['used'], 0)
        self.assertEqual(myobj.states[0].boss.name, "Boss")
        self.assertEqual(myobj.states[0].boss['hitpoints'], 13)
        self.assertEqual(myobj.states[0].boss['damage'], 8)

        # 4. Cast a Magic Missle
        nxt = myobj.turn(myobj.states[0], myobj.spells.named("Magic Missile"))
        self.assertEqual(nxt.turn, 1)
        self.assertEqual(nxt.wizard.name, "Wizard")
        self.assertEqual(nxt.wizard['hitpoints'], 2)
        self.assertEqual(nxt.wizard['damage'], 0)
        self.assertEqual(nxt.wizard['mana'], 197)
        self.assertEqual(nxt.wizard['used'], 53)
        self.assertEqual(nxt.boss.name, "Boss")
        self.assertEqual(nxt.boss['hitpoints'], 9)
        self.assertEqual(nxt.boss['damage'], 8)

    def test_demo_one(self):
        "Test the Wizsim object using the first demo"

        # 0. All the possible spells
        all_spells = spells.Spells(text=spells.SPELLS)

        # 1. Create Wizsim object from text
        myobj = wizsim.Wizsim(text=BOSS13_TEXT)
        myobj.initial_state(wizard_text=DEMO_WIZARD_TEXT)
        self.assertEqual(myobj.states[0].wizard.name, "Wizard")
        self.assertEqual(myobj.states[0].wizard['hitpoints'], 10)
        self.assertEqual(myobj.states[0].wizard['damage'], 0)
        self.assertEqual(myobj.states[0].wizard['mana'], 250)
        self.assertEqual(myobj.states[0].wizard['used'], 0)
        self.assertEqual(myobj.states[0].boss.name, "Boss")
        self.assertEqual(myobj.states[0].boss['hitpoints'], 13)
        self.assertEqual(myobj.states[0].boss['damage'], 8)

        # 2. Turn 1 -- Player casts Poison.
        # -- Player turn --
        # - Player has 10 hit points, 0 armor, 250 mana
        # - Boss has 13 hit points
        # Player casts Poison
        # -- Boss turn --
        # - Player has 10 hit points, 0 armor, 77 mana
        # - Boss has 13 hit points
        # Poison deals 3 damage; its timer is now 5.
        # Boss attacks for 8 damage.
        self.assertEqual(myobj.states[0].another(all_spells),
                         ['Drain', 'Magic Missile', 'Poison', 'Recharge', 'Shield'])
        nxt = myobj.turn(myobj.states[0], myobj.spells.named("Poison"))
        self.assertEqual(nxt.turn, 1)
        self.assertEqual(nxt.wizard.name, "Wizard")
        self.assertEqual(nxt.wizard['hitpoints'], 2)
        self.assertEqual(nxt.wizard['damage'], 0)
        self.assertEqual(nxt.wizard['mana'], 77)
        self.assertEqual(nxt.wizard['used'], 173)
        self.assertEqual(nxt.boss.name, "Boss")
        self.assertEqual(nxt.boss['hitpoints'], 10)
        self.assertEqual(nxt.boss['damage'], 8)

        # 3. Turn 2 -- Player casts Magic Missle
        # -- Player turn --
        # - Player has 2 hit points, 0 armor, 77 mana
        # - Boss has 10 hit points
        # Poison deals 3 damage; its timer is now 4.
        # Player casts Magic Missile, dealing 4 damage.
        # -- Boss turn --
        # - Player has 2 hit points, 0 armor, 24 mana
        # - Boss has 3 hit points
        # Poison deals 3 damage. This kills the boss, and the player wins.
        self.assertEqual(nxt.another(all_spells),
                         ['Drain', 'Magic Missile'])
        nxt = myobj.turn(nxt, myobj.spells.named("Magic Missile"))
        self.assertEqual(nxt.turn, 2)
        self.assertEqual(nxt.wizard.name, "Wizard")
        self.assertEqual(nxt.wizard['hitpoints'], 2)
        self.assertEqual(nxt.wizard['damage'], 0)
        self.assertEqual(nxt.wizard['mana'], 24)
        self.assertEqual(nxt.wizard['used'], 226)
        self.assertEqual(nxt.boss.name, "Boss")
        self.assertEqual(nxt.boss['hitpoints'], 0)
        self.assertEqual(nxt.boss['damage'], 8)

    def test_demo_two(self):  # pylint: disable=too-many-statements
        "Test the Wizsim object using the second demo"

        # 0. All the possible spells
        all_spells = spells.Spells(text=spells.SPELLS)

        # 1. Create Wizsim object from text
        myobj = wizsim.Wizsim(text=BOSS14_TEXT)
        myobj.initial_state(wizard_text=DEMO_WIZARD_TEXT)
        self.assertEqual(myobj.states[0].wizard['hitpoints'], 10)
        self.assertEqual(myobj.states[0].wizard['mana'], 250)
        self.assertEqual(myobj.states[0].wizard['used'], 0)
        self.assertEqual(myobj.states[0].boss['hitpoints'], 14)

        # 2. Turn 1 -- Player casts recharge
        # -- Player turn --
        # - Player has 10 hit points, 0 armor, 250 mana
        # - Boss has 14 hit points
        # Player casts Recharge.
        # -- Boss turn --
        # - Player has 10 hit points, 0 armor, 21 mana
        # - Boss has 14 hit points
        # Recharge provides 101 mana; its timer is now 4.
        # Boss attacks for 8 damage!
        self.assertEqual(myobj.states[0].another(all_spells),
                         ['Drain', 'Magic Missile', 'Poison', 'Recharge', 'Shield'])
        nxt = myobj.turn(myobj.states[0], myobj.spells.named("Recharge"))
        self.assertEqual(nxt.turn, 1)
        self.assertEqual(nxt.wizard['hitpoints'], 2)
        self.assertEqual(nxt.wizard['mana'], 122)
        self.assertEqual(nxt.wizard['used'], 229)
        self.assertEqual(nxt.boss['hitpoints'], 14)
        self.assertEqual(nxt.active.named("Recharge").turns, 4)

        # 3. Turn 2 -- Player casts Shield
        # -- Player turn --
        # - Player has 2 hit points, 0 armor, 122 mana
        # - Boss has 14 hit points
        # Recharge provides 101 mana; its timer is now 3.
        # Player casts Shield, increasing armor by 7.
        # -- Boss turn --
        # - Player has 2 hit points, 7 armor, 110 mana
        # - Boss has 14 hit points
        # Shield's timer is now 5.
        # Recharge provides 101 mana; its timer is now 2.
        # Boss attacks for 8 - 7 = 1 damage!
        self.assertEqual(nxt.another(all_spells),
                         ['Drain', 'Magic Missile', 'Shield'])
        nxt = myobj.turn(nxt, myobj.spells.named("Shield"))
        self.assertEqual(nxt.turn, 2)
        self.assertEqual(nxt.wizard['hitpoints'], 1)
        self.assertEqual(nxt.wizard['mana'], 122 + 101 + 101 - 113)  # 211
        self.assertEqual(nxt.wizard['used'], 229 + 113)  # 342
        self.assertEqual(nxt.boss['hitpoints'], 14)
        self.assertEqual(nxt.active.named("Recharge").turns, 2)
        self.assertEqual(nxt.active.named("Shield").turns, 5)

        # 4. Turn 3 -- Player casts Drain
        # -- Player turn --
        # - Player has 1 hit point, 7 armor, 211 mana
        # - Boss has 14 hit points
        # Shield's timer is now 4.
        # Recharge provides 101 mana; its timer is now 1.
        # Player casts Drain, dealing 2 damage, and healing 2 hit points.
        # -- Boss turn --
        # - Player has 3 hit points, 7 armor, 239 mana
        # - Boss has 12 hit points
        # Shield's timer is now 3.
        # Recharge provides 101 mana; its timer is now 0.
        # Recharge wears off.
        # Boss attacks for 8 - 7 = 1 damage!
        self.assertEqual(nxt.another(all_spells),
                         ['Drain', 'Magic Missile', 'Poison'])
        nxt = myobj.turn(nxt, myobj.spells.named("Drain"))
        self.assertEqual(nxt.turn, 3)
        self.assertEqual(nxt.wizard['hitpoints'], 2)
        self.assertEqual(nxt.wizard['armor'], 7)
        self.assertEqual(nxt.wizard['mana'], 211 + 101 + 101 - 73)  # 340
        self.assertEqual(nxt.wizard['used'], 229 + 113 + 73)  # 415
        self.assertEqual(nxt.boss['hitpoints'], 12)
        self.assertEqual(nxt.active.named("Recharge").turns, 0)
        self.assertEqual(nxt.active.named("Shield").turns, 3)

        # 5. Turn 4 -- Player casts Poison
        # -- Player turn --
        # - Player has 2 hit points, 7 armor, 340 mana
        # - Boss has 12 hit points
        # Shield's timer is now 2.
        # Player casts Poison.
        # -- Boss turn --
        # - Player has 2 hit points, 7 armor, 167 mana
        # - Boss has 12 hit points
        # Shield's timer is now 1.
        # Poison deals 3 damage; its timer is now 5.
        # Boss attacks for 8 - 7 = 1 damage!
        self.assertEqual(nxt.another(all_spells),
                         ['Drain', 'Magic Missile', 'Poison', 'Recharge'])
        nxt = myobj.turn(nxt, myobj.spells.named("Poison"))
        self.assertEqual(nxt.turn, 4)
        self.assertEqual(nxt.wizard['hitpoints'], 1)
        self.assertEqual(nxt.wizard['armor'], 7)
        self.assertEqual(nxt.wizard['mana'], 340 - 173)  # 167
        self.assertEqual(nxt.wizard['used'], 229 + 113 + 73 + 173)
        self.assertEqual(nxt.boss['hitpoints'], 9)
        self.assertEqual(nxt.active.named("Shield").turns, 1)
        self.assertEqual(nxt.active.named("Poison").turns, 5)

        # 6. Turn 5 -- Player casts Magic Missile
        # -- Player turn --
        # - Player has 1 hit point, 7 armor, 167 mana
        # - Boss has 9 hit points
        # Shield's timer is now 0.
        # Shield wears off, decreasing armor by 7.
        # Poison deals 3 damage; its timer is now 4.
        # Player casts Magic Missile, dealing 4 damage.
        # -- Boss turn --
        # - Player has 1 hit point, 0 armor, 114 mana
        # - Boss has 2 hit points
        # Poison deals 3 damage. This kills the boss, and the player wins.
        self.assertEqual(nxt.another(all_spells),
                         ['Drain', 'Magic Missile', 'Shield'])
        nxt = myobj.turn(nxt, myobj.spells.named("Magic Missile"))
        self.assertEqual(nxt.turn, 5)
        self.assertEqual(nxt.wizard['hitpoints'], 1)
        self.assertEqual(nxt.wizard['armor'], 0)
        self.assertEqual(nxt.wizard['mana'], 167 - 53)
        self.assertEqual(nxt.wizard['used'], 229 + 113 + 73 + 173 + 53)
        self.assertEqual(nxt.boss['hitpoints'], 0)
        self.assertEqual(nxt.active.named("Shield").turns, 0)
        self.assertEqual(nxt.active.named("Poison").turns, 3)
        print(nxt)

    def test_part_one(self):
        "Test part one example of Wizsim object"

        # 1. Create Wizsim object from text
        myobj = wizsim.Wizsim(text=BOSS13_TEXT)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Wizsim object"

        # 1. Create Wizsim object from text
        myobj = wizsim.Wizsim(part2=True, text=BOSS14_TEXT)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ w i z s i m . p y                end
# ======================================================================
