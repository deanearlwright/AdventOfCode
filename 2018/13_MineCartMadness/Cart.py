# ======================================================================
# Mine Cart Madness
#   Advent of Code 2018 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                             c a r t . p y
# ======================================================================
"Cart for Mine Card Madness problem of day 13 of Advent of Code 2018"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from functools import total_ordering

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# The four directions that a cart can go
DIRECTIONS = '<>^v'

# The difference in location when moving in one of the four directions
DELTA_LOC = {'^': (0, -1),
             'v': (0, 1),
             '<': (-1, 0),
             '>': (1, 0),
             }

# The change in direction (if any) when moving in one of the four
# directions and encountering the given track type.
# Crossings (+) are handled using CROSS_DIR
TRACK_DIR = {'|': {'^': '^',
                   'v': 'v',
                   '<': '?',
                   '>': '?',
                   },
             '-': {'^': '?',
                   'v': '?',
                   '<': '<',
                   '>': '>',
                   },
             '/': {'^': '>',
                   'v': '<',
                   '<': 'v',
                   '>': '^',
                   },
             '\\': {'^': '<',
                    'v': '>',
                    '<': '^',
                    '>': 'v',
                    },
             }

# The loop of crossing direction changes: left, straight, right
CROSSINGS = '<+>'

# The change in direction (if any) when moving in one of the four
# directions and encountering a crossing based going l, s, or r.
CROSS_DIR = {'<': {'^': '<',
                   'v': '>',
                   '<': 'v',
                   '>': '^',
                   },
             '+': {'^': '^',
                   'v': 'v',
                   '<': '<',
                   '>': '>',
                   },
             '>': {'^': '>',
                   'v': '<',
                   '<': '^',
                   '>': 'v',
                   },
             }

# ======================================================================
#                                                                   Cart
# ======================================================================


@total_ordering
class Cart():                 # pylint: disable=E0012,R0205,R0903
    """Object representing a single cart of Mine Card Madness"""

    def __init__(self,                          # pylint: disable=R0913
                 location=None,
                 direction='^',
                 crossings=0,
                 crashed=None,
                 space=' '):

        # 1. Set the initial state
        if not location:
            self.location = (0, 0)
        else:
            self.location = location
        assert direction in DIRECTIONS
        self.direction = direction
        self.crossings = crossings
        self.crashed = crashed

        # 2. Determint the track under the kart
        #    Simplifing assumtion: always | or - not +
        if space not in '|-':
            if direction in '^v':
                self.space = "|"
            elif direction in '<>':
                self.space = '-'
            else:
                self.space = '?'
        else:
            self.space = space

    def tick(self, track=None):
        "Go another step along the track"

        # 0. Preconditions
        assert track is not None

        # 1. Can't move if we have crashed
        if self.crashed:
            return False

        # 3. If we are not on the track, we crash
        if track.get_track(self.location) != self.direction:
            self.crashed = self.location
            return True

        # 4. Replace the piece of track we are on
        track.set_track(self.location, self.space)

        # 5. Determine our new location moving one step
        delta = DELTA_LOC[self.direction]
        new_loc = (self.location[0] + delta[0],
                   self.location[1] + delta[1])
        # print("loc: dir=%s, old=%s, delta=%s, new=%s" % (
        # self.direction, self.location, delta, new_loc))
        self.location = new_loc

        # 6. Get the piece of track at that location and save time of movement
        self.space = track.get_track(self.location)

        # 7. Have we hit another cart?
        if self.space in DIRECTIONS:
            track.set_crashed(self.location)
            self.crashed = self.location
            return True

        # 8. Determine our new direction
        if self.space == '+':
            cross_turn = CROSSINGS[self.crossings % 3]
            self.crossings += 1
            new_dir = CROSS_DIR[cross_turn][self.direction]
        else:
            new_dir = TRACK_DIR[self.space][self.direction]
        # print("dir: dir=%s, loc=%s, space=%s, new=%s" % (
        # self.direction, self.location, self.space, new_dir))
        self.direction = new_dir

        # 9. Put our direction on the track
        track.set_track(self.location, self.direction)

        # 10. Return success (not crashing)
        return False

    def __eq__(self, other):
        return self.location[0] == other.location[0] and self.location[1] == other.location[1]

    def __lt__(self, other):
        return self.location[1] < other.location[1] or (
            self.location[1] == other.location[1] and self.location[0] < other.location[0])

    def __str__(self):
        return "cart: l=%s d=%s x=%s c=%s s=%s" % (self.location,
                                                   self.direction,
                                                   self.crossings,
                                                   self.crashed,
                                                   self.space)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         c a r t . p y                          end
# ======================================================================
