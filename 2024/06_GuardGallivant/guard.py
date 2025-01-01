
# ======================================================================
# Guard Gallivant
#   Advent of Code 2024 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         g u a r d . p y
# ======================================================================
"Guard for the Advent of Code 2024 Day 06 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DELTA = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1),
}
TURN_RIGHT = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^",
}

# ======================================================================
#                                                                  Guard
# ======================================================================


class Guard(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Guard Gallivant"

    def __init__(self, direction="^", loc=(0, 0), max_loc=(0, 0)):

        # 1. Set the initial values
        self.dir = direction
        self.loc = loc
        self.max_loc = max_loc

        # 2. Save the starting direction and location
        self.start_dir = self.dir
        self.start_loc = self.loc

    def reset(self):
        "Return to the starting position"
        self.dir = self.start_dir
        self.loc = self.start_loc

    def did_elvis_leave_the_building(self):
        "Return True if the guard is no longer in the lab"

        # 1. Leave by north or west?
        if self.loc[0] < 0 or self.loc[1] < 0:
            return True

        # 2. Leave by south or east?
        if self.loc[0] >= self.max_loc[0] or self.loc[1] >= self.max_loc[1]:
            return True

        # 4. If not, the guard is still in the lab
        return False

    def one_step(self, obstructions):
        "Move the guard a single step"

        # 1. Where would the next location be
        delta = DELTA[self.dir]
        next_loc = (self.loc[0] + delta[0], self.loc[1] + delta[1])

        # 2. If that would be an obstructions, just turn
        if next_loc in obstructions:
            self.dir = TURN_RIGHT[self.dir]
            #print("new dir", self.dir, self.loc)
            return

        # 3. Move to the new location
        self.loc = next_loc
        #print(self.dir, next_loc)

    def multiple_steps(self, obstructions):
        "Move the guard around the lab and return the unique locations"

        # 1. Start with almost nothing
        locs = set()
        locs.add(self.loc)

        # 2. Loop until the guards leaves the building
        while True:

            # 3. Take one step
            self.one_step(obstructions)

            # 4. Did that make us leave?
            if self.did_elvis_leave_the_building():
                break

            # 5. Remember this location
            locs.add(self.loc)

        # 6. Return the unique places walked
        return locs

    def loop_steps(self, obstructions):
        "Move the guard around the lab until loop or leaves"

        # 1. Start with almost nothing
        locs = set()
        locs.add((self.dir, self.loc))

        # 2. Loop until the guards leaves the building or loops
        while True:

            # 3. Take one step
            self.one_step(obstructions)

            # 4. Did that make us leave
            if self.did_elvis_leave_the_building():
                return False

            # 5. Where are we
            here = (self.dir, self.loc)

            # 6. If we were here before, we have looped
            if here in locs:
                return True

            # 7. Remember this direction and location
            locs.add(here)

        # 8. Should never reach here
        assert len(locs) == 0

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                         g u a r d . p y                        end
# ======================================================================
