
# ======================================================================
# Linen Layout
#   Advent of Code 2024 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         t o w e l s . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 19 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import defaultdict

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Towels
# ======================================================================


class Towels(object):   # pylint: disable=R0902, R0205
    "Object for Linen Layout"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.available = defaultdict(set)
        self.designs = []
        self.remember = defaultdict(bool)
        if self.part2:
            self.remember = defaultdict(int)

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text()

    def _process_text(self):
        "Assign values from text"

        assert self.text is not None and len(self.text) > 0

        # 1. loop for each line in the file
        for line in self.text:

            # 2. If it contains a comma, then it is available patterns
            if ',' in line:

                # 3. Loop for the available patterns
                for pattern in line.split(", "):

                    # 4. Add the pattern to the available ones
                    self.available[pattern[0]].add(pattern)

            # 5. Else it is a design
            else:
                self.designs.append(line)

    def possible_start(self, design):
        "Return the patterns that can start this design"

        # 1. Start with nothing
        result = []

        # 2. Loop for the possible ones
        for pattern in self.available[design[0]]:

            # 3. Ignore if doesn't match enough
            if not design.startswith(pattern):
                continue

            # 4. Ignore if we can't match the next stripe
            if len(pattern) < len(design) and design[len(pattern)] not in self.available:
                continue

            # 5. Looks good, add to the result
            result.append(pattern)

        # 6. Return the possible starting patterns
        # print("SP:", design, result)
        return result

    def possible(self, design):
        "Returns true if it is possible to make this design"

        # 1. Empty designs are always possible
        if len(design) == 0:
            return True

        # 2. Have we seen this before?
        if design in self.remember:
            return self.remember[design]
        self.remember[design] = False

        # 3. Get the patterns that  can start this design
        patterns = self.possible_start(design)

        # 4. If there are no patterns that match the start, return False
        if len(patterns) == 0:
            return False

        # 4. Get the length of possible patterns
        lengths = set(len(pattern) for pattern in patterns)
        lengths = [x for x in lengths]
        lengths.sort(reverse=True)

        # 5. Loop for all of the lengths
        for length in lengths:

            # 6. And try to match the rest of the design
            if self.possible(design[length:]):
                self.remember[design] = True
                return True

        # 7. Return the number of designs for this pattern
        return False

    def ways(self, design):
        "Returns true if it is possible to make this design"

        # 1. Empty designs are always possible
        if len(design) == 0:
            return 1

        # 2. Have we seen this before?
        if design in self.remember:
            return self.remember[design]
        self.remember[design] = 0

        # 3. Get the patterns that  can start this design
        patterns = self.possible_start(design)

        # 4. If there are no patterns that match the start, return False
        if len(patterns) == 0:
            return 0

        # 4. Get the length of possible patterns
        lengths = set(len(pattern) for pattern in patterns)
        lengths = [x for x in lengths]
        lengths.sort(reverse=True)

        # 5. Loop for all of the lengths
        for length in lengths:

            # 6. And try to math the rest of the design
            self.remember[design] += self.ways(design[length:])

        # 7. Could not match this design
        return self.remember[design]

    def count_possible(self):
        "Return the number of possible designs"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all the designs
        for design in self.designs:

            # 3. If it can be made, increase the count
            if self.possible(design):
                result += 1
                # print(f"{result} of {len(self.designs)}")

        # 9. Return the count
        return result

    def count_ways(self):
        "Return the number of ways to implement the designs"

        # 1. Start with nothing
        result = 0
        self.remember = defaultdict(int)

        # 2. Loop for all the designs
        for design in self.designs:

            # 3. If it can be made, increase the count
            result += self.ways(design)

        # 4. Return the ways
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        return self.count_possible()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part two
        return self.count_ways()

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        t o w e l s . p y                       end
# ======================================================================
