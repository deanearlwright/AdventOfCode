# ======================================================================
# Aunt Sue
#   Advent of Code 2015 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         m f c s a m . p y
# ======================================================================
"Mfcsam for the Advent of Code 2015 Day 16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
RE_MFCSAM = re.compile('([a-z]+): ([0-9])+')

# ======================================================================
#                                                                 Mfcsam
# ======================================================================


class Mfcsam(object):   # pylint: disable=R0902, R0205
    "Object for Aunt Sue"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.compounds = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in self.text:
                match = RE_MFCSAM.match(line)
                if not match:
                    print("Unable to parse", line)
                else:
                    name, amount = match.groups()
                    self.compounds[name] = int(amount)

    def is_match(self, name, value):
        "Returns True if the experimental value matches the MFCSAM value"

        # 1. It must be present
        if name not in self.compounds:
            return False

        # 2. For part one, use exact match
        if not self.part2:
            return self.compounds[name] == value

        # 3. Part 2 has tricky rules
        # 3a. cats and trees readings indicates that there are greater than that many
        if name == 'cats' or name == 'trees':
            return self.compounds[name] < value

        # 3b. pomeranians and goldfish readings indicate that there are fewer than that many
        if name == 'pomeranians' or name == 'goldfish':
            return self.compounds[name] > value

        # 3c. rest use equality
        return self.compounds[name] == value

    def is_complete_match(self, attributes):
        "Returns True if all of the values match"

        # 1. Loop for all of the attributes
        for name, value in attributes.items():

            # 2. Does this attrabute match, return False if not
            if not self.is_match(name, value):
                return False

        # 3. Looks good to me
        return True


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        m f c s a m . p y                       end
# ======================================================================
