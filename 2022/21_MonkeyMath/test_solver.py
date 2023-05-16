
# ======================================================================
# Monkey Math
#   Advent of Code 2022 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s o l v e r . p y
# ======================================================================
"Test solver for Advent of Code 2022 day 21, Monkey Math"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_21
import solver

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 152
PART_TWO_STRING = "(((4 + (2 * (X - 3))) / 4) == 150)"
PART_TWO_RESULT = 301

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
        self.assertEqual(myobj.monkeys, None)

    def test_text_init(self):
        "Test the Solver object creation from text"

        # 1. Create Solver object from text
        myobj = solver.Solver(text=aoc_21.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 15)
        self.assertNotEqual(myobj.monkeys, None)

    def test_part_one(self):
        "Test part one example of Solver object"

        # 1. Create Solver object from text
        myobj = solver.Solver(text=aoc_21.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False),
                         PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Solver object"

        # 1. Create Solver object from text
        myobj = solver.Solver(part2=True,
                              text=aoc_21.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)

    def test_split_equation(self):
        "Check the equation splitter"

        self.assertEqual(solver.Solver.split_equation(PART_TWO_STRING),
                         ("((4 + (2 * (X - 3))) / 4)", "==", "150"))
        self.assertEqual(solver.Solver.split_equation(
            "((4 + (2 * (X - 3))) / 4)"),
            ("(4 + (2 * (X - 3)))", "/", "4"))
        self.assertEqual(solver.Solver.split_equation("(4 + (2 * (X - 3)))"),
                         ("4", "+", "(2 * (X - 3))"))
        self.assertEqual(solver.Solver.split_equation("(2 * (X - 3))"),
                         ("2", "*", "(X - 3)"))
        self.assertEqual(solver.Solver.split_equation("(X - 3)"),
                         ("X", "-", "3"))

    def test_execute(self):
        "Check updating the result"

        self.assertEqual(solver.Solver.execute(150, "/", "4", False), 600)
        self.assertEqual(solver.Solver.execute(600, "+", "4", True), 596)
        self.assertEqual(solver.Solver.execute(596, "*", "2", True), 298)
        self.assertEqual(solver.Solver.execute(298, "-", "3", False), 301)

    def not_test_solve_for_x(self):
        "Check equation solving"

        self.assertEqual(solver.Solver.solve_for_x(PART_TWO_STRING),
                         PART_TWO_RESULT)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ s o l v e r . p y                  end
# ======================================================================
