
# ======================================================================
# Cosmic Expansion
#   Advent of Code 2023 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         i m a g e . p y
# ======================================================================
"Image for the Advent of Code 2023 Day 11 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
SPACE = "."
GALAXY = "#"

# ======================================================================
#                                                                  Image
# ======================================================================


class Image(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Cosmic Expansion"

    def __init__(self, text=None, part2=False, expansion=None):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.expand_col = []
        self.expand_row = []
        self.galaxies = []
        self.expansion = expansion
        if expansion is None:
            self.expansion = 1000000 if part2 else 2

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 0. Precondition axions
        assert text is not None and len(text) > 0

        # 1. Find the expanded column numbers
        self.expand_col = [0]
        expanded = 0
        for indx in range(len(self.text[0])):
            if self.is_col_empty(indx):
                expanded += self.expansion
            else:
                expanded += 1
            self.expand_col.append(expanded)

        # 2. Find the expanded row numbers
        self.expand_row = [0]
        expanded = 0
        for indx in range(len(self.text[0])):
            if self.is_row_empty(indx):
                expanded += self.expansion
            else:
                expanded += 1
            self.expand_row.append(expanded)

        # 3. Get the expanded location of the qalaxies
        for rindx, row in enumerate(self.text):
            for cindx, square in enumerate(row):
                if square == GALAXY:
                    exp_loc = (self.expand_row[rindx], self.expand_col[cindx])
                    self.galaxies.append(exp_loc)

    def is_row_empty(self, indx):
        "Return True if there are no galaxies in this row"

        return GALAXY not in self.text[indx]

    def is_col_empty(self, indx):
        "Return True if there are no galaxies in this column"

        return all(row[indx] == SPACE for _, row in enumerate(self.text))

    @staticmethod
    def manhattan_distance(loc1, loc2):
        "Returns the manhattan (taxi cab) distance between two locations"
        return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

    def all_distances(self):
        "Returns the sum of all distances between pairs of galaxies"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all pairs of galixies
        for indx1, gal1 in enumerate(self.galaxies):
            for indx2, gal2 in enumerate(self.galaxies):
                if indx1 <= indx2:
                    continue

                # 3. Determine the distance between the pair
                dist = Image.manhattan_distance(gal1, gal2)

                # 4. Accumulate the distances
                result += dist

        # 5. Return the accumulated distances
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                         i m a g e . p y                        end
# ======================================================================
