# ======================================================================
# Rope Bridge
#   Advent of Code 2022 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s o l v e r . p y
# ======================================================================
"A solver for the Advent of Code 2022 Day 09 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import rope
# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Solver
# ======================================================================


class Solver(object):   # pylint: disable=R0902, R0205
    "Object for Rope Bridge"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rope = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            length = 2
            if self.part2:
                length = 10
            self.rope = rope.Rope(length=length)

    def move_rope(self):
        "Move the rope according to the instructions"

        # 1. Make sure we have a rope
        if not self.rope:
            return None

        # 2. Loop for all of the line of text
        for line in self.text:

            # 3. Move the head of the rope
            self.rope.move_head(line)

        # 4. Return the number of places visited
        return self.rope.tail_visited()

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.move_rope()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.move_rope()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        s o l v e r . p y                       end
# ======================================================================
