
# ======================================================================
# Race Condition
#   Advent of Code 2024 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         t r a c k . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 20 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import defaultdict

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]
VERT = [(1, 0), (-1, 0)]
HORZ = [(0, 1), (0, -1)]

# ======================================================================
#                                                                  Track
# ======================================================================


class Track(object):   # pylint: disable=R0902, R0205
    "Object for Race Condition"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rows = 0
        self.cols = 0
        self.start = None
        self.end = None
        self.walls = set()
        self.spaces = {}
        self.cheats = {}
        self.cheats2 = defaultdict(int)

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text()

    def _process_text(self):
        "Assign values from text"

        assert self.text is not None and len(self.text) > 0

        # 1. Set the rows and columns
        self.rows = len(self.text)
        self.cols = len(self.text[0])

        # 2. Loop for each row and column of the text
        for row, line in enumerate(self.text):
            for col, char in enumerate(line):
                loc = (row, col)

                # 3. Process this square
                match char:
                    case "#":
                        self.walls.add(loc)
                    case "S":
                        self.start = loc
                    case "E":
                        self.end = loc

        # 4. Should have found start and end
        assert self.start is not None
        assert self.end is not None

        # 5. Find the time at each step
        self.find_path()

        # 6. Find all the cheats
        self.find_cheats()

        # 7. And then some more
        if self.part2:
            self.find_cheats2()

    def find_path(self):
        "Follow the race track, recording the time to each space"

        # 1. Start at the very beginning, a very good place to start
        loc = self.start
        pseconds = 0
        self.spaces[loc] = pseconds

        # 2. Loop until we reach the end
        while True:

            # 3. Records the time to reach this space
            self.spaces[loc] = pseconds

            # 4. Are we there yet?
            if loc == self.end:
                break

            # 5. Determine the next space
            for delta in DELTA:
                new_loc = (loc[0] + delta[0], loc[1] + delta[1])

                # 6. Can we go there?
                if new_loc in self.walls:
                    continue

                # 7. Have we been there?
                if new_loc in self.spaces:
                    continue

                # 8. This is the way
                loc = new_loc
                pseconds += 1
                break

    def check_cheat(self, loc, deltas):
        "Return the value of the cheat or -1 if None"

        # 1. Get the locations to either side of the wall
        loc0 = ((loc[0] + deltas[0][0], loc[1] + deltas[0][1]))
        loc1 = ((loc[0] + deltas[1][0], loc[1] + deltas[1][1]))

        # 2. Are these both spaces?
        if loc0 not in self.spaces:
            return -1
        if loc1 not in self.spaces:
            return -1

        # 3. Return the value of this cheat
        return abs(self.spaces[loc0] - self.spaces[loc1]) - 2

    def find_cheats(self):
        "Find all the possible cheats"

        # 1. Loop for all of the walls
        for wall in self.walls:

            # 2. Ignore walls on the edge
            if wall[0] == 0 or wall[1] == 0:
                continue
            if wall[0] + 1 == self.rows:
                continue
            if wall[1] + 1 == self.cols:
                continue

            # 3. Is there an vertical cheat?
            cheat = self.check_cheat(wall, VERT)
            if cheat > 0:
                assert wall not in self.cheats
                self.cheats[wall] = cheat

            # 4. Is this an horieffective cheat
            cheat = self.check_cheat(wall, HORZ)
            if cheat > 0:
                assert wall not in self.cheats
                self.cheats[wall] = cheat

    def find_cheats2(self, time=20):
        "Find all cheats we can do with 20 picosecond cheat time"

        # 1. Loop for all the possible starting and ending spaces
        for beg_loc, beg_time in self.spaces.items():
            for end_loc, end_time in self.spaces.items():

                # 2. No matter where you go, there you are
                if beg_loc == end_loc:

                    continue
                # 3. Compute the time path time between the two spaces
                if beg_time > end_time:
                    continue
                track_time = end_time - beg_time

                # 3. Compute the distance between the points
                distance = abs(beg_loc[0] - end_loc[0]) + \
                    abs(beg_loc[1] - end_loc[1])
                if distance > time:
                    continue

                # 5. Calculate time saved
                time_saved = track_time - distance

                # 6. Is this a good cheat?  If so, save it
                if time_saved > 0:
                    self.cheats2[time_saved] += 1

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        return len([x for x in self.cheats.values() if x >= 100])

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part two
        return sum([self.cheats2[x] for x in self.cheats2 if x >= 100])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                         t r a c k . p y                        end
# ======================================================================
