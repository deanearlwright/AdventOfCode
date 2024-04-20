
# ======================================================================
# Step Counter
#   Advent of Code 2023 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                            g a r d e n . p y
# ======================================================================
"Garden for the Advent of Code 2023 Day 21 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple
from math import ceil

# ----------------------------------------------------------------------
#                                                                  types
# ----------------------------------------------------------------------
Loc = namedtuple("Loc", "r, c")
State = namedtuple("State", "loc, steps")

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
START = "S"
GARDEN = "."
ROCK = "#"

DELTA = [
    Loc(-1, 0),
    Loc(1, 0),
    Loc(0, 1),
    Loc(0, -1),
]

# ======================================================================
#                                                                 Garden
# ======================================================================


class Garden(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Step Counter"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rows = 0
        self.cols = 0
        self.start = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.rows = len(self.text)
            self.cols = len(self.text[0])
            assert self.cols == len(self.text[-1])
            self.start = self.find_start()

    def find_start(self):
        "Find the starting location"

        # 1. Loop for all the rows and columns
        for rindx, row in enumerate(self.text):
            for cindx, char in enumerate(row):

                # 2. If this is the staarting location, we found it
                if char == START:
                    return Loc(rindx, cindx)

        # 3. It should have been somewhere
        assert False, "Unable to find the starting position"

    def plots(self, max_steps=0):
        "Return the total number of plots that can be reach in the indicated number of steps"

        # 1. Have to start somewhere
        loc = self.start
        prev_locs = set([loc])

        # 2. Loop for all the steps
        for step in range(max_steps):
            assert 0 <= step < max_steps # Gets rid of unused variable warning

            # 3. Start of this step loop
            next_locs = set()

            # 4. Loop for all of the current locations
            while prev_locs:
                loc = prev_locs.pop()

                # 5. Where can we go from here?
                new_locs = [self.is_plot(loc, delta) for delta in DELTA]
                new_locs = [nl for nl in new_locs if nl is not None]

                # 6. Start there next round
                for loc in new_locs:
                    next_locs.add(loc)

            # 7. The future is now
            # print(f"{step} -> {next_locs}")
            prev_locs = next_locs

        # 8. Oh, the places you've been
        return len(prev_locs)

    def is_plot(self, loc, delta=Loc(0, 0), infinite=False):
        "Is this location a garden plot"

        # 1. Calculate the new row and column
        loc = Loc(loc.r + delta.r, loc.c + delta.c)

        # 2. It is not one if off the grid
        if not infinite:
            if loc.r < 0 or loc.r >= self.rows or loc.c < 0 or loc.c >= self.cols:
                return None

        # 3. Check the grid for a rock
        if self.text[loc.r % self.rows][loc.c % self.cols] == ROCK:
            return None

        # 4. It must be a garden
        return loc

    def infinite(self, max_steps=0):
        "Return the total number of plots when there are infinite gardens"

        # 1. Have to start somewhere
        loc = self.start
        prev_locs = set([loc])

        # 2. Loop for all the steps
        for step in range(max_steps):
            assert 0 <= step < max_steps # Gets rid of unused variable warning

            # 3. Start of this step loop
            next_locs = set()

            # 4. Loop for all of the current locations
            while prev_locs:
                loc = prev_locs.pop()

                # 5. Where can we go from here?
                new_locs = [self.is_plot(loc, delta, infinite=True) for delta in DELTA]
                new_locs = [nl for nl in new_locs if nl is not None]

                # 6. Start there next round
                for loc in new_locs:
                    next_locs.add(loc)

            # 7. The future is now
            # print(f"{step} -> {next_locs}")
            prev_locs = next_locs

        # 8. Oh, the places you've been
        return len(prev_locs)

    def calc_infinite(self, max_steps=26501365):
        "Return the number of plots when there are infinite gardens without actually going there"

        # 1. What are the signigicant steps
        steps = max_steps % self.rows
        assert self.rows == self.cols
        print(self.rows, steps)

        # 2. Get the plot counts at the signigicant steps
        plots = [self.infinite(max_steps=n)
                 for n in range(steps, 1 + steps + 2 * self.rows, self.rows)]
        # plots = [3778, 33833, 93864]
        print(plots)

        # 3. Copied from r/adventofcode comments because I didn't want to do the calculus myself
        #     finite-difference formulas to find coefficients of the polynomial
        diff0 = plots[1] - plots[0]
        diff1 = plots[2] - plots[1]

        polya = (diff1 - diff0) // 2
        polyb = diff0 - 3 * polya
        polyc = plots[0] - polyb - polya

        polyn = ceil(max_steps / self.rows)

        answer = polya * polyn**2 + polyb * polyn + polyc

        # 4. Oh, the places you've been
        return answer


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        g a r d e n . p y                       end
# ======================================================================
