# ======================================================================
# Like a GIF For Your Yard
#   Advent of Code 2015 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c o n w a y . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 18 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
IS_ON = '#'
IS_OFF = '.'
DELTA = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

# ======================================================================
#                                                                 Conway
# ======================================================================


class Conway(object):   # pylint: disable=R0902, R0205
    "Object for Like a GIF For Your Yard"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.grid = set()
        self.size = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for rindx, row in enumerate(self.text):
                if self.size == 0:
                    self.size = len(row)
                elif self.size != len(row):
                    print("Inconsistent row sizes", rindx, len(row), self.size)
                for cindx, col in enumerate(row):
                    if col == IS_ON:
                        self.grid.add((cindx, rindx))

        # 3. Part two needs the four corners
        if self.part2:
            self.always_on(self.grid)

    def number_on(self):
        "Return the number of lights that are on"
        return len(self.grid)

    def __str__(self):
        rows = []
        for rindx in range(self.size):
            row = []
            for cindx in range(self.size):
                if (cindx, rindx) in self.grid:
                    row.append(IS_ON)
                else:
                    row.append(IS_OFF)
            rows.append(''.join(row))
        return '\n'.join(rows)

    def neighbors(self, loc):
        "Returns the number of neighbors for the location"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the neighbot coordinates
        for delta in DELTA:

            # 3. Get the coordinates of the neighbor
            neighbor = (loc[0] + delta[0], loc[1] + delta[1])

            # 4. If the neighbor is turned on, increment the count
            if neighbor in self.grid:
                result += 1

        # 5. Return the count of the neighbors
        return result

    def next_gen(self):
        "Returns the next generation of lights"

        # 1. Start with nothing
        result = set()

        # 2. Loop for all of the rows and columns
        for rindx in range(self.size):
            for cindx in range(self.size):
                loc = (cindx, rindx)

                # 3. Get the count of neighbors
                knt = self.neighbors(loc)

                # 4. Follow the rules
                if (loc) in self.grid:
                    if knt == 3 or knt == 2:
                        result.add(loc)
                else:
                    if knt == 3:
                        result.add(loc)

        # 5. Part two needs the corners on
        if self.part2:
            self.always_on(result)

        # 6. Return the next generation
        return result

    def century(self):
        "Go for 100 turns"

        # 1. Loop 100 times
        for _ in range(100):
            self.grid = self.next_gen()

        # 2, Return the number of lights that are on
        return self.number_on()

    def always_on(self, grid):
        "Add the for corners"

        # 1. Add the four corners
        grid.add((0, 0))
        grid.add((0, self.size - 1))
        grid.add((self.size - 1, 0))
        grid.add((self.size - 1, self.size - 1))

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.century()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.century()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        c o n w a y . p y                       end
# ======================================================================
