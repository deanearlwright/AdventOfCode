# ======================================================================
# Settlers of The North Pole
#   Advent of Code 2018 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ a c r e s . p y
# ======================================================================
"Test solver for Advent of Code 2018 day 18, Settlers of The North Pole"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_18
import acres

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.
"""
AFTER_ONE = """
.......##.
......|###
.|..|...#.
..|#||...#
..##||.|#|
...#||||..
||...|||..
|||||.||.|
||||||||||
....||..|.
"""

AFTER_TWO = """
.......#..
......|#..
.|.|||....
..##|||..#
..###|||#|
...#|||||.
|||||||||.
||||||||||
||||||||||
.|||||||||
"""

AFTER_TEN = """
.||##.....
||###.....
||##......
|##.....##
|##.....##
|##....##|
||##.####|
||#####|||
||||#|||||
||||||||||
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = ""

PART_ONE_RESULT = 1147
PART_TWO_RESULT = None

# ======================================================================
#                                                              TestAcres
# ======================================================================


class TestAcres(unittest.TestCase):  # pylint: disable=R0904
    "Test Acres object"

    def test_empty_init(self):
        "Test the default Acres creation"

        # 1. Create default Acres object
        myobj = acres.Acres()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.grid, None)
        self.assertEqual(myobj.max_row, None)
        self.assertEqual(myobj.minutes, 10)

    def test_text_init(self):
        "Test the Acres object creation from text"

        # 1. Create Acres object from text
        myobj = acres.Acres(text=aoc_18.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.grid), 100)
        self.assertEqual(myobj.max_row, 9)
        self.assertEqual(myobj.minutes, 10)
        self.assertEqual(str(myobj), EXAMPLE_TEXT.strip())

        # 3. Test adjacency
        adj = myobj.adjacent(0)
        self.assertEqual(adj[acres.OPEN], 2)
        self.assertEqual(adj[acres.WOOD], 0)
        self.assertEqual(adj[acres.YARD], 1)
        adj = myobj.adjacent(1001)
        self.assertEqual(adj[acres.OPEN], 6)
        self.assertEqual(adj[acres.WOOD], 1)
        self.assertEqual(adj[acres.YARD], 1)
        adj = myobj.adjacent(2002)
        self.assertEqual(adj[acres.OPEN], 5)
        self.assertEqual(adj[acres.WOOD], 2)
        self.assertEqual(adj[acres.YARD], 1)

        # 4. Test the only universal constant
        myobj.change()
        self.assertEqual(len(myobj.grid), 100)
        self.assertEqual(str(myobj), AFTER_ONE.strip())
        myobj.change()
        self.assertEqual(len(myobj.grid), 100)
        self.assertEqual(str(myobj), AFTER_TWO.strip())
        myobj.change()
        myobj.change()
        myobj.change()
        myobj.change()
        myobj.change()
        myobj.change()
        myobj.change()
        myobj.change()
        self.assertEqual(len(myobj.grid), 100)
        self.assertEqual(str(myobj), AFTER_TEN.strip())

        # 5. Check the counts
        counts = myobj.counts()
        self.assertEqual(counts[acres.WOOD], 37)
        self.assertEqual(counts[acres.YARD], 31)
        self.assertEqual(counts[acres.RVAL], 1147)

    def test_part_one(self):
        "Test part one example of Acres object"

        # 1. Create Acres object from text
        myobj = acres.Acres(text=aoc_18.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Acres object"

        # 1. Create Acres object from text
        myobj = acres.Acres(part2=True, text=aoc_18.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ a c r e s . p y                  end
# ======================================================================
