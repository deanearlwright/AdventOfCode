# ======================================================================
# Go With The Flow
#   Advent of Code 2018 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ b a c k g r o u n d . p y
# ======================================================================
"Test solver for Advent of Code 2018 day 19, Go With The Flow"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_19
import background

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = ""

PART_ONE_RESULT = 6
PART_TWO_RESULT = 11151360

# ======================================================================
#                                                         TestBackground
# ======================================================================


class TestBackground(unittest.TestCase):  # pylint: disable=R0904
    "Test Background object"

    def test_empty_init(self):
        "Test the default Background creation"

        # 1. Create default Background object
        myobj = background.Background()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.pc_reg, None)
        self.assertEqual(myobj.program, None)
        self.assertEqual(myobj.regs, None)
        self.assertEqual(myobj.pc, None)

    def test_text_init(self):
        "Test the Background object creation from text"

        # 1. Create Background object from text
        myobj = background.Background(text=aoc_19.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 8)
        self.assertEqual(myobj.pc_reg, 0)
        self.assertEqual(len(myobj.program), 7)
        self.assertEqual(myobj.program[0], ['seti', 5, 0, 1])
        self.assertEqual(myobj.program[1], ['seti', 6, 0, 2])
        self.assertEqual(myobj.program[2], ['addi', 0, 1, 0])
        self.assertEqual(myobj.program[6], ['seti', 9, 0, 5])
        self.assertEqual(myobj.regs, None)
        self.assertEqual(myobj.pc, None)

        # 3. Step through the program
        myobj.reset()
        self.assertEqual(len(myobj.regs), 6)
        self.assertEqual(myobj.regs, [0, 0, 0, 0, 0, 0])
        self.assertEqual(myobj.pc, 0)
        self.assertEqual(myobj.step(), True)
        self.assertEqual(myobj.regs, [0, 5, 0, 0, 0, 0])
        self.assertEqual(myobj.pc, 1)
        self.assertEqual(myobj.step(), True)
        self.assertEqual(myobj.regs, [1, 5, 6, 0, 0, 0])
        self.assertEqual(myobj.pc, 2)
        self.assertEqual(myobj.step(), True)
        self.assertEqual(myobj.regs, [3, 5, 6, 0, 0, 0])
        self.assertEqual(myobj.pc, 4)
        self.assertEqual(myobj.step(), True)
        self.assertEqual(myobj.regs, [5, 5, 6, 0, 0, 0])
        self.assertEqual(myobj.pc, 6)
        self.assertEqual(myobj.step(), True)
        self.assertEqual(myobj.regs, [6, 5, 6, 0, 0, 9])
        self.assertEqual(myobj.pc, 7)
        self.assertEqual(myobj.step(), False)
        self.assertEqual(myobj.regs, [6, 5, 6, 0, 0, 9])
        self.assertEqual(myobj.pc, 7)

        # 4. Run the program
        myobj.run()
        self.assertEqual(myobj.pc, 7)
        self.assertEqual(myobj.regs, [6, 5, 6, 0, 0, 9])

    def test_part_one(self):
        "Test part one example of Background object"

        # 1. Create Background object from text
        myobj = background.Background(text=aoc_19.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Background object"

        # 1. Create Background object from text
        myobj = background.Background(part2=True, text=aoc_19.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end               t e s t _ b a c k g r o u n d . p y              end
# ======================================================================
