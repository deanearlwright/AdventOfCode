# ======================================================================
# All in a Single Night
#   Advent of Code 2015 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r o u t e s . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 09 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re
from itertools import permutations

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""
RE_INPUT = re.compile(r'([A-Za-z]+) to ([A-Za-z]+) = ([0-9+]+)')

# ======================================================================
#                                                                 Routes
# ======================================================================


class Routes(object):   # pylint: disable=R0902, R0205
    "Object for All in a Single Night"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.nodes = set()
        self.links = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self._process_line(line)

    def _process_line(self, text):
        "Assign values from a line of text"

        # 1. Parse the input line
        match = RE_INPUT.match(text)
        if match is None:
            print("Unable to parse input line <%s>" % text)
            return
        loc1, loc2, distance = match.groups()
        distance = int(distance)

        # 2. Add the locations
        self.nodes.add(loc1)
        self.nodes.add(loc2)

        # 3. Add the distances
        self.links[(loc1, loc2)] = distance
        self.links[(loc2, loc1)] = distance

    def find_route(self, shortest, verbose=False):
        "Find the shortest of longest route"

        # 1. Start with nothing
        route = []
        if shortest:
            best = 99999999999
            word = 'Shorter'
        else:
            best = 0
            word = 'Longer'

        # 2. Loop for all the permertations of locations
        for locs in permutations(self.nodes):

            # 3. Determine the length of this route
            length = 0
            last = None
            for loc in locs:
                if last is not None:
                    length += self.links[(last, loc)]
                last = loc

            # 4. Save if better than what we had
            if (shortest and length < best) or (not shortest and length > best):
                best = length
                route = locs
                if verbose:
                    print(word, route, best)

        # 5. Return the length of the best route
        if verbose:
            print("best", route, best)
        return best

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.find_route(True, verbose=verbose)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.find_route(False, verbose=verbose)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        r o u t e s . p y                       end
# ======================================================================
