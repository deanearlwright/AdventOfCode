
# ======================================================================
# Full of Hot Air
#   Advent of Code 2022 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s n a f u . p y
# ======================================================================
"Snafu for the Advent of Code 2022 Day 25 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DIGITS = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
}
SNAFU = ["0", "1", "2", "=", "-"]
ADJUST = [0, 0, 0, 1, 1]
PLACES = [5 ** x for x in range(20)]

# ======================================================================
#                                                                  Snafu
# ======================================================================


class Snafu(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Full of Hot Air"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text

    def sum_decimal(self):
        "Convert the fuel requirements to decimal and sum them"

        # 1. Convert the snafu numbers to decimal
        decimal_fuel = [int(Snafu.snafu_to_decimal(s_num)) for s_num in self.text]

        # 2. Sum the fuel requirements
        result = sum(decimal_fuel)

        # 3. Return the result
        return str(result)

    def sum_snafu(self):
        "Convert the total fuel requirements to snafu"

        # 1. Get the total fuel requirements
        total_decimal = self.sum_decimal()

        # 9. Return the total snafu fuel requirements
        return Snafu.decimal_to_snafu(total_decimal)

    @staticmethod
    def snafu_to_decimal(s_number):
        "Return the snafu number as decimal text"

        # 1. Break the snafu number into digits
        digits = list(s_number.strip())

        # 2. Convert each digit into a number
        numbers = [DIGITS[x] for x in digits]

        # 3. Reverse the numbers (ones position first)
        numbers.reverse()

        # 4. Multiply the numbers by the power for the position
        for indx, number in enumerate(numbers):
            numbers[indx] = number * PLACES[indx]

        # 5. Sum the numbers
        result = sum(numbers)

        # 6. Return the result
        return str(result)

    @staticmethod
    def decimal_to_snafu(d_number):
        "Return the decimal number (text) as snafu text"

        # 1. Start with nothing
        result = []

        # 2. Convert the decimal number to an integer
        decimal = int(d_number)

        # 3. Loop until we reduce the number to zero
        while decimal > 0:

            # 4. Take out a base 5 chunk
            decimal, five = divmod(decimal, 5)

            # 5. Add the appropiate snafu digit
            result.append(SNAFU[five])

            # 6. Adjust the number
            decimal += ADJUST[five]

        # 7. Put the snafu digits in proper order
        result.reverse()

        # 8. Return the snafu number
        return ''.join(result)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                         s n a f u . p y                        end
# ======================================================================
