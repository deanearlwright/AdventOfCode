
# ======================================================================
# Hot Springs
#   Advent of Code 2023 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s p r i n g r o w . p y
# ======================================================================
"Springrow for the Advent of Code 2023 Day 12 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple

# ----------------------------------------------------------------------
#                                                                  types
# ----------------------------------------------------------------------
Row = namedtuple("Row", "spr, knt")
# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
SPRING = "."
DAMAGED = "#"
UNKNOWN = "?"
DU = set([DAMAGED, UNKNOWN])
SU = set([SPRING, UNKNOWN])

INITIAL_SEEN = {
    Row(spr="#", knt=tuple([1])): 1,
    Row(spr="?", knt=tuple([1])): 1,
    Row(spr="#.", knt=tuple([1])): 1,
    Row(spr=".#", knt=tuple([1])): 1,
    Row(spr="##", knt=tuple([2])): 1,
    Row(spr="?.", knt=tuple([1])): 1,
    Row(spr="?#", knt=tuple([1])): 1,
    Row(spr="?#", knt=tuple([2])): 1,
    Row(spr=".?", knt=tuple([1])): 1,
    Row(spr="#?", knt=tuple([1])): 1,
    Row(spr="#?", knt=tuple([2])): 1,
    Row(spr="??", knt=tuple([1])): 2,
    Row(spr="??", knt=tuple([2])): 1,
    Row(spr="???", knt=tuple([1])): 3,
    Row(spr="???", knt=tuple([1,1])): 1,
    Row(spr="???", knt=tuple([2])): 2,
    Row(spr="???", knt=tuple([3])): 1,
}

# ======================================================================
#                                                              Springrow
# ======================================================================


class Springrow(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Hot Springs"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.individuals = ""
        self.groups = None
        self.seen = INITIAL_SEEN

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 0. Precondition axiom
        assert text is not None and len(text) > 0

        # 1. Split into individual and group information
        self.individuals, groups = text.split()

        # 2. Save goups as integers
        self.groups = tuple(int(g) for g in groups.split(','))

    def arrangements(self, row=None):
        "Return the number of possible arrangements"

        # 1. If no input is given, use the current contents
        if row is None:

            # 1a. Part 1 has a single copy of the information
            if not self.part2:
                return self.arrangements(Row(spr=self.individuals + SPRING,
                                             knt=self.groups))

            # 1b. But part2 has five times the number of individuals and groups
            return self.arrangements(Row(spr="?".join([self.individuals] * 5) + SPRING,
                                         knt=self.groups * 5))

        # 2. If we have seen this row before, return the stock answer
        if row in self.seen:
            return self.seen[row]

        # 3. Recursive base cases
        if len(row.knt) == 0:
            return 0 if DAMAGED in row.spr else 1
        if len(row.spr) == 0:
            return 0

        # 4. Start with nothing
        result = 0

        # 5. Handle good or unknown
        if row.spr[0] in SU:
            result += self.arrangements(Row(spr=row.spr[1:], knt=row.knt))

        # 6. Handle damaged or unknown
        if row.spr[0] in DU:
            if (row.knt[0] <= len(row.spr)
                and SPRING not in row.spr[:row.knt[0]]
                and (row.knt[0] == len(row.spr) or row.spr[row.knt[0]] != DAMAGED)
                ):
                result += self.arrangements(Row(spr=row.spr[1+row.knt[0]:], knt=row.knt[1:]))

        # 7. Save and return result
        self.seen[row] = result
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     s p r i n g r o w . p y                    end
# ======================================================================
