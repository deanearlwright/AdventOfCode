# ======================================================================
# Seven Segment Search
#   Advent of Code 2021 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p a t t e r n . p y
# ======================================================================
"Pattern for the Advent of Code 2021 Day 08 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
SEGMENTS_TO_DIGITS = ["", "", "1", "7", "4", "235", "069", "8"]
SEGMENTS_LIKE_ONE = [2, 2, 1, 2, 2, 1, 1, 2, 2, 2]
SEGMENTS_LIKE_FOUR = [3, 2, 2, 3, 5, 3, 3, 2, 4, 4]


# ======================================================================
#                                                                Pattern
# ======================================================================


class Pattern(object):   # pylint: disable=R0902, R0205
    "Object for Seven Segment Search"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.signals = []
        self.output = []
        self.segments = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            signals, output = text.split(' | ')
            self.signals = signals.split(' ')
            self.output = output.split(' ')
            self.segments = {len(signal): set(list(signal)) for signal in self.signals}

    def one_four_seven_eight(self):
        "Return the number of those values"

        # 1. Start with nothing
        result = 0

        # 2. Loop for the output
        for output in self.output:

            # 3. Increment the result if there is a match
            if len(output) in [2, 4, 3, 7]:
                result += 1

        # 4. Return the count of the desired digits
        return result

    def value(self):
        "Return the value of the output"

        # 1. Start with no number
        result = []

        # 3. Loop for all the displays in the output
        for digit in self.output:

            result.append(self.single_digit(digit))

        return int(''.join(result))

    def single_digit(self, digit):
        "figure out the digit"

        # 1. Do the easy ones
        decode = SEGMENTS_TO_DIGITS[len(digit)]
        if len(decode) == 1:
            return decode

        # 2. Seperate out two, three, and five
        if decode == "235":
            return self.digit_two_three_five(digit)

        # 3. Seperate out zero, six and nine
        return self.digit_zero_six_nine(digit)

    def digit_two_three_five(self, digit):
        "figure out the 2/3/5 digit"

        # 1. Make a set of the digit's segments
        segments = set(list(digit))

        # 2. Get segment counts
        one = len(segments & self.segments[2])
        four = len(segments & self.segments[4])

        # 3. Use them to discriminate
        if one == SEGMENTS_LIKE_ONE[2] and four == SEGMENTS_LIKE_FOUR[2]:
            return '2'
        if one == SEGMENTS_LIKE_ONE[3] and four == SEGMENTS_LIKE_FOUR[3]:
            return '3'
        return '5'

    def digit_zero_six_nine(self, digit):
        "figure out the 0/6/9 digit"

        # 1. Make a set of the digit's segments
        segments = set(list(digit))

        # 2. Get segment counts
        one = len(segments & self.segments[2])
        four = len(segments & self.segments[4])

        # 3. Use them to discriminate
        if one == SEGMENTS_LIKE_ONE[0] and four == SEGMENTS_LIKE_FOUR[0]:
            return '0'
        if one == SEGMENTS_LIKE_ONE[9] and four == SEGMENTS_LIKE_FOUR[9]:
            return '9'
        return '6'


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       p a t t e r n . p y                      end
# ======================================================================
