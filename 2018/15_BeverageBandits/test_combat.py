# ======================================================================
# Beverage Bandits
#   Advent of Code 2018 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c o m b a t . p y
# ======================================================================
"Test solver for Advent of Code 2018 day 15, Beverage Bandits"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_15
import combat

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######
"""
EXAMPLE_TEXT_WITH_HITPOINTS = """
#######
#.G...#   G(200)
#...EG#   E(200), G(200)
#.#.#G#   G(200)
#..G#E#   G(200), E(200)
#.....#
#######
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 27730
PART_TWO_RESULT = 4988

EXAMPLE_COMBAT1 = """
#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######
"""
EXAMPLE_COMBAT2 = """
#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######
"""
EXAMPLE_COMBAT3 = """
#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######
"""
EXAMPLE_COMBAT4 = """
#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######
"""
EXAMPLE_COMBAT5 = """
#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########
"""
EXAMPLE_COMBAT = [EXAMPLE_COMBAT1, EXAMPLE_COMBAT2, EXAMPLE_COMBAT3,
                  EXAMPLE_COMBAT4, EXAMPLE_COMBAT5]
EXAMPLE_COMBAT_ROUNDS = [37, 46, 35, 54, 20]
EXAMPLE_COMBAT_HITPOINTS = [982, 859, 793, 536, 937]
EXAMPLE_COMBAT_RESULTS = [36334, 39514, 27755, 28944, 18740]

PART_TWO_COMBAT = [EXAMPLE_TEXT, EXAMPLE_COMBAT2, EXAMPLE_COMBAT3,
                   EXAMPLE_COMBAT4, EXAMPLE_COMBAT5]
PART_TWO_COMBAT_ATTACK = [15, 4, 15, 12, 34]
PART_TWO_COMBAT_ROUNDS = [29, 33, 37, 39, 30]
PART_TWO_COMBAT_HITPOINTS = [172, 948, 94, 166, 38]
PART_TWO_COMBAT_RESULTS = [4988, 31284, 3478, 6474, 1140]

EXAMPLE_STEPS_01 = """
#######
#..G..#
#...EG#
#.#G#G#
#...#E#
#.....#
#######
"""
EXAMPLE_STEPS_02 = """
#######
#...G.#
#..GEG#
#.#.#G#
#...#E#
#.....#
#######
"""

EXAMPLE_STEPS_23 = """
#######
#...G.#
#..G.G#
#.#.#G#
#...#E#
#.....#
#######
"""

EXAMPLE_STEPS_24 = """
#######
#..G..#
#...G.#
#.#G#G#
#...#E#
#.....#
#######
"""

EXAMPLE_STEPS_25 = """
#######
#.G...#
#..G..#
#.#.#G#
#..G#E#
#.....#
#######
"""

EXAMPLE_STEPS_26 = """
#######
#G....#
#.G...#
#.#.#G#
#...#E#
#..G..#
#######
"""

EXAMPLE_STEPS_27 = """
#######
#G....#
#.G...#
#.#.#G#
#...#E#
#...G.#
#######
"""

EXAMPLE_STEPS_28 = """
#######
#G....#
#.G...#
#.#.#G#
#...#E#
#....G#
#######
"""

EXAMPLE_STEPS_47 = """
#######
#G....#
#.G...#
#.#.#G#
#...#.#
#....G#
#######
"""


# Targets:      In range:     Reachable:    Nearest:      Chosen:
# #######       #######       #######       #######       #######
# #E..G.#       #E.?G?#       #E.@G.#       #E.!G.#       #E.+G.#
# #...#.#  -->  #.?.#?#  -->  #.@.#.#  -->  #.!.#.#  -->  #...#.#
# #.G.#G#       #?G?#G#       #@G@#G#       #!G.#G#       #.G.#G#
# #######       #######       #######       #######       #######
TEST_MOVEMENT_ONE = """
#######
#E..G.#
#...#.#
#.G.#G#
#######
"""
TEST_MOVEMENT_ONE_UNIT = 101
TEST_MOVEMENT_ONE_OPPONENTS = [104, 302, 305]
TEST_MOVEMENT_ONE_IN_RANGE = [103, 105, 202, 205, 301, 303]
TEST_MOVEMENT_ONE_REACHABLE = [103, 202, 301, 303]
TEST_MOVEMENT_ONE_NEAREST = [103, 202, 301]
TEST_MOVEMENT_ONE_CHOSEN = 103
TEST_MOVEMENT_ONE_NEW_LOC = 102
TEST_MOVEMENT_ONE_MOVED = """
#######
#.E.G.#
#...#.#
#.G.#G#
#######
"""

