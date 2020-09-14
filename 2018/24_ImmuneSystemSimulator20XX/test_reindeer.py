# ======================================================================
# Immune System Simulator 20XX
#   Advent of Code 2018 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r e i n d e e r . p y
# ======================================================================
"Test solver for Advent of Code 2018 day 24, Immune System Simulator 20XX"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_24
import reindeer

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_GROUP0 = "2974 units each with 9012 hit points with an attack that does 23 slashing damage at initiative 11"
EXAMPLE_GROUP1 = "4805 units each with 8717 hit points (weak to radiation) with an attack that does 15 bludgeoning damage at initiative 5"
EXAMPLE_GROUP2 = "133 units each with 22945 hit points (weak to slashing; immune to cold, bludgeoning) with an attack that does 287 radiation damage at initiative 19"

EXAMPLE_TEXT = """
Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4
"""
EXAMPLE_STR = """
Immune System:
Group 1 contains 17 units
Group 2 contains 989 units
Infection:
Group 1 contains 801 units
Group 2 contains 4485 units
"""
AFTER_ONE_ROUND = """
Immune System:
Group 1 contains 905 units
Infection:
Group 1 contains 797 units
Group 2 contains 4434 units
"""
AFTER_TWO_ROUNDS = """
Immune System:
Group 1 contains 761 units
Infection:
Group 1 contains 793 units
Group 2 contains 4434 units
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 5216
PART_TWO_RESULT = 51

# ======================================================================
#                                                              TestGroup
# ======================================================================


class TestGroup(unittest.TestCase):  # pylint: disable=R0904
    "Test Immune/Infection group object"

    def test_empty_init(self):
        "Test the default Immune/Infection group creation"

        # 1. Create default Immune/Infection group object
        myobj = reindeer.Group()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.number, 0)
        self.assertEqual(myobj.hitpoints, 0)
        self.assertEqual(myobj.immune, [])
        self.assertEqual(myobj.weak, [])
        self.assertEqual(myobj.damage, 0)
        self.assertEqual(myobj.attack, '')
        self.assertEqual(myobj.initiative, 0)

    def test_text_init(self):
        "Test the Immune/Infection group object creation from text"

        # 1. Create Immune/Infection group object from text
        myobj = reindeer.Group(text=EXAMPLE_GROUP0)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.text, EXAMPLE_GROUP0)
        self.assertEqual(myobj.number, 2974)
        self.assertEqual(myobj.hitpoints, 9012)
        self.assertEqual(myobj.immune, [])
        self.assertEqual(myobj.weak, [])
        self.assertEqual(myobj.damage, 23)
        self.assertEqual(myobj.attack, 'slashing')
        self.assertEqual(myobj.initiative, 11)

        # 3. Create Immune/Infection group object from text (this time with an imumunity)
        myobj = reindeer.Group(text=EXAMPLE_GROUP1)

        # 4. Make sure it has the expected values
        self.assertEqual(myobj.text, EXAMPLE_GROUP1)
        self.assertEqual(myobj.number, 4805)
        self.assertEqual(myobj.hitpoints, 8717)
        self.assertEqual(myobj.immune, [])
        self.assertEqual(myobj.weak, ['radiation'])
        self.assertEqual(myobj.damage, 15)
        self.assertEqual(myobj.attack, 'bludgeoning')
        self.assertEqual(myobj.initiative, 5)

        # 5. Create Immune/Infection group object from text (with both weakness and imumunity)
        myobj = reindeer.Group(text=EXAMPLE_GROUP2)

        # 6. Make sure it has the expected values
        self.assertEqual(myobj.text, EXAMPLE_GROUP2)
        self.assertEqual(myobj.number, 133)
        self.assertEqual(myobj.hitpoints, 22945)
        self.assertEqual(myobj.immune, ['cold', 'bludgeoning'])
        self.assertEqual(myobj.weak, ['slashing'])
        self.assertEqual(myobj.damage, 287)
        self.assertEqual(myobj.attack, 'radiation')
        self.assertEqual(myobj.initiative, 19)

# ======================================================================
#                                                               TestArmy
# ======================================================================


class TestArmy(unittest.TestCase):  # pylint: disable=R0904
    "Test Immune/Infection army object"

    def test_empty_init(self):
        "Test the default Immune/Infection army creation"

        # 1. Create default Immune/Infection army object
        myobj = reindeer.Army()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.name, None)
        self.assertEqual(myobj.groups, [])

    def test_text_init(self):
        "Test the Immune/Infection group object creation from text"

        # 1. Create Immune/Infection army object from text
        myobj = reindeer.Army(text=aoc_24.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.name, 'Immune System')
        self.assertEqual(len(myobj.groups), 2)
        self.assertEqual(myobj.groups[0].number, 17)
        self.assertEqual(myobj.groups[1].number, 989)

# ======================================================================
#                                                           TestReindeer
# ======================================================================


class TestReindeer(unittest.TestCase):  # pylint: disable=R0904
    "Test Reindeer object"

    def test_empty_init(self):
        "Test the default Reindeer creation"

        # 1. Create default Reindeer object
        myobj = reindeer.Reindeer()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.armies, [])

    def test_text_init(self):
        "Test the Reindeer object creation from text"

        # 1. Create Reindeer object from text
        myobj = reindeer.Reindeer(text=aoc_24.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(len(myobj.armies), 2)
        self.assertEqual(myobj.armies[0].name, 'Immune System')
        self.assertEqual(myobj.armies[1].name, 'Infection')
        self.assertEqual(len(myobj.armies[0].groups), 2)
        self.assertEqual(len(myobj.armies[1].groups), 2)
        self.assertEqual(myobj.armies[0].groups[0].number, 17)
        self.assertEqual(myobj.armies[0].groups[1].number, 989)
        self.assertEqual(myobj.armies[1].groups[0].number, 801)
        self.assertEqual(myobj.armies[1].groups[1].number, 4485)

        # 3. Check str()
        self.assertEqual(str(myobj), EXAMPLE_STR.strip())

        # 4. Fight one round
        myobj.round()
        self.assertEqual(str(myobj), AFTER_ONE_ROUND.strip())

        # 5. And then a couple more
        result = myobj.fight()
        self.assertEqual(result, PART_ONE_RESULT)

        # 6. Give the raindeer a boast
        myobj.boast(1570)
        result = myobj.fight()
        self.assertEqual(result, PART_TWO_RESULT)

    def test_part_one(self):
        "Test part one example of Reindeer object"

        # 1. Create Reindeer object from text
        myobj = reindeer.Reindeer(text=aoc_24.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Reindeer object"

        # 1. Create Reindeer object from text
        myobj = reindeer.Reindeer(part2=True, text=aoc_24.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ r e i n d e e r . p y                end
# ======================================================================
