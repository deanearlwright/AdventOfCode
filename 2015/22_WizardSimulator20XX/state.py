# ======================================================================
# Wizard Simulator 20XX
#   Advent of Code 2015 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s t a t e . p y
# ======================================================================
"Game state for the Advent of Code 2015 Day 22 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import spells

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Spell
# ======================================================================


class State(object):   # pylint: disable=R0902, R0205
    "Object for Wizard Simulator 20XX"

    def __init__(self, wizard=None, boss=None):

        # 1. Set the initial values
        self.turn = 0
        self.wizard = wizard
        self.boss = boss
        self.active = spells.Spells()
        self.tried = set()
        self.trace = []

    def clone(self):
        "Make a clean copy"
        other = State()
        other.turn = self.turn
        other.wizard = self.wizard.clone()
        other.boss = self.boss.clone()
        other.active = self.active.clone()
        other.tried = set(list(self.tried))
        other.trace = self.trace[:]
        return other

    def another(self, spls):
        "What are the next spells to be cast"

        # 1. Determined which spells are yet to be tried
        untried = spls.names() - self.tried

        # 2. Can only cast the ones aren't currently active
        notactive = untried - self.active.are_active()

        # 4. See which ones the wizard can cast
        possible = [spl for spl in notactive if spls.named(spl).cost <= self.wizard["mana"]]

        # 5. Make testing repeatable by putting the spells in alphabetical order
        possible.sort()

        # 6. Return what is possible
        return possible

    def cast(self, name):
        "Remember that a spell has been cast"
        self.trace.append(name)

    def __str__(self):
        tried = [_[0] for _ in self.tried]
        trace = [_[0] for _ in self.trace]
        return "%d %s, %s, A=[%s], T=[%s] [%s]" % (
            self.turn, str(self.wizard), str(self.boss),
            str(self.active), ','.join(tried), ','.join(trace))


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         s t a t e . p y                        end
# ======================================================================
