
# ======================================================================
# Claw Contraption
#   Advent of Code 2024 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ m a c h i n e . p y
# ======================================================================
"Test Machine for Advent of Code 2024 day 13, Claw Contraption"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_13
import machine

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400
"""
EXAMPLE_TWO = """
Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176
"""

# ======================================================================
#                                                            TestMachine
# ======================================================================


class TestMachine(unittest.TestCase):  # pylint: disable=R0904
    "Test Machine object"

    def test_empty_init(self):
        "Test the default Machine creation"

        # 1. Create default Machine object
        myobj = machine.Machine()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.buttons), 0)
        self.assertEqual(myobj.prize, None)

    def test_text_init(self):
        "Test the Machine object creation from text"

        # 1. Create Machine object from text
        myobj = machine.Machine(text=aoc_13.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 3)
        self.assertEqual(len(myobj.buttons), 2)
        self.assertEqual(myobj.buttons[0], (94, 34))
        self.assertEqual(myobj.buttons[1], (22, 67))
        self.assertEqual(myobj.prize, (8400, 5400))

        # 3. Check methods
        self.assertEqual(myobj.brute_presses(), (80, 40))
        self.assertEqual(myobj.brute_tokens(), 280)
        self.assertEqual(myobj.presses(), (80, 40))
        self.assertEqual(myobj.tokens(), 280)

    def test_text_part2_one(self):
        "Test the Machine object creation from text for part two"

        # 1. Create Machine object from text
        myobj = machine.Machine(text=aoc_13.from_text(EXAMPLE_TEXT), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 3)
        self.assertEqual(len(myobj.buttons), 2)
        self.assertEqual(myobj.buttons[0], (94, 34))
        self.assertEqual(myobj.buttons[1], (22, 67))
        self.assertEqual(myobj.prize, (10000000008400, 10000000005400))

        # 3. Check methods
        self.assertEqual(myobj.presses(), (0, 0))
        self.assertEqual(myobj.tokens(), 0)

    def test_text_part2_two(self):
        "Test the Machine object creation from text for part two"

        # 1. Create Machine object from text
        myobj = machine.Machine(text=aoc_13.from_text(EXAMPLE_TWO), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 3)
        self.assertEqual(len(myobj.buttons), 2)
        self.assertEqual(myobj.buttons[0], (26, 66))
        self.assertEqual(myobj.buttons[1], (67, 21))
        self.assertEqual(myobj.prize, (10000000012748, 10000000012176))

        # 3. Check methods
        self.assertEqual(myobj.presses(), (118679050709, 103199174542))
        self.assertEqual(myobj.tokens(), 459236326669)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ m a c h i n e . p y                 end
# ======================================================================
