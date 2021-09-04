# ======================================================================
# Aunt Sue
#   Advent of Code 2015 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d e t e c t i v e . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import aoc_16
import aunt
import mfcsam

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
MFCSAM_TEXT = """
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
"""
# ======================================================================
#                                                              Detective
# ======================================================================


class Detective(object):   # pylint: disable=R0902, R0205
    "Object for Aunt Sue"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.csi = mfcsam.Mfcsam(text=aoc_16.from_text(MFCSAM_TEXT), part2=self.part2)
        self.aunts = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                new_aunt = aunt.Aunt(text=line, part2=self.part2)
                self.aunts[new_aunt.number] = new_aunt

    def find_aunt(self):
        "Find the aunt that matches the criteria"

        # 1. Start with nothing
        result = None

        # 2. Loop for all the aunts
        for an_aunt in self.aunts.values():

            # 3. Is this the one? If so, return the number
            if self.csi.is_complete_match(an_aunt.attributes):
                return an_aunt.number

        # 4. Well that was a waste of time
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.find_aunt()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.find_aunt()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     d e t e c t i v e . p y                    end
# ======================================================================
