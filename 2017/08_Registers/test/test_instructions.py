# ======================================================================
# I Heard You Like Registers
#   Advent of Code 2017 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                 t e s t _ i n s t r u c t i o n s . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 8, I Heard You Like Registers"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_08
import instructions

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

P1_EXAMPLES_TEXT = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10

! In this example, the largest value in any register will be 1.
"""

# ======================================================================
#                                                        TestInstruction
# ======================================================================


class TestInstruction(unittest.TestCase):  # pylint: disable=R0904
    """Test Register object"""

    def test_empty_init(self):
        """Test default Instruction creation"""

        # 1. Create default Instruction object
        myinst = instructions.Instruction()

        # 2. Make sure it has the default values
        self.assertEqual(myinst.actreg, None)
        self.assertEqual(myinst.action, 'inc')
        self.assertEqual(myinst.actval, 0)
        self.assertEqual(myinst.cmpreg, None)
        self.assertEqual(myinst.cmpopr, '==')
        self.assertEqual(myinst.cmpval, 0)


    def test_value_init(self):
        """Test Instruction creation with values"""

        # 1. Create Memory object with values
        #
        myinst = instructions.Instruction(actreg='b', action='inc', actval=5,
                                          cmpreg='a', cmpopr='>', cmpval=1)

        # 2. Make sure it has the specified values
        self.assertEqual(myinst.actreg, 'b')
        self.assertEqual(myinst.action, 'inc')
        self.assertEqual(myinst.actval, 5)
        self.assertEqual(myinst.cmpreg, 'a')
        self.assertEqual(myinst.cmpopr, '>')
        self.assertEqual(myinst.cmpval, 1)


    def test_text_init(self):
        """Test Instruction creation from text"""

        # 1. Create Instruction object from text
        myinst = instructions.Instruction(text="b inc 5 if a > 1")

        # 2. Make sure it has the specified values
        self.assertEqual(myinst.actreg, 'b')
        self.assertEqual(myinst.action, 'inc')
        self.assertEqual(myinst.actval, 5)
        self.assertEqual(myinst.cmpreg, 'a')
        self.assertEqual(myinst.cmpopr, '>')
        self.assertEqual(myinst.cmpval, 1)


# ======================================================================
#                                                       TestInstructions
# ======================================================================


class TestInstructions(unittest.TestCase):  # pylint: disable=R0904
    """Test Instructions object"""

    def test_empty_init(self):
        """Test default Instructions creation"""

        # 1. Create default Jumps object
        myinsts = instructions.Instructions()

        # 2. Make sure it has the default values
        self.assertEqual(myinsts.part2, False)
        self.assertEqual(myinsts.insts, [])


    def test_value_init(self):
        """Test Instructions creation with values"""

        # 1. Create Instructions object with values
        myinsts = instructions.Instructions(text=["b inc 5 if a > 1",
                                                  "a inc 1 if b < 5",
                                                  "c dec -10 if a >= 1",
                                                  "c inc -20 if c == 10"])

        # 2. Make sure it has the specified values
        self.assertEqual(myinsts.part2, False)
        self.assertEqual(len(myinsts.insts), 4)

        # 3. Check methods

    def test_text_init(self):
        """Test Instructs creation from text"""

        # 1. Create Jumps object from text
        myinsts = instructions.Instructions(text=aoc_08.from_text(P1_EXAMPLES_TEXT))

        # 2. Make sure it has the specified values
        self.assertEqual(myinsts.part2, False)
        self.assertEqual(len(myinsts.insts), 4)

        # 3. Check methods
        self.assertEqual(myinsts.largest(verbose=False), 1)

    def test_part_two(self):
        """Test Discs creation from text"""

        # 1. Create Jumps object from text
        myinsts = instructions.Instructions(text=aoc_08.from_text(P1_EXAMPLES_TEXT),
                                            part2=True)

        # 2. Make sure it has the specified values
        self.assertEqual(myinsts.part2, True)
        self.assertEqual(len(myinsts.insts), 4)

        # 3. Check methods
        self.assertEqual(myinsts.largest(verbose=False), 1)

        # 4. Check part two methods
        self.assertEqual(myinsts.highest(verbose=False), 10)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end            t e s t _ i n s t r u c t i o n s . p y             end
# ======================================================================
