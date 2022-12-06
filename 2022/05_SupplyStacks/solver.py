# ======================================================================
# Supply Stacks
#   Advent of Code 2022 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s o l v e r . p y
# ======================================================================
"A solver for the Advent of Code 2022 Day 05 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import crane

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Solver
# ======================================================================


class Solver(object):   # pylint: disable=R0902, R0205
    "Object for Supply Stacks"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.crane = None
        self.actions = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Create the crane with stacks of crates
        self.crane = crane.Crane(text=text, part2=self.part2)

        # 2. Save the actions
        for line in text:
            if not line.startswith("move"):
                continue
            self.actions.append(line)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0
        if not self.crane:
            return None

        # 1. Execute all the moves
        for move in self.actions:
            self.crane.move(move)

        # 2. Return the solution for part one
        return self.crane.tops()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0
        if not self.crane:
            return None

        # 1. Execute all the moves
        for move in self.actions:
            self.crane.move(move)

        # 2. Return the solution for part two
        return self.crane.tops()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        s o l v e r . p y                       end
# ======================================================================
