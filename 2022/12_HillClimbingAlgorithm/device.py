
# ======================================================================
# Hill Climbing Algorithm
#   Advent of Code 2022 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d e v i c e . p y
# ======================================================================
"Device for the Advent of Code 2022 Day 12 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import deque

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
HEIGHTS = "abcdefghijklmnopqrstuvwxyz"
DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# ======================================================================
#                                                                 Device
# ======================================================================


class Device(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Hill Climbing Algorithm"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.map = {}
        self.start = None
        self.goal = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Loop for all the rows of the text
        for row, line in enumerate(text):

            # 2. Loop for all of the columns of the line
            for col, square in enumerate(line):

                # 3. If start or goal, record it
                if square == "S":
                    self.start = (col, row)
                    square = "a"
                if square == "E":
                    self.goal = (col, row)
                    square = "z"

                # 4. Record the height
                self.map[(col, row)] = HEIGHTS.index(square)

    def one_away(self, loc):
        "Return the locations only one away"

        # 1. Start with nothing
        result = []

        # 2. Loop for the directions
        for delta in DIRS:

            # 3. Calculate the new location
            new_loc = (loc[0] + delta[0], loc[1] + delta[1])

            # 4. If it is a valid location, add it to the result
            if new_loc in self.map:
                result.append(new_loc)

        # 5. Return the locations that are one step away
        return result

    def is_reachable(self, loc, new_loc):
        "Can we get there from here without climbing?"

        # 1. We can move to the same level
        if self.map[new_loc] == self.map[loc]:
            return True

        # 2. We can move to one level higher
        if self.map[new_loc] == 1 + self.map[loc]:
            return True

        # 3. And we can always go down
        if self.map[new_loc] < self.map[loc]:
            return True

        # 4. Not without climbing gear
        return False

    def reachable(self, loc):
        "Return the reachable locations only one away"

        # 1. Get the near by locations
        nearby = self.one_away(loc)

        # 2. Keep only the ones we can reach
        return [new_loc for new_loc in nearby
                if self.is_reachable(loc, new_loc)]

    def best_path(self, loc=None):
        "Return the number of steps in the best path from S to E"

        # 1. Start with nothing
        result = 999999999
        if not loc:
            loc = self.start
        seen = set()
        queue = deque()

        # 2. Start at the very beginning
        seen.add(loc)
        queue.extend([(new_loc, 1) for new_loc in self.reachable(loc)])

        # 3. Loop while there is something to do
        while len(queue) > 0:

            # 4. Take an element from the queue
            new_loc, steps = queue.popleft()

            # 5. Have we reached the goal?
            if new_loc == self.goal:
                if steps < result:
                    result = steps
                continue

            # 5. Have we seen this square before
            if new_loc in seen:
                continue

            # 6. Prepare to search from here
            seen.add(new_loc)
            queue.extend([(newer_loc, steps + 1)
                          for newer_loc in self.reachable(new_loc)])

        # 7. Return the lowest number of steps
        return result

    def find_starts(self):
        "Return all the possible starting points"

        # 1. Start with nothing
        result = []

        # 2. Loop for all of the square in the map
        for loc, height in self.map.items():

            # 3. If the elevation is 0 (a), add to the result
            if height == 0:
                result.append(loc)

        # 4. Return the possible starting locations
        return result

    def best_trail(self):
        "Find the shortest possible trail length"

        # 1. Start with nothing
        result = 99999999

        # 2. Get the possible starting locations
        starts = self.find_starts()

        # 3. Loop for all the starting locations
        for start in starts:

            # 4. Find the length of the trail starting from here
            length = self.best_path(loc=start)

            # 5. If this one is shorter, save it
            if length < result:
                result = length

        # 6. Return the length of the shortest trail
        return result


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        d e v i c e . p y                       end
# ======================================================================