# In range:     Nearest:      Chosen:       Distance:     Step:
# #######       #######       #######       #######       #######
# #.E...#       #.E...#       #.E...#       #4E212#       #..E..#
# #...?.#  -->  #...!.#  -->  #...+.#  -->  #32101#  -->  #.....#
# #..?G?#       #..!G.#       #...G.#       #432G2#       #...G.#
# #######       #######       #######       #######       #######
TEST_MOVEMENT_TWO = """
#######
#.E...#
#.....#
#...G.#
#######
"""
TEST_MOVEMENT_TWO_UNIT = 102
TEST_MOVEMENT_TWO_OPPONENTS = [304]
TEST_MOVEMENT_TWO_IN_RANGE = [204, 303, 305]
TEST_MOVEMENT_TWO_REACHABLE = [204, 303, 305]
TEST_MOVEMENT_TWO_NEAREST = [204, 303]
TEST_MOVEMENT_TWO_CHOSEN = 204
TEST_MOVEMENT_TWO_NEW_LOC = 103
TEST_MOVEMENT_TWO_MOVED = """
#######
#..E..#
#.....#
#...G.#
#######
"""

MOVEMENT_EXAMPLE_0 = """
#########
#G..G..G#
#.......#
#.......#
#G..E..G#
#.......#
#.......#
#G..G..G#
#########
"""
MOVEMENT_EXAMPLE_1 = """
#########
#.G...G.#
#...G...#
#...E..G#
#.G.....#
#.......#
#G..G..G#
#.......#
#########
"""
MOVEMENT_EXAMPLE_2 = """
#########
#..G.G..#
#...G...#
#.G.E.G.#
#.......#
#G..G..G#
#.......#
#.......#
#########
"""
MOVEMENT_EXAMPLE_3 = """
#########
#.......#
#..GGG..#
#..GEG..#
#G..G...#
#......G#
#.......#
#.......#
#########
"""

# ======================================================================
#                                                             TestCombat
# ======================================================================


