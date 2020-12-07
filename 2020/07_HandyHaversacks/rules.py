# ======================================================================
# Handy Haversacks
#   Advent of Code 2020 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r u l e s . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 07 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import rule

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Rules
# ======================================================================


class Rules(object):   # pylint: disable=R0902, R0205
    "Object for Handy Haversacks"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rules = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                new_rule = rule.Rule(text=line, part2=part2)
                self.rules[new_rule.bag] = new_rule

    def fill_in_can_contain_shiny_gold(self):
        "Make sure can_contain_shiny_gold is True or False for all rules"

        # 1. Get the names of rules that need can_get_shiny_gold evaluated
        noners = [_.bag for _ in self.rules.values() if _.can_contain_shiny_gold is None]

        # 2. Loop for each of these rules
        for name in noners:

            # 3. And get it evaluated
            can = self.evaluate_shiny_gold(name)

            # 4. This should work
            if can is None:
                print('Unable to determine if %s can hold a shiny gold bag' % name)
                assert can is not None

    def evaluate_shiny_gold(self, name):
        "Determine if a bag can hold a shiny gold bag"

        # 1. Get the current rule
        this_rule = self.rules[name]

        # 2. If we already know, return the knowledge
        if this_rule.can_contain_shiny_gold is not None:
            return this_rule.can_contain_shiny_gold

        # 3. Assume that this bag can't contain shiny gold
        this_rule.can_contain_shiny_gold = False

        # 4. Loop for all of the bags this bag can contain
        for bag in this_rule.bags:

            # 4. Make Use we know if this bag can contain shinny gold
            if self.rules[bag].can_contain_shiny_gold is None:
                new_value = self.evaluate_shiny_gold(bag)
                self.rules[bag].can_contain_shiny_gold = new_value

            # 5. If this bag can contain shiny gold so can it's parent
            if self.rules[bag].can_contain_shiny_gold:
                this_rule.can_contain_shiny_gold = True

        # 6. Return what we now know
        return this_rule.can_contain_shiny_gold

    def how_many_can_hold_shiny_gold(self):
        "Return the number of bags that can hold shinny gold"

        bags = [_.bag for _ in self.rules.values() if _.can_contain_shiny_gold == True]
        return len(bags)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Evaluate "shiny gold" for each rule that needs it
        self.fill_in_can_contain_shiny_gold()

        # 1. Return the solution for part one
        return self.how_many_can_hold_shiny_gold()

    def bags_within(self, name):
        "Returns number of bags within the bag"

        # 1. Get the current rule
        this_rule = self.rules[name]

        # 2. If we know the number of bags within, return it
        if this_rule.bags_within is not None:
            return this_rule.bags_within

        # 2. Start with no bags
        result = 0

        # 3. Loop for all of the sub bags and numbers
        for number, bag in zip(this_rule.numbers, this_rule.bags):

            # 4. Add the number of these bags
            result += number * (1 + self.bags_within(bag))

        # 5. Return the total number of bags
        this_rule.bags_within = result
        return result

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.bags_within('shiny gold')


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          r u l e s . p y                       end
# ======================================================================
