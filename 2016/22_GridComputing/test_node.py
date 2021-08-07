# ======================================================================
# Grid Computing
#   Advent of Code 2016 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      t e s t _ n o d e . p y
# ======================================================================
"Test Node for Advent of Code 2016 day 22, Grid Computing"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import node

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "/dev/grid/node-x4-y2     85T   73T    12T   85%"

# ======================================================================
#                                                               TestNode
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
        self.assertEqual(myobj.loc, (0, 0))
        self.assertEqual(myobj.size, 0)
        self.assertEqual(myobj.used, 0)
        self.assertEqual(myobj.avail, 0)

    def test_text_init(self):
        "Test the Node object creation from text"

        # 1. Create Node object from text
        myobj = node.Node(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 47)
        self.assertEqual(myobj.loc, (4, 2))
        self.assertEqual(myobj.size, 85)
        self.assertEqual(myobj.used, 73)
        self.assertEqual(myobj.avail, 12)

        # 3. Check methods
        self.assertEqual(myobj.is_empty(), False)
        self.assertEqual(myobj.is_wall(), False)
        self.assertEqual(myobj.can_hold(10), True)
        self.assertEqual(myobj.can_hold(20), False)
        locs = myobj.nearby()
        self.assertEqual(len(locs), 4)
        self.assertEqual(locs, [(3, 2), (5, 2), (4, 1), (4, 3)])
        self.assertEqual(myobj.receive(10), True)
        self.assertEqual(myobj.receive(10), False)
        self.assertEqual(myobj.used, 83)
        self.assertEqual(myobj.avail, 2)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ n o d e . p y                    end
# ======================================================================
