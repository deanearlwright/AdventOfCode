# ======================================================================
# Binary Diagnostic
#   Advent of Code 2021 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d i a g n o s t i c . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 03 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                             Diagnostic
# ======================================================================


class Diagnostic(object):   # pylint: disable=R0902, R0205
    "Object for Binary Diagnostic"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text

    def get_bits(self, common=True):
        "get the maximum or minimum bits"

        # 1. Get dimensions of the problem
        width = len(self.text[0])
        depth = len(self.text)

        # 1. Start with many nothings
        result = ['0' for _ in range(width)]
        #print("initial", width, depth, result)

        # 2. Loop through the bits
        for indx in range(width):

            # 3. Start the bit count
            ones = 0

            # 4. Loop for all the rows
            for line in self.text:

                # 5. Count the ones
                if line[indx] == '1':
                    ones += 1

            # 6. Which is more popular?
            if ones + ones > depth:
                result[indx] = '1'
            #print(indx, ones, result)

        # 7. If we wanted the least popular, invert the bits
        if not common:
            for indx in range(width):
                if result[indx] == '1':
                    result[indx] = '0'
                else:
                    result[indx] = '1'

        # 8. Convert to decimal
        return int(''.join(result), 2)

    @staticmethod
    def most(text, index):
        "Return the most popular bit '0' or '1' at the given position of the specifiec list"

        # 1. Start counts of ones
        count = 0

        # 2. Loop for all of the lines of text
        for line in text:

            # 3. Get the specified bit
            bit = line[index]

            # 4. If it is a one, count it
            if bit == '1':
                count += 2

        # 3. Which was most popular
        if count > len(text):
            return '1'
        if count == len(text):
            return '='
        return '0'

    @staticmethod
    def handle_ties(most, digit):
        "Break most ties in favor of the digit"
        if most == '=':
            return digit
        return most

    @staticmethod
    def most_or_least(digit, most=True):
        if most:
            return Diagnostic.handle_ties(digit, '1')
        if digit == '0':
            return '1'
        if digit == '1':
            return '0'
        return Diagnostic.handle_ties(digit, '0')

    @staticmethod
    def keep(text, digit, index):
        "Keep numbers that match the digit in the specified position"

        # 1. Start with nothing
        result = []

        # 2. Loop for all of the lines of text
        for line in text:

            # 3. Get the determining bit
            bit = line[index]

            # 4. Keep only the ones that match
            if bit == digit:
                result.append(line)

        # 5. Return the matching lines
        return result

    def keep_one(self, most=True):
        "Loop sheading number from the list until there is only one"

        # 1. Start with all the lines
        lines = self.text[:]
        index = 0

        # 2. Loop until there is only one
        while len(lines) > 1:

            # 3. Which is the most popular digit
            most_popular = Diagnostic.most(lines, index)

            # 4. We may want the least popular
            want = Diagnostic.most_or_least(most_popular, most)
            #print(len(lines), index, most_popular, want)

            # 5. Keep only the number with that digit
            lines = Diagnostic.keep(lines, want, index)
            # print(lines)

            # 6. Increment the index for next time
            index += 1

        # 7. Return the remaining number as decimal
        return int(lines[0], 2)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.get_bits() * self.get_bits(False)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.keep_one() * self.keep_one(False)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    d i a g n o s t i c . p y                   end
# ======================================================================
