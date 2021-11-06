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


# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Spell
# ======================================================================


class Spell(object):   # pylint: disable=R0902, R0205
    "Object for Wizard Simulator 20XX"

    def __init__(self, text=None):

        # 1. Set the initial values
        self.name = 'None'
        self.cost = 9999
        self.turns = 0
        self.damage = 0
        self.heal = 0
        self.armor = 0
        self.mana = 0

        # 2. Process Text (if any)
        if text and len(text) > 0:
            parts = text.split(',')
            if len(parts) != 7:
                print("Unable to parse: %s" % text)
            else:
                self.name = parts[0].strip()
                self.cost = int(parts[1])
                self.turns = int(parts[2])
                self.damage = int(parts[3])
                self.heal = int(parts[4])
                self.armor = int(parts[5])
                self.mana = int(parts[6])

    def can_be_cast(self, wizard):
        "Check if I can afford to cast the spell"
        return wizard.mana >= self.cost

    def cast(self, wizard, boss):
        "Cast the spell"

        # 1. Absorb the cost to cast the spell
        wizard['mana'] -= self.cost
        wizard['used'] += self.cost

        # 2. Does it happen immediately? If so, do it
        if self.turns == 0:
            boss.defend(self.damage)
            wizard['hitpoints'] += self.heal
            return None

        # 3. Create a copy of spell for delayed effect
        return self.clone()

    def effect(self, wizard, boss):
        "Execute a spell's delayed effect"

        # 1. Shield
        if self.armor > 0:
            wizard['armor'] = self.armor

        # 2. Poison
        if self.damage > 0:
            boss.defend(self.damage)

        # 3. Recharge
        if self.mana > 0:
            wizard['mana'] += self.mana

        # 4. Decrement timer
        self.turns -= 1

        # 5. Return True if the spell is still active
        return self.turns > 0

    def __str__(self):
        return "%s, %d, %d, %d, %d, %d, %d" % (
            self.name, self.cost, self.turns, self.damage, self.heal, self.armor, self.mana)

    def clone(self):
        "Make a clean copy"
        other = Spell()
        other.name = self.name
        other.cost = self.cost
        other.turns = self.turns
        other.damage = self.damage
        other.heal = self.heal
        other.armor = self.armor
        other.mana = self.mana
        return other


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         s p e l l . p y                        end
# ======================================================================
