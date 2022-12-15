
# ======================================================================
# Regolith Reservoir
#   Advent of Code 2022 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s o l v e r . p y
# ======================================================================
"Test solver for Advent of Code 2022 day 14, Regolith Reservoir"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_14
import solver

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 24
PART_TWO_RESULT = 93

# ======================================================================
#                                                             TestSolver
# ======================================================================


class TestSolver(unittest.TestCase):  # pylint: disable=R0904
    "Test Solver object"

    def test_empty_init(self):
        "Test the default Solver creation"

        # 1. Create default Solver object
        myobj = solver.Solver()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.device, None)

    def test_text_init(self):
        "Test the Solver object creation from text"

        # 1. Create Solver object from text
        myobj = solver.Solver(text=aoc_14.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 2)
        self.assertNotEqual(myobj.device, None)

    def test_part_one(self):
        "Test part one example of Solver object"

        # 1. Create Solver object from text
        myobj = solver.Solver(text=aoc_14.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Solver object"

        # 1. Create Solver object from text
        myobj = solver.Solver(part2=True,
                              text=aoc_14.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ s o l v e r . p y                  end
# ======================================================================
