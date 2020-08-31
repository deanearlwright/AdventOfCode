# ======================================================================
# Beverage Bandits
#   Advent of Code 2018 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ p a t h . p y
# ======================================================================
"Test paths for Advent of Code 2018 day 15, Beverage Bandits"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_15
import cave
import path

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######
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
        self.assertEqual(myobj.steps, 0)
        self.assertEqual(myobj.distance, None)
        self.assertEqual(myobj.shortest, [])
        self.assertEqual(myobj.adjacent, [None, None, None, None])


    def test_value_init(self):
        "Test the Node object creation with location and cave"

        # 1. Create Node object from values
        mycave = cave.Cave(text=aoc_15.from_text(EXAMPLE_TEXT))
        myobj = path.Node(location=102, cave=mycave)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.location, 102)
        self.assertEqual(myobj.previous, None)
        self.assertEqual(myobj.cave, mycave)
        self.assertEqual(myobj.steps, 0)
        self.assertEqual(myobj.distance, None)
        self.assertEqual(myobj.shortest, [])
        self.assertEqual(myobj.adjacent, [None, 101, 103, 202])

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
        self.assertEqual(myobj.source, None)
        self.assertEqual(myobj.destination, None)
        self.assertEqual(myobj.cave, None)
        self.assertEqual(myobj.node, None)
        self.assertEqual(myobj.distance, None)
        self.assertEqual(len(myobj.nodes), 0)
        self.assertEqual(len(myobj.queue), 0)

    def test_value_init(self):
        "Test the Path object creation with values"

        # 1. Create Node object from values
        mycave = cave.Cave(text=aoc_15.from_text(EXAMPLE_TEXT))
        myobj = path.Path(source=102, destination=104, cave=mycave)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.source, 102)
        self.assertEqual(myobj.destination, 104)
        self.assertEqual(myobj.cave, mycave)
        self.assertNotEqual(myobj.node, None)
        self.assertEqual(myobj.node.location, myobj.source)
        self.assertEqual(myobj.node.cave, mycave)
        self.assertEqual(myobj.distance, 2)
        self.assertTrue(len(myobj.nodes) > 0)
        self.assertEqual(len(myobj.queue), 0)

    def test_longer_init(self):
        "Test the Path object creation with values with a longer path"

        # 1. Create Node object from values
        mycave = cave.Cave(text=aoc_15.from_text(EXAMPLE_TEXT))
        myobj = path.Path(source=102, destination=505, cave=mycave)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.source, 102)
        self.assertEqual(myobj.destination, 505)
        self.assertEqual(myobj.cave, mycave)
        self.assertNotEqual(myobj.node, None)
        self.assertEqual(myobj.node.location, myobj.source)
        self.assertEqual(myobj.node.cave, mycave)
        self.assertEqual(myobj.distance, 9)
        self.assertTrue(len(myobj.nodes) > 0)
        self.assertEqual(len(myobj.queue), 0)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       t e s t _ p a t h . p y                  end
# ======================================================================
