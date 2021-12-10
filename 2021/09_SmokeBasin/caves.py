# ======================================================================
# Smoke Basin
#   Advent of Code 2021 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c a v e s . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 09 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import math

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DELTA = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# ======================================================================
#                                                                  Caves
# ======================================================================


class Caves(object):   # pylint: disable=R0902, R0205
    "Object for Smoke Basin"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.heights = {}
        self.basins = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for row, line in enumerate(text):
                for col, height in enumerate(line):
                    self.heights[(col, row)] = int(height)

    def adjacent_heights(self, loc):
        "Return list of heights of adjacent locations"

        # 1. Start with nothing
        result = []

        # 2. Loop for the deltas
        for delta in DELTA:

            # 3. Get adjacent location
            delta_loc = (loc[0] + delta[0], loc[1] + delta[1])

            # 4. If the location exists, save the height
            if delta_loc in self.heights:
                result.append(self.heights[delta_loc])

        # 5. Return heights in adjacent locations
        return result

    def not_nines(self, loc):
        "Return_the_adjacent locations that aren't height of 9 (or are off the map)"

        # 1. Start with nothing
        result = []

        # 2. Loop for the deltas
        for delta in DELTA:

            # 3. Get adjacent location
            delta_loc = (loc[0] + delta[0], loc[1] + delta[1])

            # 4. If the location exists, add it if the height is not nine
            if delta_loc in self.heights and self.heights[delta_loc] < 9:
                result.append(delta_loc)

        # 5. Return adjacent non-nine locations
        return result

    def is_lowest(self, loc):
        "Returns True if the location is the lower than the adjacent locations"

        # 1. Get the height at the location
        height = self.heights[loc]

        # 2. Get the adjacent heights
        heights = self.adjacent_heights(loc)

        # 3. Is the locations hight the lowest of them all?
        return height < min(heights)

    def lowest_points(self):
        "Return a list of the lowest points"

        # 1. Start with nothing
        result = []

        # 2. Loop for all the locations
        for loc in self.heights:

            # 3. If this is a low, add it to the result
            if self.is_lowest(loc):
                result.append(loc)

        # 4. Return the lowest points
        return result

    def risk(self, loc):
        "Returns the risk at the location"

        # 1. Get the height of the location
        height = self.heights[loc]

        # 2. Risk is height plus one
        return height + 1

    def total_risk(self, locs=None):
        "Return the total risk of the given locations or the lowest ones"

        # 1. If locs are not given, get the lowest ones
        if locs is None:
            locs = self.lowest_points()

        # 2. Return the total risk of all the locations
        return sum([self.risk(l) for l in locs])

    def grow_basin(self, loc):
        "Grow a basin starting at the lowest point"

        # 1. Start with the lowest point and the locations to check
        result = set([loc])
        check = [loc]

        # 2. Loop while there are locations to check
        while len(check) > 0:

            # 3. Take a location to check
            loc = check.pop()

            # 4. Get the non-nine locations near this one
            nearby = self.not_nines(loc)

            # 5. Look at all of these locations
            for nloc in nearby:

                # 6. If this is a new location, add it
                if nloc not in result:
                    result.add(nloc)
                    check.append(nloc)

        # 7. Return the basin
        return result

    def get_basins(self):
        "Get all the basins and return the product of the top three"

        # 1. Loop for all of the losest points
        for loc in self.lowest_points():

            # 2. Grow the basin abound that point
            basin = self.grow_basin(loc)

            # 3. Add the basin
            self.basins.append(basin)

        # 4. Get the size of the basins in sorted order
        sizes = [len(b) for b in self.basins]
        sizes.sort()

        # 5. Return the product of the largest three
        return math.prod(sizes[-3:])

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.total_risk()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.get_basins()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         c a v e s . p y                        end
# ======================================================================
