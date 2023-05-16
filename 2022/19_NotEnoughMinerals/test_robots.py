
# ======================================================================
# Not Enough Minerals
#   Advent of Code 2022 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r o b o t s . p y
# ======================================================================
"Test Robots for Advent of Code 2022 day 19, Not Enough Minerals"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import robots

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "Each ore robot costs 4 ore. " \
    "Each clay robot costs 2 ore. " \
    "Each obsidian robot costs 3 ore and 14 clay. " \
    "Each geode robot costs 2 ore and 7 obsidian."

# ======================================================================
#                                                             TestRobots
# ======================================================================


class TestRobots(unittest.TestCase):  # pylint: disable=R0904
    "Test Robots object"

    def test_empty_init(self):
        "Test the default Robots creation"

        # 1. Create default Robots object
        myobj = robots.Robots()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.robots), 0)

    def test_text_init(self):
        "Test the Robots object creation from text"

        # 1. Create Robots object from text
        myobj = robots.Robots(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 146)
        self.assertEqual(len(myobj.robots), 4)
        self.assertEqual(myobj.names(), ['ore', 'clay', 'obsidian', 'geode'])
        self.assertEqual(myobj.needs('ore', 'ore'), 4)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ r o b o t s . p y                  end
# ======================================================================
