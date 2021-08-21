# ======================================================================
# Some Assembly Required
#   Advent of Code 2015 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                     t e s t _ g a t e s . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 07, Some Assembly Required"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_07
import gates

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
0 -> b
g OR b -> a
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = ""

PART_ONE_RESULT = 114
PART_TWO_RESULT = None

# ======================================================================
#                                                              TestGates
# ======================================================================


class TestGates(unittest.TestCase):  # pylint: disable=R0904
    "Test Gates object"

    def test_empty_init(self):
        "Test the default Gates creation"

        # 1. Create default Gates object
        myobj = gates.Gates()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.wires), 0)

    def test_text_init(self):
        "Test the Gates object creation from text"

        # 1. Create Gates object from text
        myobj = gates.Gates(text=aoc_07.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.wires), 0)

        # 3. Check methods
        self.assertEqual(myobj.execute(["SET", 1, 1, "aa"]), 1)
        self.assertEqual(myobj.execute(["SET", 123, 123, "bb"]), 123)
        myobj.run_once()
        self.assertEqual(myobj.wires["d"], 72)
        self.assertEqual(myobj.wires["e"], 507)
        self.assertEqual(myobj.wires["f"], 492)
        self.assertEqual(myobj.wires["g"], 114)
        self.assertEqual(myobj.wires["h"], 65412)
        self.assertEqual(myobj.wires["i"], 65079)
        self.assertEqual(myobj.wires["x"], 123)
        self.assertEqual(myobj.wires["y"], 456)
        self.assertEqual(myobj.wires["a"], 114)

    def test_part_one(self):
        "Test part one example of Gates object"

        # 1. Create Gates object from text
        myobj = gates.Gates(text=aoc_07.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Gates object"

        # 1. Create Gates object from text
        myobj = gates.Gates(part2=True, text=aoc_07.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ g a t e s . p y                   end
# ======================================================================
