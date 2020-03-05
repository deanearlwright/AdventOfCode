# ======================================================================
# Coprocessor Conflagration
#   Advent of Code 2017 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                t e s t _ c o n f l a g r a t i o n . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 23, Coprocessor Conflagration"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_23
import conflagration

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
set b 0
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = None
PART_TWO_RESULT = None

PRIMES = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
             59, 61, 67, 71, 73, 79, 83, 89, 97])


# ======================================================================
#                                                            TestUtility
# ======================================================================

class TestPrimes(unittest.TestCase):  # pylint: disable=R0904
    "Test utility function for primes"

    def test_is_prime(self):

        # 1. Try numbers from 10 to 100
        for number in range(10, 101):

            # 2. Check if it is prime or not
            self.assertEqual(conflagration.is_prime(number),
                             number in PRIMES)

# ======================================================================
#                                                      TestConflagration
# ======================================================================


class TestConflagration(unittest.TestCase):  # pylint: disable=R0904
    "Test Conflagration object"

    def test_empty_init(self):
        "Test the default Conflagration creation"

        # 1. Create default Conflagration object
        myobj = conflagration.Conflagration()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.instructions, [])
        self.assertEqual(myobj.position, 0)
        self.assertEqual(len(myobj.registers), len(conflagration.REGS))
        self.assertEqual(myobj.terminated, False)
        self.assertEqual(myobj.mul_knt, 0)

    def test_text_init(self):
        "Test the Conflagration object creation from text"

        # 1. Create Conflagration object from text
        myobj = conflagration.Conflagration(text=aoc_23.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 32)
        self.assertEqual(len(myobj.instructions), 32)
        self.assertEqual(myobj.position, 0)
        self.assertEqual(len(myobj.registers), len(conflagration.REGS))
        self.assertEqual(myobj.terminated, False)
        self.assertEqual(myobj.mul_knt, 0)

    def test_part_one(self):
        "Test part one example of Conflagration object"

        # 1. Create Conflagration object from text
        myobj = conflagration.Conflagration(text=aoc_23.from_text(PART_ONE_TEXT))

        # 2. Find the solution for numbers between 10 and 20
        for number in range(10, 20):

            # 3. Set the instruction value
            inst_zero = myobj.instructions[0]
            myobj.instructions[0] = (inst_zero[0], inst_zero[1], number)

            # 4. Reset the co-processor
            myobj.reset()

            # 5. Check the part one result
            self.assertEqual(myobj.part_one(verbose=False),
                             myobj.part_one_slow(verbose=False))


    def test_part_two(self):
        "Test part two example of Conflagration object"

        # 1. Create Conflagration object from text
        myobj = conflagration.Conflagration(part2=True, text=aoc_23.from_text(PART_TWO_TEXT))

        # 2. Make it easier for the slow method to complete
        inst = myobj.instructions[4]
        myobj.instructions[4] = (inst[0], inst[1], 1)
        inst = myobj.instructions[5]
        myobj.instructions[5] = (inst[0], inst[1], 0)
        inst = myobj.instructions[7]
        myobj.instructions[7] = (inst[0], inst[1], -10)

        # 2. Find the solution for numbers between 4 and 8
        for number in range(2, 2):

            # 3. Set the instruction value
            inst = myobj.instructions[0]
            myobj.instructions[0] = (inst[0], inst[1], number)

            # 4. Reset the co-processor
            myobj.reset()

            # 5. Check the part two result
            self.assertEqual(myobj.part_two(verbose=False),
                             myobj.part_two_slow(verbose=False))


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end            t e s t _ c o n f l a g r a t i o n . p y           end
# ======================================================================
