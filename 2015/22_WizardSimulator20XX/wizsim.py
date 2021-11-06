# ======================================================================
# Wizard Simulator 20XX
#   Advent of Code 2015 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         w i z s i m . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 22 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import deque

import spells
import state
import player

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
WIZARD_TEXT = [
    "Hit Points: 50",
    "Mana: 500",
]

BOSS_TEXT = [
    "Hit Points: 13",
    "Armor: 8",
]

MAX_MANA = 2000


# ======================================================================
#                                                                 Wizsim
# ======================================================================


class Wizsim(object):   # pylint: disable=R0902, R0205
    "Object for Wizard Simulator 20XX"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.spells = spells.Spells(text=spells.SPELLS)
        self.states = deque([])

    def initial_state(self, wizard_text=None, boss_text=None):
        "Create the initial game state"

        # 1. Create the two combatants
        if wizard_text is None:
            wizard = player.Player(name="Wizard", text=WIZARD_TEXT, part2=self.part2)
        else:
            wizard = player.Player(name="Wizard", text=wizard_text, part2=self.part2)
        if boss_text is None:
            if self.text is None:
                boss = player.Player(name="Boss", text=BOSS_TEXT, part2=self.part2)
            else:
                boss = player.Player(name="Boss", text=self.text, part2=self.part2)
        else:
            boss = player.Player(name="Boss", text=boss_text, part2=self.part2)

        # 2. Create and save the initial state
        self.states = deque([state.State(wizard=wizard, boss=boss)])

    def least_mana(self):
        "Find the spells that will defeat the boss with the lease expendature of mana"

        # 1. Start assumne that it costs plenty
        result = MAX_MANA
        trace = []

        # 2. Loop while there are states to explore
        while len(self.states) > 0:

            # 3. Get the newest state (depth first)
            utah = self.states.pop()

            # 4. If the boss is dead, check mana usage
            if utah.boss.is_dead():
                print("killed him on turn %d cost %d" % (utah.turn, utah.wizard["used"]))
                if utah.wizard["used"] < result:
                    result = utah.wizard["used"]
                    trace = utah.trace
                continue

            # 5. If the wizard is dead, get a differnt state
            if utah.wizard.is_dead():
                continue

            # 6. Ignore this state if we have already used more than the "best" solution
            if utah.wizard["used"] >= result:
                continue

            # 7. Is there another spell to try? If not, try something else
            spls = utah.another(self.spells)
            if len(spls) == 0:
                continue
            #print("utah", result, utah, spls)

            # 8. Create a new state where we have cast the spell
            ohio = self.turn(utah, self.spells.named(spls[0]))
            if ohio.wizard["used"] >= result:
                continue
            ohio.tried = set()
            self.states.append(ohio)

            # 9. Remember that we used this one and put back for next time
            utah.tried.add(spls[0])
            self.states.appendleft(utah)

        # 10. Return the least amout of mana used
        print(trace)
        return result

    def turn(self, current, spl):
        "Create a new state after the wizard casts the spell and the Boss attacks"

        # 1. Clone the current state and increase the turn number
        ohio = current.clone()
        ohio.turn += 1

        # 2. If "Hard" mode, decrease the player's hit points by one
        if self.part2:
            ohio.wizard.wack()
            if ohio.wizard.is_dead():
                return ohio

        # 3. Give active spells a chance
        ohio.active.effects(ohio.wizard, ohio.boss)

        # 4. If either are dead, that is the end of it
        if ohio.wizard.is_dead() or ohio.boss.is_dead():
            return ohio

        # 4. Cast the spell
        active = spl.cast(ohio.wizard, ohio.boss)
        ohio.cast(spl.name)

        # 5. If a delayed spell, add it to the active set
        if active is not None:
            ohio.active.activate(active)

        # 6. Give active spells a chance
        ohio.active.effects(ohio.wizard, ohio.boss)

        # 7. If either are dead, that is the end of it
        if ohio.wizard.is_dead() or ohio.boss.is_dead():
            return ohio

        # 8. Let the Boss have a go
        ohio.wizard.defend(ohio.boss.attack())

        # 9. Return the new state
        return ohio

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        self.initial_state()
        return self.least_mana()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        self.initial_state()
        return self.least_mana()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        w i z s i m . p y                       end
# ======================================================================
