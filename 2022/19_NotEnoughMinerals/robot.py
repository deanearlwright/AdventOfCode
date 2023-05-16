
# ======================================================================
# Not Enough Minerals
#   Advent of Code 2022 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r o b o t . p y
# ======================================================================
"Robot for the Advent of Code 2022 Day 19 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import defaultdict

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Robot
# ======================================================================


class Robot(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Not Enough Minerals"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.produces = None
        self.costs = defaultdict(int)

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Split text into type and costs
        each, costs = text.split(" costs ")

        # 2. Save what the robot produces
        self.produces = each.split()[1]

        # 3. Everything starts out free
        needs = defaultdict(int)

        # 4. Loop for all the ingredients (might be one or two)
        for ingredient in costs.replace(".", "").split(" and "):

            # 5. Get number and what
            number, what = ingredient.split()

            # 6. Save the ingredient
            needs[what] = int(number)

        # 7. Save the costs
        self.costs = needs

    def needs(self, what):
        "Return how much of what it takes to make the robot"
        return self.costs[what]

    @staticmethod
    def names():
        "Return the names of the ingredients"
        return ['ore', 'clay', 'obsidian', 'geode']

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                         r o b o t . p y                        end
# ======================================================================
