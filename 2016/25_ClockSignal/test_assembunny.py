# ======================================================================
# Clock Signal
#   Advent of Code 2016 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ a s s e m b u n n y . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 25, Clock Signal"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_25
import assembunny

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
cpy a d
cpy 15 c
cpy 170 b
inc d
dec b
jnz b -2
dec c
jnz c -5
cpy d a
jnz 0 0
cpy a b
cpy 0 a
cpy 2 c
jnz b 2
jnz 1 6
dec b
dec c
jnz c -4
inc a
jnz 1 -7
cpy 2 b
jnz c 2
jnz 1 4
dec b
dec c
jnz 1 -4
jnz 0 0
out b
jnz a -19
jnz 1 -21
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 180
PART_TWO_RESULT = 180

# ======================================================================
#                                                         TestAssembunny
# ======================================================================


class TestAssembunny(unittest.TestCase):  # pylint: disable=R0904
    "Test Assembunny object"

    def test_empty_init(self):
        "Test the default Assembunny creation"

        # 1. Create default Assembunny object
        myobj = assembunny.Assembunny()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.registers, {'a': 0, 'b': 0, 'c': 0, 'd': 0})
        self.assertEqual(myobj.program_counter, 0)

    def test_text_init(self):
        "Test the Assembunny object creation from text"

        # 1. Create Assembunny object from text
        myobj = assembunny.Assembunny(text=aoc_25.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 30)
        self.assertEqual(myobj.registers, {'a': 0, 'b': 0, 'c': 0, 'd': 0})
        self.assertEqual(myobj.program_counter, 0)

        # 3. Check methods

    def test_part_one(self):
        "Test part one example of Assembunny object"

        # 1. Create Assembunny object from text
        myobj = assembunny.Assembunny(text=aoc_25.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Assembunny object"

        # 1. Create Assembunny object from text
        myobj = assembunny.Assembunny(part2=True, text=aoc_25.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end               t e s t _ a s s e m b u n n y . p y              end
# ======================================================================
