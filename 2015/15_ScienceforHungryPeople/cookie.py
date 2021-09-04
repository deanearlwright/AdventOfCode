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
MAX_TEASPOONS = 100
MAX_CALORIES = 500

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

    def vary_ingredients(self, indx, last, teaspoons, best_score, verbose=False):
        "Try various amounts of the remaining ingredients"

        # 1. Determine amount used and high/low values
        if indx == 0:
            used = 0
        else:
            used = sum(teaspoons[0:indx])
        high = MAX_TEASPOONS - used
        if indx == last:
            low = high
        else:
            low = 0

        # 2. Loop for the various amounts
        for amount in range(low, high + 1):
            teaspoons[indx] = amount

            # 3. Do we have it all?
            if sum(teaspoons) == MAX_TEASPOONS:

                # 4. Is it better than all the rest?
                # 4a. Part 2 only looks at a specific calorie count
                if not self.part2 or self.calories(teaspoons) == MAX_CALORIES:
                    new_score = self.score(teaspoons)
                    if new_score > best_score:
                        if verbose:
                            print("score improved from", best_score, "to", new_score, "using", teaspoons)
                        best_score = new_score

            #  5. Else we hight have to go deeper
            elif indx != last:
                best_score = self.vary_ingredients(indx + 1, last, teaspoons, best_score, verbose)

        # 6. Return the best score
        return best_score

    def best_cookie_score(self, verbose=False):

        # 1. Start with nothing
        teaspoons = [0] * len(self.ingredients)

        # 2. Try different amounts of the ingredients
        best_score = self.vary_ingredients(0, len(self.ingredients) - 1, teaspoons, 0, verbose)

        # 8. Return the best score
        return best_score

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

    def calories(self, teaspoons):
        "Return the calorie count of cookies made with these proportions"

        # 1. Start with nothing
        total = 0

        # 2. Loop for all of the ingredients
        for indx_i, ingrd in enumerate(self.ingredients):

            # 3. Get the values for this ingredient
            cals = ingrd.calories(teaspoons[indx_i])

            # 4. Update the totals
            total += cals

        # 5. Return total calorie count
        return total

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.best_cookie_score(verbose=verbose)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.best_cookie_score(verbose=verbose)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        c o o k i e . p y                       end
# ======================================================================
