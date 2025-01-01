
# ======================================================================
# Monkey Market
#   Advent of Code 2024 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         m a r k e t . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 22 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import defaultdict

import buyer

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Market
# ======================================================================


class Market(object):   # pylint: disable=R0902, R0205
    "Object for Monkey Market"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.buyers = []
        self.memo = defaultdict(int)

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text()

    def _process_text(self):
        "Assign values from text"

        assert self.text is not None and len(self.text) > 0

        # 1. Loop for all of the lines of text
        for line in self.text:

            # 2. Create a new buyer
            byr = buyer.Buyer(initial=int(line), part2=self.part2)

            # 3. Add them to the list
            self.buyers.append(byr)

    def evolve_all(self, n=2000):
        "Evolve all of the secret numbers"

        # 1. Loop for all of the buyers
        for byr in self.buyers:

            # 2. Evolve the secret number
            byr.darwin(n)

    def secret_sum(self):
        "Return the sum of the buyers secret numbers"
        return sum(byr.secret for byr in self.buyers)

    def best_delta(self):
        "Return the delta that gets the most bananas"

        # 1. Loop for all the buyers
        for byr in self.buyers:

            # 2. Get the deltas to bananas for that buyer
            d2b = byr.deltas_to_bananas()

            # 3. Add in those bananas
            for deltas, bananas in d2b.items():
                self.memo[deltas] += bananas

        # 4. Return the deltas that gives the most bananas
        most = max(self.memo.values())
        return max(d for d in self.memo if self.memo[d] == most)

    def total_bananas(self, delta):
        "Return the total bananas for the given delta"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the buyers
        for byr in self.buyers:

            # 3. How many bananas from this buyer
            bananas = byr.buy_at(delta)

            # 4. Accumulate the number of bananas
            if bananas is not None:
                result += bananas

        # 5. Return the total number of bananas
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        self.evolve_all()
        return self.secret_sum()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part two
        self.evolve_all()
        delta = self.best_delta()
        return self.total_bananas(delta)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        m a r k e t . p y                       end
# ======================================================================
