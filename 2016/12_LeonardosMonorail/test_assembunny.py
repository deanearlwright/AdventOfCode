# ======================================================================
# Leonardos Monorail
#   Advent of Code 2016 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ a s s e m b u n n y . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 12, Leonardos Monorail"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_12
import assembunny

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 42
PART_TWO_RESULT = 42

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

    def test_text_init(self):
        "Test the Assembunny object creation from text"

        # 1. Create Assembunny object from text
        myobj = assembunny.Assembunny(text=aoc_12.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 6)

    def test_part_one(self):
        "Test part one example of Assembunny object"

        # 1. Create Assembunny object from text
        myobj = assembunny.Assembunny(text=aoc_12.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Assembunny object"

        # 1. Create Assembunny object from text
        myobj = assembunny.Assembunny(part2=True, text=aoc_12.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end              t e s t _ a s s e m b u n n y . p y               end
# ======================================================================
