# ======================================================================
# Recursive Circus
#   Advent of Code 2017 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                          d i s c s . p y
# ======================================================================
"A solver for Recursive Circus for Advent of Code 2017 Day 07"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

from collections import Counter

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DECODE = re.compile(r'([a-z]+) \(([0-9]+)\)(?: -> )?([a-z, ]*)')

# ======================================================================
#                                                                   Disc
# ======================================================================


class Disc(object):
    """Object representing a single recursive program disc"""

    def __init__(self, name=None, weight=0, above=None, text=None):

        # 1. Set the initial values
        self.name = name
        self.weight = weight
        if above is not None:
            self.above = above
        else:
            self.above = []

        # 2. If text is not None, set the values from it
        if text is not None:
            match = DECODE.match(text)
            if not match:
                print("Unable to decode %s" % (text))
            else:
                #print("decoding %s to %s" % (text, match.groups()))
                self.name = match.group(1)
                self.weight = int(match.group(2))
                mg3 = match.group(3)
                if mg3 is not None and len(mg3.strip()) > 0:
                    self.above = [_.strip() for _ in mg3.split(',')]
                else:
                    self.above = []



# ======================================================================
#                                                                  Discs
# ======================================================================


class Discs(object):
    """Object representing a memory redistribution solver"""

    def __init__(self, part2=False, text=None):

        # 1. Set the initial values
        self.part2 = part2
        self.discs = {}
        if text is not None:
            for line in text:
                disc = Disc(text=line)
                self.discs[disc.name] = disc

    def __str__(self):
        return '|'.join(str(_) for _ in self.discs)

    def number_above(self, name):
        "Return the total number of disks above the named disc"

        # 1. If no discs above this one, return zero
        above = self.discs[name].above
        if not above:
            return 0

        # 2. Else return the number of disc here and further above
        return len(above) + sum([self.number_above(_) for _ in above])

    def weight_above(self, name):
        "Return the weight of disks above the named disc"

        # 1. If no discs above this one, return its weight
        above = self.discs[name].above
        if not above:
            return self.discs[name].weight

        # 2. Else return the weight of the discs above this one
        return self.discs[name].weight + sum([self.weight_above(_) for _ in above])

    def bottom(self, verbose=False, limit=0):
        """Return the key of the disc on the bottom
        The one with the most discs above it"""

        # 1. Assume there is no bottom
        result_name = None
        result_knt = -1

        # 2. Loop for all of the discs
        for name in self.discs:

            # 3. If this disc has more above, record it
            knt = self.number_above(name)
            if knt > result_knt:
                if verbose:
                    print("Saving %s as the bottom with %d discs above" %
                          (name, knt))
                result_knt = knt
                result_name = name

        # 4. Return the name of the disc with the most discs above it
        return result_name

    def balance(self, verbose=False, limit=0):
        """Balance the entire tree, return the adjusted weight of the now-balanced disc"""

        # 1. Start at the bottom
        bottom_name = self.bottom(verbose=verbose, limit=limit)

        # 2. Determine the amount of adjustment needed
        adjustment = self.adjustment(bottom_name)

        # 3. Balance the entire tree
        return self.balance_me(bottom_name, adjustment, verbose=verbose, limit=limit)

    def adjustment(self, name):
        "Determine the adjust"

        # 1. Get the weights of the discs above this one
        weights = [self.weight_above(_) for _ in self.discs[name].above]

        # 2. Find the odd one out
        counts = Counter(weights)
        most_common = counts.most_common(1)[0][0]
        least_common = counts.most_common()[-1][0]
        #print("most=%s, least=%s" % (most_common, least_common))

        # 3. The adjustment is the most common minus the least common
        return most_common - least_common

    def balance_me(self, name, adjustment, verbose=False, limit=0):
        """Balance this part of the tree, return the adjusted weight of the now-balanced disc"""

        # 1. If there is nothing to adjust above, I am the problem
        if self.adjustment(name) == 0:
            return self.discs[name].weight + adjustment

        # 2. Get the weights of the discs above
        weights = [self.weight_above(_) for _ in self.discs[name].above]

        # 3. Find the odd one out
        counts = Counter(weights)
        least_common = counts.most_common()[-1][0]


        # 4. Get the name of the least common one
        to_balance = None
        for above in self.discs[name].above:
            if least_common == self.weight_above(above):
                to_balance = above
                break

        # 5. If we don't have a stack, to balance, admit defeat
        if not to_balance:
            return None

        # 6. Else balance this stack
        return self.balance_me(to_balance, adjustment, verbose=verbose, limit=limit)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          d i s c s . p y                       end
# ======================================================================
