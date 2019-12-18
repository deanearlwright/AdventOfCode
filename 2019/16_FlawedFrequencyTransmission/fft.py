# ======================================================================
# Flawed Frequency Transmission
#   Advent of Code 2019 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                              f f t . p y
# ======================================================================
"Flawed Frequency Transmission transformer for AoC 2019 Day 16"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from itertools import repeat

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
BASE_PATTERN = [0, 1, 0, -1]
DEFAULT_PHASES = 100

# ======================================================================
#                                                                    FFT
# ======================================================================


class FFT():
    """Object for a Flawed Frequency Transmission transformer"""

    def __init__(self, pattern=None):

        # 1. Set the initial values
        if pattern is None:
            self.pattern = BASE_PATTERN
        else:
            self.pattern = pattern


    def transform(self, digits, phases=DEFAULT_PHASES, watch=False):
        "Return a transformed input"

        # 1. if input is a string, convert to integer vector
        if isinstance(digits, str):
            digits = [int(c) for c in digits]
        if watch:
            print('Before=%s' % (str(digits)))

        # 2. Loop for the required number of phases
        for num in range(phases):

            # 3. Execute one phase
            digits = self.phase(digits)
            if watch:
                print('%5d=%s' % (num+1, str(digits)))


        # 4. Return the very phased digits
        return digits


    def phase(self, digits):
        "Return the digits after a single phase"

        # 1. Start with nothing
        result = []
        length = len(digits)

        # 2. Loop for each of the digits
        for num in range(1, length+1):

            # 3. Create the mask to use
            mask = self.mask(num, length)

            # 4. Transfor a digit
            digit = abs(sum([x * y for x, y in zip(mask, digits)])) % 10

            # 5. Add it the result
            result.append(digit)

        # 6. Return the result
        return result

    def mask(self, num, length):
        "Create a mask for the num'th digit of length length"

        # 1. Expand the pattern for the digit
        exp_pattern = []
        for pat in self.pattern:
            exp_pattern.extend(list(repeat(pat, num)))

        # 2. Create the complete mask
        mask = exp_pattern
        while len(mask) < length + 1:
            mask.extend(exp_pattern)

        # 3. Return just the bit we want
        return mask[1:length+1]


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           f f t . p y                          end
# ======================================================================
