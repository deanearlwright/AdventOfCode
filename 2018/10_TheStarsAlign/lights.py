# ======================================================================
# The Stars Align
#   Advent of Code 2018 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         l i g h t s . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 10 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Light
# ======================================================================


class Light(object):   # pylint: disable=R0902, R0205
    "Object for The Stars Align - one light"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.posX = 0;
        self.posY = 0;
        self.velX = 0;
        self.velY = 0;

        # 2. Process text (if any)
        if text is not None:
            parts = text.replace('<',' ').replace('>','').replace(',','').replace('=', '').replace('  ', ' ').split(' ')
            self.posX = int(parts[1], 10)
            self.posY = int(parts[2], 10)
            self.velX = int(parts[4], 10)
            self.velY = int(parts[5], 10)

    def step(self):
        self.posX += self.velX
        self.posY += self.velY

# ======================================================================
#                                                                 Lights
# ======================================================================


class Lights(object):   # pylint: disable=R0902, R0205
    "Object for The Stars Align - multiple lights"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.points = []

        # 2. Process text (if any)
        if text is not None:
            for line in text:
                self.points.append(Light(text=line, part2=part2))

    def step(self):
        for point in self.points:
            point.step()

    def rows(self):
        if len(self.points) == 0:
            return 0
        minRow = self.points[0].posY
        maxRow = minRow
        for point in self.points:
            minRow = min(minRow, point.posY)
            maxRow = max(maxRow, point.posY)
        return 1 + maxRow - minRow

    def display(self):
        if len(self.points) == 0:
            return ''
        minCol = self.points[0].posX
        maxCol = minCol
        minRow = self.points[0].posY
        maxRow = minRow
        for point in self.points:
            minCol = min(minCol, point.posX)
            maxCol = max(maxCol, point.posX)
            minRow = min(minRow, point.posY)
            maxRow = max(maxRow, point.posY)
        cols = 1 + maxCol - minCol

        # rows = 1 + maxRow - minRow
        result = []
        for row in range(minRow, maxRow + 1):
            empty = [' ']*cols
            for point in self.points:
                if point.posY == row:
                    empty[point.posX - minCol] = '.'
            result.append(''.join(empty))
        return '\n'.join(result)


    def run_until_image(self, verbose=False, limit=0):
        minRows = self.rows()
        steps = 0
        while limit == 0 or steps < limit:
            numRows = self.rows()
            if verbose:
                print("step %s rows %s" % (steps, numRows))
            if numRows <= 10:
                print(steps)
                print(self.display())
            if numRows <= minRows:
                minRows = numRows
            else:
                return 'HI'
            self.step()
            steps += 1
        return None

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.run_until_image(verbose=verbose, limit=limit)


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return None

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          l i g h t s . p y                     end
# ======================================================================
