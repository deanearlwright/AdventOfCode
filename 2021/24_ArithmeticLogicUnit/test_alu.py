# ======================================================================
# Arithmetic Logic Unit
#   Advent of Code 2021 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ a l u . p y
# ======================================================================
"Test Alu for Advent of Code 2021 day 24, Arithmetic Logic Unit"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_24
import alu

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_ONE = """
inp x
mul x -1
"""
EXAMPLE_TWO = """
inp z
inp x
mul z 3
eql z x
"""
EXAMPLE_THREE = """
inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2
"""
# ======================================================================
#                                                                TestAlu
# ======================================================================


class TestAlu(unittest.TestCase):  # pylint: disable=R0904
    "Test Alu object"

    def test_empty_init(self):
        "Test the default Alu creation"

        # 1. Create default Alu object
        myobj = alu.Alu()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.regs), 4)
        self.assertEqual(len(myobj.inst), 0)
        self.assertEqual(myobj.step, 0)
        self.assertEqual(len(myobj.inp), 0)

    def test_text_one(self):
        "Test the Alu object creation from text - example one"

        # 1. Create Alu object from text
        myobj = alu.Alu(text=aoc_24.from_text(EXAMPLE_ONE), inp='6')

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 2)
        self.assertEqual(len(myobj.regs), 4)
        self.assertEqual(len(myobj.inst), 2)
        self.assertEqual(myobj.step, 0)
        self.assertEqual(len(myobj.inp), 1)

        # 3. Check methods
        self.assertEqual(myobj.regs['w'], 0)
        self.assertEqual(myobj.regs['x'], 0)
        self.assertEqual(myobj.regs['y'], 0)
        self.assertEqual(myobj.regs['z'], 0)
        self.assertEqual(myobj.one_step(), True)
        self.assertEqual(myobj.regs['w'], 0)
        self.assertEqual(myobj.regs['x'], 6)
        self.assertEqual(myobj.regs['y'], 0)
        self.assertEqual(myobj.regs['z'], 0)
        self.assertEqual(myobj.step, 1)
        self.assertEqual(len(myobj.inp), 0)
        self.assertEqual(myobj.one_step(), True)
        self.assertEqual(myobj.regs['w'], 0)
        self.assertEqual(myobj.regs['x'], -6)
        self.assertEqual(myobj.regs['y'], 0)
        self.assertEqual(myobj.regs['z'], 0)
        self.assertEqual(myobj.step, 2)
        self.assertEqual(len(myobj.inp), 0)
        self.assertEqual(myobj.one_step(), False)
        self.assertEqual(myobj.regs['w'], 0)
        self.assertEqual(myobj.regs['x'], -6)
        self.assertEqual(myobj.regs['y'], 0)
        self.assertEqual(myobj.regs['z'], 0)
        self.assertEqual(myobj.step, 2)
        self.assertEqual(len(myobj.inp), 0)

    def test_text_two(self):
        "Test the Alu object creation from text - example two"

        # 1. Create Alu object from text
        myobj = alu.Alu(text=aoc_24.from_text(EXAMPLE_TWO), inp='26')

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(len(myobj.regs), 4)
        self.assertEqual(len(myobj.inst), 4)
        self.assertEqual(myobj.step, 0)
        self.assertEqual(len(myobj.inp), 2)

        # 3. Check methods
        self.assertEqual(myobj.regs['w'], 0)
        self.assertEqual(myobj.regs['x'], 0)
        self.assertEqual(myobj.regs['y'], 0)
        self.assertEqual(myobj.regs['z'], 0)
        self.assertEqual(myobj.one_step(), True)
        self.assertEqual(myobj.regs['w'], 0)
        self.assertEqual(myobj.regs['x'], 0)
        self.assertEqual(myobj.regs['y'], 0)
        self.assertEqual(myobj.regs['z'], 2)
        self.assertEqual(myobj.step, 1)
        self.assertEqual(len(myobj.inp), 1)
        self.assertEqual(myobj.one_step(), True)
        self.assertEqual(myobj.regs['w'], 0)
        self.assertEqual(myobj.regs['x'], 6)
        self.assertEqual(myobj.regs['y'], 0)
        self.assertEqual(myobj.regs['z'], 2)
        self.assertEqual(myobj.step, 2)
        self.assertEqual(len(myobj.inp), 0)
        self.assertEqual(myobj.one_step(), True)
        self.assertEqual(myobj.regs['w'], 0)
        self.assertEqual(myobj.regs['x'], 6)
        self.assertEqual(myobj.regs['y'], 0)
        self.assertEqual(myobj.regs['z'], 6)
        self.assertEqual(myobj.step, 3)
        self.assertEqual(len(myobj.inp), 0)
        self.assertEqual(myobj.one_step(), True)
        self.assertEqual(myobj.regs['w'], 0)
        self.assertEqual(myobj.regs['x'], 6)
        self.assertEqual(myobj.regs['y'], 0)
        self.assertEqual(myobj.regs['z'], 1)
        self.assertEqual(myobj.step, 4)
        self.assertEqual(len(myobj.inp), 0)
        self.assertEqual(myobj.one_step(), False)
        self.assertEqual(myobj.regs['w'], 0)
        self.assertEqual(myobj.regs['x'], 6)
        self.assertEqual(myobj.regs['y'], 0)
        self.assertEqual(myobj.regs['z'], 1)
        self.assertEqual(myobj.step, 4)
        self.assertEqual(len(myobj.inp), 0)

    def test_text_three(self):
        "Test the Alu object creation from text - example three"

        # 1. Create Alu object from text
        myobj = alu.Alu(text=aoc_24.from_text(EXAMPLE_THREE), inp='6')

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 11)
        self.assertEqual(len(myobj.regs), 4)
        self.assertEqual(len(myobj.inst), 11)
        self.assertEqual(myobj.step, 0)
        self.assertEqual(len(myobj.inp), 1)

        # 3. Check methods
        self.assertEqual(myobj.regs['w'], 0)
        self.assertEqual(myobj.regs['x'], 0)
        self.assertEqual(myobj.regs['y'], 0)
        self.assertEqual(myobj.regs['z'], 0)
        self.assertEqual(myobj.run(), 0)
        self.assertEqual(myobj.regs['w'], 0)
        self.assertEqual(myobj.regs['x'], 1)
        self.assertEqual(myobj.regs['y'], 1)
        self.assertEqual(myobj.regs['z'], 0)
        self.assertEqual(len(myobj.inp), 0)
        self.assertEqual(myobj.one_step(), False)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      t e s t _ a l u . p y                     end
# ======================================================================
