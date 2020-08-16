# ======================================================================
# Memory Maneuver
#   Advent of Code 2018 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ n o d e . p y
# ======================================================================
"Single Node for Advent of Code 2018 day 08, Memory Maneuver"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import node

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
A_METADATA = [1, 1, 2]
B_METADATA = [10, 11, 12]
C_METADATA = [2]
D_METADATA = [99]
D_CHILDREN = []
D_NODE = node.Node(children=D_CHILDREN, metadata=D_METADATA)
C_CHILDREN = [D_NODE]
C_NODE = node.Node(children=C_CHILDREN, metadata=C_METADATA)
B_CHILDREN = []
B_NODE = node.Node(children=B_CHILDREN, metadata=B_METADATA)
A_CHILDREN = [B_NODE, C_NODE]
A_NODE = node.Node(children=A_CHILDREN, metadata=A_METADATA)

NUMBERS = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

# ======================================================================
#                                                               TestNode
# ======================================================================


class TestNode(unittest.TestCase):  # pylint: disable=R0904
    "Test Node object"

    def test_empty_init(self):
        "Test the default Node creation"

        # 1. Create default License object
        myobj = node.Node()

        # 2. Make sure it has the default values
        self.assertEqual(len(myobj.children), 0)
        self.assertEqual(len(myobj.metadata), 0)

        # 3. Should have no metadata
        self.assertEqual(myobj.add_metadata_entries(), 0)

    def test_value_init(self):
        "Test the Node object creation with values"

        # 1. Create License object from text
        myobj = node.Node(children=[], metadata=[123])

        # 2. Make sure it has the expected values
        self.assertEqual(len(myobj.children), 0)
        self.assertEqual(len(myobj.metadata), 1)

        # 3. Should have  metadata
        self.assertEqual(myobj.add_metadata_entries(), 123)

    def test_example(self):
        "Test the Node object from the example"

        # 1. Make sure it has the expected values
        self.assertEqual(len(A_NODE.children), 2)
        self.assertEqual(len(A_NODE.metadata), 3)

        # 3. Should have  metadata
        self.assertEqual(A_NODE.add_metadata_entries(), 138)

    def test_from_numbers(self):
        "Test the Node object creation from numbers"

        # 1. Create License object from text
        myobj = node.from_numbers(NUMBERS.copy())

        # 2. Make sure it has the expected values
        self.assertEqual(len(myobj.children), 2)
        self.assertEqual(len(myobj.metadata), 3)

        # 3. Should have the expeced sum of metadata
        self.assertEqual(myobj.add_metadata_entries(), 138)

        # 4. Should have the expected part2 value
        self.assertEqual(myobj.value, 66)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ n o d e . p y                    end
# ======================================================================
