# ======================================================================
# Memory Reallocation
#   Advent of Code 2017 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ m e m o r y . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 5, Memory Reallocation"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_06
import memory

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

P1_EXAMPLES_TEXT = """
0  2  7  0
! In this example, the answer is 5.
"""

# ======================================================================
#                                                             TestMemory
# ======================================================================


class TestMemory(unittest.TestCase):  # pylint: disable=R0904
    """Test Memory object"""

    def test_empty_init(self):
        """Test default Memory creation"""

        # 1. Create default Jumps object
        mymem = memory.Memory()

        # 2. Make sure it has the default values
        self.assertEqual(mymem.part2, False)
        self.assertEqual(mymem.banks, [])


    def test_value_init(self):
        """Test Memory creation with values"""

        # 1. Create Memory object with values
        mymem = memory.Memory(text="0 2 7 0")

        # 2. Make sure it has the specified values
        self.assertEqual(mymem.part2, False)
        self.assertEqual(len(mymem.banks), 4)
        self.assertEqual(mymem.banks, [0, 2, 7, 0])

        # 3. Check methods
        self.assertEqual(mymem.previously_seen(), False)
        self.assertEqual(mymem.maximum(), 2)
        self.assertEqual(mymem.one_cycle(), 7)
        self.assertEqual(mymem.banks, [2, 4, 1, 2])
        self.assertEqual(mymem.maximum(), 1)
        self.assertEqual(mymem.one_cycle(), 4)
        self.assertEqual(mymem.banks, [3, 1, 2, 3])
        self.assertEqual(mymem.maximum(), 0)
        self.assertEqual(mymem.one_cycle(), 3)
        self.assertEqual(mymem.banks, [0, 2, 3, 4])
        self.assertEqual(mymem.maximum(), 3)
        self.assertEqual(mymem.one_cycle(), 4)
        self.assertEqual(mymem.banks, [1, 3, 4, 1])
        self.assertEqual(mymem.maximum(), 2)
        self.assertEqual(mymem.one_cycle(), 4)
        self.assertEqual(mymem.banks, [2, 4, 1, 2])

    def test_text_init(self):
        """Test Memory creation from text"""

        # 1. Create Jumps object from text
        mymem = memory.Memory(text=aoc_06.from_text(P1_EXAMPLES_TEXT)[0])

        # 2. Make sure it has the specified values
        self.assertEqual(mymem.part2, False)
        self.assertEqual(len(mymem.banks), 4)
        self.assertEqual(mymem.banks, [0, 2, 7, 0])

        # 3. Check methods
        self.assertEqual(mymem.cycle_until_seen(verbose=False, limit=9), 5)

    def test_part_two(self):
        """Test Memory puzzle part two"""

        # 1. Create Jumps object from text
        mymem = memory.Memory(text=aoc_06.from_text(P1_EXAMPLES_TEXT)[0],
                              part2=True)

        # 2. Make sure it has the specified values
        self.assertEqual(mymem.part2, True)
        self.assertEqual(len(mymem.banks), 4)
        self.assertEqual(mymem.banks, [0, 2, 7, 0])

        # 3. Check methods
        self.assertEqual(mymem.cycle_until_seen(verbose=False, limit=9), 4)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ m e m o r y . p y                  end
# ======================================================================
