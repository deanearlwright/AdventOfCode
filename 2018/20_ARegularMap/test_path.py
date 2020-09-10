# ======================================================================
# A Regular Map
#   Advent of Code 2018 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ p a t h . p y
# ======================================================================
"Test paths for Advent of Code 2018 day 20 (was 15), A Regular Map"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_20
import rooms
import path

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_ONE_TEXT = """
^WNE$
"""
EXAMPLE_ONE_DOORS = 3

EXAMPLE_TWO_TEXT = """
^ENWWW(NEEE|SSE(EE|N))$
"""
EXAMPLE_TWO_DOORS = 10

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
        self.assertEqual(myobj.doors, None)
        self.assertEqual(myobj.steps, 0)
        self.assertEqual(myobj.adjacent, [None, None, None, None])


    def test_value_init(self):
        "Test the Node object creation with location and doors"

        # 1. Create Node object from values
        myrooms = rooms.Rooms(text=aoc_20.from_text(EXAMPLE_ONE_TEXT))
        myobj = path.Node(location=rooms.START, doors=myrooms.doors)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.location, rooms.START)
        self.assertEqual(myobj.previous, None)
        self.assertEqual(myobj.doors, myrooms.doors)
        self.assertEqual(myobj.steps, 0)
        self.assertEqual(myobj.adjacent, [None, None, None, -1])

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
        self.assertEqual(myobj.doors, None)
        self.assertEqual(myobj.node, None)
        self.assertEqual(len(myobj.nodes), 0)
        self.assertEqual(len(myobj.queue), 0)

    def test_value_init(self):
        "Test the Path object creation with values"

        # 1. Create Node object from values
        myrooms = rooms.Rooms(text=aoc_20.from_text(EXAMPLE_ONE_TEXT))
        myobj = path.Path(start=rooms.START, doors=myrooms.doors)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.start, rooms.START)
        self.assertEqual(myobj.doors, myrooms.doors)
        self.assertNotEqual(myobj.node, None)
        self.assertEqual(myobj.node.location, myobj.start)
        self.assertEqual(myobj.node.doors, myrooms.doors)
        self.assertTrue(myobj.nodes, 4)
        self.assertEqual(len(myobj.queue), 0)
        self.assertEqual(myobj.furthest(), EXAMPLE_ONE_DOORS)

    def test_longer_init(self):
        "Test the Path object creation with values with a longer path"

        # 1. Create Node object from values
        myrooms = rooms.Rooms(text=aoc_20.from_text(EXAMPLE_TWO_TEXT))
        myobj = path.Path(start=rooms.START, doors=myrooms.doors)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.start, rooms.START)
        self.assertEqual(myobj.doors, myrooms.doors)
        self.assertNotEqual(myobj.node, None)
        self.assertEqual(myobj.node.location, myobj.start)
        self.assertEqual(myobj.node.doors, myrooms.doors)
        self.assertTrue(myobj.nodes, 16)
        self.assertEqual(len(myobj.queue), 0)
        self.assertEqual(myobj.furthest(), EXAMPLE_TWO_DOORS)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       t e s t _ p a t h . p y                  end
# ======================================================================
