# ======================================================================
# Dragon Checksum
#   Advent of Code 2016 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d r a g o n . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
SAME_DIFF = {'00': '1', '01': '0', '10': '0', '11': '1', }

# ----------------------------------------------------------------------
#                                                                utility
# ----------------------------------------------------------------------


def dragon_fill(seed, size):
    "Starting with the seed, expand to fill size bytes"

    # 1. Start with the seed
    result = ''.join(list(seed))

    # 2. Loop until the size is reached
    while len(result) < size:
        # 2. Copy and reverse the seed
        other = list(result)
        other.reverse()
        other = ''.join(other)
        # 3. Flip the bits
        flipped = other.replace('0', 'X').replace('1', '0').replace('X', '1')
        # 4. Merge the parts
        result = result + '0' + flipped

    # 5. Return the expanded string
    return result[:size]


def checksum(data):
    "Generate a checksum for the data"

    # 1. Start with the data
    result = ''.join(list(data))

    # 2. Loop while the result is even
    while len(result) % 2 == 0:
        # 3. Process it in pairs
        chksum = []
        for indx in range(0, len(result), 2):
            chksum.append(SAME_DIFF[result[indx:indx + 2]])
        # 4. This is the new result
        result = ''.join(chksum)

    # Return the odd checksum
    return result


# ======================================================================
#                                                                 Dragon
# ======================================================================


class Dragon(object):   # pylint: disable=R0902, R0205
    "Object for Dragon Checksum"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.seed = ""

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.seed = self.text[0]

    def fill_and_check(self, size):
        "Return checksum of filled disk"

        # 1. Fill the disk
        data = dragon_fill(self.seed, size)

        # 2. Return the checksum
        return checksum(data)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.fill_and_check(272)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.fill_and_check(35651584)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      d r a g o n . p y                     end
# ======================================================================
