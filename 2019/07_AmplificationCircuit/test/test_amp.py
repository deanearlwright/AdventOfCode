# ======================================================================
# Amplification Circuit
#   Advent of Code 2019 Day 0p -- Eric Wastl -- https://adventofcode.com
#
# codeuter simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        t e s t _ u a m a p . p y
# ======================================================================
"Test Amp[s] for Advent of Code 2019 day 7, Amplification Circuit"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from __future__ import print_function

import unittest

import amp

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
PROG1 = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
BEST1 = 43210  # from phase setting sequence 4,3,2,1,0
PROG2 = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'
BEST2 = 54321  # from phase setting sequence 0,1,2,3,4
PROG3 = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'
BEST3 = 65210  # from phase setting sequence 1,0,4,3,2

FB_PROG1 = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'
FB_BEST1 = 139629729 # from phase setting sequence 9,8,7,6,5
FB_PROG2 = '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'
FB_BEST2 = 18216 # from phase setting sequence 9,7,8,5,6

# ======================================================================
#                                                               TestAmps
# ======================================================================


class TestAmps(unittest.TestCase):  # pylint: disable=R0904
    """Test Amplifiers"""

    def test_example_1(self):
        """Test Amplifiers Example One"""

        # 1. Create the amplifiers
        myamps = amp.Amps(num=5, inp=0, text=PROG1)

        # 2. Find the best
        self.assertEqual(myamps.find_best(), BEST1)

    def test_example_2(self):
        """Test Amplifiers Example Two"""

        # 1. Create the amplifiers
        myamps = amp.Amps(num=5, inp=0, text=PROG2)

        # 2. Find the best
        self.assertEqual(myamps.find_best(), BEST2)

    def test_example_3(self):
        """Test Amplifiers Example Three"""

        # 1. Create the amplifiers
        myamps = amp.Amps(num=5, inp=0, text=PROG3)

        # 2. Find the best
        self.assertEqual(myamps.find_best(), BEST3)

    def test_feedback_1(self):
        """Test Amplifiers Feedback Example One"""

        # 1. Create the amplifiers
        myamps = amp.Amps(num=5, inp=0, text=FB_PROG1, feedback=True)

        # 2. Find the best (with feedback)
        self.assertEqual(myamps.find_best(), FB_BEST1)

    def test_feedback_2(self):
        """Test Amplifiers Feedback Example Two"""

        # 1. Create the amplifiers
        myamps = amp.Amps(num=5, inp=0, text=FB_PROG2, feedback=True)

        # 2. Find the best (with feedback)
        self.assertEqual(myamps.find_best(), FB_BEST2)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ u o m a p . p y                   end
# ======================================================================
