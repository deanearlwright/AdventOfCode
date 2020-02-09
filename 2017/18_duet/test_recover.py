# ======================================================================
# duet
#   Advent of Code 2017 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r e c o v e r . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 18, duet"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_18
import recover

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
"""

PART_ONE_TEXT = """
set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
"""

PART_TWO_TEXT = """
snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d
"""

PART_ONE_RESULT = 4
PART_TWO_RESULT = 3

# ======================================================================
#                                                                  Recover
# ======================================================================


class TestRecover(unittest.TestCase):  # pylint: disable=R0904
    "Test Recover object"

    def test_empty_init(self):
        "Test the default Recover creation"

        # 1. Create default Recover object
        myobj = recover.Recover()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.instructions), 0)
        self.assertEqual(myobj.position, [0, 0])
        self.assertEqual(myobj.proc, 0)
        self.assertEqual(myobj.sound, None)
        self.assertEqual(myobj.recovered, None)
        self.assertEqual(len(myobj.registers), 2)
        self.assertEqual(len(myobj.registers[0]), 26)
        self.assertEqual(myobj.registers[0]['a'], 0)
        self.assertEqual(myobj.registers[0]['p'], 0)
        self.assertEqual(myobj.registers[0]['z'], 0)

    def test_text_init(self):
        "Test the Recover object creation from text"

        # 1. Create Recover object from text
        myobj = recover.Recover(text=aoc_18.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.instructions), 10)
        self.assertEqual(myobj.instructions[0], ('set', 'a', 1))
        self.assertEqual(myobj.instructions[9], ('jgz', 'a', -2))
        self.assertEqual(myobj.position, [0, 0])
        self.assertEqual(myobj.proc, 0)
        self.assertEqual(myobj.sound, None)
        self.assertEqual(myobj.recovered, None)
        self.assertEqual(len(myobj.registers[0]), 26)
        self.assertEqual(myobj.registers[0]['a'], 0)
        self.assertEqual(myobj.registers[0]['p'], 0)
        self.assertEqual(myobj.registers[0]['z'], 0)

        # 3. Do a few steps
        # 3a. The first four instructions set a to 1, add 2 to it, square it, and
        #     then set it to itself modulo 5, resulting in a value of 4.
        self.assertEqual(myobj.step(), True) # set a 1
        self.assertEqual(myobj.position[0], 1)
        self.assertEqual(myobj.registers[0]['a'], 1)
        self.assertEqual(myobj.sound, None)
        self.assertEqual(myobj.recovered, None)
        self.assertEqual(myobj.step(), True) # add a 2
        self.assertEqual(myobj.position[0], 2)
        self.assertEqual(myobj.registers[0]['a'], 3)
        self.assertEqual(myobj.sound, None)
        self.assertEqual(myobj.recovered, None)
        self.assertEqual(myobj.step(), True) # mul a a
        self.assertEqual(myobj.position[0], 3)
        self.assertEqual(myobj.registers[0]['a'], 9)
        self.assertEqual(myobj.sound, None)
        self.assertEqual(myobj.recovered, None)
        self.assertEqual(myobj.step(), True) # mod a 5
        self.assertEqual(myobj.position[0], 4)
        self.assertEqual(myobj.registers[0]['a'], 4)
        self.assertEqual(myobj.sound, None)
        self.assertEqual(myobj.recovered, None)
        # 3b. Then, a sound with frequency 4 (the value of a) is played.
        self.assertEqual(myobj.step(), True) # snd a
        self.assertEqual(myobj.position[0], 5)
        self.assertEqual(myobj.registers[0]['a'], 4)
        self.assertEqual(myobj.sound, 4)
        self.assertEqual(myobj.recovered, None)
        # 3c. After that, a is set to 0, causing the subsequent rcv and jgz
        #     instructions to both be skipped (rcv because a is 0, and jgz because a
        #     is not greater than 0).
        self.assertEqual(myobj.step(), True) # set a 0
        self.assertEqual(myobj.position[0], 6)
        self.assertEqual(myobj.registers[0]['a'], 0)
        self.assertEqual(myobj.sound, 4)
        self.assertEqual(myobj.recovered, None)
        self.assertEqual(myobj.step(), True) # rcv a
        self.assertEqual(myobj.position[0], 7)
        self.assertEqual(myobj.registers[0]['a'], 0)
        self.assertEqual(myobj.sound, 4)
        self.assertEqual(myobj.recovered, None)
        self.assertEqual(myobj.step(), True) # jgz a -1
        self.assertEqual(myobj.position[0], 8)
        self.assertEqual(myobj.registers[0]['a'], 0)
        self.assertEqual(myobj.sound, 4)
        self.assertEqual(myobj.recovered, None)
        # 3d. Finally, a is set to 1, causing the next jgz instruction to activate,
        #     jumping back two instructions to another jump, which jumps again to
        #     the rcv, which ultimately triggers the recover operation.
        self.assertEqual(myobj.step(), True) # set a 1
        self.assertEqual(myobj.position[0], 9)
        self.assertEqual(myobj.registers[0]['a'], 1)
        self.assertEqual(myobj.sound, 4)
        self.assertEqual(myobj.recovered, None)
        self.assertEqual(myobj.step(), True) # jgz a -2
        self.assertEqual(myobj.position[0], 7)
        self.assertEqual(myobj.registers[0]['a'], 1)
        self.assertEqual(myobj.sound, 4)
        self.assertEqual(myobj.recovered, None)
        self.assertEqual(myobj.step(), True) # jgz a -1
        self.assertEqual(myobj.position[0], 6)
        self.assertEqual(myobj.registers[0]['a'], 1)
        self.assertEqual(myobj.sound, 4)
        self.assertEqual(myobj.recovered, None)
        self.assertEqual(myobj.step(), True) # rcv a
        self.assertEqual(myobj.position[0], 7)
        self.assertEqual(myobj.registers[0]['a'], 1)
        self.assertEqual(myobj.sound, 4)
        self.assertEqual(myobj.recovered, 4)


    def test_part_one(self):
        "Test part one example of Recover object"

        # 1. Create Spinlock object from text
        myobj = recover.Recover(text=aoc_18.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Recover object"

        # 1. Create Spinlock object from text
        myobj = recover.Recover(part2=True, text=aoc_18.from_text(PART_TWO_TEXT))

        # 2. Check the part two
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)
        self.assertEqual(myobj.registers[0]['c'], 1)
        self.assertEqual(myobj.registers[1]['c'], 0)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ r e c o v e r . p y                end
# ======================================================================
