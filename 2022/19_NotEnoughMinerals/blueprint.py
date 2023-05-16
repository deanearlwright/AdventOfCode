
# ======================================================================
# Not Enough Minerals
#   Advent of Code 2022 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         b l u e p r i n t . p y
# ======================================================================
"Blueprint for the Advent of Code 2022 Day 19 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

import robots
import state

# ----------------------------------------------------------------------
#                                                                  types
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------


# ======================================================================
#                                                              Blueprint
# ======================================================================


class Blueprint(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Not Enough Minerals"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.number = 0
        self.robots = None
        self.cost = {}
        self.useful = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

        # 3. Summary
        if self.robots:
            self.cost = self.robots.cost
            self.useful = self.robots.useful

    def _process_text(self, text):
        "Assign values from text"

        # 1. Get the blueprint number
        parts = text.split(":")
        self.number = int(parts[0][10:])

        # 2. Get the robot information
        self.robots = robots.Robots(text=parts[1], part2=self.part2)

    def geode_production(self, minutes):
        "How many geodes can this recipe product in the alloted time"

        # 1. Start at the very beginning
        states = [state.State()]

        # 2. Get the most geodes
        result = self.expand_recipe(states, minutes)

        # 3. Return the most geodes producable in the alloted time
        return result[0]

    def expand_recipe(self, previous, minutes):
        "Determine the best course from the current state"

        # 1. The most recent state is the current one
        current = previous[-1]

        # 2. Is there any time left?  If not, Return what we have
        remaining = minutes - current.time
        if remaining < 0:
            return current.resources["geode"], previous

        # 3. Find a new, affordable robot to build next?
        build = []
        for robot, cost in self.cost.items():
            if (current.robots[robot] < self.useful[robot]
                    and all(current.resources[k] >= v for k, v in cost.items())
                    and robot not in current.ignored):
                build.append(robot)

        # 4. Priortize geodes, deal with the end days, and prune selections
        if "geode" in build:
            build = ["geode"]
        elif remaining < 1:
            build = []
        else:
            # 4a. goedes and obsidian have multiple inputs
            if ((current.robots["clay"] > 3 or current.robots["obsidian"]
                 or "obsidian" in build) and "ore" in build):
                build.remove("ore")
            if ((current.robots["obsidian"] > 3 or current.robots["geode"]
                 or "geode" in build) and "clay" in build):
                build.remove("clay")

        # 5. Create the next state with addition resources based on current robots
        future = current.copy()
        future.time += 1
        for resource, quanity in future.robots.items():
            future.resources[resource] += quanity

        # 6. What is the best we can do if we do nothing?
        future.ignored += build
        results = [self.expand_recipe(previous + [future], minutes)]

        # 7. Try each to the robots that we can build
        for rbt in build:

            # 7a. Create an alternative future
            alternate = future.copy()
            alternate.ignored = []

            # 7b. We can a new robot but it costs us come resources
            alternate.robots[rbt] += 1
            for resource, quanity in self.cost[rbt].items():
                alternate.resources[resource] -= quanity

            # 7c. What is the best we can do using this new robot?
            results.append(self.expand_recipe(previous + [alternate], minutes))

        # 8. Return the best of the best
        return max(results)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     b l u e p r i n t . p y                    end
# ======================================================================
