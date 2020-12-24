# ======================================================================
# Conway Cubes
#   Advent of Code 2020 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p o c k e t . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 17 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
ACTIVE = '#'
INACTIVE = '.'
ACTIVE_COUNT = frozenset([2, 3])
INACTIVE_COUNT = frozenset([3])

# ======================================================================
#                                                                 Pocket
# ======================================================================


class Pocket(object):   # pylint: disable=R0902, R0205
    "Object for Conway Cubes"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.cycle = 0
        self.active = set()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for y, cells in enumerate(text):
                for x, cell in enumerate(cells):
                    if cell == ACTIVE:
                        if self.part2:
                            self.active.add((x, y, 0, 0))
                        else:
                            self.active.add((x, y, 0))
        self.active = frozenset(self.active)

    def nearby(self, loc):
        "Returns the count of nearby active cells"
        if self.part2:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    for z in range(-1, 2):
                        for w in range(-1, 2):
                            if x != 0 or y != 0 or z != 0 or w != 0:
                                yield (x + loc[0], y + loc[1], z + loc[2], w + loc[3])

        else:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    for z in range(-1, 2):
                        if x != 0 or y != 0 or z != 0:
                            yield (x + loc[0], y + loc[1], z + loc[2])

    def count_nearby(self, loc):
        result = 0
        for neighbor in self.nearby(loc):
            if neighbor in self.active:
                result += 1
        return result

    def one_cycle(self):
        "Run the simulation for one cycle"

        # 1. Start with nothing
        next_active = set()
        next_checked = set()

        # 2. Loop for all active cells
        for act_loc in self.active:

            # 3. Determine if it will remain active
            if self.count_nearby(act_loc) in ACTIVE_COUNT:
                next_active.add(act_loc)

            # 4. Loop for all of the empty neighbors of that cell
            for act_neighbor in self.nearby(act_loc):
                if act_neighbor in self.active:
                    continue

                # 5. If we have already checked this location, move on
                if act_neighbor in next_checked:
                    continue

                # 6. Determine if it will become active
                if self.count_nearby(act_neighbor) in INACTIVE_COUNT:
                    next_active.add(act_neighbor)

                # 7. Remember that we have checked this location
                next_checked.add(act_neighbor)

        # 8. The future is now
        self.active = frozenset(next_active)

        # 9. Update the cycle count
        self.cycle += 1

    def count(self):
        "Returns the count of active cubes"
        return len(self.active)

    def run_until(self, cycle):
        "Run the simulation until the specified time, returns count of active cubes"

        while self.cycle < cycle:
            self.one_cycle()
        return self.count()

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.run_until(6)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.run_until(6)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        p o c k e t . p y                       end
# ======================================================================
