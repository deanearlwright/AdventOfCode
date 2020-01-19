# ======================================================================
# Dueling Generators
#   Advent of Code 2017 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         g e n e r a t o r . p y
# ======================================================================
"A solver for Dueling Generators for Advent of Code 2017 Day 15"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

import itertools
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
FACTOR_A = 16807
FACTOR_B = 48271
FACTORS = {'A': FACTOR_A, 'B': FACTOR_B}

MULTIPLE_A = 4
MULTIPLE_B = 8
MULTIPLES = {'A': MULTIPLE_A, 'B': MULTIPLE_B}

MODULO = 2147483647

JUDGE_LEN = 16

RE_INPUT = re.compile(r'Generator ([A-Z]+) starts with ([0-9]+)')

# ----------------------------------------------------------------------
#                                                      Utility Functions
# ----------------------------------------------------------------------
def all_equal(iterable):
    "Returns True if all the elements are equal to each other"

    g = itertools.groupby(iterable)
    return next(g, True) and not next(g, False)

# ======================================================================
#                                                              Generator
# ======================================================================


class Generator(object):   # pylint: disable=R0902, R0205
    """Object for a generator"""

    def __init__(self, factor=FACTOR_A, modulo=MODULO, start=None,
                  name=None, text=None, part2=False, multiple=None):

        # 1. Set the initial values
        self.factor = factor
        self.modulo = modulo
        self.start = start
        self.value = start
        self.count = 0
        self.name = name
        self.part2 = part2
        self.multiple = multiple

        # 2. Process text (if any)
        if text is not None:
            re_match = RE_INPUT.match(text)
            if re_match is None:
                raise "Failed to match generator input %s" % text
            self.name = re_match.group(1)
            self.start = int(re_match.group(2))
            self.factor = FACTORS[self.name]
            self.multiple = MULTIPLES[self.name]
            self.value = self.start


    def __iter__(self):
        return self

    def __next__(self):

        return self.next_value()

    def reset(self):
        "Reset the value back to the start"

        self.value = self.start
        self.count = 0

    def next_value(self):
        "Compute the next value"

        # 1. We may loop for a bit
        while True:

            # 2. Compute the value
            self.value = (self.value * self.factor) % self.modulo

            # 3. Increment the count
            self.count += 1

            # 4. That's all you need for part one
            if not self.part2:
                break

            # 5. Else it must be a even multiple
            if 0 == self.value % self.multiple:
                break

        # 6. Return the value just calculated
        return self.value

# ======================================================================
#                                                             Generators
# ======================================================================


class Generators(object):   # pylint: disable=R0902, R0205
    """Object for two generators and a judge"""

    def __init__(self, text=None, judge=JUDGE_LEN, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.judge = 16
        self.modulo = 2**16
        self.count = 0
        self.generators = {}

        # 2. Process the text (if any)
        if text is not None:

            # 3. Loop for the text lines
            for line in text:

                # 4. Create a generator
                gen = Generator(text=line, part2=part2)

                # 5. And save it
                self.generators[gen.name] = gen

    def __getitem__(self, key):
        return self.generators[key]


    def judge_equal(self, verbose=False, limit=None):
        "Returns the judge confirmed matches"

        # 1. Start with nothing
        self.count = 0

        # 2. Loop for all of the rows
        for tick in range(limit):

            # 3. Advance each of the generators and get the values
            values = [_.next_value() for _ in self.generators.values()]

            # 4. Get the part of the values to compare
            compare = [_ % self.modulo for _ in values]

            # 5. If they are all the same, increment count
            if all_equal(compare):
                if verbose:
                    print("At time {0:d}, Generators all equal at {1:016b}".format(tick, compare[0]))
                self.count += 1

        # 6. Return the number of time the generators were equal
        if verbose:
            print("After %d iterations, there were %d matched" %
                  (limit, self.count))
        return self.count

    def next_values(self):
        "Generate the next values for all of the generators"

        # 1. Loop for all of the generators
        for gen in self.generators.values():

            # 2. Generate the next value for this generator
            gen.next_value()


    def part_one(self, verbose=False, limit=40000000):
        "Returns the judge confirmed matches"

        # 1. Return the judge confirmed matches
        return self.judge_equal(verbose=verbose, limit=limit)


    def part_two(self, verbose=False, limit=5000000):
        "Returns the judge confirmed matches"

        # 1. Return the judge confirmed matches
        return self.judge_equal(verbose=verbose, limit=limit)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    g e n e r a t o r . p y                     end
# ======================================================================
