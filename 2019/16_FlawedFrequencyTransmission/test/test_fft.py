# ======================================================================
# Flawed Frequency Transmission
#   Advent of Code 2019 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ f f t . p y
# ======================================================================
"Test transformet for AoC 2019 day 16, Flawed Frequency Transmission"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import fft

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
MASK_TEXT = [0, 1, 1, 0, 0, -1, -1, 0, 0, 1, 1, 0, 0, -1, -1]

MASK_EXAMPLE = [
    [],
    [1, 0, -1, 0, 1, 0, -1, 0],
    [0, 1, 1, 0, 0, -1, -1, 0],
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1]
]

PHASES = [
    '12345678',
    '48226158',
    '34040438',
    '03415518',
    '01029498',
]

LARGER_INP = [
    '80871224585914546619083218645595',
    '19617804207202209144916044189917',
    '69317163492948606335995924319873',
]

LARGER_OUT = [
    '24176176',
    '73745418',
    '52432133',
]

# ======================================================================
#                                                                TestFFT
# ======================================================================


class TestFFT(unittest.TestCase):  # pylint: disable=R0904
    """Test Panels object"""

    def test_empty_init(self):
        """Test default FFT object creation"""

        # 1. Create default FFT object
        myfft = fft.FFT()

        # 2. Make sure it has the default values
        self.assertEqual(myfft.pattern, fft.BASE_PATTERN)

    def test_value_init(self):
        "Test FFT object creation with values"

        # 1. Create Panel object with values
        myfft = fft.FFT(pattern=[1, 2, 3])

        # 2. Make sure it has the specified values
        self.assertEqual(myfft.pattern, [1, 2, 3])

    def test_mask(self):
        "Test generation of a mask"

        # 1. Test mask from problem discription
        myfft = fft.FFT()
        self.assertEqual(myfft.mask(2, 15), MASK_TEXT)

        # 2. Test masks from example
        myfft = fft.FFT()
        for num in range(1, 9):
            self.assertEqual(myfft.mask(num, 8), MASK_EXAMPLE[num])

    def test_phase(self):
        "Test phase transformations"

        # 1. Create a transformer
        myfft = fft.FFT()

        # 2. Get the starting digite
        digits = [int(_) for _ in PHASES[0]]

        # 3. Do four phases, checking the result
        for num in range(1, 5):
            digits = myfft.phase(digits)
            self.assertEqual(digits, [int(_) for _ in PHASES[num]])

    def test_short(self):
        "Test short transformations"

        # 1. Create a transformer
        myfft = fft.FFT()

        # 2. Do the transformation
        digits = myfft.transform(PHASES[0], phases=4)

        # 3. Verify the results
        self.assertEqual(digits, [int(_) for _ in PHASES[4]])

    def test_larger(self):
        "Test transformations of larger inputs"

        # 1. Create a transformer
        myfft = fft.FFT()

        # 2. Loop for the three examples
        for num in range(3):

            # 3. Transform the digits
            digits = myfft.transform(LARGER_INP[num])

            # 4. Verify the results
            self.assertEqual('%d%d%d%d%d%d%d%d' %
                             (digits[0], digits[1], digits[2], digits[3],
                              digits[4], digits[5], digits[6], digits[7]),
                             LARGER_OUT[num])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ p a n e l . p y                    end
# ======================================================================
