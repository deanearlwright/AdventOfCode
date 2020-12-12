# ======================================================================
# Rain Risk
#   Advent of Code 2020 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                          f e r r y . p y
# ======================================================================
"A storm tossed ship for the Advent of Code 2020 Day 12 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EAST = (1, 0)
WEST = (-1, 0)
NORTH = (0, -1)
SOUTH = (0, 1)
TURN = {
    'L': {
        NORTH: {90: WEST, 180: SOUTH, 270: EAST},
        EAST: {90: NORTH, 180: WEST, 270: SOUTH},
        SOUTH: {90: EAST, 180: NORTH, 270: WEST},
        WEST: {90: SOUTH, 180: EAST, 270: NORTH},
    },
    'R': {
        SOUTH: {90: WEST, 180: NORTH, 270: EAST},
        WEST: {90: NORTH, 180: EAST, 270: SOUTH},
        NORTH: {90: EAST, 180: SOUTH, 270: WEST},
        EAST: {90: SOUTH, 180: WEST, 270: NORTH},
    }
}
DIRECTION = {'N': NORTH, 'S': SOUTH, 'E': EAST, 'W': WEST}
HEADING = {NORTH: 'N', SOUTH: 'S', EAST: 'E', WEST: 'W'}

# ======================================================================
#                                                                  Ferry
# ======================================================================


class Ferry(object):   # pylint: disable=R0902, R0205
    "Moveable Object for Rain Risk"

    def __init__(self, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.start = (0, 0)
        self.loc = (0, 0)
        self.heading = EAST
        self.waypoint = (10, -1)

    def execute(self, instruction, verbose=False):
        "Execute a single instruction"

        # 1. Break into letter and number
        letter = instruction[0]
        number = int(instruction[1:])

        # 2. Execute the instruction
        if letter in 'NSEW':
            if self.part2:
                self.move_waypoint(DIRECTION[letter], number)
            else:
                self.move(DIRECTION[letter], number)
        elif letter in 'LR':
            if self.part2:
                self.rotate_waypoint(letter, number)
            else:
                self.turn(letter, number)
        elif letter == 'F':
            if self.part2:
                self.move(self.waypoint, number)
            else:
                self.move(self.heading, number)
        else:
            print('Illegal instruction: %s' % instruction)

    def move(self, delta, number):
        "Go west young man, or east or wherever"
        self.loc = (self.loc[0] + number * delta[0],
                    self.loc[1] + number * delta[1])

    def move_waypoint(self, delta, number):
        "Go west young man, or east or wherever"
        self.waypoint = (self.waypoint[0] + number * delta[0],
                         self.waypoint[1] + number * delta[1])

    def turn(self, way, number):
        "Turn this way or that"
        assert way in 'LR'
        assert number in [90, 180, 270]
        self.heading = TURN[way][self.heading][number]

    def rotate_waypoint(self, way, number):
        "Rotate the waypoint around the ship"
        assert way in 'LR'
        assert number in [90, 180, 270]
        if way == 'R':
            if number == 90:
                new_wp = (-self.waypoint[1], self.waypoint[0])
            elif number == 180:
                new_wp = (-self.waypoint[0], -self.waypoint[1])
            else:
                new_wp = (self.waypoint[1], -self.waypoint[0])
        else:
            if number == 90:
                new_wp = (self.waypoint[1], -self.waypoint[0])
            elif number == 180:
                new_wp = (-self.waypoint[0], -self.waypoint[1])
            else:
                new_wp = (-self.waypoint[1], self.waypoint[0])
        self.waypoint = new_wp

    def manhattan(self):
        "Taxicab distance from start"
        return abs(self.start[0] - self.loc[0]) + abs(self.start[1] - self.loc[1])

    def __str__(self):
        heading = HEADING[self.heading]
        if self.loc[0] < 0:
            ew = 'west %d' % -self.loc[0]
        else:
            ew = 'east %d' % self.loc[0]
        if self.loc[1] < 0:
            ns = 'north %d' % -self.loc[1]
        else:
            ns = 'south %d' % self.loc[1]
        if self.part2:
            if self.waypoint[0] < 0:
                wpew = 'west %d' % -self.waypoint[0]
            else:
                wpew = 'east %d' % self.waypoint[0]
            if self.waypoint[1] < 0:
                wpns = 'north %d' % -self.waypoint[1]
            else:
                wpns = 'south %d' % self.waypoint[1]
            return '%s, %s; wp: %s, %s' % (ew, ns, wpew, wpns)
        return '%s: %s, %s' % (heading, ew, ns)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         f e r r y . p y                        end
# ======================================================================
