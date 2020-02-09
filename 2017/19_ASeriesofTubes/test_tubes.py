# ======================================================================
# A Series of Tubes
#   Advent of Code 2017 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ t u b e s . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 19, A Series of Tubes"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_19
import tubes

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+
"""
PART_ONE_TEXT = EXAMPLE_TEXT

PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = "ABCDEF"

PART_TWO_RESULT = 38

# ======================================================================
#                                                                  Tubes
# ======================================================================


class TestTubes(unittest.TestCase):  # pylint: disable=R0904
    "Test Tubes object"

    def test_empty_init(self):
        "Test the default Tubes creation"

        # 1. Create default Tubes object
        myobj = tubes.Tubes()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.start, None)
        self.assertEqual(myobj.position, None)
        self.assertEqual(myobj.direction, None)
        self.assertEqual(myobj.letters, [])
        self.assertEqual(myobj.steps, 0)

    def test_text_init(self):
        "Test the Tubes object creation from text"

        # 1. Create Tubes object from text
        myobj = tubes.Tubes(text=aoc_19.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(myobj.start, 5)
        self.assertEqual(myobj.position, (5, 0))
        self.assertEqual(myobj.direction, 'v')
        self.assertEqual(myobj.letters, [])
        self.assertEqual(myobj.steps, 0)

    def test_part_one(self):
        "Test part one example of Tubes object"

        # 1. Create Spinlock object from text
        myobj = tubes.Tubes(text=aoc_19.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Tubes object"

        # 1. Create Spinlock object from text
        myobj = tubes.Tubes(part2=True, text=aoc_19.from_text(PART_TWO_TEXT))

        # 2. Check the part two
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ t u b e s . p y                end
# ======================================================================
