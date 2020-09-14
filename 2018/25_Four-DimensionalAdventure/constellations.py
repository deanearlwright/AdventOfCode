# ======================================================================
# Four-Dimensional Adventure
#   Advent of Code 2018 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c o n s t e l l a t i o n s . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 25 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
CLOSE = 3
# ----------------------------------------------------------------------
#                                                      utility functions
# ----------------------------------------------------------------------
def distance(star1, star2):
    return sum([abs(s1 - s2) for s1,s2 in zip(star1,star2)])

def stars_are_close(star1, star2):
    return distance(star1, star2) <= CLOSE

def star_is_close_to_constellation(star, constellation):
    # 1. Loop for all the stars in the constellation
    for cstar in constellation:
        # 2. If the star is close, return True
        if stars_are_close(star, cstar):
            return True
    # 3. The star is not close to any star in the constellation, return False
    return False

def constellations_are_close(con1, con2):
    # 1. Loop for all of the stars in the first constellation
    for star in con1:
        # 2. Return True if the star it close to the other constellation
        if star_is_close_to_constellation(star, con2):
            return True
    # 3. None of the stars from the constellation are close to the others, return False
    return False


# ======================================================================
#                                                         Constellations
# ======================================================================


class Constellations(object):   # pylint: disable=R0902, R0205
    "Object for Four-Dimensional Adventure"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.points = []
        self.constellations = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.points.append([int(p) for p in line.split(',')])

    def form_constellations(self):
        # 1. Start with the constallations as individual stars
        self.constellations = [[points] for points in self.points]

        # 2. Loop until there are no changes
        prev_len = 0
        while prev_len != len(self.constellations):
            prev_len = len(self.constellations)
            # 3. Merge constellations (if possible)
            self.merge_constellations()

    def merge_constellations(self):
        compress = False
        for index1 in range(len(self.constellations)-1):
            for index2 in range(index1 +1, len(self.constellations)):
                if constellations_are_close(self.constellations[index1],
                                            self.constellations[index2]):
                    self.constellations[index1].extend(self.constellations[index2])
                    self.constellations[index2] = []
                    compress = True
        if compress:
            cons = []
            for con in self.constellations:
                if con:
                    cons.append(con)
            self.constellations = cons


    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Map the points into constellations
        self.form_constellations()
        # 1. Return the solution for part one
        return len(self.constellations)


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return None

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end               c o n s t e l l a t i o n s . p y                end
# ======================================================================
