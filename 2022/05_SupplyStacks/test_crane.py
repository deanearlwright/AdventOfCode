# ======================================================================
# Supply Stacks
#   Advent of Code 2022 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c r a n e . p y
# ======================================================================
"Test Crane for Advent of Code 2022 day 05, Supply Stacks"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import crane
import aoc_05

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

# ======================================================================
#                                                              TestCrane
# ======================================================================


class TestCrane(unittest.TestCase):  # pylint: disable=R0904
    "Test Crane object"

    def test_empty_init(self):
        "Test the default Crane creation"

        # 1. Create default Crane object
        myobj = crane.Crane()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.stacks), 0)
        self.assertEqual(len(myobj), 0)

    def test_text_init(self):
        "Test the Crane object creation from text"

        # 1. Create Crane object from text
        myobj = crane.Crane(aoc_05.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 8)
        self.assertEqual(len(myobj.stacks), 3)
        self.assertEqual(len(myobj.stacks[0]), 2)
        self.assertEqual(len(myobj.stacks[1]), 3)
        self.assertEqual(len(myobj.stacks[2]), 1)

        # 3. Check methods
        self.assertEqual(len(myobj), 3)
        self.assertEqual(myobj.tops(), "NDP")
        myobj.move("move 1 from 2 to 1")
        self.assertEqual(myobj.tops(), "DCP")
        myobj.move("move 3 from 1 to 3")
        self.assertEqual(myobj.tops(), " CZ")
        myobj.move("move 2 from 2 to 1")
        self.assertEqual(myobj.tops(), "M Z")
        myobj.move("move 1 from 1 to 2")
        self.assertEqual(myobj.tops(), "CMZ")


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ c r a n e . p y                   end
# ======================================================================
