# ======================================================================
# Chronal Conversion
#   Advent of Code 2018 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ b i t w i s e . p y
# ======================================================================
"Test solver for Advent of Code 2018 day 21, Chronal Conversion"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_21
import bitwise

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
#ip 3
seti 123 0 4
bani 4 456 4
eqri 4 72 4
addr 4 3 3
seti 0 0 3
seti 0 9 4
bori 4 65536 2
seti 6152285 4 4
bani 2 255 1
addr 4 1 4
bani 4 16777215 4
muli 4 65899 4
bani 4 16777215 4
gtir 256 2 1
addr 1 3 3
addi 3 1 3
seti 27 4 3
seti 0 3 1
addi 1 1 5
muli 5 256 5
gtrr 5 2 5
addr 5 3 3
addi 3 1 3
seti 25 9 3
addi 1 1 1
seti 17 4 3
setr 1 9 2
seti 7 4 3
eqrr 4 0 1
addr 1 3 3
seti 5 6 3
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = ""

PART_ONE_RESULT = None
PART_TWO_RESULT = None

# ======================================================================
#                                                            TestBitwise
# ======================================================================


class TestBitwise(unittest.TestCase):  # pylint: disable=R0904
    "Test Bitwise object"

    def test_empty_init(self):
        "Test the default Bitwise creation"

        # 1. Create default Bitwise object
        myobj = bitwise.Bitwise()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.device.part2, False)
        self.assertEqual(myobj.device.text, None)
        self.assertEqual(myobj.device.pc_reg, None)
        self.assertEqual(myobj.device.program, None)
        self.assertEqual(myobj.device.regs, None)
        self.assertEqual(myobj.device.pc, None)


    def test_text_init(self):
        "Test the Bitwise object creation from text"

        # 1. Create Bitwise object from text
        myobj = bitwise.Bitwise(text=aoc_21.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 32)
        self.assertEqual(myobj.device.part2, False)
        self.assertEqual(len(myobj.device.text), 32)
        self.assertEqual(myobj.device.pc_reg, 3)
        self.assertEqual(len(myobj.device.program), 31)
        self.assertEqual(myobj.device.regs, None)
        self.assertEqual(myobj.device.pc, None)

        # 3. Step through the program
        myobj.device.reset()
        self.assertEqual(myobj.device.regs, [0, 0, 0, 0, 0, 0])
        self.assertEqual(myobj.device.pc, 0)
        myobj.device.run(verbose=True, limit=40)

    def test_part_one(self):
        "Test part one example of Bitwise object"

        # 1. Create Bitwise object from text
        myobj = bitwise.Bitwise(text=aoc_21.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Bitwise object"

        # 1. Create Bitwise object from text
        myobj = bitwise.Bitwise(part2=True, text=aoc_21.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ b i t w i s e . p y                end
# ======================================================================