class TestCombat(unittest.TestCase):  # pylint: disable=R0904
    "Test Combat object"

    def test_empty_init(self):
        "Test the default Combat creation"

        # 1. Create default Combat object
        myobj = combat.Combat()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.cave), 0)

    def test_text_init(self):
        "Test the Combat object creation from text"

        # 1. Create Combat object from text
        myobj = combat.Combat(text=aoc_15.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 7)
        self.assertEqual(len(myobj.cave), 3)
        self.assertEqual(len(myobj.cave['#']), 27)
        self.assertEqual(len(myobj.cave['E']), 2)
        self.assertEqual(len(myobj.cave['G']), 4)
        self.assertEqual(myobj.cave.max_loc(), 606)
        self.assertEqual(str(myobj), EXAMPLE_TEXT.strip())
        self.assertEqual(myobj.map(), EXAMPLE_TEXT_WITH_HITPOINTS.strip())

        # 3. A couple of rounds
        self.assertEqual(myobj.cave['E'].hitpoints(), 2*200)
        self.assertEqual(myobj.cave['G'].hitpoints(), 4*200)
        myobj.round()
        self.assertEqual(myobj.cave['E'].hitpoints(), 197+197)
        self.assertEqual(myobj.cave['G'].hitpoints(), 200+200+197+197)
        self.assertEqual(str(myobj), EXAMPLE_STEPS_01.strip())
        myobj.round()
        self.assertEqual(myobj.cave['E'].hitpoints(), 188+194)
        self.assertEqual(myobj.cave['G'].hitpoints(), 200+200+194+194)
        self.assertEqual(str(myobj), EXAMPLE_STEPS_02.strip())

        # 4. And then several more
        for _ in range(3, 24):
            assert _ > 0
            myobj.round()
        self.assertEqual(str(myobj), EXAMPLE_STEPS_23.strip())
        self.assertEqual(myobj.cave['E'].hitpoints(), 131)
        self.assertEqual(myobj.cave['G'].hitpoints(), 200+200+131+131)
        myobj.round() # 24
        self.assertEqual(str(myobj), EXAMPLE_STEPS_24.strip())
        self.assertEqual(myobj.cave['E'].hitpoints(), 128)
        self.assertEqual(myobj.cave['G'].hitpoints(), 200+200+131+128)
        myobj.round() # 25
        self.assertEqual(str(myobj), EXAMPLE_STEPS_25.strip())
        self.assertEqual(myobj.cave['E'].hitpoints(), 125)
        self.assertEqual(myobj.cave['G'].hitpoints(), 200+200+131+125)
        myobj.round() # 26
        self.assertEqual(str(myobj), EXAMPLE_STEPS_26.strip())
        self.assertEqual(myobj.cave['E'].hitpoints(), 122)
        self.assertEqual(myobj.cave['G'].hitpoints(), 200+200+131+122)
        myobj.round() # 27
        self.assertEqual(str(myobj), EXAMPLE_STEPS_27.strip())
        self.assertEqual(myobj.cave['E'].hitpoints(), 119)
        self.assertEqual(myobj.cave['G'].hitpoints(), 200+200+131+119)
        myobj.round() # 28
        self.assertEqual(str(myobj), EXAMPLE_STEPS_28.strip())
        self.assertEqual(myobj.cave['E'].hitpoints(), 113)
        self.assertEqual(myobj.cave['G'].hitpoints(), 200+200+131+116)

        # 5. And then several more again
        for _ in range(29, 48):
            assert _ > 0
            myobj.round()
        self.assertEqual(str(myobj), EXAMPLE_STEPS_47.strip())
        self.assertEqual(myobj.cave['E'].hitpoints(), 0)
        self.assertEqual(myobj.cave['G'].hitpoints(), 200+200+131+59)

    def test_movement_one(self):
        "Test movement example one"

        # 1. Create a cave from movement example one
        myobj = combat.Combat(text=aoc_15.from_text(TEST_MOVEMENT_ONE))
        self.assertEqual(str(myobj), TEST_MOVEMENT_ONE.strip())

        # 2. Check the opponents
        unit = myobj.cave.get_by_location(TEST_MOVEMENT_ONE_UNIT)
        opponents = myobj.opponents(unit)
        self.assertEqual(set(opponents), set(TEST_MOVEMENT_ONE_OPPONENTS))

        # 3. Check the empty locations adjacent to the opponents
        in_range = myobj.move_in_range(unit, opponents)
        self.assertEqual(in_range, set(TEST_MOVEMENT_ONE_IN_RANGE))

        # 4. Check the reachable locations
        reachable = myobj.move_reachable(unit, in_range)
        self.assertEqual(set(reachable), set(TEST_MOVEMENT_ONE_REACHABLE))

        # 5. Check the nearest reachable locations
        nearest = myobj.move_nearest(unit, reachable)
        self.assertEqual(set(nearest), set(TEST_MOVEMENT_ONE_NEAREST))

        # 6. Choose one of the nearest reachable locations
        chosen = myobj.move_choose(nearest)
        self.assertEqual(chosen, TEST_MOVEMENT_ONE_CHOSEN)

        # 7. Determine the first step toward the chosen location
        new_loc = myobj.move_location(reachable, chosen)
        self.assertEqual(new_loc, TEST_MOVEMENT_ONE_NEW_LOC)

        # 8. Execute the move
        myobj.move_execute(unit, new_loc)
        self.assertEqual(str(myobj), TEST_MOVEMENT_ONE_MOVED.strip())

    def test_movement_two(self):
        "Test movement example two"

        # 1. Create a cave from movement example one
        myobj = combat.Combat(text=aoc_15.from_text(TEST_MOVEMENT_TWO))
        self.assertEqual(str(myobj), TEST_MOVEMENT_TWO.strip())

        # 2. Check the opponents
        unit = myobj.cave.get_by_location(TEST_MOVEMENT_TWO_UNIT)
        opponents = myobj.opponents(unit)
        self.assertEqual(set(opponents), set(TEST_MOVEMENT_TWO_OPPONENTS))

        # 3. Check the empty locations adjacent to the opponents
        in_range = myobj.move_in_range(unit, opponents)
        self.assertEqual(in_range, set(TEST_MOVEMENT_TWO_IN_RANGE))

        # 4. Check the reachable locations
        reachable = myobj.move_reachable(unit, in_range)
        self.assertEqual(set(reachable), set(TEST_MOVEMENT_TWO_REACHABLE))

        # 5. Check the nearest reachable locations
        nearest = myobj.move_nearest(unit, reachable)
        self.assertEqual(set(nearest), set(TEST_MOVEMENT_TWO_NEAREST))

        # 6. Choose one of the nearest reachable locations
        chosen = myobj.move_choose(nearest)
        self.assertEqual(chosen, TEST_MOVEMENT_TWO_CHOSEN)

        # 7. Determine the first step toward the chosen location
        new_loc = myobj.move_location(reachable, chosen)
        self.assertEqual(new_loc, TEST_MOVEMENT_TWO_NEW_LOC)

        # 8. Execute the move
        myobj.move_execute(unit, new_loc)
        self.assertEqual(str(myobj), TEST_MOVEMENT_TWO_MOVED.strip())

    def test_larger_movement_example(self):
        "Test the Combat object movement example"

        # 1. Create Combat object from text
        myobj = combat.Combat(text=aoc_15.from_text(MOVEMENT_EXAMPLE_0))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 9)
        self.assertEqual(len(myobj.cave), 3)
        self.assertEqual(len(myobj.cave['#']), 32)
        self.assertEqual(len(myobj.cave['E']), 1)
        self.assertEqual(len(myobj.cave['G']), 8)
        self.assertEqual(myobj.cave.max_loc(), 808)
        self.assertEqual(str(myobj), MOVEMENT_EXAMPLE_0.strip())

        # 3. A couple of rounds of movement
        myobj.round()
        self.assertEqual(str(myobj), MOVEMENT_EXAMPLE_1.strip())
        myobj.round()
        self.assertEqual(str(myobj), MOVEMENT_EXAMPLE_2.strip())
        myobj.round()
        self.assertEqual(str(myobj), MOVEMENT_EXAMPLE_3.strip())
        myobj.round()
        self.assertEqual(str(myobj), MOVEMENT_EXAMPLE_3.strip())
        myobj.round()
        self.assertEqual(str(myobj), MOVEMENT_EXAMPLE_3.strip())

    def test_attacks(self):
        pass


    def test_example_combat_results(self):
        "Test combat results"

        # 1. Loop for all of the examples
        for index, text in enumerate(EXAMPLE_COMBAT):
            #print("test_rounds %d" % index)

            # 2. Create the Combat object
            myobj = combat.Combat(text=aoc_15.from_text(text))

            # 3. Engage in combat
            rounds = myobj.fight(verbose=False)

            # 4. Get the surviving hit points
            hitpoints = myobj.hitpoints()

            # 5. Verify that things are the way they should be
            self.assertEqual(rounds, EXAMPLE_COMBAT_ROUNDS[index])
            self.assertEqual(hitpoints, EXAMPLE_COMBAT_HITPOINTS[index])
            self.assertEqual(hitpoints * rounds, EXAMPLE_COMBAT_RESULTS[index])

    def test_example_part_two_combat_results(self):
        "Test combat results for part two with given attack rate"

        # 1. Loop for all of the examples
        for index, text in enumerate(PART_TWO_COMBAT):
            #print("test_rounds %d" % index)

            # 2. Create the Combat object
            myobj = combat.Combat(text=aoc_15.from_text(text),
                                  elf_attack=PART_TWO_COMBAT_ATTACK[index])

            # 3. Engage in combat
            rounds = myobj.fight(verbose=False)

            # 4. Get the surviving hit points
            hitpoints = myobj.hitpoints()

            # 5. Verify that things are the way they should be
            self.assertEqual(rounds, PART_TWO_COMBAT_ROUNDS[index])
            self.assertEqual(hitpoints, PART_TWO_COMBAT_HITPOINTS[index])
            self.assertEqual(hitpoints * rounds, PART_TWO_COMBAT_RESULTS[index])

    def test_example_part_two_elf_attack(self):
        "Test determine attack rate for part two"

        # 1. Loop for all of the examples
        for index, text in enumerate(PART_TWO_COMBAT):
            #print("test_rounds %d" % index)

            # 2. Create the Combat object
            myobj = combat.Combat(text=aoc_15.from_text(text))

            # 3. Determine the minimum attack rate
            elf_attack = myobj.minimum_elf_attack(verbose=False, limit=40)

            # 5. Verify that things are the way they should be
            self.assertEqual(elf_attack, PART_TWO_COMBAT_ATTACK[index])

    def test_part_one(self):
        "Test part one example of Combat object"

        # 1. Create Combat object from text
        myobj = combat.Combat(text=aoc_15.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Combat object"

        # 1. Create Combat object from text
        myobj = combat.Combat(part2=True, text=aoc_15.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ c o m b a t . p y                  end
# ======================================================================
