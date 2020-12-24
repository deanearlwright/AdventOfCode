# ======================================================================
# Allergen Assessment
#   Advent of Code 2020 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s h o p p i n g . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 21 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import label

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                               Shopping
# ======================================================================


class Shopping(object):   # pylint: disable=R0902, R0205
    "Object for Allergen Assessment"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.labels = []
        self.ingredients = set()
        self.allergens = set()
        self.mapping = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Create labels, ingredients, and allergens from input text"

        # 1. Process text to create list of labels
        for line in text:
            self.labels.append(label.Label(text=line, part2=self.part2))

        # 2. Get list of ingredients
        for lab in self.labels:
            self.ingredients.update(lab.ingredients)

        # 3. Get list of allergens
        for lab in self.labels:
            self.allergens.update(lab.allergens)

        # 4. Map the allergens to (possible) ingredents
        for lab in self.labels:
            for allergen in lab.allergens:
                if allergen not in self.mapping:
                    self.mapping[allergen] = set(lab.ingredients)
                else:
                    self.mapping[allergen] &= set(lab.ingredients)

    def definitely_allergenic(self, limit=10):
        "Returns the ingredients and their allergen"

        # 1. And now it is suduku time (but limit the time)
        for _ in range(limit):
            assert _ >= 0  # Suppress code warning about _ not used
            done = True

            # 2. Once we find an allergen that can be in only one ingredient
            #    We can remove that ingredient from the other allergen lists
            for ingredients in self.mapping.values():
                if len(ingredients) == 1:
                    ingredient = ingredients.pop()
                    for other in self.mapping.values():
                        other.discard(ingredient)
                    ingredients.add(ingredient)
                else:
                    done = False

            # 3. If all allergens have only one ingredent, we are done
            if done:
                return True

        # 4. All that work and nothing to show for it
        return False

    def not_safe(self):
        "Determine the dangerous ingredients"

        # 1. Determine the not-safe ingredients
        dangerous = set()
        for ingredient in self.mapping.values():
            dangerous |= ingredient

        # 2. Return the non-safe ingredients
        return dangerous

    def safe(self):
        "Determine the safe ingredients"

        # 1. Determine the non-safe ingredients
        dangerous = self.not_safe()

        # 2. Safe ingredients are all the rest
        safe = self.ingredients.copy()
        safe -= dangerous

        # 4. Return the safe ingredients
        return safe

    def count_ingredient(self, ingredient):
        "Count the time number of labels that contain the ingredient"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the labels
        for lab in self.labels:

            # 3. Increment the count if the label includes this ingredient
            if ingredient in lab.ingredients:
                result += 1

        # 4. Return the number of labels that contain this ingredient
        return result

    def count_ingredients(self, ingredients):
        "Count the time number of the ingredients appeard on a label"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the ingredients
        for ingredient in ingredients:

            # 3. Add in the number of times that ingredient appears
            result += self.count_ingredient(ingredient)

        # 4. Return the total count
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.count_ingredients(self.safe())

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Reduce the list of allergens and in ingredients they are in
        solved = self.definitely_allergenic()
        if not solved:
            return None

        # 2. Sort them alphabetically by thier allergen
        dangerous = []
        for allergen in sorted(self.mapping.keys()):
            dangerous.append(list(self.mapping[allergen])[0])

        # 3. Return the solution for part two
        return ','.join(dangerous)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      s h o p p i n g . p y                     end
# ======================================================================
