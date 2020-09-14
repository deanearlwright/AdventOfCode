# ======================================================================
# Immune System Simulator 20XX
#   Advent of Code 2018 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r e i n d e e r . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 24 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import operator
import re
# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
re_group = re.compile(r"^(\d+) units each with (\d+) hit points ([()a-z ;,]+)?with an attack that does (\d+) (\w+) damage at initiative (\d+)$")

# ======================================================================
#                                                                  Group
# ======================================================================

class Group(object):   # pylint: disable=R0902, R0205
    "Object for Immune System Simulator 20XX - Group of units"

    def __init__(self, text=None):

        # 1. Set the initial values
        self.text = text
        self.number = 0
        self.hitpoints = 0
        self.immune = []
        self.weak = []
        self.damage = 0
        self.attack = ''
        self.initiative = 0
        self.target_selection_key = 0
        self.targeting = None

        # 2. Process text (if any)
        if text is not None:
            self.process_text(text)

    def process_text(self, text):
        # 1. Parse with regex
        re_result = re_group.match(text)
        if re_result is None:
            print("Unable to decode Group [%s]" % text)
            return
        # 2. Fill in the non-paren stuff
        grps = re_result.groups()
        self.number = int(grps[0])
        self.hitpoints = int(grps[1])
        self.damage = int(grps[3])
        self.attack = grps[4]
        self.initiative = int(grps[5])
        # 3. Handle any immutities and weeknesses
        if grps[2] is not None:
            for phrase in grps[2].strip().replace('(','').replace(')','').split(';'):
                words = phrase.replace(',','').strip().split(' ')
                if words[0] == 'weak':
                    self.weak = words[2:]
                else:
                    self.immune = words[2:]

    def effective_power(self):
        return self.number * self.damage

    def potential_damage(self, other):
        # 1. Start with my effective power
        result = self.effective_power()
        # 2. But if the other is immune to my attack, no damage would be done
        if self.attack in other.immune:
            result = 0
        # 3. But if the other is weak to my attack, I will crush them like bugs
        if self.attack in other.weak:
            result *= 2
        return result

    def prepare_for_target_selection(self):
        self.target_selection_key = (self.number * self.damage, self.initiative)
        self.targeting = None

    def select_target(self, targets):
        # 1. Not much to do if no targets
        if not targets:
            return targets
        # 2. Assume there is nothing to target
        my_target = None
        my_damage = 0
        # 3. Loop for all of the targets
        for target in targets:
            # 4. Determine the amount of damage that would be done
            damage = self.potential_damage(target)
            # 5. Can only target if we do some damage
            if damage > 0:
                # 6. If this is more than before, keep it
                if damage > my_damage:
                    my_target = target
                    my_damage = damage
                # 7. If the same as another, tie breakers: largest effective, highest initiative
                elif damage == my_damage:
                    if target.effective_power() > my_target.effective_power():
                        my_target = target
                        my_damage = damage
                    elif target.effective_power() == my_target.effective_power():
                        if target.initiative > my_target.initiative:
                            my_target = target
                            my_damage = damage
        # 8. If we found a target, remember it
        self.targeting = my_target

        # 9. Remove it from the avilable targets
        if my_target:
            targets.remove(my_target)

    def execute_attack(self):
        # 1. If we have no target, we do not attack
        if not self.targeting:
            return
        # 2. If the target has no more units, we do not attack
        if self.targeting.number == 0:
            return
        # 3. Determine how much damage we will do
        damage = self.potential_damage(self.targeting)
        # 4. Convert that to units
        units = damage // self.targeting.hitpoints
        # 5. Eliminate that many units
        self.targeting.number = max(0, self.targeting.number - units)

    def boast(self, amount):
        self.damage += amount


# ======================================================================
#                                                                   Army
# ======================================================================

