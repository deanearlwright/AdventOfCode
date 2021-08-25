# ======================================================================
# Elves Look Elves Say
#   Advent of Code 2015 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         l o o k a n d s a y . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 10 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
PART_ONE_TIMES = 40
PART_TWO_TIMES = 50

# ======================================================================
#                                                             Lookandsay
# ======================================================================


class Lookandsay(object):   # pylint: disable=R0902, R0205
    "Object for Elves Look Elves Say"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.seed = '1'

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.seed = text[0]

    @staticmethod
    def next_sequence(sequence):
        "Return the next number in the sequence"

        # 1. Start with nothing
        result = []
        last_digit = '?'
        count = 0

        # 2. Loop for every digit in the current sequence
        for digit in sequence:

            # 3. If this is the same, accumulate it
            if digit == last_digit:
                count += 1

            # 4. Else, output last_digit and start anew
            else:
                if count > 0:
                    result.append(str(count))
                    result.append(last_digit)
                count = 1
                last_digit = digit

        # 5. Output any last digits
        if count > 0:
            result.append(str(count))
            result.append(last_digit)

        # 6. Output the new sequence
        return ''.join(result)

    def many_times(self, times=PART_ONE_TIMES, verbose=False):
        "Output the length of the sequence after many times"

        # 1. Start with the seed
        sequence = self.seed
        if verbose:
            print("Starting with", sequence)

        # 2. Loop many times
        for num in range(1, 1 + times):
            sequence = Lookandsay.next_sequence(sequence)
            if verbose:
                print(num, len(sequence))

        # 3. Return the length of the final sequence
        return len(sequence)

    def part_one(self, times=PART_ONE_TIMES, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.many_times(times=times, verbose=verbose)

    def part_two(self, times=PART_TWO_TIMES, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.many_times(times=times, verbose=verbose)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    l o o k a n d s a y . p y                   end
# ======================================================================
