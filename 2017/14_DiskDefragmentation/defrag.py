# ======================================================================
# Disk Defragmenter
#   Advent of Code 2017 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d e f r a g . p y
# ======================================================================
"A solver for Disk Defragmenter for Advent of Code 2017 Day 14"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import knots

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
HEX_TO_BITS = {
    '0': [0, 0, 0, 0],
    '1': [0, 0, 0, 1],
    '2': [0, 0, 1, 0],
    '3': [0, 0, 1, 1],
    '4': [0, 1, 0, 0],
    '5': [0, 1, 0, 1],
    '6': [0, 1, 1, 0],
    '7': [0, 1, 1, 1],
    '8': [1, 0, 0, 0],
    '9': [1, 0, 0, 1],
    'a': [1, 0, 1, 0],
    'b': [1, 0, 1, 1],
    'c': [1, 1, 0, 0],
    'd': [1, 1, 0, 1],
    'e': [1, 1, 1, 0],
    'f': [1, 1, 1, 1],
}

DELTA = [(0, -1), (0, 1), (1, 0), (-1, 0)]

# ======================================================================
#                                                                 Defrag
# ======================================================================


class Defrag(object):   # pylint: disable=R0902, R0205
    """Object for a disk defragmenter"""

    def __init__(self, size=128, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.size = size
        self.bits = [[0 for _ in range(size)] for _ in range(size)]
        self.region = None

        # 2. if there is text, use key to populate bits
        if text is not None:
            self.populate_bits()

    def __getitem__(self, key):

        return self.bits[key[1]][key[0]]

    def __setitem__(self, key, value):

        self.bits[key[1]][key[0]] = value

    def is_key_valid(self, key):
        "Check if the key is valid for getting a bit"

        if key[0] < 0 or key[0] >= self.size or key[1] < 0 or key[1] >= self.size:
            return False
        return True

    def populate_bits(self):
        "Populate the bits from the knot hash"

        # 0. Precondition axiom
        assert self.size <= 128

        # 1. loop for each row of bits
        for rnum in range(self.size):

            # 2. Generate row key
            row_key = self.text + '-%d' % rnum

            # 3. Get the dense hash
            knot = knots.Knots(length=256, part2=True)

            # 4. Get the dense hash
            dense_hash = knot.process_knots(text=row_key, verbose=False)

            # 5. Convert the dense_hash to bits
            bits = self.hash_to_bits(dense_hash)

            # 6. Save the bits
            self.bits[rnum] = bits

    def hash_to_bits(self, dense_hash):
        "Turn a dense hash into bits"

        # 0. Precondition axiom
        assert self.size <= 128

        # 1. Start with nothing
        result = []

        # 2. Loop for all of the hex digits
        for digit in dense_hash:

            # 3. Add the bits to the result
            result.extend(HEX_TO_BITS[digit])

        # 4. Return the bits
        return result[0:self.size]

    def bits_to_regions(self, verbose=False):
        "Group the bits into regions"

        # 1. Set initial region number
        self.region = 2

        # 2. Loop for every row and every column
        for rnum in range(self.size):
            for cnum in range(self.size):

                # 3. Ignore unused squares or one already in regions
                if self[(cnum, rnum)] != 1:
                    continue

                # 4. This square is now a region
                if verbose:
                    print("Starting region %d at (%d, %d" %
                          (self.region, cnum, rnum))
                self[(cnum, rnum)] = self.region

                # 5. Add neighbors of this square to the region
                self.add_neighbors(cnum, rnum)

                # 6. Increment region number
                self.region += 1

    def add_neighbors(self, cnum, rnum):
        "Add neighboring squares to an existing region"

        # 1. Add the neighbors of the given square
        for delta in DELTA:

            # 2. Determine the square of the neighbot
            ncol = cnum + delta[0]
            nrow = rnum + delta[1]

            # 3. Ignore the neighbor if invalid location
            if not self.is_key_valid((ncol, nrow)):
                continue

            # 4. Ignore the neighbor if empty or already in region
            if self[(ncol, nrow)] != 1:
                continue

            # 5. This square is now in the region
            self[(ncol, nrow)] = self.region

            # 6. Add the neighbors of this square
            self.add_neighbors(ncol, nrow)

    def part_one(self, verbose=False, limit=0):
        "Returns the number of squares used"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the rows
        for row in self.bits:

            # 3. Add up the bits in the row and accumulate the result
            result += sum(row)

        # 4. Return the number of bits used
        return result

    def part_two(self, verbose=False, limit=0):
        "Returns the number of squares used"

        # 1. Convert bits to regions
        self.bits_to_regions(verbose=verbose)

        # 2. Return the number of regions
        return self.region - 2


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        d e f r a g . p y                       end
# ======================================================================
