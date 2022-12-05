# ======================================================================
# Rucksack Reorganization
#   Advent of Code 2022 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s o l v e r . p y
# ======================================================================
"A solver for the Advent of Code 2022 Day 03 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import rucksack

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Solver
# ======================================================================


class Solver(object):   # pylint: disable=R0902, R0205
    "Object for Rucksack Reorganization"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rucksacks = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Loop for each line of the text
        for line in text:

            # 2. Create a rucksack
            sack = rucksack.Rucksack(line, self.part2)

            # 3. Add it to the pile
            self.rucksacks.append(sack)

    def total_prioirity(self):
        "Get the total priority of duplicate items"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all the rucksacks
        for sack in self.rucksacks:

            # 3. Get the priority of the duplicate items in this sack
            number = sack.priority(sack.both())

            # 4. Add that to the total
            result += number

        # 5. Return the grand total
        return result

    def get_badge_letters(self):
        "Get the badge letter for each three elf group"

        # 1. Start with nothing
        badges = []

        # 2. Loop for each three elf group
        for indx in range(0, len(self.rucksacks), 3):

            # 3. Get the common letter
            letter = self.rucksacks[indx].badge(self.rucksacks[indx + 1], self.rucksacks[indx + 2])

            # 4. Add the badge letter to the collection
            badges.append(letter)

        # 5. Return all the badges
        return ''.join(badges)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.total_prioirity()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return rucksack.Rucksack.priority(self.get_badge_letters())


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      s o l v e r . p y                     end
# ======================================================================
