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

    def any_leftovers(self):
        "Return True if there are left over resources"

        # 1. Assume there are none
        result = False

        # 2. Loop over any resources we may have
        for number in self.resources.values():

            # 3. If we have some of this one, Return True
            if number > 0:
                result = True
                break

        # 4. Return True if there are left over resources
        return result

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
            if watch:
                print("Looking for %s in recipe: %s" % (in_item, str(recipe)))
            if not self.produce(in_item):
                if watch:
                    print("Unable to produce %s in recipe: %s" % (in_item, str(recipe)))
                return False

        # 2. We have everything, Cook it up
        self.resources[recipe.produces] += recipe.quanity

        # 3. And return success
        return True

    def fuel_per_trillion(self, watch=False):
        "Determine amount of fuel that can be produced with one trillion ore"

        # 1. Keep track of ore for fuel (and our best guess)
        ore_for_fuel = {}
        fuel_no_leftovers = 0

        best_fuel = 0
        best_ore = 0
        best_base = 0
        best_remaining = TRILLION

        # 2. Loop until we find a fuel amount that generates no left-overs
        while self.ore < TRILLION:

            # 3. Generate one more fuel
            assert self.produce('1 FUEL')

            # 4. Save it
            fuel_no_leftovers += 1
            ore_for_fuel[fuel_no_leftovers] = self.ore
            if watch:
                print("Producing %d FUEL takes %d ORE" % (fuel_no_leftovers, self.ore))

            # 5. If there are no left overs, we have all that we need
            if not self.any_leftovers():
                break

            # 5a. Else make a guess based on what we have
            this_ore = self.ore
            this_times = TRILLION // this_ore
            this_fuel = fuel_no_leftovers * this_times
            this_total = this_ore * this_times
            this_remaining = TRILLION - this_total
            extra_fuel = 0
            extra_ore = 0
            skeys = sorted(ore_for_fuel)
            for key in skeys:
                if ore_for_fuel[key] < this_remaining:
                    extra_fuel = key
                    extra_ore = ore_for_fuel[key]
            this_fuel += extra_fuel
            this_ore += extra_ore
            this_remaining -= extra_ore

            # 5b. If this guess uses more ore than the last guess, record it
            if this_fuel > best_fuel:
                best_ore = this_ore
                best_remaining = this_remaining
                best_fuel = this_fuel
                best_base = fuel_no_leftovers
                print("Better guess at %d: Producing %d FUEL leaves %d ORE remaining" %
                      (best_base, best_fuel, best_remaining), flush=True)
                if best_remaining == 0:
                    return best_fuel

        # 6. If no production had no leftovers
        if self.ore >= TRILLION:
            fuel_no_leftovers -= 1
            return ore_for_fuel[fuel_no_leftovers]

        # 7. Compute max ore used with no leftovers
        if watch:
            print("Producing %d FUEL has no left over resources" % (fuel_no_leftovers))
        ore_no_leftovers = self.ore
        times_no_leftovers = TRILLION // ore_no_leftovers
        total_fuel = fuel_no_leftovers * times_no_leftovers
        total_ore = ore_no_leftovers * times_no_leftovers
        remaining_ore = TRILLION - total_ore
        if watch:
            print("Producing %d FUEL %d times would produce %d FUEL with %d ORE remaining" %
                  (fuel_no_leftovers, times_no_leftovers, total_fuel, remaining_ore))

        # 8. Find a production FUEL number to use up the last of the ore
        extra_fuel = 0
        extra_ore = 0
        skeys = sorted(ore_for_fuel)
        for key in skeys:
            if ore_for_fuel[key] < remaining_ore:
                extra_fuel = key
                extra_ore = ore_for_fuel[key]

        # 9. Compute total_fuel we can produce
        total_fuel += extra_fuel
        total_ore += extra_ore
        if watch:
            print("An additional %d FUEL can be produced using %d ORE for a total of %d FUEL (%d ORE)" %
                  (extra_fuel, extra_ore, total_fuel, total_ore))
        return total_fuel

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  n a n o f a c t o r y . p y                   end
# ======================================================================
