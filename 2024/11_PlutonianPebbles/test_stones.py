
# ======================================================================
# Plutonian Pebbles
#   Advent of Code 2024 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s t o n e s . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 11, Plutonian Pebbles"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_11
import stones

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
125 17
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 55312
PART_TWO_RESULT = 65601038650482

# ======================================================================
#                                                             TestStones
# ======================================================================


class TestStones(unittest.TestCase):  # pylint: disable=R0904
    "Test Stones object"

    def test_empty_init(self):
        "Test the default Stones creation"

        # 1. Create default Stones object
        myobj = stones.Stones()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.stones), 0)
        self.assertEqual(len(myobj.counts), 0)

    def test_text_init(self):
        "Test the Stones object creation from text"

        # 1. Create Stones object from text
        myobj = stones.Stones(text=aoc_11.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(len(myobj.stones), 2)
        self.assertEqual(myobj.stones[0], 125)
        self.assertEqual(myobj.stones[1], 17)
        self.assertEqual(len(myobj.counts), 2)
        self.assertEqual(myobj.counts[125], 1)
        self.assertEqual(myobj.counts[17], 1)

        # 3. Test methods
        myobj.blink()
        self.assertEqual(len(myobj.stones), 3)
        self.assertEqual(myobj.stones[0], 253000)
        self.assertEqual(myobj.stones[1], 1)
        self.assertEqual(myobj.stones[2], 7)
        myobj.blink()
        self.assertEqual(len(myobj.stones), 4)
        myobj.blink()
        self.assertEqual(len(myobj.stones), 5)
        myobj.blink()
        self.assertEqual(len(myobj.stones), 9)
        myobj.blink()
        self.assertEqual(len(myobj.stones), 13)
        myobj.blink()
        self.assertEqual(len(myobj.stones), 22)

        myobj.count_blinks(25)
        self.assertEqual(sum(myobj.counts.values()), PART_ONE_RESULT)

    def test_part_one(self):
        "Test part one example of Stones object"

        # 1. Create Stones object from text
        text = aoc_11.from_text(PART_ONE_TEXT)
        myobj = stones.Stones(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Stones object"

        # 1. Create Stones object from text
        text = aoc_11.from_text(PART_TWO_TEXT)
        myobj = stones.Stones(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ s t o n e s . p y                  end
# ======================================================================
