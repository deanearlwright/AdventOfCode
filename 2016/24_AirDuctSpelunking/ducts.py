# ======================================================================
# Air Duct Spelunking
#   Advent of Code 2016 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d u c t s . p y
# ======================================================================
"Ducts for the Advent of Code 2016 Day 24 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import deque

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
WALL = '#'
DELTA = [
  (1, 0),
  (-1, 0),
  (0, 1),
  (0, -1),
]

# ======================================================================
#                                                                  Ducts
# ======================================================================


class Ducts(object):   # pylint: disable=R0902, R0205
    "Object for Air Duct Spelunking"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.num_to_loc = {}
        self.loc_to_num = {}

        # 2. Find the numbered locations
        if self.text:
            self.find_locs()

    def find_locs(self):
        "Find the number locations in the text"

        # 1. Loop for all of the rows
        for rindex, row in enumerate(self.text):

            # 2. Loop for all of the columns in the row
            for cindex, col in enumerate(row):

                # 3. Is this a marked location
                if col.isdigit():
                    self.num_to_loc[int(col)] = (cindex, rindex)
                    self.loc_to_num[(cindex, rindex)] = int(col)

    def where_is(self, number):
        "Returns the (x,y) of the numbered location"
        if number in self.num_to_loc:
            return self.num_to_loc[number]
        return None

    def what_is_at(self, loc):
        "Returns the number of (x,y)"
        if loc in self.loc_to_num:
            return self.loc_to_num[loc]
        return None

    def is_wall(self, location):
        "This this a wall"

        # 1. Validate the location
        square = self.get_square(location)

        # 2. If location invalid, say it is a wall
        if not square:
            return True

        # 3. If it is a square say so
        if square == WALL:
            return True

        # 4. It doesn't seem to be a wall
        return False

    def get_square(self, location):
        "Get the value at the location (x,y)"

        # 1. Return None if bad location
        if not location or len(location) != 2:
            return None
        if not self.text:
            return None
        cindex, rindex = location
        if cindex < 0 or rindex < 0:
            return None
        if rindex >= len(self.text) or cindex >= len(self.text[rindex]):
            return None

        # 2. Return the square at the location
        return self.text[rindex][cindex]

    def steps_to_others(self, number, full=False):
        "Number of steps to other directly reachable locations"

        # 1. Start with nothing
        result = {}
        queue = deque()
        seen = set([None])

        # 2. Start here
        queue.append((self.where_is(number), 0))

        # 3. Loop while there is more to explore
        while len(queue) > 0:

            # 4. Take off a location from the queue
            loc, steps = queue.popleft()

            # 5. If this is new, explore it
            if loc not in seen:

                # 6. Now we have seen it
                seen.add(loc)

                # 7. If this is a numbered location, add it to the result
                new_num = self.what_is_at(loc)
                if new_num is not None and new_num != number:
                    result[new_num] = steps
                    if not full:
                        continue

                # 8. Loop for all the places we can go from here
                for new_loc in self.one_step(loc):

                    # 9. If we have been here before, explore it
                    if new_loc not in seen:
                        queue.append((new_loc, steps + 1))

        # 10. Return the locations we found and the steps to get there
        return result

    def one_step(self, loc):
        "Return the non-wall locations one step away"

        # 1. Start with nothing
        result = []

        # 2. Loop for the four directions
        for delta in DELTA:

            # 3. Calculate the new location
            new_loc = (loc[0] + delta[0], loc[1] + delta[1])

            # 4. If not a wall, save it
            if not self.is_wall(new_loc):
                result.append(new_loc)

        # 5. Return the neaby navigable locations
        return result

    def all_steps(self):
        "Return the distances from all locations to all others"

        # 1. Start with nothing
        result = {}

        # 2. Loop for all of the locations
        for number in self.num_to_loc:

            # 3. Get the distance to the other locations
            steps = self.steps_to_others(number, full=True)

            # 4. Remember the steps
            result[number] = steps

        # 5. Return the step matrix
        return result


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         d u c t s . p y                        end
# ======================================================================
