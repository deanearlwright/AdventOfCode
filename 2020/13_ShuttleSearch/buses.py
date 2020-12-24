# ======================================================================
# Shuttle Search
#   Advent of Code 2020 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           b u s e s . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 13 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import math

import bus

# ----------------------------------------------------------------------
#                                                      Chinese Remainder
# from https://rosettacode.org/wiki/Chinese_remainder_theorem
# Use math.prod() and change / --> // for integer division
# ----------------------------------------------------------------------


def chinese_remainder(n, a):
    sum = 0
    prod = math.prod(n)

    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

# ======================================================================
#                                                                  Buses
# ======================================================================


class Buses(object):   # pylint: disable=R0902, R0205
    "Object for Shuttle Search"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.earliest = 0
        self.buses = []

        # 2. Process text (if any)
        if text is not None and len(text) > 1:
            self.earliest = int(text[0])
            for offset, bid in enumerate(text[1].split(',')):
                if bid != 'x':
                    self.buses.append(bus.Bus(bid=bid, offset=offset))

    def get_earliest(self):
        "Get bus ID and next time it departs"

        # 1. Start with a very bad best time
        best_time = None
        best_bus = None

        # 2. Loop for all the buses
        for shuttle in self.buses:

            # 3. What is the next departure for this bus?
            btime = shuttle.next_depart_after(self.earliest)

            # 4. Remember the earliest time and bus ID
            if best_time is None or btime < best_time:
                best_time = btime
                best_bus = shuttle.bid

        # 5. Return the bus number and wait time
        if best_time is not None:
            return best_bus, best_time - self.earliest
        return None, None

    def contest(self):
        "Return the earliest timestamp for the contest"

        # 1. Get bus modulos and offset times
        mods = [_.bid for _ in self.buses]
        offsets = [-_.offset for _ in self.buses]

        # 2. And then CRT does the magic
        return chinese_remainder(mods, offsets)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Get the bus ID and wait time
        best = self.get_earliest()

        # 2. No ID means no solution
        if best[0] is None:
            return None

        # 3. Return the solution for part one (ID * wait)
        return best[0] * best[1]

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.contest()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          b u s e s . p y                       end
# ======================================================================
