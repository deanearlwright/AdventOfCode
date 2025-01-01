
# ======================================================================
# Claw Contraption
#   Advent of Code 2024 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ m a c h i n e s . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 13, Claw Contraption"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_13
import machines

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 480
PART_TWO_RESULT = 875318608908

# ======================================================================
#                                                           TestMachines
# ======================================================================


class TestMachines(unittest.TestCase):  # pylint: disable=R0904
    "Test Machines object"

    def test_empty_init(self):
        "Test the default Machines creation"

        # 1. Create default Machines object
        myobj = machines.Machines()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.machines), 0)

    def test_text_init(self):
        "Test the Machines object creation from text"

        # 1. Create Machines object from text
        myobj = machines.Machines(text=aoc_13.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 12)
        self.assertEqual(len(myobj.machines), 4)
        self.assertEqual(myobj.machines[0].prize, (8400, 5400))
        self.assertEqual(myobj.machines[3].prize, (18641, 10279))

        # 3. Check methods
        self.assertEqual(myobj.machines[0].presses(), (80, 40))
        self.assertEqual(myobj.machines[1].presses(), (0, 0))
        self.assertEqual(myobj.machines[2].presses(), (38, 86))
        self.assertEqual(myobj.machines[3].presses(), (0, 0))

        self.assertEqual(myobj.tokens(), 480)

    def test_text_two(self):
        "Test the Machines object creation from text for part2"

        # 1. Create Machines object from text
        myobj = machines.Machines(text=aoc_13.from_text(EXAMPLE_TEXT), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 12)
        self.assertEqual(len(myobj.machines), 4)
        self.assertEqual(myobj.machines[0].prize, (10000000008400, 10000000005400))
        self.assertEqual(myobj.machines[3].prize, (10000000018641, 10000000010279))

        # 3. Check methods
        self.assertEqual(myobj.machines[0].presses(), (0, 0))
        self.assertEqual(myobj.machines[1].presses(), (118679050709, 103199174542))
        self.assertEqual(myobj.machines[2].presses(), (0, 0))
        self.assertEqual(myobj.machines[3].presses(), (102851800151, 107526881786))

        self.assertEqual(myobj.tokens(), 875318608908)

    def test_part_one(self):
        "Test part one example of Machines object"

        # 1. Create Machines object from text
        text = aoc_13.from_text(PART_ONE_TEXT)
        myobj = machines.Machines(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Machines object"

        # 1. Create Machines object from text
        text = aoc_13.from_text(PART_TWO_TEXT)
        myobj = machines.Machines(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ m a c h i n e s . p y                end
# ======================================================================
