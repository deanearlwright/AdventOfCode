# ======================================================================
# A Maze of Twisty Trampolines, All Alike
#   Advent of Code 2017 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ j u m p s . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 5, Twisty Trampolines"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_05
import jumps

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

P1_EXAMPLES_TEXT = """
0
3
0
1
-3

! In this example, the exit is reached in 5 steps.
"""

# ======================================================================
#                                                              TestJumps
# ======================================================================


class TestJumps(unittest.TestCase):  # pylint: disable=R0904
    """Test Jumps object"""

    def test_empty_init(self):
        """Test default Jumps creation"""

        # 1. Create default Jumps object
        myjumps = jumps.Jumps()

        # 2. Make sure it has the default values
        self.assertEqual(myjumps.part2, False)
        self.assertEqual(myjumps.location, 0)
        self.assertEqual(myjumps.offsets, [])

        # 3. Check methods
        self.assertEqual(myjumps.escaped(), True)

    def test_value_init(self):
        """Test PassPhrases creation with values"""

        # 1. Create Jumps object with values
        myjumps = jumps.Jumps(text=['2', '4', '0', '1', '-2'],
                              location=1)

        # 2. Make sure it has the specified values
        self.assertEqual(myjumps.part2, False)
        self.assertEqual(myjumps.location, 1)
        self.assertEqual(len(myjumps.offsets), 5)

        # 3. Check methods
        self.assertEqual(myjumps.escaped(), False)
        self.assertEqual(myjumps.one_jump(), True)
        self.assertEqual(myjumps.location, 5)
        self.assertEqual(myjumps.escaped(), True)
        self.assertEqual(myjumps.offsets, [2, 5, 0, 1, -2])

    def test_text_init(self):
        """Test Jumps creation from text"""

        # 1. Create Jumps object from text
        myjumps = jumps.Jumps(text=aoc_05.from_text(P1_EXAMPLES_TEXT))

        # 2. Make sure it has the specified values
        self.assertEqual(myjumps.part2, False)
        self.assertEqual(myjumps.location, 0)
        self.assertEqual(len(myjumps.offsets), 5)

        # 3. Check methods
        self.assertEqual(myjumps.escaped(), False)
        self.assertEqual(myjumps.goto_the_exit(), 5)
        self.assertEqual(myjumps.location, 5)
        self.assertEqual(myjumps.escaped(), True)
        self.assertEqual(myjumps.offsets, [2, 5, 0, 1, -2])

    def test_part_two(self):
        """Test Part Two"""

        # 1. Create Jumps object from text for part two
        myjumps = jumps.Jumps(text=aoc_05.from_text(P1_EXAMPLES_TEXT),
                              part2=True)

        # 2. Make sure it has the specified values
        self.assertEqual(myjumps.part2, True)
        self.assertEqual(myjumps.location, 0)
        self.assertEqual(len(myjumps.offsets), 5)

        # 3. Check methods
        self.assertEqual(myjumps.escaped(), False)
        self.assertEqual(myjumps.goto_the_exit(), 10)
        self.assertEqual(myjumps.location, 5)
        self.assertEqual(myjumps.escaped(), True)
        self.assertEqual(myjumps.offsets, [2, 3, 2, 3, -1])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ j u m p s . p y                   end
# ======================================================================
