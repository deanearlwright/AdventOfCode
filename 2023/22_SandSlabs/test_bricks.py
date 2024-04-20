
# ======================================================================
# Sand Slabs
#   Advent of Code 2023 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ b r i c k s . p y
# ======================================================================
"Test Bricks for Advent of Code 2023 day 22, Sand Slabs"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import bricks

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "0,0,2~2,0,2",
    "0,2,3~2,2,3",
    "1,1,8~1,1,9",
    "0,0,4~0,2,4",
    "1,0,1~1,2,1",
    "2,0,5~2,2,5",
    "0,1,6~2,1,6",
] # rearranged to test sorting

# ======================================================================
#                                                             TestBricks
# ======================================================================


class TestBricks(unittest.TestCase):  # pylint: disable=R0904
    "Test Bricks object"

    def test_empty_init(self):
        "Test the default Bricks creation"

        # 1. Create default Bricks object
        myobj = bricks.Bricks()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.bricks), 0)

    def test_text_init(self):
        "Test the Bricks object creation from text"

        # 1. Create Bricks object from text
        myobj = bricks.Bricks(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 7)
        self.assertEqual(len(myobj.bricks), 7)
        self.assertEqual(myobj.bricks[0].corners, ((1, 0, 1), (1, 2, 1)))
        self.assertEqual(myobj.bricks[-1].corners, ((1, 1, 8), (1, 1, 9)))

        # 3. Check methods
        self.assertEqual(myobj.drop(), 5)
        self.assertEqual(myobj.bricks[0].corners, ((1, 0, 1), (1, 2, 1)))
        self.assertEqual(myobj.bricks[-1].corners, ((1, 1, 5), (1, 1, 6)))

        self.assertEqual(myobj.drop(modify=False, minus=myobj.bricks[0]), 6)
        self.assertEqual(myobj.drop(modify=False, minus=myobj.bricks[1]), 0)
        self.assertEqual(myobj.drop(modify=False, minus=myobj.bricks[2]), 0)
        self.assertEqual(myobj.drop(modify=False, minus=myobj.bricks[3]), 0)
        self.assertEqual(myobj.drop(modify=False, minus=myobj.bricks[4]), 0)
        self.assertEqual(myobj.drop(modify=False, minus=myobj.bricks[5]), 1)
        self.assertEqual(myobj.drop(modify=False, minus=myobj.bricks[6]), 0)

        self.assertEqual(myobj.disingratable(), 5)
        self.assertEqual(myobj.chain_reaction(), 7)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------

if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ b r i c k s . p y                end
# ======================================================================
