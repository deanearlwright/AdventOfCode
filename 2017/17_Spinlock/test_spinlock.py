# ======================================================================
# Spinlock
#   Advent of Code 2017 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s p i n l o c k . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 17, Spinlock"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_17
import spinlock

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

EXAMPLE_STEP = 3
EXAMPLE_TEXT = "3"
PART_ONE_STR = """
(0)
0 (1)
0 (2) 1
0  2 (3) 1
0  2 (4) 3  1
0 (5) 2  4  3  1
0  5  2  4  3 (6) 1
0  5 (7) 2  4  3  6  1
0  5  7  2  4  3 (8) 6  1
0 (9) 5  7  2  4  3  8  6  1
"""

PART_ONE_RESULT = 638

PART_TWO_RESULT = None

# ======================================================================
#                                                               Spinlock
# ======================================================================


class TestSpinkock(unittest.TestCase):  # pylint: disable=R0904
    """Test circular buffer spinlock object"""

    def test_empty_init(self):
        """Test the default Spinkock creation"""

        # 1. Create default Spinlock object
        mylock = spinlock.Spinlock()

        # 2. Make sure it has the default values
        self.assertEqual(mylock.part2, False)
        self.assertEqual(mylock.text, None)

    def test_text_init(self):
        """Test the Spinlock object creation from text"""

        # 1. Create Spinlock object from text
        mylock = spinlock.Spinlock(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(mylock.part2, False)
        self.assertEqual(mylock.text, EXAMPLE_TEXT)

    def test_part_one_initial(self):
        """Test initial Spinlock step step by step from example"""

        # 1. Create Spinlock object from text
        mylock = spinlock.Spinlock(text=EXAMPLE_TEXT)

        # 2. Split example buffer text into a list
        part_one_buffers = aoc_17.from_text(PART_ONE_STR)

        # 3. Loop for the configurations in the example
        for configuration in part_one_buffers:

            # 4. Check this configuration
            self.assertEqual(str(mylock), configuration)

            # 5. Advance the spinlock one step
            mylock.advance()

        # 6. Spin until the end
        mylock.spin(spinlock.P1_LAST_NUMBER, verbose=False)

        # 7. Check the number in the next position
        self.assertEqual(mylock.buffer[0], 0)
        self.assertEqual(mylock.buffer[mylock.position], spinlock.P1_LAST_NUMBER)
        self.assertEqual(mylock.buffer[mylock.position+1], PART_ONE_RESULT)

    def test_part_one(self):
        """Test final dancer configuration from example"""

        # 1. Create Spinlock object from text
        mylock = spinlock.Spinlock(text=EXAMPLE_TEXT)

        # 2. Check the dancers after executing the steps
        self.assertEqual(mylock.part_one(verbose=False), PART_ONE_RESULT)


    def not_test_part_two(self):
        """Test final dancer configuration from example for part two"""

        # 1. Create Spinlock object from text
        mylock = spinlock.Spinlock(text=EXAMPLE_TEXT, part2=True)

        # 2. Check the dancers after executing the steps
        self.assertEqual(mylock.part_two(verbose=True), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ s p i n l o c k . p y                end
# ======================================================================
