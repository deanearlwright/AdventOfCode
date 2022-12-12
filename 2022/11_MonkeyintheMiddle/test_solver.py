# ======================================================================
# Monkey in the Middle
#   Advent of Code 2022 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s o l v e r . p y
# ======================================================================
"Test solver for Advent of Code 2022 day 11, Monkey in the Middle"

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
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 10605
PART_TWO_RESULT = 2713310158

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
        self.assertEqual(len(myobj.monkeys), 0)

    def test_text_init(self):
        "Test the Solver object creation from text"

        # 1. Create Solver object from text
        myobj = solver.Solver(text=aoc_11.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 24)
        self.assertEqual(len(myobj.monkeys), 4)
        self.assertEqual(myobj.monkeys[0].items, [79, 98])
        self.assertEqual(myobj.monkeys[1].items, [54, 65, 75, 74])
        self.assertEqual(myobj.monkeys[2].items, [79, 60, 97])
        self.assertEqual(myobj.monkeys[3].items, [74])

        # 3. Check methods
        myobj.round()
        self.assertEqual(myobj.monkeys[0].items, [20, 23, 27, 26])
        self.assertEqual(myobj.monkeys[1].items, [2080, 25, 167, 207, 401, 1046])
        self.assertEqual(myobj.monkeys[2].items, [])
        self.assertEqual(myobj.monkeys[3].items, [])
        myobj.round()
        self.assertEqual(myobj.monkeys[0].items, [695, 10, 71, 135, 350])
        self.assertEqual(myobj.monkeys[1].items, [43, 49, 58, 55, 362])
        self.assertEqual(myobj.monkeys[2].items, [])
        self.assertEqual(myobj.monkeys[3].items, [])
        myobj.round()
        myobj.round()
        myobj.round()
        myobj.round()
        myobj.round()
        myobj.round()
        myobj.round()
        myobj.round()
        self.assertEqual(myobj.monkeys[0].items, [91, 16, 20, 98])
        self.assertEqual(myobj.monkeys[1].items, [481, 245, 22, 26, 1092, 30])
        self.assertEqual(myobj.monkeys[2].items, [])
        self.assertEqual(myobj.monkeys[3].items, [])
        myobj.round()
        myobj.round()
        myobj.round()
        myobj.round()
        myobj.round()
        self.assertEqual(myobj.monkeys[0].items, [83, 44, 8, 184, 9, 20, 26, 102])
        self.assertEqual(myobj.monkeys[1].items, [110, 36])
        self.assertEqual(myobj.monkeys[2].items, [])
        self.assertEqual(myobj.monkeys[3].items, [])
        myobj.round()
        myobj.round()
        myobj.round()
        myobj.round()
        myobj.round()
        self.assertEqual(myobj.monkeys[0].items, [10, 12, 14, 26, 34])
        self.assertEqual(myobj.monkeys[1].items, [245, 93, 53, 199, 115])
        self.assertEqual(myobj.monkeys[2].items, [])
        self.assertEqual(myobj.monkeys[3].items, [])
        self.assertEqual(myobj.monkey_business(), 10605)

    def test_text_two_20(self):
        "Test the Solver object creation from text"

        # 1. Create Solver object from text
        myobj = solver.Solver(text=aoc_11.from_text(EXAMPLE_TEXT), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 24)
        self.assertEqual(len(myobj.monkeys), 4)
        self.assertEqual(myobj.monkeys[0].items, [79, 98])
        self.assertEqual(myobj.monkeys[1].items, [54, 65, 75, 74])
        self.assertEqual(myobj.monkeys[2].items, [79, 60, 97])
        self.assertEqual(myobj.monkeys[3].items, [74])

        # 3. Check methods
        myobj.rounds(verbose=False, rounds=20)
        self.assertEqual(myobj.monkeys[0].inspections, 99)
        self.assertEqual(myobj.monkeys[1].inspections, 97)
        self.assertEqual(myobj.monkeys[2].inspections, 8)
        self.assertEqual(myobj.monkeys[3].inspections, 103)

    def test_text_two_1000(self):
        "Test the Solver object creation from text"

        # 1. Create Solver object from text
        myobj = solver.Solver(text=aoc_11.from_text(EXAMPLE_TEXT), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 24)
        self.assertEqual(len(myobj.monkeys), 4)
        self.assertEqual(myobj.monkeys[0].items, [79, 98])
        self.assertEqual(myobj.monkeys[1].items, [54, 65, 75, 74])
        self.assertEqual(myobj.monkeys[2].items, [79, 60, 97])
        self.assertEqual(myobj.monkeys[3].items, [74])

        # 3. Check methods
        myobj.rounds(verbose=False, rounds=1000)
        self.assertEqual(myobj.monkeys[0].inspections, 5204)
        self.assertEqual(myobj.monkeys[1].inspections, 4792)
        self.assertEqual(myobj.monkeys[2].inspections, 199)
        self.assertEqual(myobj.monkeys[3].inspections, 5192)

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
