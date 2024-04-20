
# ======================================================================
# Lavaduct Lagoon
#   Advent of Code 2023 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        t e s t _ p l a n . p y
# ======================================================================
"Test Plan for Advent of Code 2023 day 18, Lavaduct Lagoon"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import plan

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "R 6 (#70c710)",
    "D 5 (#0dc571)",
    "L 2 (#5713f0)",
    "D 2 (#d2c081)",
    "R 2 (#59c680)",
    "D 2 (#411b91)",
    "L 5 (#8ceee2)",
    "U 2 (#caa173)",
    "L 1 (#1b58a2)",
    "U 2 (#caa171)",
    "R 2 (#7807d2)",
    "U 3 (#a77fa3)",
    "L 2 (#015232)",
    "U 2 (#7a21e3)",
]

# ======================================================================
#                                                               TestPlan
# ======================================================================


class TestPlan(unittest.TestCase):  # pylint: disable=R0904
    "Test Plan object"

    def test_empty_init(self):
        "Test the default Plan creation"

        # 1. Create default Plan object
        myobj = plan.Plan()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.steps), 0)

    def test_text_init(self):
        "Test the Plan object creation from text"

        # 1. Create Plan object from text
        myobj = plan.Plan(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 14)
        self.assertEqual(len(myobj.steps), 14)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ p l a n . p y                    end
# ======================================================================
