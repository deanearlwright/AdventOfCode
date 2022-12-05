# ======================================================================
# Camp Cleanup
#   Advent of Code 2022 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s o l v e r . p y
# ======================================================================
"A solver for the Advent of Code 2022 Day 04 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import elf

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Solver
# ======================================================================


class Solver(object):   # pylint: disable=R0902, R0205
    "Object for Camp Cleanup"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.pairs = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Loop for every line
        for line in text:

            # 2. Split the line
            parts = line.split(",")

            # 3. Create the elves
            elf0 = elf.Elf(part2=self.part2, text=parts[0])
            elf1 = elf.Elf(part2=self.part2, text=parts[1])

            # 4. Save the elves
            self.pairs.append((elf0, elf1))

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the pairs of elves
        for elves in self.pairs:

            # 3. Does either elf's assignment contain the others?
            if elves[0].contains(elves[1]) or elves[1].contains(elves[0]):

               # 4. Increment count of contained pairs
                result += 1

        # 5. Return the solution for part one
        return result

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the pairs of elves
        for elves in self.pairs:

            # 3. Does either elf's assignment overlap the others?
            if elves[0].overlaps(elves[1]) or elves[1].overlaps(elves[0]):

               # 4. Increment count of overlapped pairs
                result += 1

        # 5. Return the solution for part two
        return result


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      s o l v e r . p y                     end
# ======================================================================
