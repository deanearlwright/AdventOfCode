# ======================================================================
# Beverage Bandits
#   Advent of Code 2018 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p e r s o n . p y
# ======================================================================
"People and persons for the Advent of Code 2018 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
ROW_MULT = 100

ADJACENT = [-100, -1, 1, 100]

# ----------------------------------------------------------------------
#                                                               location
# ----------------------------------------------------------------------
def row_col_to_loc(row, col):
    return row * ROW_MULT + col

def loc_to_row_col(loc):
    return divmod(loc, ROW_MULT)

def distance(loc1, loc2):
    loc1row, loc1col = loc_to_row_col(loc1)
    loc2row, loc2col = loc_to_row_col(loc2)
    return abs(loc1row - loc2row) + abs(loc1col - loc2col)

def adjacent(loc1, loc2):
    return distance(loc1, loc2) == 1

# ======================================================================
#                                                                 Person
# ======================================================================


class Person(object):   # pylint: disable=R0902, R0205
    "Elf/Goblin for Beverage Bandits"

    def __init__(self, letter='#', location=0, attack=3):

        # 1. Set the initial values
        self.letter = letter
        self.location = location
        self.hitpoints = 200
        self.attack = attack

    def distance(self, location):
        return distance(self.location, location)

    def attacks(self, other):
        other.hitpoints = max(0, other.hitpoints - self.attack)

    def adjacent(self):
        return [self.location + a for a in ADJACENT]


# ======================================================================
#                                                                 People
# ======================================================================


class People(object):   # pylint: disable=R0902, R0205
    "Multiple Elf/Goblin for Beverage Bandits"

    def __init__(self, letter='#'):

        # 1. Set the initial values
        self.letter = letter
        self.persons = {}

    def __len__(self):
        return len(self.persons)

    def __getitem__(self, loc):
        if loc in self.persons:
            return self.persons[loc]
        else:
            raise AttributeError("No such location: %s" % loc)

    def __setitem__(self, loc, person):
        if self.letter != person.letter:
            raise ValueError("Incompatable letters: %s != %s" % (self.letter, person.letter))
        if loc != person.location:
            raise ValueError("Incompatable locations: %s != %s" % (loc, person.location))
        self.persons[loc] = person

    def __delitem__(self, loc):
        if loc in self.persons:
            del self.persons[loc]
        else:
            raise AttributeError("No such location: %s" % loc)

    def __iter__(self):
        return iter(self.persons)

    def __contains__(self, loc):
        return loc in self.persons

    def add(self, person):
        if self.letter != person.letter:
            raise ValueError("Incompatable letters: %s != %s" % (self.letter, person.letter))
        if person.location in self.persons:
            raise ValueError("Location %s already occuried" % (person.location))
        self.persons[person.location] = person

    def locations(self):
        keys = list(self.persons.keys())
        keys.sort()
        return keys

    def hitpoints(self):
        return sum([x.hitpoints for x in self.persons.values()])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        p e r s o n . p y                       end
# ======================================================================
