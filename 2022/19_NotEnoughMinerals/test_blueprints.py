
# ======================================================================
# Not Enough Minerals
#   Advent of Code 2022 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ b l u e p r i n t s . p y
# ======================================================================
"Test Blueprints for Advent of Code 2022 day 19, Not Enough Minerals"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import blueprints

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ["Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.",
                "Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."]

# ======================================================================
#                                                         TestBlueprints
# ======================================================================


class TestBlueprints(unittest.TestCase):  # pylint: disable=R0904
    "Test Blueprints object"

    def test_empty_init(self):
        "Test the default Blueprints creation"

        # 1. Create default Blueprints object
        myobj = blueprints.Blueprints()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.recipes), 0)

    def test_text_init(self):
        "Test the Blueprints object creation from text"

        # 1. Create Blueprints object from text
        myobj = blueprints.Blueprints(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 2)
        self.assertEqual(len(myobj.recipes), 2)

        # 3. Check methods
        self.assertEqual(myobj.quality_level(), 33)

    def test_text_two(self):
        "Test the Blueprints object creation from text for part2"

        # 1. Create Blueprints object from text
        myobj = blueprints.Blueprints(text=EXAMPLE_TEXT, part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 2)
        self.assertEqual(len(myobj.recipes), 2)

        # 3. Check methods
        self.assertEqual(myobj.product(), 56 * 62)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end               t e s t _ b l u e p r i n t s . p y              end
# ======================================================================
