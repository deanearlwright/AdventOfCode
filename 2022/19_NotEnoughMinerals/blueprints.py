
# ======================================================================
# Not Enough Minerals
#   Advent of Code 2022 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         b l u e p r i n t s . p y
# ======================================================================
"Blueprints for the Advent of Code 2022 Day 19 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import math
import blueprint

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
PART_ONE_TIME = 24
PART_TWO_TIME = 32
PART_TWO_RECIPES = 3

# ======================================================================
#                                                             Blueprints
# ======================================================================


class Blueprints(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Not Enough Minerals"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.recipes = []
        self.resources = []
        self.geodes = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Loop for each line of text
        for line in text:

            # 2. Create a single blueprint from the line
            a_recipe = blueprint.Blueprint(text=line, part2=self.part2)

            # 3. Add the recipe
            self.recipes.append(a_recipe)

            # 4. Part2 only has the first three blueprints
            if self.part2 and len(self.recipes) == PART_TWO_RECIPES:
                break

    def geode_production(self):
        "Determine the maximum number of goedes for all recipes"

        # 1. Start with nothing
        geodes = [0 for _ in range(1 + len(self.recipes))]

        # 2. Determine the amount of time available
        time = PART_ONE_TIME
        if self.part2:
            time = PART_TWO_TIME

        # 3. Loop for all the recipes
        for recipe in self.recipes:

            # 4. Get the amount of geodes this recipe can produce
            amount = recipe.geode_production(time)

            # 5. Save the number of geodes
            geodes[recipe.number] = amount

        # 9. Save the number of geodes
        return geodes

    def quality_level(self):
        "Return the quality level for these recipes"

        # 1. Get the number of qeodes produced
        geodes = self.geode_production()

        # 2. Quality is the recipe number times production
        result = sum([indx * amount for indx, amount in enumerate(geodes)])
        return result

    def product(self):
        "Return the product of the geode amounts for these recipes"

        # 1. Get the number of qeodes produced
        geodes = self.geode_production()

        # 2. Return the product of the amounts
        result = math.prod(geodes[1:])
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    b l u e p r i n t s . p y                   end
# ======================================================================