class Army(object):   # pylint: disable=R0902, R0205
    "Object for Immune System Simulator 20XX - Army"

    def __init__(self, text=None):

        # 1. Set the initial values
        self.name = None
        self.groups = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                if ':' in line:
                    if self.name is None:
                        self.name = line.replace(':', '')
                    else:
                        break
                elif line[0] in '123456789':
                    self.groups.append(Group(text=line))
                else:
                    print("Unexpected army line [%s]" % line)
                    break

    def prune(self):
        # 1. Start with no effective groups
        effective = []
        # 2. Loop for all of the groups
        for group in self.groups:
            # 3. If the group is effective, add it to the new list
            if group.effective_power() > 0:
                effective.append(group)
        # 4. Keep only the effective groups
        self.groups = effective

    def target_selection_order(self):
        return sorted(self.groups,
                      reverse=True,
                      key=operator.attrgetter('target_selection_key'))

    def target_selection(self, others):
        # 1. Get the groups ready
        for group in self.groups:
            group.prepare_for_target_selection()
        # 2. Loop for the groups in order of effective power / initiative
        targets = [target for target in others]
        for group in self.target_selection_order():
            group.select_target(targets)

    def total_units(self):
        return sum([grp.number for grp in self.groups])

    def boast(self, amount):
        for grp in self.groups:
            grp.boast(amount)

    def contains_units(self):
        return self.total_units() > 0

# ======================================================================
#                                                               Reindeer
# ======================================================================


class Reindeer(object):   # pylint: disable=R0902, R0205
    "Object for Immune System Simulator 20XX"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.armies = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.process_text(text)

    def process_text(self, text):
        # 1. Find the lines with colons
        self.armies = []
        colons = []
        for lnum, line in enumerate(text):
            if ':' in line:
                colons.append(lnum)
        # 2. There should be 2 of them
        if len(colons) != 2:
            print("Unexpected number of Army names [%d]" % len(colons))
            return
        # 3. Add the two armies
        self.armies.append(Army(text=text[colons[0]:colons[1]]))
        self.armies.append(Army(text=text[colons[1]:]))

    def round(self):
        # 1. Targeting
        self.targeting()
        # 2. Attacking
        self.attacking()
        # 3. Pruning
        self.armies[0].prune()
        self.armies[1].prune()

    def targeting(self):
        # 1. Army 0 targets Army 1
        self.armies[0].target_selection(self.armies[1].groups)
        # 2. Army 1 targets Army 0
        self.armies[1].target_selection(self.armies[0].groups)

    def attacking(self):
        # 1. Get list of all groups sorted by initiative
        groups = sorted(self.armies[0].groups + self.armies[1].groups,
                        reverse=True,
                        key=operator.attrgetter('initiative'))
        # 2. Loop for all the groups
        for group in groups:
            # 3. Execute the attack
            group.execute_attack()

    def fight(self, verbose=False):
        ## TODO ## Add stalemate checker
        while self.armies[0].contains_units() and self.armies[1].contains_units():
            self.round()
            if verbose:
                print(str(self))
        if self.armies[0].contains_units():
            return self.armies[0].total_units()
        return self.armies[1].total_units()

    def winner(self):
        if self.armies[0].contains_units():
            return self.armies[0].name
        return self.armies[1].name

    def boast(self, amount):
        # 1. Reload the armies from text
        self.process_text(self.text)
        # 2. Add a boast to the immune system
        self.armies[0].boast(amount)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.fight(verbose=verbose)


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Loop for a while
        # ## TODO ## Binary search would be nice as well as dealing with statemates
        for boast in range(51, 2000):
            # 2. Give the raindeer a little help
            self.boast(boast)
            # 3. Retry the conflict
            result = self.fight(verbose=verbose)
            if verbose:
                print("boast %d winner %s by %d" % (boast, self.winner(), result))
            # 4. Did we do it?
            if self.winner() == "Immune System":
                return result
        # 5. Return the unhappy news
        return None

    def __str__(self):
        if not self.armies:
            return ''
        result = []
        result.append("%s:" % self.armies[0].name)
        if not self.armies[0].groups:
            result.append("No groups remain.")
        for num, grp in enumerate(self.armies[0].groups):
            result.append("Group %d contains %d units" % (num + 1, grp.number))
        result.append("%s:" % self.armies[1].name)
        if not self.armies[1].groups:
            result.append("No groups remain.")
        for num, grp in enumerate(self.armies[1].groups):
            result.append("Group %d contains %d units" % (num + 1, grp.number))
        return '\n'.join(result)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      r e i n d e e r . p y                     end
# ======================================================================
