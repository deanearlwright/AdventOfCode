# ======================================================================
# How About a Nice Game of Chess
#   Advent of Code 2016 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d o o r p a s s . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 05 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import hashlib

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
ZEROES = "00000"
INDEXES = '01234567'

# ======================================================================
#                                                               Doorpass
# ======================================================================


class Doorpass(object):   # pylint: disable=R0902, R0205
    "Object for How About a Nice Game of Chess"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.doorID = ''

        # 2. Set the door ID
        if self.text and len(self.text) > 0:
            self.doorID = self.text[0]

    def password_one(self):
        "Return the password for part one"

        # 1. Start with nothing
        result = []
        base = 0

        # 2. Loop until we get all 8 characters
        while len(result) < 8:

            # 3. Loop until we get a hash that starts with zeroes
            hstr = 'not zeroes'
            while not hstr.startswith(ZEROES):
                hstr = hashlib.md5((self.doorID + str(base)).encode('utf-8')).hexdigest()
                base += 1

            #  4. The next password digit is the 6th char of the hash
            result.append(hstr[5])

        # 9. Return the password
        return ''.join(result)

    def password_two(self):
        "Return the password for part one"

        # 1. Start with nothing
        result = ['_', '_', '_', '_', '_', '_', '_', '_']
        base = 0

        # 2. Loop until we get all 8 characters
        while '_' in result:

            # 3. Loop until we get a hash that starts with zeroes
            hstr = 'not zeroes'
            while not hstr.startswith(ZEROES):
                hstr = hashlib.md5((self.doorID + str(base)).encode('utf-8')).hexdigest()
                base += 1

            #  4. 6th char (if 0-7) says where to place the 7th character
            char6 = hstr[5]
            if char6 in INDEXES:
                indx = int(char6)
                if result[indx] == '_':
                    result[indx] = hstr[6]
                    print(''.join(result))

        # 9. Return the password
        return ''.join(result)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.password_one()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.password_two()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      d o o r p a s s . p y                     end
# ======================================================================
