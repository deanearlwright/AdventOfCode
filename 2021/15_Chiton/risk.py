# ======================================================================
# Chiton
#   Advent of Code 2021 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r i s k . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple
import networkx

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
START = (0, 0)

# ----------------------------------------------------------------------
#                                                            namedtuples
# ----------------------------------------------------------------------
TODO = namedtuple('TODO', 'before at options total')

# ======================================================================
#                                                                   Risk
# ======================================================================


class Risk(object):   # pylint: disable=R0902, R0205
    "Object for Chiton"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.risks = {}
        self.goal = START
        self.network = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for row, line in enumerate(text):
                for col, digit in enumerate(line):
                    self.goal = (col, row)
                    self.risks[self.goal] = int(digit)
            if part2:
                self.expand_risks()
            self.build_network()

    def expand_risks(self):
        "Expand the risks to 5x5 for part two"

        # 1. Loop for every row and every column
        for row in range(self.goal[1] + 1):
            for col in range(self.goal[0] + 1):
                risk = self.risks[(col, row)]

                # 2. Now make twenty-four more copies
                for delta_row in range(5):
                    for delta_col in range(5):
                        if delta_row == delta_col == 0:
                            continue

                        # 3. Determine new location
                        new_row = row + delta_row * (self.goal[1] + 1)
                        new_col = col + delta_col * (self.goal[0] + 1)

                        # 4. Adjust the risk value
                        new_risk = risk + delta_row + delta_col
                        if new_risk > 9:
                            new_risk -= 9

                        # 5. Add the new location
                        self.risks[(new_col, new_row)] = new_risk

        # 6. Set the new goal
        self.goal = (self.goal[0] + 4 * (1 + self.goal[0]),
                     self.goal[1] + 4 * (1 + self.goal[1]))

    def from_here(self, loc, before):
        "Return the new adjacent locations that aren't off the map"

        # 1. Start with nothing
        result = []

        # 2. Loop for the deltas
        for delta in DELTA:

            # 3. Get adjacent location
            delta_loc = (loc[0] + delta[0], loc[1] + delta[1])

            # 4. If the location exists and is new add it
            if delta_loc in self.risks and delta_loc not in before:
                result.append(delta_loc)

        # 5. Return adjacent locations
        return result

        # 2. Compute score going down then right

    def find_brute_force_risk(self):
        "Find the safest path from the start to the goal and return lowest total risk"

        # 1. Start with nothing
        result = 999999999
        explore = []

        # 2. Add the initial exploration
        todo = TODO(before=set(), at=START, options=self.from_here(START, []), total=0)
        explore.append(todo)

        # 3. Loop while there is something to explore
        while len(explore) > 0:

            # 4. Take a todo from the stack
            todo = explore.pop()
            if todo.total > result:
                continue

            # 5. Have we reached the end? If so, is it better?
            if todo.at == self.goal:
                if todo.total < result:
                    result = todo.total
                continue

            # 6. Are there any options? No --> This path is dead
            if len(todo.options) == 0:
                continue

            # 7. Get one of the options for the next move
            next_loc = todo.options.pop()

            # 8. Put back to current todo (less one option)
            explore.append(
                TODO(before=todo.before, at=todo.at,
                     options=todo.options, total=todo.total))

            # 9. Craft the next todo
            before = todo.before.copy()
            before.add(todo.at)
            options = self.from_here(next_loc, before)
            total = todo.total + self.risks[next_loc]

            # 10. Have we gone to far?
            if total > result:
                continue

            # 11. Add the next todo
            explore.append(
                TODO(before=before, at=next_loc, options=options, total=total))

        # 12. Return the lowest total risk
        return result

    def build_network(self):
        "Build a directed graph from the risks"

        self.network = networkx.DiGraph()
        for loc in self.risks:
            self.network.add_node(loc)
            for next_loc in self.from_here(loc, []):
                self.network.add_edge(loc, next_loc, weight=self.risks[next_loc])

    def find_network_risk(self):
        "Return the risk of the safest path from the start to the goal"

        # 1. Do it
        return networkx.shortest_path_length(self.network, source=START,
                                             target=self.goal, weight='weight')

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.find_network_risk()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.find_network_risk()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          r i s k . p y                         end
# ======================================================================
