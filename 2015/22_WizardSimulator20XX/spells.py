# ======================================================================
# Wizard Simulator 20XX
#   Advent of Code 2015 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s p e l l s . p y
# ======================================================================
"Spells for the Advent of Code 2015 Day 22 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import spell


# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
# - Magic Missile costs 53 mana. It instantly does 4 damage.
# - Drain costs 73 mana. It instantly does 2 damage and heals you for
#    2 hit points.
# - Shield costs 113 mana. It starts an effect that lasts for 6 turns.
#    While it is active, your armor is increased by 7.
# - Poison costs 173 mana. It starts an effect that lasts for 6 turns. At
#    the start of each turn while it is active, it deals the boss 3 damage.
# - Recharge costs 229 mana. It starts an effect that lasts for 5 turns.
#    At the start of each turn while it is active, it gives you 101 new
#    mana.

SPELLS = [
    # Name         Cost Turns Damage Heal Armor Mana
    "Magic Missile,  53,  0,    4,    0,    0,    0",
    "Drain,          73,  0,    2,    2,    0,    0",
    "Shield,        113,  6,    0,    0,    7,    0",
    "Poison,        173,  6,    3,    0,    0,    0",
    "Recharge,      229,  5,    0,    0,    0,  101",
]

# ======================================================================
#                                                                 Spells
# ======================================================================


class Spells(object):   # pylint: disable=R0902, R0205
    "Object for Wizard Simulator 20XX"

    def __init__(self, text=None):

        # 1. Set the initial values
        self.text = text
        self.spells = {}

        # 2. Add in the spells (if any)
        if self.text and len(self.text) > 0:
            for line in self.text:
                spl = spell.Spell(text=line)
                self.spells[spl.name] = spl

    def clone(self):
        "Make a clean copy"
        other = Spells()
        for name, spl in self.spells.items():
            other.spells[name] = spl.clone()
        return other

    def activate(self, spl):
        "Add a spell"
        self.spells[spl.name] = spl

    def remove(self, spl):
        "Remove a spell"
        del self.spells[spl.name]

    def names(self):
        "Return the names of the spells"
        return set(self.spells.keys())

    def named(self, name):
        "Return the named spell"
        return self.spells[name]

    def effects(self, wizard, boss):
        "Feel the effect of spells that are still active"
        wizard['armor'] = 0
        for spl in self.spells.values():
            if spl.turns > 0:
                spl.effect(wizard, boss)

    def are_active(self):
        "Return the name of active spells"
        return set(spl.name for spl in self.spells.values() if spl.turns > 1)

    def __len__(self):
        return len(self.spells)

    def __str__(self):
        act = ["%s:%d" % (spl.name[0], spl.turns) for spl in self.spells.values() if spl.turns > 0]
        return ",".join(act)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        s p e l l s . p y                       end
# ======================================================================
