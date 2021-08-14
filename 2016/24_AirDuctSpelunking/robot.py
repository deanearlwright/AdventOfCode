# ======================================================================
# Air Duct Spelunking
#   Advent of Code 2016 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r o b o t . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 24 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from itertools import permutations
import ducts

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Robot
# ======================================================================


class Robot(object):   # pylint: disable=R0902, R0205
    "Object for Air Duct Spelunking"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.ducts = None
        self.steps = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.ducts = ducts.Ducts(text=text, part2=part2)
            self.steps = self.ducts.all_steps()

    def visit_all(self, verbose=False, loop=False):
        "Return the number of steps to locations"

        # 1. Start with a very bad guess
        best_steps = None
        best_route = None

        # 2. Loop for all possible routes between locations
        for route in permutations(range(1, max(self.steps) + 1)):

            # 3. Get the number of steps in this route
            full_route = [0]
            full_route.extend(list(route))
            if loop:
                full_route.append(0)
            steps = self.cost_of_route(full_route)

            # 4. If better than the previous best, save it
            if best_steps is None or steps < best_steps:
                if verbose:
                    print("saving better route", steps, full_route)
                best_steps = steps
                best_route = full_route

        # 5. Return the number of steps in the best route
        if verbose:
            print("Returning best", best_steps, best_route)
        return best_steps

    def cost_of_route(self, route):
        "Return the cost of the route"

        # 1. Start with nothing
        result = 0
        if route is None or len(route) == 0:
            return result

        # 2. Start at the first location
        previous = route[0]

        # 3. Loop for the rest of the locations
        for loc in route[1:]:

            # 4. Add in the distance to that location
            result += self.steps[previous][loc]

            # 5. Advance to that location
            previous = loc

        # 6. Return the total cost of the route
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.visit_all(verbose=verbose)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.visit_all(verbose=verbose, loop=True)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         r o b o t . p y                        end
# ======================================================================
