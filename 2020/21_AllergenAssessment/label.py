# ======================================================================
# Allergen Assessment
#   Advent of Code 2020 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                          l a b e l . p y
# ======================================================================
"A food label for the Advent of Code 2020 Day 21 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
CONTAINS = ' (contains '
COMMA = ', '

# ======================================================================
#                                                                  Label
# ======================================================================


class Label(object):   # pylint: disable=R0902, R0205
    "Object for Allergen Assessment"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.ingredients = []
        self.allergens = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            ingredients, allergens = text.split(CONTAINS)
            self.ingredients = ingredients.split()
            self.allergens = allergens[:-1].split(COMMA)

    def has_ingredient(self, ingredient):
        "Returns True if the label lists the ingredient"
        return ingredient in self.ingredients

    def has_allergen(self, allergen):
        "Returns True if the label lists the allergen"
        return allergen in self.allergens


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          l a b e l . p y                       end
# ======================================================================
