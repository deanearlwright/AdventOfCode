# ======================================================================
# Grid Computing
#   Advent of Code 2016 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ g r i d . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 22, Grid Computing"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_22
import grid

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
root@ebhq-gridcenter# df -h
Filesystem              Size  Used  Avail  Use%
/dev/grid/node-x0-y0     86T   73T    13T   84%
/dev/grid/node-x0-y1     88T   65T    23T   73%
/dev/grid/node-x0-y2     88T   68T    20T   77%
/dev/grid/node-x0-y3     85T   71T    14T   83%
/dev/grid/node-x0-y4     85T   71T    14T   83%
/dev/grid/node-x1-y0     86T   69T    17T   80%
/dev/grid/node-x1-y1     94T   65T    29T   69%
/dev/grid/node-x1-y2     92T   66T    26T   71%
/dev/grid/node-x1-y3     87T   73T    14T   83%
/dev/grid/node-x1-y4     87T   73T    14T   83%
/dev/grid/node-x2-y0     86T   64T    22T   74%
/dev/grid/node-x2-y1     92T   73T    19T   79%
/dev/grid/node-x2-y2     94T   72T    22T   76%
/dev/grid/node-x2-y3     91T   72T    19T   79%
/dev/grid/node-x2-y4     91T   72T    19T   79%
/dev/grid/node-x3-y0     85T   25T    60T   30%
/dev/grid/node-x3-y1     90T   66T    24T   73%
/dev/grid/node-x3-y2    506T  492T    14T   97%
/dev/grid/node-x3-y3     93T   67T    26T   72%
/dev/grid/node-x3-y4     93T   67T    26T   72%
/dev/grid/node-x4-y0     87T   65T    22T   74%
/dev/grid/node-x4-y1     85T   68T    17T   80%
/dev/grid/node-x4-y2    506T  493T    13T   97%
/dev/grid/node-x4-y3     91T   71T    20T   78%
/dev/grid/node-x4-y4     40T    0T    40T    0%
/dev/grid/node-x5-y0     85T   64T    21T   75%
/dev/grid/node-x5-y1     90T   45T    45T   50%
/dev/grid/node-x5-y2    502T  494T     8T   98%
/dev/grid/node-x5-y3     91T   71T    20T   78%
/dev/grid/node-x5-y4     91T   71T    20T   78%

"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 7
PART_TWO_RESULT = 29

# ======================================================================
#                                                               TestGrid
# ======================================================================


class TestGrid(unittest.TestCase):  # pylint: disable=R0904
    "Test Grid object"

    def test_empty_init(self):
        "Test the default Grid creation"

        # 1. Create default Grid object
        myobj = grid.Grid()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.nodes), 0)
        self.assertEqual(myobj.max_loc, [0, 0])

        # 3. Check methods
        self.assertEqual(myobj.viable_pairs(), 0)
        self.assertEqual(myobj.find_access(), None)
        self.assertEqual(myobj.find_goal(), None)
        self.assertEqual(myobj.find_wall(), None)
        self.assertEqual(myobj.find_empty(), None)

    def test_text_init(self):
        "Test the Grid object creation from text"

        # 1. Create Grid object from text
        myobj = grid.Grid(text=aoc_22.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 32)
        self.assertEqual(len(myobj.nodes), 30)
        self.assertEqual(myobj.max_loc, [5, 4])

        # 3. Check methods
        self.assertEqual(myobj.viable_pairs(), 7)
        print(myobj)
        self.assertEqual(myobj.find_access(), myobj.nodes[(0, 0)])
        self.assertEqual(myobj.find_goal(), myobj.nodes[(5, 0)])
        self.assertEqual(myobj.find_wall(), myobj.nodes[(3, 2)])
        self.assertEqual(myobj.find_empty(), myobj.nodes[(4, 4)])

    def test_part_one(self):
        "Test part one example of Grid object"

        # 1. Create Grid object from text
        myobj = grid.Grid(text=aoc_22.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Grid object"

        # 1. Create Grid object from text
        myobj = grid.Grid(part2=True, text=aoc_22.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ g r i d . p y                    end
# ======================================================================
