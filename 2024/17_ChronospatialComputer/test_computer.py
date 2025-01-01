
# ======================================================================
# Chronospatial Computer
#   Advent of Code 2024 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c o m p u t e r . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 17, Chronospatial Computer"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_17
import computer

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""
INST_ONE = """
Register A: 0
Register B: 0
Register C: 9

Program: 2,6
"""
INST_TWO = """
Register A: 10
Register B: 0
Register C: 0

Program: 5,0,5,1,5,4
"""
INST_THREE = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""
INST_FOUR = """
Register A: 0
Register B: 29
Register C: 0

Program: 1,7
"""
INST_FIVE = """
Register A: 0
Register B: 2024
Register C: 43690

Program: 4,0
"""
EXAMPLE_TWO = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TWO

PART_ONE_RESULT = "4,6,3,5,6,3,5,2,1,0"
PART_TWO_RESULT = 117440

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
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.registers, [0, 0, 0])
        self.assertEqual(myobj.instructions, [])
        self.assertEqual(myobj.pointer, 0)

    def test_text_init(self):
        "Test the Computer object creation from text"

        # 1. Create Computer object from text
        myobj = computer.Computer(text=aoc_17.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(myobj.registers, [729, 0, 0])
        self.assertEqual(myobj.instructions, [0, 1, 5, 4, 3, 0])
        self.assertEqual(myobj.pointer, 0)

        # 3. Check methods
        myobj.run()
        self.assertEqual(myobj.output, [4, 6, 3, 5, 6, 3, 5, 2, 1, 0])

    def test_inst_one(self):
        "Test the Computer operation for first instruction example"

        # 1. Create Computer object from text
        myobj = computer.Computer(text=aoc_17.from_text(INST_ONE))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(myobj.registers, [0, 0, 9])
        self.assertEqual(myobj.instructions, [2, 6])
        self.assertEqual(myobj.pointer, 0)

        # 3. Check methods
        self.assertFalse(myobj.step())
        self.assertEqual(myobj.registers, [0, 1, 9])

    def test_inst_two(self):
        "Test the Computer operation for second instruction example"

        # 1. Create Computer object from text
        myobj = computer.Computer(text=aoc_17.from_text(INST_TWO))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(myobj.registers, [10, 0, 0])
        self.assertEqual(myobj.instructions, [5, 0, 5, 1, 5, 4])
        self.assertEqual(myobj.pointer, 0)

        # 3. Check methods
        myobj.run()
        self.assertEqual(myobj.output, [0, 1, 2])

    def test_inst_three(self):
        "Test the Computer operation for third instruction example"

        # 1. Create Computer object from text
        myobj = computer.Computer(text=aoc_17.from_text(INST_THREE))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(myobj.registers, [2024, 0, 0])
        self.assertEqual(myobj.instructions, [0, 1, 5, 4, 3, 0])
        self.assertEqual(myobj.pointer, 0)

        # 3. Check methods
        myobj.run()
        self.assertEqual(myobj.output, [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0])
        self.assertEqual(myobj.registers, [0, 0, 0])

    def test_inst_four(self):
        "Test the Computer operation for fourth instruction example"

        # 1. Create Computer object from text
        myobj = computer.Computer(text=aoc_17.from_text(INST_FOUR))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(myobj.registers, [0, 29, 0])
        self.assertEqual(myobj.instructions, [1, 7])
        self.assertEqual(myobj.pointer, 0)

        # 3. Check methods
        myobj.run()
        self.assertEqual(myobj.registers, [0, 26, 0])

    def test_inst_five(self):
        "Test the Computer operation for fifth instruction example"

        # 1. Create Computer object from text
        myobj = computer.Computer(text=aoc_17.from_text(INST_FIVE))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(myobj.registers, [0, 2024, 43690])
        self.assertEqual(myobj.instructions, [4, 0])
        self.assertEqual(myobj.pointer, 0)

        # 3. Check methods
        myobj.run()
        self.assertEqual(myobj.registers, [0, 44354, 43690])

    def test_inst_for_part2(self):
        "Test the Computer operation for fifth instruction example"

        # 1. Create Computer object from text
        myobj = computer.Computer(text=aoc_17.from_text(EXAMPLE_TWO), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(myobj.registers, [2024, 0, 0])
        self.assertEqual(myobj.instructions, [0, 3, 5, 4, 3, 0])
        self.assertEqual(myobj.pointer, 0)

        # 3. Check methods
        self.assertEqual(myobj.find_copy(), 117440)

    def test_part_one(self):
        "Test part one example of Computer object"

        # 1. Create Computer object from text
        text = aoc_17.from_text(PART_ONE_TEXT)
        myobj = computer.Computer(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Computer object"

        # 1. Create Computer object from text
        text = aoc_17.from_text(PART_TWO_TEXT)
        myobj = computer.Computer(part2=True, text=text)

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
