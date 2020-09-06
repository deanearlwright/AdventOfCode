# ======================================================================
# Reservoir Research
#   Advent of Code 2018 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                            s c a n s . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 17 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
ROW_MULT = 1000
MIN_X = 0
MAX_X = 1
MIN_Y = 2
MAX_Y = 3

CHAR_CLAY = '#'
CHAR_SAND = '.'
CHAR_WATR = '|'
CHAR_FILL = '~'
CHAR_STRM = '+'

DOWN = 1000
LEFT = -1
RIGHT = 1

# ======================================================================
#                                                                  Scans
# ======================================================================


class Scans(object):   # pylint: disable=R0902, R0205
    "Object for Reservoir Research"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.clay = None
        self.water = None
        self.filled = None

        # 2. Process text (if any)
        if text is not None:
            self.process_text(text)

    def process_text(self, text):
        # 1. Start with no clay or water
        self.clay = set()
        self.water = set()
        self.filled = set()
        # 1. Loop for all lines of text
        for line in text:
            # 2. split line into x an y parts
            parts = line.split(', ')
            # 3. Process vertical clay lines
            if line.startswith('x'):
                x = int(parts[0][2:])
                y_range = parts[1][2:].split('..')
                for y in range(int(y_range[0]), int(y_range[1]) + 1):
                    self.clay.add(ROW_MULT * y + x)
            # 4. Process horizontal clay lines
            else:
                y = int(parts[0][2:])
                x_range = parts[1][2:].split('..')
                for x in range(int(x_range[0]), int(x_range[1]) + 1):
                    self.clay.add(ROW_MULT * y + x)
        # 5. Add in the spring
        self.water.add(500)

    def clay_range(self):
        # 1. Start the dimensions
        result = [999, 0, 999, 0]
        # 2. Loop for all of the clay locations
        for clay in self.clay:
            # 3. Break into x and y
            y, x = divmod(clay, ROW_MULT)
            # 4. Extend the result as
            if x < result[MIN_X]:
                result[MIN_X] = x
            if x > result[MAX_X]:
                result[MAX_X] = x
            if y < result[MIN_Y]:
                result[MIN_Y] = y
            if y > result[MAX_Y]:
                result[MAX_Y] = y
        # 5. Return the dimensions
        return result

    def __str__(self):
        # 1. Nothing to see if no clay defined
        if not self.clay:
            return ''
        # 1. Get Clay dimensions
        dimensions = self.clay_range()
        dimensions[MIN_X] = dimensions[MIN_X] - 1
        dimensions[MAX_X] = dimensions[MAX_X] + 1
        dimensions[MIN_Y] = 0
        # 3. Start with nothing
        result = []
        # 4. Loop for all of the rows in the grid
        for row_num in range(dimensions[MAX_Y] + 1):
            # 5. Start the row
            row = []
            # 6. Loop for all of the columns in the row
            for col_num in range(dimensions[MIN_X], dimensions[MAX_X] + 1):
                loc = row_num * ROW_MULT + col_num
                if loc in self.clay:
                    row.append(CHAR_CLAY)
                elif loc in self.water:
                    if row_num == 0:
                        row.append(CHAR_STRM)
                    else:
                        row.append(CHAR_WATR)
                elif loc in self.filled:
                    row.append(CHAR_FILL)
                else:
                    row.append(CHAR_SAND)
            # 7. Add the row
            result.append(''.join(row))
        # 8. Return the grid
        return '\n'.join(result)

    def drip(self, max_y):
        # 1. Loop for all of the water
        more = set()
        fill = set()
        for loc in self.water:
            #  2. Water want to flow down
            down = loc + DOWN
            if down not in self.clay and down not in self.water and down not in self.filled:
                # print("loc=%d, max_y=%d, down=%d not clay or water or filled: more water" % (loc, max_y, down))
                m = self.fill_down(down, max_y)
                more = more | m
            # 3. Expand on same level
            elif down in self.clay or down in self.filled:
                # print("loc=%d, max_y=%d, down=%d is clay or filled: more water" % (loc, max_y, down))
                f, m = self.fill_level(loc)
                fill = fill | f
                more = more | m

        # 4. Add in all the new water
        self.water = self.water | more
        for f in fill:
            self.filled.add(f)
            if f in self.water:
                self.water.remove(f)

    def fill_down(self, down, max_y):
        result = set()
        while down not in self.clay and down not in self.water and down not in self.filled and down < max_y:
            result.add(down)
            down += DOWN
        return result

    def fill_level(self, loc):
        #  1. Initially just fill the current location
        fill = set([loc])
        more = set()
        overflow = False
        # 2. Fill left
        left = loc + LEFT
        down = left + DOWN
        while left not in self.clay and (down in self.clay or down in self.filled):
            #  print("Filling left from %d at %d" % (loc, left))
            fill.add(left)
            left = left + LEFT
            down = left + DOWN
        if left not in self.clay:
            more.add(left)
            overflow = True
        # 3. Fill right
        right = loc + RIGHT
        down = right + DOWN
        while right not in self.clay and (down in self.clay or down in self.filled):
            #  print("Filling right from %d at %d" % (loc, right))
            fill.add(right)
            right = right + RIGHT
            down = right + DOWN
        if right not in self.clay:
            more.add(right)
            overflow = True
        # 4. If overflow, all are water
        if overflow:
            more = more | fill
            fill = set()
        # 5. Return filled and running water
        return fill, more

    def flood(self, verbose=False, limit=0):
        # 1. Determine the lowest level for water calculations
        dimension = self.clay_range()
        max_y = (1 + dimension[MAX_Y]) * ROW_MULT
        # 2. Loop until the amount of water doesn't change
        water = 0
        filled = 0
        drips = 0
        while (water != len(self.water) or filled != len(self.filled)) and (limit == 0 or drips < limit):
            water = len(self.water)
            filled = len(self.filled)
            # 3. Add a little more water
            self.drip(max_y)
            drips += 1
            if verbose:
                print(str(self))
                print("drips=%d water was=%d now=%d, filled was %d now=%d" %
                      (drips, water, len(self.water), filled, len(self.filled)))

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Let the water flow
        self.flood(verbose=verbose, limit=limit)
        # print(str(self))
        # 2. Return the solution for part one
        dimensions = self.clay_range()
        return len(self.water) + len(self.filled) - dimensions[MIN_Y]

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"
        # 1. Let the water flow
        self.flood(verbose=verbose, limit=limit)
        # print(str(self))
        # 2. Return the solution for part two
        return len(self.filled)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          s c a n s . p y                       end
# ======================================================================
