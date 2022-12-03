# ======================================================================
# Rock Paper Scissors
#   Advent of Code 2022 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s o l v e r . p y
# ======================================================================
"A solver for the Advent of Code 2022 Day 02 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
SCORE = {'A': {'X': 4, 'Y': 8, 'Z': 3},
         'B': {'X': 1, 'Y': 5, 'Z': 9},
         'C': {'X': 7, 'Y': 2, 'Z': 6},
         }
ACTION = {'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'},
          'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
          'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'},
          }

# ======================================================================
#                                                                 Solver
# ======================================================================


class Solver(object):   # pylint: disable=R0902, R0205
    "Object for Rock Paper Scissors"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.total = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Loop for all of the lines of text
        for line in text:

            # 2. Split the line
            elf, me = line.split(' ')

            # 2.5 For part two, we select the action
            if self.part2:
                me = self.action(elf, me)

            # 3. Get the score for this round
            round = self.score(elf, me)

            # 4. Add the store to the total
            self.total += round

    @staticmethod
    def score(elf, me):
        "Score a single contest"
        return SCORE[elf][me]

    @staticmethod
    def action(elf, me):
        "Choose the appropiate action a single contest"
        return ACTION[elf][me]

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.total

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.total


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      s o l v e r . p y                     end
# ======================================================================
