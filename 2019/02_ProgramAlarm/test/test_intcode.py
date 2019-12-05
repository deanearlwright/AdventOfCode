# ======================================================================
# Program Alarm
#   Advent of Code 2019 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# codeuter simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ i n t c o d e . p y
# ======================================================================
"Test codeuter for Advent of Code 2019 day 2, Program Alarm"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import intcode

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------


# ======================================================================
#                                                            TestIntcode
# ======================================================================


class TestIntcode(unittest.TestCase):  # pylint: disable=R0904
    """Test Intcode object"""

    def test_empty_init(self):
        """Test default intcode object creation"""

        # 1. Create default Intcode object
        mycode = intcode.IntCode()

        # 2. Make sure it has the default values
        self.assertEqual(mycode.counter, 0)
        self.assertEqual(len(mycode.positions), 0)

        # 3. Check methods
        self.assertEqual(mycode.fetch(0), None)
        self.assertEqual(mycode.alter(0, 0), None)
        self.assertEqual(mycode.step(), intcode.STOP_XPC)
        mycode.reset()
        self.assertEqual(mycode.run(), intcode.STOP_XPC)

    def test_value_init(self):
        """Test Intcode object creation with values"""

        # 1. Create Intcode obhect with values
        mycode = intcode.IntCode(counter=0, positions=[99, 30, 40, 50])

        # 2. Make sure it has the specified values
        self.assertEqual(mycode.counter, 0)
        self.assertEqual(len(mycode.positions), 4)
        self.assertEqual(mycode.positions, [99, 30, 40, 50])

        # 3. Check methods
        self.assertEqual(mycode.fetch(0), 99)
        self.assertEqual(mycode.alter(0, 99), 99)
        self.assertEqual(mycode.step(), intcode.STOP_HLT)
        mycode.reset()
        self.assertEqual(mycode.run(), intcode.STOP_HLT)

    def test_text_init(self):
        """Test Intcode object creation with text"""

        # 1. Create Intcode obhect with values
        mycode = intcode.IntCode(text='1,0,0,0,99')

        # 2. Make sure it has the specified values
        self.assertEqual(mycode.counter, 0)
        self.assertEqual(len(mycode.positions), 5)
        self.assertEqual(mycode.positions, [1, 0, 0, 0, 99])

        # 3. Check methods
        self.assertEqual(mycode.fetch(0), 1)
        self.assertEqual(mycode.alter(0, 1), 1)
        self.assertEqual(mycode.step(), intcode.STOP_RUN)
        self.assertEqual(mycode.positions, [2, 0, 0, 0, 99])
        self.assertEqual(mycode.alter(0, 1), 2)
        self.assertEqual(mycode.positions, [1, 0, 0, 0, 99])
        mycode.reset()
        self.assertEqual(mycode.run(), intcode.STOP_HLT)
        self.assertEqual(mycode.positions, [2, 0, 0, 0, 99])

    def test_samples(self):
        """Test Intcode object with samples from problem description"""

        # 1. 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2)
        mycode = intcode.IntCode(text='1,0,0,0,99')
        self.assertEqual(mycode.run(), intcode.STOP_HLT)
        self.assertEqual(mycode.positions, [2, 0, 0, 0, 99])

        # 2. 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6)
        mycode = intcode.IntCode(text='2,3,0,3,99')
        self.assertEqual(mycode.run(), intcode.STOP_HLT)
        self.assertEqual(mycode.positions, [2, 3, 0, 6, 99])

        # 3. 2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801)
        mycode = intcode.IntCode(text='2,4,4,5,99,0')
        self.assertEqual(mycode.run(), intcode.STOP_HLT)
        self.assertEqual(mycode.positions, [2, 4, 4, 5, 99, 9801])

        # 4. 1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99
        mycode = intcode.IntCode(text='1,1,1,4,99,5,6,0,99')
        self.assertEqual(mycode.run(), intcode.STOP_HLT)
        self.assertEqual(mycode.positions, [30, 1, 1, 4, 2, 5, 6, 0, 99])

        # 5. 1,9,10,3,2,3,11,0,99,30,40,50 becomes 3500,9,10,70,2,3,11,0,99,30,40,50
        mycode = intcode.IntCode(text='1,9,10,3,2,3,11,0,99,30,40,50')
        self.assertEqual(mycode.run(), intcode.STOP_HLT)
        self.assertEqual(mycode.positions,
                         [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ i n t c o d e . p y                  end
# ======================================================================
