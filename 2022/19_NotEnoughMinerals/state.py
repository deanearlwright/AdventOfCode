
# ======================================================================
# NotEnoughMinerals
#   Advent of Code 2022 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s t a t e . p y
# ======================================================================
"State for the Advent of Code 2022 Day 19 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  State
# ======================================================================


class State(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Not Enough Minerals"

    def __init__(self, time=1, robots=None, resources=None, ignored=None):

        # 1. Set the initial values
        self.time = time
        self.robots = robots.copy() if robots else {
            "ore": 1, "clay": 0, "obsidian": 0, "geode": 0
        }
        self.resources = resources.copy() if resources else {
            "ore": 0, "clay": 0, "obsidian": 0, "geode": 0
        }
        self.ignored = ignored.copy() if ignored else []

    def copy(self):
        "Copy the state"
        return State(self.time, self.robots, self.resources, self.ignored)

    def __gt__(self, other):
        return self.resources["geode"] > other.resources["geode"]

    def __repr__(self):
        return f"{{time={self.time}, bots={self.robots}, res={self.resources}}}"

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                         s t a t e . p y                        end
# ======================================================================
