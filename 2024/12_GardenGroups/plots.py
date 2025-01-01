
# ======================================================================
# Garden Groups
#   Advent of Code 2024 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p l o t s . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 12 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import region

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# ======================================================================
#                                                                  Plots
# ======================================================================


class Plots(object):   # pylint: disable=R0902, R0205
    "Object for Garden Groups"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rows = 0
        self.cols = 0
        self.regions = []
        self.mapped = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text()

    def _process_text(self):
        "Assign values from text"

        assert self.text is not None and len(self.text) > 0

        # 1. Get the number of rows and columns
        self.rows = len(self.text)
        self.cols = len(self.text[0])

        # 2. Loop for all of the rows and columns
        for row, line in enumerate(self.text):
            for col, label in enumerate(line):
                loc = (row, col)

                # 3. Ignore location if already mapped
                if loc in self.mapped:
                    continue

                # 4. Map this region
                self.map_this_region(label, loc)

    def map_this_region(self, label, loc):
        "Create and expand this region"

        # 1. Create a new region for this location
        reg = region.Region(label=label, plot=loc, part2=self.part2)

        # 2. You are known
        self.mapped[loc] = reg
        self.regions.append(reg)

        # 3. Expand the region
        self.expand_region(reg, loc)

    def expand_region(self, reg, loc):
        "Expand the region from this location"

        # 1. Loop for all the nearby locations
        for adjacent in self.get_nearby_plot_locations(loc):

            # 2. Ignore if already mapped
            if adjacent in self.mapped:
                continue

            # 3. Ignore if not the same label
            if reg.label != self.text[adjacent[0]][adjacent[1]]:
                continue

            # 4. Add this location to the region
            reg.expand(adjacent)
            self.mapped[adjacent] = reg

            # 5. Expand the region further
            self.expand_region(reg, adjacent)

    def get_nearby_plot_locations(self, loc):
        "return list of adjacent plot locations"

        # 1. Start with nothing
        result = []

        # 2. Loop for four directions
        for delta in DELTA:

            # 3. Calculate adjacent location
            adjacent = (loc[0] + delta[0], loc[1] + delta[1])

            # 4. Ignore if not a valid location
            if adjacent[0] < 0 or adjacent[0] >= self.rows:
                continue
            if adjacent[1] < 0 or adjacent[1] >= self.cols:
                continue

            # 5. Add this location to the result
            result.append(adjacent)

        # 6. Return the valid adjacent locations
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
        return sum(x.price() for x in self.regions)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part two
        return sum(x.price2() for x in self.regions)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                         p l o t s . p y                        end
# ======================================================================
