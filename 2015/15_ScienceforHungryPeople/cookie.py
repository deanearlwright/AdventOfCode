# ======================================================================
# Science for Hungry People
#   Advent of Code 2015 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c o o k i e . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import ingredient

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Cookie
# ======================================================================


class Cookie(object):   # pylint: disable=R0902, R0205
    "Object for Science for Hungry People"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.ingredients = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in self.text:
                self.ingredients.append(ingredient.Ingredient(text=line, part2=self.part2))

    def score(self, teaspoons):
        "Return the score of cookies made with these proportions"

        # 1. Start with nothing
        totals = [0, 0, 0, 0]

        # 2. Loop for all of the ingredients
        for indx_i, ingrd in enumerate(self.ingredients):

            # 3. Get the values for this ingredient
            props = ingrd.properties(teaspoons[indx_i])

            # 4. Update the totals
            for indx_p, prop in enumerate(props):
                totals[indx_p] += prop

        # 5. Zero out negative property totals
        totals = [max(0, _) for _ in totals]

        # 6. Compute total property score
        result = 1
        for ptotal in totals:
            result *= ptotal

        # 7. Return total property score
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return None

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return None


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        c o o k i e . p y                       end
# ======================================================================
