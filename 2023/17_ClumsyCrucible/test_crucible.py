
# ======================================================================
# Clumsy Crucible
#   Advent of Code 2023 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c r u c i b l e . p y
# ======================================================================
"Test Crucible for Advent of Code 2023 day 17, Clumsy Crucible"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import crucible

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "2413432311323",
    "3215453535623",
    "3255245654254",
    "3446585845452",
    "4546657867536",
    "1438598798454",
    "4457876987766",
    "3637877979653",
    "4654967986887",
    "4564679986453",
    "1224686865563",
    "2546548887735",
    "4322674655533",
]

EXAMPLE_ULTRA = [
    "111111111111",
    "999999999991",
    "999999999991",
    "999999999991",
    "999999999991",
]
# ======================================================================
#                                                           TestCrucible
# ======================================================================


class TestCrucible(unittest.TestCase):  # pylint: disable=R0904
    "Test Crucible object"

    def test_empty_init(self):
        "Test the default Crucible creation"

        # 1. Create default Crucible object
        myobj = crucible.Crucible()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.loc, (0, 0))
        self.assertEqual(myobj.goal, (0, 0))
        self.assertEqual(myobj.directions, crucible.EAST)
        self.assertEqual(myobj.total_heat_loss, 0)
        self.assertEqual(myobj.min_steps, 1)
        self.assertEqual(myobj.max_steps, 3)

    def test_text_init(self): # pylint: disable=R0915
        "Test the Crucible object creation from text"

        # 1. Create Crucible object from text
        myobj = crucible.Crucible(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 13)
        self.assertEqual(myobj.loc, (0, 0))
        self.assertEqual(myobj.directions, crucible.EAST)
        self.assertEqual(myobj.directions, crucible.EAST)
        self.assertEqual(myobj.total_heat_loss, 0)
        self.assertEqual(myobj.min_steps, 1)
        self.assertEqual(myobj.max_steps, 3)

        # 3. Check methods
        self.assertEqual(myobj.is_goal(), False)
        self.assertEqual(myobj.possible(), [crucible.SOUTH, crucible.EAST])
        self.assertEqual(myobj.next_action(crucible.EAST), True)
        self.assertEqual(myobj.loc, (0, 1))
        self.assertEqual(myobj.directions, crucible.EAST + crucible.EAST)
        self.assertEqual(myobj.total_heat_loss, 4)
        self.assertEqual(myobj.possible(), [crucible.SOUTH, crucible.EAST])
        self.assertEqual(myobj.next_action(crucible.EAST), True)
        self.assertEqual(myobj.loc, (0, 2))
        self.assertEqual(myobj.next_action(crucible.SOUTH), True)
        self.assertEqual(myobj.loc, (1, 2))
        self.assertEqual(myobj.next_action(crucible.EAST), True)
        self.assertEqual(myobj.loc, (1, 3))
        self.assertEqual(myobj.next_action(crucible.EAST), True)
        self.assertEqual(myobj.loc, (1, 4))
        self.assertEqual(myobj.next_action(crucible.EAST), True)
        self.assertEqual(myobj.loc, (1, 5))
        self.assertEqual(myobj.possible(), [crucible.NORTH, crucible.SOUTH])
        self.assertEqual(myobj.next_action(crucible.NORTH), True)
        self.assertEqual(myobj.loc, (0, 5))
        self.assertEqual(myobj.next_action(crucible.EAST), True)
        self.assertEqual(myobj.loc, (0, 6))
        self.assertEqual(myobj.next_action(crucible.EAST), True)
        self.assertEqual(myobj.loc, (0, 7))
        self.assertEqual(myobj.next_action(crucible.EAST), True)
        self.assertEqual(myobj.loc, (0, 8))
        self.assertEqual(myobj.directions, crucible.EAST + crucible.EAST + crucible.EAST)
        self.assertEqual(myobj.next_action(crucible.SOUTH), True)
        self.assertEqual(myobj.next_action(crucible.SOUTH), True)
        self.assertEqual(myobj.next_action(crucible.EAST), True)
        self.assertEqual(myobj.next_action(crucible.EAST), True)
        self.assertEqual(myobj.next_action(crucible.SOUTH), True)
        self.assertEqual(myobj.next_action(crucible.SOUTH), True)
        self.assertEqual(myobj.next_action(crucible.EAST), True)
        self.assertEqual(myobj.next_action(crucible.SOUTH), True)
        self.assertEqual(myobj.next_action(crucible.SOUTH), True)
        self.assertEqual(myobj.next_action(crucible.SOUTH), True)
        self.assertEqual(myobj.next_action(crucible.EAST), True)
        self.assertEqual(myobj.next_action(crucible.SOUTH), True)
        self.assertEqual(myobj.next_action(crucible.SOUTH), True)
        self.assertEqual(myobj.next_action(crucible.SOUTH), True)
        self.assertEqual(myobj.next_action(crucible.WEST), True)
        self.assertEqual(myobj.next_action(crucible.SOUTH), True)
        self.assertEqual(myobj.next_action(crucible.SOUTH), True)
        self.assertEqual(myobj.next_action(crucible.EAST), True)
        self.assertEqual(myobj.loc, (12, 12))
        self.assertEqual(myobj.is_goal(), True)
        self.assertEqual(myobj.total_heat_loss, 102)

    def test_search_one(self):
        "Test the Crucible object creation from text"

        # 1. Create Crucible object from text
        myobj = crucible.Crucible(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 13)
        self.assertEqual(myobj.loc, (0, 0))
        self.assertEqual(myobj.goal, (12, 12))
        self.assertEqual(myobj.directions, crucible.EAST)
        self.assertEqual(myobj.total_heat_loss, 0)
        self.assertEqual(myobj.min_steps, 1)
        self.assertEqual(myobj.max_steps, 3)

        # 3. Check methods
        self.assertEqual(myobj.search(), 102)

    def test_search_two(self):
        "Test the Crucible object creation from text"

        # 1. Create Crucible object from text
        myobj = crucible.Crucible(text=EXAMPLE_TEXT, part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 13)
        self.assertEqual(myobj.loc, (0, 0))
        self.assertEqual(myobj.goal, (12, 12))
        self.assertEqual(myobj.directions, crucible.EAST)
        self.assertEqual(myobj.total_heat_loss, 0)
        self.assertEqual(myobj.min_steps, 4)
        self.assertEqual(myobj.max_steps, 10)

        # 3. Check methods
        self.assertEqual(myobj.search(), 94)

    def test_search_ultra(self):
        "Test the Crucible object creation from text"

        # 1. Create Crucible object from text
        myobj = crucible.Crucible(text=EXAMPLE_ULTRA, part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(myobj.loc, (0, 0))
        self.assertEqual(myobj.directions, crucible.EAST)
        self.assertEqual(myobj.total_heat_loss, 0)
        self.assertEqual(myobj.min_steps, 4)
        self.assertEqual(myobj.max_steps, 10)

        # 3. Check methods
        self.assertEqual(myobj.search(), 71)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ c r u c i b l e . p y                end
# ======================================================================
