# ======================================================================
# RPG Simulator 20XX
#   Advent of Code 2015 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s h o p . p y
# ======================================================================
"Shop for the Advent of Code 2015 Day 21 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple
from itertools import permutations

import aoc_21

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
ITEMS_TEXT = """
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage+1     25     1       0
Damage+2     50     2       0
Damage+3    100     3       0
Defense+1    20     0       1
Defense+2    40     0       2
Defense+3    80     0       3
"""
NOTHING_TEXT = """
Armor:      Cost  Damage  Armor
NoArmor       0     0       0
Rings:      Cost  Damage  Armor
NoRight       0     0       0
NoLeft        0     0       0
"""

Item = namedtuple('Item', 'section, name, cost, damage, armor')

# ======================================================================
#                                                                   Shop
# ======================================================================


class Shop(object):   # pylint: disable=R0902, R0205
    "Object for RPG Simulator 20XX"

    def __init__(self, text=None):

        # 1. Set the initial values
        self.items = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)
        else:
            self._process_text(aoc_21.from_text(ITEMS_TEXT))
            self._process_text(aoc_21.from_text(NOTHING_TEXT))

    def _process_text(self, text):
        "Assign values from text"

        # 1. Start with nothing
        section = 'unknown'

        # 1. Loop for all records
        for line in text:

            # 2. Split up the line

            name, cost, damage, armor = line.split()

            # 3. If this is a section line, write out previous inventory, and start new one
            if ':' in name:
                section = name[0:-1]

            # 4. Else add item to the shop's inventory
            else:
                self.items.append(Item(section, name, int(cost), int(damage), int(armor)))

    def combinations(self):
        "Yield all valid combinations"

        # 1. Get the items for each section
        weapon = [_ for _ in self.items if _.section == 'Weapons']
        armor = [_ for _ in self.items if _.section == 'Armor']
        rings = [_ for _ in self.items if _.section == 'Rings']

        # 2. Loop for all of the permutations
        for weapon_used in permutations(weapon, 1):
            for armor_used in permutations(armor, 1):
                for rings_used in permutations(rings, 2):

                    # 3. Return the weapons, armor, and rings
                    yield [weapon_used[0], armor_used[0], rings_used[0], rings_used[1]]

    @staticmethod
    def total_price(items):
        "Return the total cost of the items"
        return sum(_.cost for _ in items)

    @staticmethod
    def total_attack(items):
        "Return the total attach damage of the items"
        return sum(_.damage for _ in items)

    @staticmethod
    def total_defense(items):
        "Return the total armor value of the items"
        return sum(_.armor for _ in items)

    @staticmethod
    def item_names(items):
        "Return the total armor value of the items"
        return ', '.join(_.name for _ in items)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          s h o p . p y                         end
# ======================================================================
