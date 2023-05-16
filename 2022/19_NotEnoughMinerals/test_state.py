
# ======================================================================
# NotEnoughMinerals
#   Advent of Code 2022 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s t a t e . p y
# ======================================================================
"Test State for Advent of Code 2022 day 19, NotEnoughMinerals"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import state

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                              TestState
# ======================================================================


class TestState(unittest.TestCase):  # pylint: disable=R0904
    "Test State object"

    def test_empty_init(self):
        "Test the default State creation"

        # 1. Create default State object
        myobj = state.State()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.time, 1)
        self.assertEqual(myobj.robots, {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0})
        self.assertEqual(myobj.resources, {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0})

    def test_value_init(self):
        "Test the State object creation from text"

        # 1. Create State object from text
        myobj = state.State(time=33)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.time, 33)
        self.assertEqual(myobj.robots, {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0})
        self.assertEqual(myobj.resources, {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0})

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ s t a t e . p y                   end
# ======================================================================
