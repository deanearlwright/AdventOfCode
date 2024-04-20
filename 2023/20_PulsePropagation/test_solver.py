
# ======================================================================
# Pulse Propagation
#   Advent of Code 2023 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      t e s t _ s o l v e r . p y
# ======================================================================
"Test solver for Advent of Code 2023 day 20, Pulse Propagation"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_20
import solver

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_ONE = """
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
""" # l=8000, h=4000, p=32000000

EXAMPLE_TWO = """
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
""" # l=4250, h=2750, p=11687500

EXAMPLE_RX = """
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> rx
"""

PART_ONE_TEXT = EXAMPLE_TWO
PART_TWO_TEXT = EXAMPLE_RX

PART_ONE_RESULT = 11687500
PART_TWO_RESULT = 0

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
        self.assertEqual(myobj.configuration, None)

    def test_text_init(self):
        "Test the Solver object creation from text"

        # 1. Create Solver object from text
        myobj = solver.Solver(text=aoc_20.from_text(EXAMPLE_ONE))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertNotEqual(myobj.configuration, None)

        # 3. Check Methods
        self.assertEqual(myobj.configuration.multiple_presses(), 32000000)

    def test_part_one(self):
        "Test part one example of Solver object"

        # 1. Create Solver object from text
        text = aoc_20.from_text(PART_ONE_TEXT)
        myobj = solver.Solver(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Solver object"

        # 1. Create Solver object from text
        text = aoc_20.from_text(PART_TWO_TEXT)
        myobj = solver.Solver(part2=True, text=text)

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
