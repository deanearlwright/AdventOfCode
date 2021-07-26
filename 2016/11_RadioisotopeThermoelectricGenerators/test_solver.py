# ======================================================================
# Radioisotope Thermoelectric Generators
#   Advent of Code 2016 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s o l v e r . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 11, Radioisotope Thermoelectric Generators"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_11
import solver

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
"""


PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = ""

PART_ONE_RESULT = 11
PART_TWO_RESULT = None

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

    def test_text_init(self):
        "Test the Solver object creation from text"

        # 1. Create Solver object from text
        myobj = solver.Solver(text=aoc_11.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)

        # 3. Check methods
        self.assertEqual(myobj.number_moves(), 11)

    def test_part_one(self):
        "Test part one example of Solver object"

        # 1. Create Solver object from text
        myobj = solver.Solver(text=aoc_11.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Solver object"

        # 1. Create Solver object from text
        myobj = solver.Solver(part2=True, text=aoc_11.from_text(PART_TWO_TEXT))

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
