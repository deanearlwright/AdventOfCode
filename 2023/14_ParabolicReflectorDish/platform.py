
# ======================================================================
# Parabolic Reflector Dish
#   Advent of Code 2023 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p l a t f o r m . p y
# ======================================================================
"Platform for the Advent of Code 2023 Day 14 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EMPTY = "."
ROUND = "O"
SQUARE = "#"

# ======================================================================
#                                                               Platform
# ======================================================================


class Platform(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Parabolic Reflector Dish"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.grid = []
        self.rows = 0
        self.cols = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 0. Precondition axiom
        assert text is not None and len(text) > 0

        # 1. Loop for each line in the text
        for line in text:

            # 2. Expand it into a list
            expanded = list(line)

            # 3. And add it to the grid
            self.grid.append(expanded)

        # 4. Set the number of rows and columns
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def total_load(self):
        "Returns the total load of rounded rock on the north support beam"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the rows and all of the columns
        for rindx, row in enumerate(self.grid):
            load = len(self.text) - rindx
            for _, char in enumerate(row):

                # 3. If this is a round rock, add in its load
                if char == ROUND:
                    result += load

        # 4. Return the total load
        return result

    def tilt_north(self):
        "Tilt the platform to the north allowing rocks to roll"

        # 1. Loop for every column
        for cindx in range(self.cols):

            # 2. Rock will roll to the lowest free row
            free = 0

            # 3. Loop for every row (north to south)
            for rindx in range(self.rows):
                char = self.grid[rindx][cindx]

                # 4. If it is a square rock, it is not moving
                if char == SQUARE:
                    free = rindx + 1

                # 5. If it is a round rock, it wants to roll
                if char == ROUND:
                    if free < rindx:
                        self.grid[free][cindx] = ROUND
                        self.grid[rindx][cindx] = EMPTY
                        free = free + 1
                    else:
                        free = rindx + 1

    def tilt_west(self):
        "Tilt the platform to the west allowing rocks to roll"

        # 1. Loop for every row
        for rindx in range(self.rows):

            # 2. Rock will roll to the lowest free column
            free = 0

            # 3. Loop for every row (west to east)
            for cindx in range(self.cols):
                char = self.grid[rindx][cindx]

                # 4. If it is a square rock, it is not moving
                if char == SQUARE:
                    free = cindx + 1

                # 5. If it is a round rock, it wants to roll
                if char == ROUND:
                    if free < cindx:
                        self.grid[rindx][free] = ROUND
                        self.grid[rindx][cindx] = EMPTY
                        free = free + 1
                    else:
                        free = cindx + 1

    def tilt_south(self):
        "Tilt the platform to the south allowing rocks to roll"

        # 1. Loop for every column
        for cindx in range(self.cols):

            # 2. Rock will roll to the highest free row
            free = self.rows - 1

            # 3. Loop for every row (north to south)
            for rindx in reversed(range(self.rows)):
                char = self.grid[rindx][cindx]

                # 4. If it is a square rock, it is not moving
                if char == SQUARE:
                    free = rindx - 1

                # 5. If it is a round rock, it wants to roll
                if char == ROUND:
                    if free > rindx:
                        self.grid[free][cindx] = ROUND
                        self.grid[rindx][cindx] = EMPTY
                        free = free - 1
                    else:
                        free = rindx - 1

    def tilt_east(self):
        "Tilt the platform to the west allowing rocks to roll"

        # 1. Loop for every row
        for rindx in range(self.rows):

            # 2. Rock will roll to the lowest free column
            free = self.cols - 1

            # 3. Loop for every row (west to east)
            for cindx in reversed(range(self.cols)):
                char = self.grid[rindx][cindx]

                # 4. If it is a square rock, it is not moving
                if char == SQUARE:
                    free = cindx - 1

                # 5. If it is a round rock, it wants to roll
                if char == ROUND:
                    if free > cindx:
                        self.grid[rindx][free] = ROUND
                        self.grid[rindx][cindx] = EMPTY
                        free = free - 1
                    else:
                        free = cindx - 1

    def spin(self):
        "Tilt the platform north, west, south, and then east"
        self.tilt_north()
        self.tilt_west()
        self.tilt_south()
        self.tilt_east()

    def grid_key(self):
        "Return a key for the current grid"

        return str(self)

    def you_spin_me_round(self, revolutions=1000000000):
        "Return the total load after the given number of revolutions"

        # 1. Remember what we have seen
        seen = {}
        spins = 0

        # 2. Loop for a long, long time
        while spins < revolutions:

            # 3. Get the key for the current grid state
            key = self.grid_key()

            # 4. If we have been here before, ...
            if key in seen:

                # 5. Determine what is left to do
                period = spins - seen[key]
                todo = (revolutions - spins) % period

                # 6. And do it
                return self.you_spin_me_round(revolutions=todo)

            # 7. Else we keep on keeping on
            seen[key] = spins
            self.spin()
            spins += 1

        return None

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.grid)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      p l a t f o r m . p y                     end
# ======================================================================
