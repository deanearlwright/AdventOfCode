
# ======================================================================
# RAM Run
#   Advent of Code 2024 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ m e m o r y . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 18, RAM Run"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_18
import memory

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 22
PART_TWO_RESULT = "6,1"

# ======================================================================
#                                                             TestMemory
# ======================================================================


class TestMemory(unittest.TestCase):  # pylint: disable=R0904
    "Test Memory object"

    def test_empty_init(self):
        "Test the default Memory creation"

        # 1. Create default Memory object
        myobj = memory.Memory()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.size, 70)
        self.assertEqual(myobj.start, (0, 0))
        self.assertEqual(myobj.exit, (70, 70))
        self.assertEqual(myobj.falling, [])
        self.assertEqual(myobj.fall, 1024)
        self.assertEqual(myobj.corrupted, set())

    def test_text_init(self):
        "Test the Memory object creation from text"

        # 1. Create Memory object from text
        myobj = memory.Memory(text=aoc_18.from_text(EXAMPLE_TEXT),
                              size=6, fall=12)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 25)
        self.assertEqual(myobj.size, 6)
        self.assertEqual(myobj.start, (0, 0))
        self.assertEqual(myobj.exit, (6, 6))
        self.assertEqual(len(myobj.falling), 25)
        self.assertEqual(myobj.fall, 12)
        self.assertEqual(len(myobj.corrupted), 12)

        # 3. Check methods
        self.assertSetEqual(set(myobj.next_step((0, 0))),
                            set([(1, 0), (0, 1)]))
        self.assertSetEqual(set(myobj.next_step((2, 0))),
                            set([(1, 0)]))
        self.assertEqual(myobj.min_steps_to_exit(), 22)
        self.assertEqual(myobj.find_blockage(), (6, 1))

    def test_part_one(self):
        "Test part one example of Memory object"

        # 1. Create Memory object from text
        text = aoc_18.from_text(PART_ONE_TEXT)
        myobj = memory.Memory(text=text, size=6, fall=12)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Memory object"

        # 1. Create Memory object from text
        text = aoc_18.from_text(PART_TWO_TEXT)
        myobj = memory.Memory(part2=True, text=text, size=6, fall=12)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ m e m o r y . p y                  end
# ======================================================================
