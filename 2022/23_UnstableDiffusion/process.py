
# ======================================================================
# Unstable Diffusion
#   Advent of Code 2022 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p r o c e s s . p y
# ======================================================================
"Process for the Advent of Code 2022 Day 23 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple
from collections import deque
from collections import Counter

import grove

# ----------------------------------------------------------------------
#                                                                 tuples
# ----------------------------------------------------------------------
Loc = namedtuple('Loc', 'col, row')

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
NORTH = Loc(col=0, row=-1)
SOUTH = Loc(col=0, row=1)
EAST = Loc(col=1, row=0)
WEST = Loc(col=-1, row=0)
NORTH_WEST = Loc(col=-1, row=-1)
NORTH_EAST = Loc(col=1, row=-1)
SOUTH_WEST = Loc(col=-1, row=1)
SOUTH_EAST = Loc(col=1, row=1)

ALL = [
    NORTH, SOUTH, EAST, WEST,
    NORTH_WEST, NORTH_EAST,
    SOUTH_WEST, SOUTH_EAST,
]

MOVES = {
    'N': NORTH,
    'S': SOUTH,
    'E': EAST,
    'W': WEST,
}

LOOK = {
    'N': [NORTH_WEST, NORTH, NORTH_EAST],
    'S': [SOUTH_WEST, SOUTH, SOUTH_EAST],
    'E': [NORTH_EAST, EAST, SOUTH_EAST],
    'W': [NORTH_WEST, WEST, SOUTH_WEST],
}

RULES = ['N', 'S', 'W', 'E']

STAY = Loc(col=0, row=0)

# ======================================================================
#                                                                Process
# ======================================================================


class Process(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Unstable Diffusion"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.grove = None
        self.rules = deque(RULES)

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.grove = grove.Grove(text=text, part2=part2)

    def one_round(self):
        "Conduct one round of elf considering/movement process"

        # 1. Conduct the considering phase
        # print(self.rules)
        self.considering()

        # 2. Conduct the movement phase
        moved = self.movement()

        # 3. Set up rules for the next_round
        self.next_rule()

        # 4. Return number of moved elves
        return moved

    def considering(self):
        "Conduct the elf considering part of a round"

        # 1. Loop for all of the elves
        for elf in self.grove.elves:

            # 2. Each elf makes an individual decision
            goes = self.elf_considers(elf)

            # 3. Save the elf's decision
            self.grove.set_next(elf, goes)

    def elf_considers(self, elf):
        "The deliberations of a single elf"

        # 1. If there are no other elfs nearby, this elf stays put
        if self.grove.is_clear(elf, ALL):
            return STAY

        # 2. The elf considers the rules in order
        for rule in self.rules:

            # 3. If the way is clear, move that way!
            if self.grove.is_clear(elf, LOOK[rule]):
                return MOVES[rule]

        # 4. All ways blocked, stay where you are
        return STAY

    def movement(self):
        "Conduct the elf movement part of a round"

        # 1. Get all of the proposed new locations
        proposed = self.grove.elves.values()
        # print(proposed)

        # 2. How many elves what to move to each space
        cntr = Counter(proposed)

        # 3. Find the conflicts (2 or more elfs want to go to same place)
        conflicts = set()
        for loc, knt in cntr.items():
            if knt > 1:
                conflicts.add(loc)

        # 4. Start with no moved elves
        moved = 0
        moved_elves = {}

        # 5. Loop for all of the elves
        for elf, new_loc in self.grove.elves.items():

            # 6. If this elf was to go to a non-confliced space, do it
            if new_loc not in conflicts:
                moved_elves[new_loc] = None
                if elf != new_loc:
                    moved += 1

            # 7. Else elf stays where they are
            else:
                moved_elves[elf] = None

        # 8. Set the new elf locations
        self.grove.elves = moved_elves
        # print(self.grove.elves)
        # print(self.grove)

        # 9. Return the number of moved elves
        return moved

    def next_rule(self):
        "Determine the rule to use in this round"

        # 1. Get the rule for this round
        result = self.rules[0]

        # 2. Set up for the next round
        self.rules.rotate(-1)

        # 3. Return the rule for this round
        return result

    def rounds(self, limit=10):
        "Do several rounds and return the number of empty ground tiles"

        # 1. Do the specified number of rounds
        for number in range(limit):

            # 2. Execute a single round
            moved = self.one_round()

            # 3. If no elf moved, we are done
            if moved == 0:
                break
            print(number, moved)

        # 4. Return the number of empty ground tiles
        return self.grove.empty_ground_tiles()

    def until_still(self, limit=10000):
        "Do several rounds and return the number of empty ground tiles"

        # 1. Loop until no elves move
        for number in range(limit):

            # 2. Execute a single round
            moved = self.one_round()

            # 3. If no elf moved, we are done
            if moved == 0:
                return 1 + number
            print(number, moved)

        # 4. Return the number of empty ground tiles
        return None

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                       p r o c e s s . p y                      end
# ======================================================================
