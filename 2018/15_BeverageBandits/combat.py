# ======================================================================
# Beverage Bandits
#   Advent of Code 2018 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c o m b a t . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import cave
import path

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

ENEMY = {
  'E': 'G',
  'G': 'E'
}

# ======================================================================
#                                                                 Combat
# ======================================================================


class Combat(object):   # pylint: disable=R0902, R0205
    "Object for Beverage Bandits"

    def __init__(self, text=None, part2=False, elf_attack=3):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.cave = cave.Cave(text=text, elf_attack=elf_attack)

    def hitpoints(self):
        return self.cave.hitpoints()

    def fight(self, verbose=False):
        # 1. Start with round 1
        rounds = 0
        if verbose:
            print('Starting position');
            print(self.map())

        # 2. Loop until the fight is done
        while True:
            if self.round():
                rounds += 1
                if verbose:
                    print('After %d rounds' % rounds);
                    print(self.map())
            else:
                break

        # 3. Return the number of rounds fought
        if verbose:
            print('Fight ended after %d complete rounds' % rounds)
        return rounds

    def round(self):
        # 1. Get the locations of the elves and goblins in turn order
        locs = self.cave['E'].locations()
        locs.extend(self.cave['G'].locations())
        locs.sort()

        # 2. Loop for all of the units in turn order
        for loc in locs:

            # 3. Execute the turn for that unit, stopping if there are no enemies
            unit = self.cave.get_by_location(loc)
            if unit is not None and unit.hitpoints > 0:
                if self.turn(unit):
                    return False

        # 4. We can keep going
        return True

    def turn(self, unit):

        # 1. Are we the victors?
        others = self.opponents(unit)
        if len(others) == 0:
            return True

        # 2. Attack if you can
        if not self.attack(unit, others):

            # 3. Else move if you can
            self.move(unit, others)

            # 4. And then attack if you can
            self.attack(unit, others)

        # 5. Are we the victors now?
        return False

    def opponents(self, unit):
        enemy_letter = ENEMY[unit.letter]
        return self.cave[enemy_letter]

    def attack_adjacent(self, unit, others):
        # 1. Start with none
        enemy = []
        # 2. Loop for the adjacent locations
        for loc in unit.adjacent():
            # 3. If there is an enemy at that location, remember it
            if loc in others:
                enemy.append(loc)
        # 4. Return all the adjacent enemies
        return enemy

    def attack_weakest(self, enemy, others):
        # 1. Start with none
        weakest = []
        hitpoints = 999999
        # 2. Loop for all the adjacent enemy
        for loc in enemy:
            hp = others[loc].hitpoints
            # 3. If less hitpoints then we current have, use it
            if hp < hitpoints:
                hitpoints = hp
                weakest = [loc]
            # 4. Else if the same hit point, remember them as well
            elif hp == hitpoints:
                weakest.append(loc)
        # 5. Return the location(s) of the weakest enemy
        return weakest

    def attack_choose(self, weakest):
        # 1. If more than one, choose the one in reading order
        if len(weakest) > 0:
            weakest.sort()
        # 2. Return the location to head towards
        return weakest[0]

    def attack_execute(self, unit, chosen, others):
        # 1. Get the chosen enemy
        enemy = others[chosen]
        # 2. Attack it
        unit.attacks(enemy)
        # 3. If we killed it, remove the poor soul
        if enemy.hitpoints <= 0:
            del others[enemy.location]
            #del self.cave[enemy.letter][enemy.location]

    def attack(self, unit, others):
        # 1. Get the squares with enemies adjacent to this unit
        adj = self.attack_adjacent(unit, others)

        # 2. If there are none, report failure
        if not adj:
            return False

        # 3. Find the weakest of the adjacent enemies
        weakest = self.attack_weakest(adj, others)

        # 4. Choose the enemy to attack
        chosen = self.attack_choose(weakest)

        # 5. Attack the enemy
        self.attack_execute(unit, chosen, others)

        # 6. Report that we have engaged the enemy
        return True

    def get_by_location(self, location):
        return self.cave.get_by_location(location)

    def move_in_range(self, unit, others):
        # 1. Start with no locations adjacent to opponents
        adjacent = set()
        # 2. Loop for all of the opponents
        for loc in others:
            # 4. Loop for all of the locations adjacent to the opponents
            for adj in others[loc].adjacent():
                # 5. We are only interested in the empty ones
                if None == self.get_by_location(adj):
                    adjacent.add(adj)
        # 6. Return the empty locations next to opponents
        return adjacent

    def move_reachable(self, unit, in_range):
        # 1. Start with no paths to the locations
        paths = {}
        # 2. Loop for all of the in range locations
        for location in in_range:
            # 3. Find a path(s) to the location (if any)
            the_way = self.find_path(unit.location, location)
            # 4. If there is/are path(s), save it/them
            if the_way is not None:
                paths[location] = the_way
        # 5. Return the reachable locations and thier paths
        return paths

    def move_nearest(self, unit, reachable):
        # 1. Oh so far away
        distance = 99999999
        nearest = []
        # 2. Loop for all of the reachable locations
        for location in reachable:
            # 3. Get the distance from the unit to the destination
            dist = reachable[location].distance
            # 4. If this is a shorter that what we have, replace it
            if dist < distance:
                distance = dist
                nearest = [location]
            # 5. It if os the same distance, add it to what we have
            elif dist == distance:
                nearest.append(location)
        # 5. Return the nearest location(s)/path(s)
        return nearest

    def move_choose(self, nearest):
        # 1. If more than one, choose the one in reading order
        if len(nearest) > 0:
            nearest.sort()
        # 2. Return the location to head towards
        return nearest[0]

    def move_location(self, reachable, chosen):
        return reachable[chosen].move()

    def move_execute(self, unit, new_loc):
        # 0. Preconditions
        assert None == self.get_by_location(new_loc)
        assert 1 == unit.distance(new_loc)
        # 1. Where we came from
        old_loc = unit.location
        # 2. Delete ourselves from that location
        del self.cave[unit.letter][old_loc]
        # 3. Set our new location
        unit.location = new_loc
        # 4. And puts in the cave there
        self.cave[unit.letter][new_loc] = unit

    def move(self, unit, others):
        # 1. Get the empty locations adjacent to your opponents
        in_range = self.move_in_range(unit, others)
        # 2. Reduce those locations by the ones that can be reached
        reachable = self.move_reachable(unit, in_range)
        # 3. If there are no reachable locations, the unit can't move
        if len(reachable) == 0:
            return False
        # 4. Get the nearest locations
        nearest = self.move_nearest(unit, reachable)
        # 5. ChooseIf more than one, choose the one in reading order
        chosen = self.move_choose(nearest)
        # 6. Get the adjacent location toward the chosen destination
        new_loc = self.move_location(reachable, chosen)
        assert new_loc is not None
        # 7. Execute the move
        self.move_execute(unit, new_loc)
        # 8. Return the news that we moved
        return True

    def find_path(self, source, destination):
        directions = path.Path(source=source, destination=destination, cave=self.cave)
        if directions.distance == None:
            return None
        return directions

    def __str__(self):
        return str(self.cave)

    def map(self):
        return self.cave.map_with_hitpoints()

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Fight until there is a victor
        rounds = self.fight(verbose=verbose)
        # 2. Get the surviving hit points
        hitpoints = self.hitpoints()
        # 3. Return the solution for part one
        return rounds*hitpoints

    def no_casualities(self, elf_attack=3, verbose=False):
        # 1. Reset the cave at this elf attack level
        self.cave = cave.Cave(text=self.text, elf_attack=elf_attack)

        # 2. How many elves to we start with
        elf_count = len(self.cave.items['E'])
        if verbose:
            print('attack=%d, elves=%d' % (elf_attack, elf_count));

        # 3. Loop until an elf death or fighting is done
        rounds = 0
        while elf_count == len(self.cave.items['E']):
            if self.round():
                rounds += 1
                if verbose:
                    print('Elves survived round %d' % rounds);
            else:
                break

        # 4. Return True if no elves died
        if verbose:
            if elf_count == len(self.cave.items['E']):
                print('Fight ended after %d complete rounds' % rounds)
            else:
                print('An elf died in round %d' % rounds)
        return elf_count == len(self.cave.items['E'])

    def minimum_elf_attack(self, verbose=False, limit=99):
        # 1. Start at the lowest possible attack
        elf_attack = 4

        # 2. Loop until no elves have died
        while not self.no_casualities(elf_attack=elf_attack, verbose=verbose):

            # 3. Increase the attack level
            elf_attack += 1

            # 4. Stop if we reached the limit (if any)
            if limit > 0 and elf_attack > limit:
                print('Reached elf attack limit of %d' % limit)

        # 5. Return the elf attack value
        return elf_attack


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Determine the elf_attach value
        elf_attack = self.minimum_elf_attack(verbose=verbose, limit=limit)
        # 2. Reset the cave
        self.cave = cave.Cave(text=self.text, elf_attack=elf_attack)
        # 3. Fight until there is a victor
        rounds = self.fight(verbose=verbose)
        # 4. Get the surviving hit points
        hitpoints = self.hitpoints()
        # 5. Return the solution for part two
        return rounds*hitpoints

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        c o m b a t . p y                       end
# ======================================================================
