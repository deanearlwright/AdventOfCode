# ======================================================================
# RPG Simulator 20XX
#   Advent of Code 2015 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r p g s i m . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 21 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import player
import shop

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Rpgsim
# ======================================================================


class Rpgsim(object):   # pylint: disable=R0902, R0205
    "Object for RPG Simulator 20XX"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.shop = shop.Shop()
        self.boss = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.boss = player.Player(text)

    def boss_wins_fight(self, items):
        "Have the boss fight the player"

        # 1. Create the combatents
        boss = self.boss.clone()
        plyr = player.Player(part2=self.part2, items=items)

        # 2. Do battle until one or the other is dean
        while not (boss.is_dead() or plyr.is_dead()):

            # 3. Player attacks
            if boss.defend(plyr.attack()):
                return False

            # 4. Boss attacks
            if plyr.defend(boss.attack()):
                return True

    def cheapest_win(self, verbose=False):
        "Determine the cheapeast win"

        # 1. Start with nothing
        cheapest_cost = 999999999999
        cheapest_items = []

        # 2. Loop for all the possible items for the player
        for items in self.shop.combinations():

            # 3. Battle
            if not self.boss_wins_fight(items):

                # 4. Player won, is this win cheaper?
                this_cost = shop.Shop.total_price(items)
                if this_cost < cheapest_cost:
                    cheapest_cost = this_cost
                    cheapest_items = items
                    if verbose:
                        print('Cheaper %d %s' % (cheapest_cost, shop.Shop.item_names(items)))

        # 5. Return the cheapest win cost
        if verbose:
            print('Cheapest Win $%d with %s' %
                  (cheapest_cost, shop.Shop.item_names(cheapest_items)))
        return cheapest_cost

    def costliest_loss(self, verbose=False):
        "Determine the the most expensive loss"

        # 1. Start with nothing
        expensive_cost = -1
        expensive_items = []

        # 2. Loop for all the possible items for the player
        for items in self.shop.combinations():

            # 3. Battle
            if self.boss_wins_fight(items):

                # 4. boss won, is this loss more expensive?
                this_cost = shop.Shop.total_price(items)
                if this_cost > expensive_cost:
                    expensive_cost = this_cost
                    expensive_items = items
                    if verbose:
                        print('Costlier %d %s' % (expensive_cost, shop.Shop.item_names(items)))

        # 5. Return the most expensive loss win cost
        if verbose:
            print('Most Expensive $%d with %s' %
                  (expensive_cost, shop.Shop.item_names(expensive_items)))
        return expensive_cost

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.cheapest_win(verbose=verbose)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.costliest_loss(verbose=verbose)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        r p g s i m . p y                       end
# ======================================================================
