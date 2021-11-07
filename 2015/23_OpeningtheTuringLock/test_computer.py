# ======================================================================
# Opening the Turing Lock
#   Advent of Code 2015 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c o m p u t e r . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 23, Opening the Turing Lock"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_23
import computer

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
inc a
jio a, +2
tpl a
inc a
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 0
PART_TWO_RESULT = 0

# ======================================================================
#                                                           TestComputer
# ======================================================================


class TestComputer(unittest.TestCase):  # pylint: disable=R0904
    "Test Computer object"

    def test_empty_init(self):
        "Test the default Computer creation"

        # 1. Create default Computer object
        myobj = computer.Computer()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 0)
        self.assertEqual(len(myobj.regs), 2)
        self.assertEqual(myobj.regs['a'], 0)
        self.assertEqual(myobj.regs['b'], 0)
        self.assertEqual(myobj.addr, 0)

    def test_text_init(self):
        "Test the Computer object creation from text"

        # 1. Create Computer object from text
        myobj = computer.Computer(text=aoc_23.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(len(myobj.regs), 2)
        self.assertEqual(myobj.regs['a'], 0)
        self.assertEqual(myobj.regs['b'], 0)
        self.assertEqual(myobj.addr, 0)

        # 3. Check methods
        self.assertEqual(myobj.step(), True)
        self.assertEqual(myobj.regs['a'], 1)
        self.assertEqual(myobj.regs['b'], 0)
        self.assertEqual(myobj.addr, 1)

        self.assertEqual(myobj.step(), True)
        self.assertEqual(myobj.regs['a'], 1)
        self.assertEqual(myobj.regs['b'], 0)
        self.assertEqual(myobj.addr, 3)

        self.assertEqual(myobj.step(), True)
        self.assertEqual(myobj.regs['a'], 2)
        self.assertEqual(myobj.regs['b'], 0)
        self.assertEqual(myobj.addr, 4)

        self.assertEqual(myobj.step(), False)
        self.assertEqual(myobj.regs['a'], 2)
        self.assertEqual(myobj.regs['b'], 0)
        self.assertEqual(myobj.addr, 4)

        myobj.reset()
        self.assertEqual(myobj.regs['a'], 0)
        self.assertEqual(myobj.regs['b'], 0)
        self.assertEqual(myobj.addr, 0)

        self.assertEqual(myobj.run(), 0)
        self.assertEqual(myobj.regs['a'], 2)
        self.assertEqual(myobj.regs['b'], 0)
        self.assertEqual(myobj.addr, 4)

    def test_part_one(self):
        "Test part one example of Computer object"

        # 1. Create Computer object from text
        myobj = computer.Computer(text=aoc_23.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Computer object"

        # 1. Create Computer object from text
        myobj = computer.Computer(part2=True, text=aoc_23.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ c o m p u t e r . p y                end
# ======================================================================
