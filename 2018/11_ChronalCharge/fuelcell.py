# ======================================================================
# Chronal Charge
#   Advent of Code 2018 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         f u e l c e l l . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 11 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
WIDTH = 300
HEIGHT = 300

# ======================================================================
#                                                               Fuelcell
# ======================================================================


class Fuelcell(object):   # pylint: disable=R0902, R0205
    "Object for Chronal Charge"

    def __init__(self, height=HEIGHT, width=WIDTH, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.height = height
        self.width = width
        self.grid_offset = [0, 1, 2,
                            self.width + 0, self.width + 1, self.width + 2,
                            self.width + self.width + 0, self.width + self.width + 1, self.width + self.width + 2]
        self.serial = None
        self.cells = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.cells = []
            self.serial = int(text[0], 10)
            for y in range(1, self.height + 1):
                for x in range(1, self.width + 1):
                    self.cells.append(self.level(x, y))

    def level(self, x, y):
        # 1. Find the fuel cell's rack ID, which is its X coordinate plus 10.
        rackID = x + 10
        # 2. Begin with a power level of the rack ID times the Y coordinate.
        level = rackID * y
        # 3. Increase the power level by the value of the grid serial number (your puzzle input).
        level += self.serial
        # 4. Set the power level to itself multiplied by the rack ID.
        level *= rackID
        # 5. Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
        digit = (level // 100) % 10
        # 6. Subtract 5 from the power level.
        return digit - 5

    def grid_sum(self, x, y):
        upper_right = (x - 1) + (y - 1) * self.width
        result = 0
        for offset in self.grid_offset:
            result += self.cells[upper_right + offset]
        return result

    def cell_at(self, x, y):
        return self.cells[(x - 1) + (y - 1) * self.width]

    def max_grid(self):
        result = (1, 1)
        maximum = self.grid_sum(1, 1)
        for y in range(1, self.height - 2):
            for x in range(1, self.width - 2):
                sum = self.grid_sum(x, y)
                if sum > maximum:
                    maximum = sum
                    result = (x, y)
        return result

    def part2_grid_sum(self, x, y, size):
        upper_right = (x - 1) + (y - 1) * self.width
        result = 0
        for delta_x in range(size):
            for delta_y in range(size):
                offset = delta_x + delta_y * self.width
                result += self.cells[upper_right + offset]
        return result

    def part2_max_grid(self, max_size=20):
        result = (1, 1, 3)
        maximum = self.grid_sum(1, 1)
        for size in range(3, max_size):
            print("serial=%d, size=%d, maximum=%d, rsize=%d" % (self.serial, size, maximum, result[2]))
            for y in range(1, self.height - size):
                for x in range(1, self.width - size):
                    sum = self.part2_grid_sum(x, y, size)
                    if sum > maximum:
                        maximum = sum
                        result = (x, y, size)
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.max_grid()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.part2_max_grid()

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      f u e l c e l l . p y                     end
# ======================================================================
