
# ======================================================================
# Haunted Wasteland
#   Advent of Code 2023 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ n o d e . p y
# ======================================================================
"Test Node for Advent of Code 2023 day 08, Haunted Wasteland"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import node

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "AAA = (BBB, CCC)"

# ======================================================================
#                                                             TestNode
# ======================================================================


class TestNode(unittest.TestCase):  # pylint: disable=R0904
    "Test Node object"

    def test_empty_init(self):
        "Test the default Node creation"

        # 1. Create default Node object
        myobj = node.Node()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.name, "")
        self.assertEqual(len(myobj.next), 0)

    def test_text_init(self):
        "Test the Node object creation from text"

        # 1. Create Node object from text
        myobj = node.Node(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 16)
        self.assertEqual(myobj.name, "AAA")
        self.assertEqual(len(myobj.next), 2)

        # 3. Check methods
        self.assertEqual(myobj.next_node('L'), "BBB")
        self.assertEqual(myobj.next_node('R'), "CCC")


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ n o d e . p y                end
# ======================================================================
