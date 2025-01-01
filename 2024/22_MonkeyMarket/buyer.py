
# ======================================================================
# Monkey Market
#   Advent of Code 2024 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         b u y e r . p y
# ======================================================================
"Buyer for the Advent of Code 2024 Day 22 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import defaultdict

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
PRUNE = 16777216
STEP1 = 64
STEP2 = 32
STEP3 = 2048

# ======================================================================
#                                                                  Buyer
# ======================================================================


class Buyer(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Monkey Market"

    def __init__(self, initial=0, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.initial = initial
        self.secret = initial
        self.secrets = [initial]
        self.memo = defaultdict(int)

    def reset(self, secret=None):
        "Reset the secret number to it's initial value"
        self.secret = self.initial
        if secret is not None:
            self.secret = secret
        self.secrets = [self.secret]
        self.memo = defaultdict(int)

    @staticmethod
    def mix(secret, number):
        "Return the new secret number after mixing"
        return secret ^ number

    @staticmethod
    def prune(secret):
        "Return the new secret number after pruning"
        return secret % PRUNE

    def evolve(self):
        "Return the the buyers evolved secret number"

        # 1. Step 1
        new_secret = Buyer.prune(Buyer.mix(self.secret * STEP1, self.secret))

        # 2. Step 2
        new_secret = Buyer.prune(Buyer.mix(new_secret // STEP2, new_secret))

        # 3. Step 3
        new_secret = Buyer.prune(Buyer.mix(new_secret * STEP3, new_secret))

        # 4. Save the new secret
        self.secret = new_secret
        self.secrets.append(new_secret)

        # 5. And return it (for ease in testing)
        return new_secret

    def darwin(self, n=2000):
        "Evolve the secret number many times"

        # 1. Loop for the indicated number of times
        for _ in range(n):

            # 2. Evolve the secret one step
            self.evolve()

        # 3. Return the much evolved secret number (for ease in testing)
        return self.secret

    def price(self):
        "Return the current price"
        return self.secret % 10

    def price_n(self, n):
        "Return the price at time n"
        assert 0 <= n < len(self.secrets)
        return self.secrets[n] % 10

    def delta_n(self, n):
        "Return the delta in price at n and n+1"
        return self.price_n(n + 1) - self.price_n(n)

    def deltas_n(self, n):
        "Return the deltas in price at n+1, n+2, n+3, n+4"
        price0 = self.price_n(n)
        price1 = self.price_n(n + 1)
        price2 = self.price_n(n + 2)
        price3 = self.price_n(n + 3)
        price4 = self.price_n(n + 4)
        return (price1 - price0, price2 - price1,
                price3 - price2, price4 - price3)

    def buy_at(self, deltas):
        "Get the price when the first deltas appear"

        # 1. If we know the answer, just give it
        if deltas in self.memo:
            return self.memo[deltas]

        # 1. Find the first delta
        for n in range(len(self.secrets) - 4):

            # 2. Is the delta we want
            if self.delta_n(n) == deltas[0]:

                # 3. How about the rest
                if self.delta_n(n + 1) == deltas[1] and \
                   self.delta_n(n + 2) == deltas[2] and \
                   self.delta_n(n + 3) == deltas[3]:

                    # 4. Buy at this price
                    price = self.price_n(n + 4)
                    self.memo[deltas] = price
                    return price

        # 5. Never did find the price
        self.memo[deltas] = 0
        return 0

    def deltas_to_bananas(self):
        "Return all of the delta and the bananas at that delta"

        # 1. Loop for the secrets
        for n in range(len(self.secrets) - 4):

            # 2. Get the deltas
            deltas = self.deltas_n(n)

            # 3. Get the price if we don't already know it
            if deltas not in self.memo:
                price = self.price_n(n + 4)
                self.memo[deltas] = price

        # 4. Return the mapping
        return self.memo

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                         b u y e r . p y                        end
# ======================================================================
