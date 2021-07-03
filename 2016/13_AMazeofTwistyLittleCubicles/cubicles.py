# ======================================================================
# A Maze of Twisty Little Cubicles
#   Advent of Code 2016 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c u b i c l e s . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 13 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
OPEN = 0
WALL = 1

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# ======================================================================
#                                                               Cubicles
# ======================================================================


class Cubicles(object):   # pylint: disable=R0902, R0205
    "Object for A Maze of Twisty Little Cubicles"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.maze = {(1, 1): OPEN}
        self.number = 0
        if text:
            self.number = int(text[0])

    def which(self, x, y):
        "Determine if the area is a wall or open"
        if x < 0 or y < 0:
            return WALL
        if (x, y) in self.maze:
            return self.maze[(x, y)]
        value = self.number + x * x + 3 * x + 2 * x * y + y + y * y
        knt = bin(value).count("1")
        result = knt % 2
        self.maze[(x, y)] = result
        #  print("x=%d, y=%d, v=%d, k=%d r=%d" % (x, y, value, knt, result))
        return result

    def shortest(self, x, y):
        "Determine the shortest path from (1, 1) to (x, y)"
        # 1. Set up maximum steps
        if self.part2:
            shortest = 51
        else:
            shortest = 999
        visited = {(1, 1): 0}
        # 2. Initialize goal and search
        goal = (x, y)
        backtrack = [((1, 1), self.directions(1, 1))]
        # 3. Loop until there is no more to search
        while len(backtrack) > 0:
            loc, dirs = backtrack.pop()
            steps = visited[loc]
            # 4. If goal is reached,
            if loc == goal:
                shortest = min(steps, shortest)
            # 5. If it is worth continuing from here ...
            if steps + 1 < shortest:
                # 6. Determine where to go next
                goto = dirs.pop()
                # 7. If there are more exits from here, we still need to search from those
                if len(dirs) > 0:
                    backtrack.append((loc, dirs))
                # 8. If this place is new (or we got here faster), add it for further searching
                if goto not in visited or (goto in visited and steps + 1 < visited[goto]):
                    backtrack.append((goto, self.directions(goto[0], goto[1])))
                    visited[goto] = steps + 1
        # 9. Return the answer for the question for part 1 or 2
        if self.part2:
            return len(visited)
        else:
            return shortest

    def directions(self, x, y):
        "Determine the directions from the indicated space"
        result = []
        for delta in DIRS:
            new_x = x + delta[0]
            new_y = y + delta[1]
            if self.which(new_x, new_y) == OPEN:
                result.append((new_x, new_y))
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.shortest(31, 39)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.shortest(999, 999)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      c u b i c l e s . p y                     end
# ======================================================================
