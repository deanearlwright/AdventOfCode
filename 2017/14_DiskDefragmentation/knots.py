# ======================================================================
# Knot Hash
#   Advent of Code 2017 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         k n o t s . p y
# ======================================================================
"A solver for Knot Hash for Advent of Code 2017 Day 10"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from functools import reduce
from operator import xor

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
PART2_LENGTHS = [17, 31, 73, 47, 23]

# ======================================================================
#                                                                  Knots
# ======================================================================


class Knots(object):   # pylint: disable=R0902, R0205
    """Knotty String Object"""

    def __init__(self, part2=False, length=0):

        # 1. Set the initial values
        self.part2 = part2
        self.length = length
        self.level = 0
        self.current = 0
        self.skip = 0
        self.values = list(range(length))
        self.knots = []
        if part2:
            self.rounds = 64
        else:
            self.rounds = 1

    def process_knots(self, text=None, verbose=False, limit=0):
        "Process the text of knots"

        # 1. If no text, not much to do
        if text is None:
            return None

        # 2. Get the knot lengths
        if self.part2:
            self.knots = [ord(_) for _ in text] + PART2_LENGTHS
        else:
            self.knots = [int(_) for _ in text.split(',')]

        # 3. Loop for all of the rounds
        for rnum in range(self.rounds):

            # 4. Loop for all of the knot lengths
            for knum, klen in enumerate(self.knots):

                # 5. Process the one knot of the set of knots
                self.process_one_knot(klen, rnum=rnum, verbose=verbose)

                # 6. Check if processing limit reached
                if knum > limit > 0:
                    break

        # 7. Return the part1: product of the first two values
        #    or for part2: the dense hash as hexidecimal
        if self.part2:
            return self.dense_hash()
        return self.values[0] * self.values[1]

    def process_one_knot(self, klen, rnum=1, verbose=False):
        "Process a single know"

        # 1. Reverse the order of length elements in the list,
        #    starting with the element at the current position
        new_values = self.reverse(klen)

        # 2. Move the current position forward by that length plus the skip size
        new_current = (self.current + klen + self.skip) % self.length

        # 3. Increase the skip size by one
        new_skip = self.skip + 1

        # 4. Descibe the changes
        if verbose:
            print("klen=%d, rnum=%d, cur=%d, skip=%d, newc=%d, news=%d, v=%s" %
                  (klen, rnum, self.current, self.skip, new_current, new_skip, new_values))

        # 5. Update the values and the skip size
        self.values = new_values
        self.current = new_current
        self.skip = new_skip

    def reverse(self, klen):
        "Reverse a portion of the values"

        # 1. Make all changes to a copy of the values
        result = self.values.copy()

        # 2. Collect the characters to reverse
        reversing = [result[(self.current + _) % self.length] for _ in range(klen)]

        # 3. Reverse what needs to be reversed
        reversing.reverse()

        # 4. Put them back in the copy of the values
        for index in range(klen):
            result[(self.current + index) % self.length] = reversing[index]

        # 5. Return the new values
        return result


    def dense_hash(self):
        "Return a dense hash of the sparse hash"

        # 0. Precondition axioms
        assert len(self.values) == 256

        # 1. Start with nothing
        result = []

        # 2. Loop for sixteen blocks
        for bnum in range(0, len(self.values), 16):

            # 3. Exclusive or the 16 number in the block
            block = reduce(xor, self.values[bnum:bnum+16])

            # 4. Convert to hexidecimal and add to result
            result.append('%02x' % (block))

        # 5. Return the complete hash
        return ''.join(result)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          k n o t s . p y                       end
# ======================================================================
