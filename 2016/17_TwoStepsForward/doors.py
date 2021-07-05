# ======================================================================
# Two Steps Forward
#   Advent of Code 2016 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           d o o r s . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 17 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import hashlib

# ----------------------------------------------------------------------
#                                                         hash functions
# ----------------------------------------------------------------------


def md5_hash(value: str) -> str:
    "Return the md5 hash"
    m = hashlib.md5()
    m.update(bytes(value, 'utf8'))
    return m.hexdigest()


def is_vault(loc: tuple) -> bool:
    "Return true if at the Vault"
    return loc == VAULT


def is_unlocked(digit: str) -> bool:
    "Check is hex digit indicates unlocked or not"
    return digit in UNLOCKED


def unlocked(path: str) -> str:
    "Returned the unlocked doors"
    # 1. Get the hash of the path
    hashed = md5_hash(path)
    result = []
    for indx, value in enumerate(hashed[:4]):
        if is_unlocked(value):
            result.append(DOORS[indx])
    return ''.join(result)


def is_wall(loc: tuple, door: str) -> bool:
    "Returns true if there is a wall in that direction"
    if loc[0] == 0 and door == "L":
        return True
    if loc[0] == 3 and door == "R":
        return True
    if loc[1] == 0 and door == "U":
        return True
    if loc[1] == 3 and door == "D":
        return True
    return False


def exits(loc: tuple, path: str) -> str:
    "Returns the doors from the location along the path"
    doors = unlocked(path)
    result = []
    for door in doors:
        if not is_wall(loc, door):
            result.append(door)
    return ''.join(result)


def new_loc(loc: tuple, door: str) -> tuple:
    "Return the new location"
    delta = DELTA[door]
    return (loc[0] + delta[0], loc[1] + delta[1])


# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DELTA = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}
START = (0, 0)
VAULT = (3, 3)
UNLOCKED = "bcdef"
DOORS = "UDLR"

# ======================================================================
#                                                                  Doors
# ======================================================================


class Doors(object):   # pylint: disable=R0902, R0205
    "Object for Two Steps Forward"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.seed = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.seed = text[0]

    def shortest(self):
        "Return the shortest path to the vault"
        # 1. Initialization
        best = "X" * 999
        search = [(START, "", exits(START, self.seed))]
        # 2. Loop while there is somewhere to try
        while search:
            # 3. Where are we now?
            here, path, doors = search.pop()
            #  print(here, path, doors)
            # 4. is this taking too long
            if len(path) >= len(best):
                continue
            # 5. Get the next door to try
            door = doors[0]
            doors = doors[1:]
            # 6. If there are more doors to try here, save them for later
            if doors:
                search.append((here, path, doors))
            # 7. Advance to the next place
            there = new_loc(here, door)
            path += door
            # 8. Are we there yet?
            if there == VAULT:
                best = path
            else:
                doors = exits(there, self.seed + path)
                if doors:
                    search.append((there, path, doors))
        # 9. Return the best path
        return best

    def longest(self):
        "Return the shortest path to the vault"
        # 1. Initialization
        best = ""
        search = [(START, "", exits(START, self.seed))]
        # 2. Loop while there is somewhere to try
        while search:
            # 3. Where are we now?
            here, path, doors = search.pop()
            #  print(here, path, doors)
            # 4. Get the next door to try
            door = doors[0]
            doors = doors[1:]
            # 5. If there are more doors to try here, save them for later
            if doors:
                search.append((here, path, doors))
            # 6. Advance to the next place
            there = new_loc(here, door)
            path += door
            # 7. Are we there yet?
            if there == VAULT:
                if len(path) > len(best):
                    best = path
            else:
                doors = exits(there, self.seed + path)
                if doors:
                    search.append((there, path, doors))
        # 8. Return the length of the longest path
        return len(best)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.shortest()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.longest()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         d o o r s . p y                        end
# ======================================================================
