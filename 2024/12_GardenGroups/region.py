
# ======================================================================
# Garden Groups
#   Advent of Code 2024 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r e g i o n . p y
# ======================================================================
"Region for the Advent of Code 2024 Day 12 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple

# ----------------------------------------------------------------------
#                                                                   type
# ----------------------------------------------------------------------
CORNER = namedtuple("Corner", "north south east west knt corners")

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
N = (-1, 0)
S = (1, 0)
E = (0, 1)
W = (0, -1)
DELTA = [N, S, E, W]

NE = (-1, 1)
NW = (-1, -1)
SE = (1, 1)
SW = (1, -1)

CORNERS = [
    CORNER(north=False, south=False, east=False, west=False, knt=4, corners=[]), # 0
    CORNER(north=False, south=False, east=False, west=True, knt=2, corners=[]),  # 1
    CORNER(north=False, south=False, east=True, west=False, knt=2, corners=[]),  # 2
    CORNER(north=False, south=False, east=True, west=True, knt=0, corners=[]),   # 3

    CORNER(north=False, south=True, east=False, west=False, knt=2, corners=[]),  # 4
    CORNER(north=False, south=True, east=False, west=True, knt=1, corners=[SW]), # 5
    CORNER(north=False, south=True, east=True, west=False, knt=1, corners=[SE]), # 6
    CORNER(north=False, south=True, east=True, west=True, knt=0, corners=[SE, SW]), # 7

    CORNER(north=True, south=False, east=False, west=False, knt=2, corners=[]),     # 8
    CORNER(north=True, south=False, east=False, west=True, knt=1, corners=[NW]),    # 9
    CORNER(north=True, south=False, east=True, west=False, knt=1, corners=[NE]),    # 10
    CORNER(north=True, south=False, east=True, west=True, knt=0, corners=[NE, NW]), # 11

    CORNER(north=True, south=True, east=False, west=False, knt=0, corners=[]),      # 12
    CORNER(north=True, south=True, east=False, west=True, knt=0, corners=[NW, SW]), # 13
    CORNER(north=True, south=True, east=True, west=False, knt=0, corners=[NE, SE]), # 14
    CORNER(north=True, south=True, east=True, west=True, knt=0, corners=[NE, NW, SE, SW]),
]

DIR_INDX = {
    N: 8,
    S: 4,
    E: 2,
    W: 1,
}

# ======================================================================
#                                                                 Region
# ======================================================================


class Region(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Garden Groups"

    def __init__(self, label=None, plot=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.label = label
        self.plots = set()
        if plot is not None:
            self.plots.add(plot)

    def expand(self, plot):
        "Add another plot"
        self.plots.add(plot)

    def area(self):
        "Return the area of the region"
        return len(self.plots)

    def touches(self):
        "Return the number of connects between the plots"

        # 1. Start with nothing
        result = 0

        # 2. Loop for each plot
        for plot in self.plots:

            # 3. Loop for each directions
            for delta in DELTA:

                # 4. Compute the nearby location
                loc = (plot[0] + delta[0], plot[1] + delta[1])

                # 5. Increase touches if that loc is also in the region
                if self.has_loc(loc):
                    result += 1

        # 6. Return the number of aligned edges
        return result

    def perimeter(self):
        "Return the perimeter of the region"
        return len(self.plots) * 4 - self.touches()

    def price(self):
        "Return the price of a fence for the region"
        return self.area() * self.perimeter()

    def has_loc(self, loc):
        "Returns True if location in the region"
        return loc in self.plots

    def corner_index(self, loc):
        "Get the index to CORNERS"

        # 1. Start with nothing
        result = 0

        # 2. Loop for the cardinal directions
        for delta, indx in DIR_INDX.items():

            # 3. Compute the new location
            neighbor = (loc[0] + delta[0], loc[1] + delta[1])

            # 4. Increment the index if the neighbor is not in the region
            if self.has_loc(neighbor):
                result += indx

        # 5. Return the index
        # print(loc, result)
        return result

    def corners_at_loc(self, loc):
        "Count the number of corners at the location"
        assert loc in self.plots

        # 1. Get the corners index based on the neighbors
        indx = self.corner_index(loc)

        # 2. Start with the basic corner count
        result = CORNERS[indx].knt

        # 3. Check any other neighbors
        for delta in CORNERS[indx].corners:
            if not self.has_loc((loc[0] + delta[0], loc[1] + delta[1])):
                result += 1

        # 4. Return the total of the corners
        # print(loc, indx, result)
        return result

    def sides(self):
        "Return the number of sides of the region"
        return sum([self.corners_at_loc(loc) for loc in self.plots])

    def price2(self):
        "Return the price of a fence for the region"
        return self.area() * self.sides()

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        r e g i o n . p y                       end
# ======================================================================
