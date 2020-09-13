# ======================================================================
# Mode Maze
#   Advent of Code 2018 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ p a t h . p y
# ======================================================================
"Test paths for Advent of Code 2018 day 22 (from 15 and 20), Mode Maze"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_22
import cave
import path

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
depth: 510
target: 10,10
"""

# ======================================================================
#                                                               TestNode
# ======================================================================


class TestNode(unittest.TestCase):  # pylint: disable=R0904
    "Test Node object"

    def test_empty_init(self):
        "Test the default Node creation"

        # 1. Create default Node object
        myobj = path.Node()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.location, None)
        self.assertEqual(myobj.previous, None)
        self.assertEqual(myobj.cave, None)
        self.assertEqual(myobj.minutes, 0)


    def test_value_init(self):
        "Test the Node object creation with location and doors"

        # 1. Create Node object from values
        mycave = cave.Cave(text=aoc_22.from_text(EXAMPLE_TEXT), part2=True)
        myobj = path.Node(location=mycave.start, cave=mycave)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.location, 100000000)
        self.assertEqual(myobj.previous, None)
        self.assertEqual(myobj.cave, mycave)
        self.assertEqual(myobj.minutes, 0)

# ======================================================================
#                                                               TestPath
# ======================================================================


class TestPath(unittest.TestCase):  # pylint: disable=R0904
    "Test Path object"

    def test_empty_init(self):
        "Test the default Path creation"

        # 1. Create default Path object
        myobj = path.Path()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.start, None)
        self.assertEqual(myobj.cave, None)
        self.assertEqual(myobj.node, None)
        self.assertEqual(len(myobj.nodes), 0)
        self.assertEqual(len(myobj.queue), 0)

    def test_value_init(self):
        "Test the Path object creation with values"

        # 1. Create Node object from values
        mycave = cave.Cave(text=aoc_22.from_text(EXAMPLE_TEXT), part2=True)
        myobj = path.Path(start=mycave.start, cave=mycave)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.start, 100000000)
        self.assertEqual(myobj.cave, mycave)
        self.assertNotEqual(myobj.node, None)
        self.assertEqual(myobj.node.location, myobj.start)
        self.assertEqual(myobj.node.cave, mycave)
        self.assertTrue(len(myobj.nodes), 4)
        self.assertEqual(len(myobj.queue), 0)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       t e s t _ p a t h . p y                  end
# ======================================================================
