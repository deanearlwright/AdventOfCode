
# ======================================================================
# Lavaduct Lagoon
#   Advent of Code 2023 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           l a g o o n . p y
# ======================================================================
"Lagoon for the Advent of Code 2023 Day 18 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

from plan import Plan
# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DELTA = {
    'U': (-1, 0),
    'D': (1, 0),
    'R': (0, 1),
    'L': (0, -1),
}

MAP_TRENCH = '#'
MAP_GROUND = '.'
MAP_DOUBLE = ".#."

# ======================================================================
#                                                                 Lagoon
# ======================================================================


class Lagoon(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Lavaduct Lagoon"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.plan = None
        self.trench = {}
        self.corners = []
        self.distance = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.plan = Plan(text=text, part2=part2)

    def execute_plan(self):
        "Execute the plan"

        # 1. Start at the very beginning
        loc = (0, 0)
        self.trench[loc] = "000000"
        self.corners.append(loc)
        distance = 0

        # 2. Follow each step of the plan
        for step in self.plan:

            # 3. Get the step specifics
            action, meters, hex_color = step.specs()
            delta = DELTA[action]

            # 4. Dig in the indicated direction
            if not self.part2:
                for _ in range(meters):
                    loc = (loc[0] + delta[0], loc[1] + delta[1])
                    self.trench[loc] = hex_color
            else:
                loc = (loc[0] + meters * delta[0], loc[1] + meters * delta[1])
                distance += meters

            # 5. Keep track of the corners
            self.corners.append(loc)

        # 6. Remember the lenght of the trench
        if not self.part2:
            self.distance = len(self.trench)
        else:
            self.distance = distance

        # 7. Return the trench distance (mainly for testing)
        return self.distance

    def get_dimensions(self):
        "Determine the outside dimensions of the lagoon"

        # 1. Start with nothing
        min_row = 99999999
        min_col = 99999999
        max_row = 0
        max_col = 0

        # 2. Loop for all of the trench locations
        for trench in self.trench:

            # 3. Adjust the bounding box
            row, col = trench
            min_row = min(min_row, row)
            max_row = max(max_row, row)
            min_col = min(min_col, col)
            max_col = max(max_col, col)

        # 4. Return the bounding box
        return min_row, min_col, max_row, max_col

    def __str__(self):
        "Returns a map of the trench"

        # 1. Start with nothing
        rows = []

        # 2. Get the dimensions of the trench
        min_row, min_col, max_row, max_col = self.get_dimensions()

        # 3. Loop for all the rows
        for rindx in range(min_row, max_row + 1):

            # 4. Loop for all the columns
            this_row = self.map_this_row(rindx, min_col, max_col)

            # 5. Add the the newly mapped row
            rows.append(this_row)

        # 6. return the trench map
        return '\n'.join(rows)

    def map_this_row(self, rindx, min_col, max_col):
        "Map this row"

        # 1. Start with nothing
        this_row = []

        # 2. Map this row
        for cindx in range(min_col, max_col + 1):
            if (rindx, cindx) in self.trench:
                this_row.append(MAP_TRENCH)
            else:
                this_row.append(MAP_GROUND)

        # 4. Return the row as a string
        return ''.join(this_row)

    def row_interior(self, rindx, min_col, max_col):
        "Return the number of internal spaces in this lagoon row"

        # 1. Start with nothing
        result = 0
        parity = False

        # 2. Map this row
        this_row = MAP_GROUND + self.map_this_row(rindx, min_col, max_col) + MAP_GROUND

        # 3. Replace pairs of trenches with a single trench
        for pounds in range(2, 1 + max_col - min_col, 2):
            repl = MAP_GROUND + (MAP_TRENCH * pounds) + MAP_GROUND
            this_row = this_row.replace(repl, MAP_DOUBLE)
        this_row = this_row.strip(MAP_GROUND)
        # print(f"{rindx}: {this_row}")

        # 4. Loop for all the columns in the adjusted row
        for char in this_row:

            # 5. If this column is part of the trench, adjust parity
            if char == MAP_TRENCH:
                parity = not parity

            # 6. Else the column is part of the lagoon if parity is True
            elif parity:
                result += 1

        # 7. Return the number of interier spaces in this row
        return result

    def shoelace_area(self):
        "Return the area computed by the Shoelace Formula (since parity isn't working)"

        # 1. Start with nothing
        result = 0

        # 2. Loop for every corner
        for cindx, corner in enumerate(self.corners):

            # 3. Calculate the signed area contribution of the current segment
            area = (corner[0]
                    * (self.corners[cindx - 1][1] -
                     self.corners[(cindx + 1) % len(self.corners)][1]))
            result += area

        # 4. Normalize the area
        return abs(result) // 2

    def cubic_meters(self):
        "Return the number of cubic meters in the dug out lagoon"

        # 1. Get the area of the lagoon
        area = self.shoelace_area()

        # 2. Use Pick's theorem to calculate the number of interior points
        # https://en.wikipedia.org/wiki/Pick%27s_theorem
        interior = area - self.distance // 2 + 1

        # 4. Normalize the area
        return interior + self.distance

    def old_cubic_meters(self):
        "Return the number of cubic meters in the dug out lagoon"

        # 1. Start with nothing
        result = 0

        # 2. Get the dimensions of the trench
        min_row, min_col, max_row, max_col = self.get_dimensions()

        # 3. Loop for all the rows
        for rindx in range(min_row, max_row + 1):

            # 4. Get the number of interior spaces in this row
            row_spaces = self.row_interior(rindx, min_col, max_col)

            # 5. Add these to the total
            result += row_spaces

        # 6. Return the total size of lagoon (interior and trench)
        return result + len(self.trench)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        l a g o o n . p y                       end
# ======================================================================
