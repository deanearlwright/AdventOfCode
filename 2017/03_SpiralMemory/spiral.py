# ======================================================================
# Spiral Memory
#   Advent of Code 2017 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s p i r a l . p y
# ======================================================================
"A solver for Spiral Memory for Advent of Code 2017 Day 03"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from math import sqrt, ceil

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
HERE = (0, 0)
CENTER = (0, 0)

DIR_E = 'E'
DIR_W = 'W'
DIR_S = 'S'
DIR_N = 'N'

DELTA = [(1, 0), (-1, 0), (0, 1), (0, -1),
         (1, 1), (-1, 1), (1, -1), (-1, -1)]

MOVE = {DIR_E: (1, 0),
        DIR_W: (-1, 0),
        DIR_N: (0, 1),
        DIR_S: (0, -1)}

LEFT = {DIR_E: DIR_N,
        DIR_W: DIR_S,
        DIR_N: DIR_W,
        DIR_S: DIR_E}

# ======================================================================
#                                                      Utility Functions
# ======================================================================

def manhattan_distance(xy_one, xy_two):
    "Taxicab Geometry Distance"

    return abs(xy_one[0] - xy_two[0]) + \
           abs(xy_one[1] - xy_two[1])

def ring_side(number):
    "Length of ring side"

    if number < 0:
        return None
    if number == 0:
        return 1
    return 2*number + 1

def ring_length(number):
    "Length of ring"

    if number < 0:
        return None
    if number == 0:
        return 1
    return 4*(ring_side(number) - 1)

def delta_loc(location, delta):
    "Return the nearby location"

    return (location[0] + delta[0],
            location[1] + delta[1])

# ======================================================================
#                                                                 Spiral
# ======================================================================


class Spiral(object):
    """Object representing a Spiral solver"""

    def __init__(self, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.spiral = {}

    def ring_number(self, square):
        "Return the ring number of a square"

        if self.part2:
            return None
        if square < 1:
            return None
        return int(ceil(sqrt(square)) // 2)

    def ring_max(self, number):
        "Return the highest square on the ring"

        if self.part2:
            return None
        if number < 0:
            return None
        if number == 0:
            return 1
        return ring_side(number)**2

    def ring_min(self, number):
        "Return the lowest square on the ring"

        if self.part2:
            return None
        if number < 0:
            return None
        if number == 0:
            return 1
        return self.ring_max(number-1) + 1

    def ring_offset(self, square):
        "return offset from start of the ring"

        if self.part2:
            return None
        if square < 1:
            return None
        ring_num = self.ring_number(square)
        if square == self.ring_max(ring_num):
            return 0
        return 1 + square - self.ring_min(ring_num)

    def side_offset(self, square):
        "return offset from start of the ring"

        if self.part2:
            return None
        if square < 1:
            return None
        if square == 1:
            return 0
        return self.ring_offset(square) % (2 * self.ring_number(square))

    def side_distance(self, square):
        "return distance for square to vertical or horizontal"

        if self.part2:
            return None
        if square < 1:
            return None
        if square == 1:
            return 0
        return abs(self.side_offset(square) - self.ring_number(square))

    def steps(self, square, verbose=False):
        "Calculate the number of steps needed"

        if self.part2:
            return None
        if square < 1:
            return None
        dist_ring = self.ring_number(square)
        dist_side = self.side_distance(square)
        if verbose:
            print("Number of steps needed for %d is %d + %d" %
                  (square, dist_ring, dist_side))
        return dist_ring + dist_side

    def build_until_gt(self, number, verbose=False):
        "Create a spiral until bigger than the given number"

        # 1. Start with nothing
        self.spiral = {}

        # 2. Put a 1 in the center
        self.spiral[CENTER] = 1

        # 3. Set initial location and direction
        location = CENTER
        direction = DIR_E
        value = 1

        # 4. Loop until we set a square greater than specified number
        while value <= number:

            # 5. Determine the next location
            new_location = delta_loc(location, MOVE[direction])

            # 6. Determine the value for this new square
            new_value = self.new_value(new_location, value)

            # 7. Determine the next direction
            new_direction = self.new_direction(new_location, direction)

            # 8. Set the next loc, dir, and value
            if verbose:
                print("From %s moved %s to %s and wrote %d" %
                      (location, direction, new_location, new_value))
            location = new_location
            value = new_value
            direction = new_direction
            assert location not in self.spiral
            self.spiral[location] = value

        # 9. Return the last value written
        return value

    def new_value(self, location, value):
        "Determine the next value"

        # 1. If part1, increment value
        if not self.part2:
            return 1 + value

        # 2. Start with nothing
        result = 0

        # 3. Loop for the surrounding squares
        for delta in DELTA:

            # 4. Add the value of the surrounding square
            result += self.square_value(location, delta)

        # 5. Return the sum of surrounding square
        return result

    def new_direction(self, location, direction):
        "Determine the next direction"

        # 1. If we can turn left do so
        if 0 == self.square_value(location, MOVE[LEFT[direction]]):
            return LEFT[direction]

        # 2. Else we keep going this way
        return direction

    def square_value(self, location, delta):
        "Determine the value of a nearby square"

        # 1. Determine the xy loc of the nearby square
        other_loc = delta_loc(location, delta)

        # 2. If it has a value return it
        if other_loc in self.spiral:
            return self.spiral[other_loc]

        # 3. Else return 0
        return 0

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          s p i r a l . p y                     end
# ======================================================================
