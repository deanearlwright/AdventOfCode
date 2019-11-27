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
                 crashed=False,
                 space=' '):

        # 1. Set the initial state
        if not location:
            self.location = (0, 0)
        else:
            self.location = location
        assert(direction in DIRECTIONS)
        self.direction = direction
        self.crossings = crossings
        self.crashed = crashed
        self.time = 0

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

        # 1. If we have no track, we crash
        if not track:
            self.crashed = True
            return True

        # 1.5. If we have already moved this tick, don't move again
        if self.time >= track.time:
            return False

        # 2. If we are not on the track, we crash
        if track.get_track(self.location) != self.direction:
            self.crashed = True
            return True

        # 3. Replace the piece of track we are on
        track.set_track(self.location, self.space)

        # 4. Determine our new location moving one step
        delta = DELTA_LOC[self.direction]
        new_loc = (self.location[0] + delta[0],
                   self.location[1] + delta[1])
        #print("loc: dir=%s, old=%s, delta=%s, new=%s" % (self.direction, self.location, delta, new_loc))
        self.location = new_loc

        # 5. Get the piece of track at that location and save time of movement
        self.space = track.get_track(self.location)
        self.time = track.time

        # 6. Have we hit another cart?
        if self.space in DIRECTIONS:
            track.set_crashed(self.location)
            self.crashed = True
            return True

        # 7. Determine our new direction
        if self.space == '+':
            cross_turn = CROSSINGS[self.crossings % 3]
            self.crossings += 1
            new_dir = CROSS_DIR[cross_turn][self.direction]
        else:
            new_dir = TRACK_DIR[self.space][self.direction]
        #print("dir: dir=%s, loc=%s, space=%s, new=%s" % (self.direction, self.location, self.space, new_dir))
        self.direction = new_dir

        # 8. Put our direction on the track
        track.set_track(self.location, self.direction)

        # 9. Return success (not crashing)
        return False


    def __eq__(self, other):
        return self.location == other.location

    def __lt__(self, other):
        return self.location < other.location

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         c a r t . p y                          end
# ======================================================================
