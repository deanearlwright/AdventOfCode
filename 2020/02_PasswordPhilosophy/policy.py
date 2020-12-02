# ======================================================================
# Password Philosophy
#   Advent of Code 2020 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p o l i c y . p y
# ======================================================================
"A password policy for the Advent of Code 2020 Day 02 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re
import collections

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
re_text = re.compile('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)')

# ======================================================================
#                                                                 Policy
# ======================================================================


class Policy(object):   # pylint: disable=R0902, R0205
    "A password policy object for Password Philosophy"

    def __init__(self, text=None):

        # 1. Set the initial values
        self.text = text
        self.low = 0
        self.high = 0
        self.letter = None
        self.password = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            result = re_text.fullmatch(text)
            if result is None:
                print("unable to match [%s]" % text)
            else:
                self.low = int(result.group(1))
                self.high = int(result.group(2))
                self.letter = result.group(3)
                self.password = result.group(4)

    def count(self):
        "Returns the number of times the selected letter appears"
        # 1. Count all the letters in the policy
        assert self.password is not None
        letters = collections.Counter(self.password)

        # 2. Check the number of occurences of the selected letter
        return letters[self.letter]

    def locations(self):
        "Returns the locations of the selected letter"

        # 1. Start with nothing
        result = set()

        # 2. Loop for all of the letters in the password
        for index, letter in enumerate(self.password):

            # 3. If this is the letter we want, add the locations
            if self.letter == letter:
                result.add(1 + index)

        # 4. Return the locations
        return result

    def is_valid(self):
        "Returns True if the password is valid according to the policy"

        # 1. Get the number of times the letter appears
        count = self.count()

        # 2. Check the number of occurences of the selected letter
        return count >= self.low and count <= self.high

    def is_valid2(self):
        "Returns True if the password is valid according to the policy"

        # 1. Get the number of times the letter appears
        locs = self.locations()

        # 2. Count the number of occurences of the selected letter
        result = 0
        if self.low in locs:
            result += 1
        if self.high in locs:
            result += 1

        # 3. There can be only one
        return result == 1


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        p o l i c y . p y                       end
# ======================================================================
