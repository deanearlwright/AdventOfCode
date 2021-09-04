# ======================================================================
# Science for Hungry People
#   Advent of Code 2015 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         i n g r e d i e n t . p y
# ======================================================================
"Ingredient for the Advent of Code 2015 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
RE_INGREDIENT = re.compile("([A-Za-z]+): capacity (-?[0-9]+), durability (-?[0-9]+)," +
                           " flavor (-?[0-9]+), texture (-?[0-9]+), calories (-?[0-9]+)")

# ======================================================================
#                                                             Ingredient
# ======================================================================


class Ingredient(object):   # pylint: disable=R0902, R0205
    "Object for Science for Hungry People"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.name = ""
        self.qualities = [0, 0, 0, 0]
        self.cals = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            match = RE_INGREDIENT.match(text)
            if not match:
                print("Unable to parse", text)
            else:
                name, capacity, durability, flavor, texture, calories = match.groups()
                self.name = name
                self.qualities = [int(capacity), int(durability), int(flavor), int(texture)]
                self.cals = int(calories)

    def properties(self, teaspoons=1):
        "Return the score for the ingredient"
        return [teaspoons * _ for _ in self.qualities]

    def calories(self, teaspoons=1):
        "Return the calaries"
        return teaspoons * self.cals


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    i n g r e d i e n t . p y                   end
# ======================================================================
