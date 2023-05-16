
# ======================================================================
# Not Enough Minerals
#   Advent of Code 2022 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ b l u e p r i n t . p y
# ======================================================================
"Test Blueprint for Advent of Code 2022 day 19, Not Enough Minerals"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import blueprint

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "Blueprint 1: Each ore robot costs 4 ore. " \
    "Each clay robot costs 2 ore. " \
    "Each obsidian robot costs 3 ore and 14 clay. " \
    "Each geode robot costs 2 ore and 7 obsidian."

EXAMPLE_TWO = "Blueprint 2: Each ore robot costs 2 ore. " \
    "Each clay robot costs 3 ore. "\
    "Each obsidian robot costs 3 ore and 8 clay. " \
    "Each geode robot costs 3 ore and 12 obsidian."

# ======================================================================
#                                                          TestBlueprint
# ======================================================================


class TestBlueprint(unittest.TestCase):  # pylint: disable=R0904
    "Test Blueprint object"

    def test_empty_init(self):
        "Test the default Blueprint creation"

        # 1. Create default Blueprint object
        myobj = blueprint.Blueprint()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.number, 0)
        self.assertEqual(myobj.robots, None)
        self.assertEqual(myobj.cost, {})
        self.assertEqual(myobj.useful, {})

    def test_text_init(self):
        "Test the Blueprint object creation from text"

        # 1. Create Blueprint object from text
        myobj = blueprint.Blueprint(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 159)
        self.assertEqual(myobj.number, 1)
        self.assertNotEqual(myobj.robots, None)
        self.assertEqual(len(myobj.robots), 4)
        self.assertIn('ore', myobj.robots)
        self.assertIn('clay', myobj.robots)
        self.assertIn('obsidian', myobj.robots)
        self.assertIn('geode', myobj.robots)

        # 3. Check methods
        self.assertEqual(myobj.geode_production(24), 9)
        self.assertEqual(myobj.geode_production(32), 56)

    def test_text_two(self):
        "Test the Blueprint object creation from example two text"

        # 1. Create Blueprint object from text
        myobj = blueprint.Blueprint(text=EXAMPLE_TWO)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 159)
        self.assertEqual(myobj.number, 2)
        self.assertEqual(len(myobj.robots), 4)
        self.assertIn('ore', myobj.robots)
        self.assertIn('clay', myobj.robots)
        self.assertIn('obsidian', myobj.robots)
        self.assertIn('geode', myobj.robots)

        # 3. Check methods
        self.assertEqual(myobj.geode_production(24), 12)
        self.assertEqual(myobj.geode_production(32), 62)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                t e s t _ b l u e p r i n t . p y               end
# ======================================================================
