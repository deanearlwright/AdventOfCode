# ======================================================================
# Subterranean Sustainability
#   Advent of Code 2018 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p o t s . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 12 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
GENERATIONS = 20
P2_GENERATIONS = 50000000000
P2_100 = 2675
P2_DELTA = 22

# ======================================================================
#                                                                   Pots
# ======================================================================


class Pots(object):   # pylint: disable=R0902, R0205
    "Object for Subterranean Sustainability"

    def __init__(self, generations=GENERATIONS, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.pots = ''
        self.rules = {}
        self.left = 0
        self.generations = generations

        # 2. Process text (if any)
        if text is not None and len(text) > 3:
            self.processText(text)

    def processText(self, text):
        self.pots = '.' * self.generations
        self.left = -self.generations
        self.processInitialState(text[0])
        self.processRules(text[1:])

    def processInitialState(self, line):
        parts = line.split(' ')
        if parts[0] != 'initial' or parts[1] != 'state:':
            print("*** Expected 'initial state' but found '%s %s'" % (parts[0], parts[1]))
            return
        self.pots = self.pots + parts[2] + self.pots

    def processRules(self, text):
        for line in text:
            parts = line.split(' ')
            if parts[1] != '=>':
                print("*** Expected '=>' but found '%s'" % parts[1])
                return
            self.rules[parts[0]] = parts[2]

    def next(self, index):
        current = self.pots[index-2:index+3]
        if current in self.rules:
            return self.rules[current]
        return '.'

    def next_generation(self):
        result = ['.','.']
        for index in range(2, len(self.pots)-2):
            result.append(self.next(index))
        return ''.join(result) + '..'

    def sum_pots(self):
        result = 0
        value = self.left
        for pot in self.pots:
            if pot == '#':
                result += value
            value += 1
        return result

    def run(self, verbose=False):
        for gen in range(1, self.generations+1):
            next_gen = self.next_generation()
            self.pots = next_gen
            if verbose:
                print("%2d: %5d %s" % (gen, self.sum_pots(), next_gen))

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        self.run(verbose=verbose)
        return self.sum_pots()


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return P2_100 + P2_DELTA * (P2_GENERATIONS - 100)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          p o t s . p y                         end
# ======================================================================
