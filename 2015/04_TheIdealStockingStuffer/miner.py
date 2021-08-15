# ======================================================================
# The Ideal Stocking Stuffer
#   Advent of Code 2015 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         m i n e r . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 04 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import hashlib

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
START = 0

# ======================================================================
#                                                                  Miner
# ======================================================================


class Miner(object):   # pylint: disable=R0902, R0205
    "Object for The Ideal Stocking Stuffer"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.secret = ''

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.secret = text[0]

    def md5_number(self, number):
        "Return the md5 hash of the secret and the number"

        # 1. Combine the parts
        combined = bytearray(self.secret + str(number), 'ascii')

        # 2. Hash the combined string
        md5_hasher = hashlib.md5()
        md5_hasher.update(combined)

        # 3. Return the hash
        return md5_hasher.hexdigest()

    def match_start(self, start):
        "Generate hashes until we match the given starting sequence"

        # 1. Start at the very beginning
        result = START - 1
        hashed = ''

        # 2. Loop generating hashes
        while not hashed.startswith(start):
            result += 1
            hashed = self.md5_number(result)

        # 3. Return the number of the first hash that matches
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.match_start('00000')

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.match_start('000000')


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         m i n e r . p y                        end
# ======================================================================
