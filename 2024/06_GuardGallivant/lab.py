
# ======================================================================
# Guard Gallivant
#   Advent of Code 2024 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         L a b . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 06 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import guard

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                    Lab
# ======================================================================


class Lab(object):   # pylint: disable=R0902, R0205
    "Object for Guard Gallivant"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.obstructions = []
        self.rows = 0
        self.cols = 0
        self.guard = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Set the maximum rows and columns
        self.rows = len(self.text)
        self.cols = len(self.text[0])

        # 2. Loop for all of the lines of text
        for row, line in enumerate(text):

            # 3. Loop for all of the characters in the line
            for col, char in enumerate(line):

                # 4. If this is an obstruction, remember it
                if char == "#":
                    self.obstructions.append((row, col))
                    continue

                # 5. If this is not a space, it must be the guard
                if char != ".":
                    assert self.guard is None
                    self.guard = guard.Guard(char, (row, col), (self.rows, self.cols))

        # 6. Change the list of obstructions into a frozenset for faster access
        self.obstructions = frozenset(self.obstructions)

    def guard_tour(self):
        "Walk the guard around the lab and return the unique locations"

        # 1. If no guard, no steps
        if self.guard is None:
            return None

        # 2. Walk the guard and return the unique locations
        return self.guard.multiple_steps(self.obstructions)

    def guard_loop(self, new_obstruction):
        "Does the guard loop with the new_obstruction"

        # 1. Add the new obstrution to the existing one
        new_obstructions = set(self.obstructions)
        new_obstructions.add(new_obstruction)
        new_obstructions = frozenset(new_obstructions)

        # 2. Restart the guard
        self.guard.reset()

        # 3. Does the guard loop?
        return self.guard.loop_steps(new_obstructions)

    def place_obstructions(self):
        "Determine how many new obstructions can be placed"

        # 1. Start with nothing
        result = 0

        # 2. Get possible locations for the new obstructions
        self.guard.reset()
        possible = self.guard_tour()
        self.guard.reset()

        # 3. Loop for all the possible locations
        for loc in possible:

            # 4. It can't be in the guard's starting location
            if loc == self.guard.loc:
                continue

            # 4. Try it out
            result += self.guard_loop(loc)

        # 6. Return the number of new obstructions that can be placed
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return len(self.guard_tour())

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        if not self.text:
            return None
        return self.place_obstructions()

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                           l a b . p y                          end
# ======================================================================
