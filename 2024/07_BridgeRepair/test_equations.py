
# ======================================================================
# Bridge Repair
#   Advent of Code 2024 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ e q u a t i o n s . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 07, Bridge Repair"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_07
import equations

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 3749
PART_TWO_RESULT = 11387

# ======================================================================
#                                                          TestEquations
# ======================================================================


class TestEquations(unittest.TestCase):  # pylint: disable=R0904
    "Test Equations object"

    def test_empty_init(self):
        "Test the default Equations creation"

        # 1. Create default Equations object
        myobj = equations.Equations()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.equations), 0)

    def test_text_init(self):
        "Test the Equations object creation from text"

        # 1. Create Equations object from text
        myobj = equations.Equations(text=aoc_07.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 9)
        self.assertEqual(len(myobj.equations), 9)

    def test_part_one(self):
        "Test part one example of Equations object"

        # 1. Create Equations object from text
        text = aoc_07.from_text(PART_ONE_TEXT)
        myobj = equations.Equations(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Equations object"

        # 1. Create Equations object from text
        text = aoc_07.from_text(PART_TWO_TEXT)
        myobj = equations.Equations(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                t e s t _ e q u a t i o n s . p y               end
# ======================================================================
