# ======================================================================
# Space Stoichiometry
#   Advent of Code 2019 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        n a n o f a c t o r y . p y
# ======================================================================
"Factory for Space Stoichiometry Problem for Advent of Code 2019 Day 14"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

import reaction

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
ORE = "ORE"

TRILLION = 1000000000000

# ======================================================================
#                                                            NanoFactory
# ======================================================================


class NanoFactory():
    """Object representing a factory producing fuel from ore"""

    def __init__(self, text=None):

        # 1. Start with no resources
        self.resources = {}
        self.recipes = {}
        self.ore = 0

        # 2. If we have text, create reactions and add to list of recipies
        if text is not None:

            # 3. Loop for each line of text
            for line in text:

                # 4. Create a new reaction
                recipe = reaction.Reaction(text=line)

                # 5. Add this reaction to the list
                self.recipes[recipe.produces] = recipe

    def reset(self):
        "Clear out previous production"
        self.resources = {}
        self.ore = 0


    def produce(self, desired, watch=False):
        "Have the factory produce the desired item at the indicated quanity"

        # 1. Get the desired item and quanity
        quanity, item = desired.split()
        quanity = int(quanity)
        if watch:
            print("Looking for %d of %s" % (quanity, item))

        # 2. If they want ore, give it to them
        if item == ORE:
            self.ore += quanity
            return True

        # 3. Do we have what they want on hand, give it to them
        if item not in self.resources:
            self.resources[item] = 0
        if self.resources[item] >= quanity:
            self.resources[item] -= quanity
            return True

        # 4. Do we know how to make this?
        if item in self.recipes:
            recipe = self.recipes[item]

            # 5. Follow this recipe until we have enough
            while self.resources[item] < quanity:
                if not self.follow(recipe, watch=watch):
                    return False

            # 6. Finally we have enough
            self.resources[item] -= quanity
            return True

        # 7. Well this is disapointing
        return False

    def follow(self, recipe, watch=False):
        "Follow a recipe to get more of something"

        # 1. Gollect all of the inputs
        if watch:
            print("Following recipe: %s" % str(recipe))
        for in_item in recipe.requires:
            if not self.produce(in_item):
                return False

        # 2. We have everything, Cook it up
        self.resources[recipe.produces] += recipe.quanity

        # 3. And return success
        return True

    def fuel_per_trillion(self, watch=True):
        "Determine amount of fuel that can be produced with one trillion ore"

        # 1. Keep track of ore for fuel
        ore_for_fuels = {}

        # 2. Determine cost for one fuel
        assert self.produce('1 FUEL')
        ore_for_one = self.ore
        guess = TRILLION//ore_for_one
        if watch:
            print("Ore cost for single FUEL is %d, initial guess = %d" %
                  (ore_for_one, guess))

        # 3. Determine cost at the guess level
        self.reset()
        assert self.produce('%d FUEL' % (guess))
        ore_for_guess = self.ore
        if watch:
            print("Ore cost for %d FUEL is %d" %
                  (guess, ore_for_quess))

        return guess

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  n a n o f a c t o r y . p y                   end
# ======================================================================
