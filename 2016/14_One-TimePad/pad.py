# ======================================================================
# One-Time Pad
#   Advent of Code 2016 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                              p a d . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 14 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re
import hashlib

# ----------------------------------------------------------------------
#                                                         hash functions
# ----------------------------------------------------------------------


def part_one_hash(value):
    "Return the md5 has for part 1"
    m = hashlib.md5()
    m.update(bytes(value, 'utf8'))
    return m.hexdigest()


def part_two_hash(value):
    "Return the stretched md5 has for part 2"
    # 1. Start with the regular md5 hash
    h = part_one_hash(value)
    # 2. Now rehash it 2016 additional times
    for _ in range(2016):
        h = part_one_hash(h)
    # 3. Return the stretched hash
    return h


# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
RE_THREE = re.compile('000|111|222|333|444|555|666|777|888|999|aaa|bbb|ccc|ddd|eee|fff')

# ======================================================================
#                                                                    Pad
# ======================================================================


class Pad(object):   # pylint: disable=R0902, R0205
    "Object for One-Time Pad"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.salt = ""
        self.hashes = {}
        self.keys = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.salt = text[0]

    def get_hash(self, number):
        "Generate a hash from the salt+number"
        # 1. Get the value to hash
        value = self.salt + str(number)
        # 2. If we have already computed it, return the hashed value
        if value in self.hashes:
            return self.hashes[value]
        # 3. Part two uses key streatching
        if self.part2:
            h = part_two_hash(value)
        else:
            h = part_one_hash(value)
        # 4. Saved the hased value (we might need it for another)
        self.hashes[value] = h
        # 5. Return the hashed value
        return h

    def remove_hash(self, number):
        "Get rid of unneeded hash"
        value = self.salt + str(number)
        if value in self.hashes:
            del self.hashes[value]

    def is_key(self, number):
        "Does this number represent a key"
        # 1. Get the hash for this number
        hash_number = self.get_hash(number)
        # 2. Needs to have a triple
        hash_match = RE_THREE.search(hash_number)
        if not hash_match:
            return False
        # 3. Get the digits to match
        digits = 5 * hash_match.group(0)[0]
        re_five = re.compile(digits)
        # 4. Is there a group of five within the next 1000?
        for delta in range(1000):
            if re_five.search(self.get_hash(number + delta + 1)):
                return True
        # 5. nnnnn not found, return False
        return False

    def get_keys(self, count):
        "Get a bunch of keys"
        # 1. Start with nothing
        number = 0
        # 2. Loop until we get enough keys
        while len(self.keys) < count:
            # 3. Is this is a key, add it
            if self.is_key(number):
                self.keys.append(number)
            # 4. Try the next number
            number += 1
        # 5. Return the number of the last key
        return self.keys[-1]

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.get_keys(64)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.get_keys(64)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           p a d . p y                          end
# ======================================================================
