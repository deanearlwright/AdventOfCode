# ======================================================================
# Medicine for Rudolph
#   Advent of Code 2015 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         m e d i c i n e . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 19 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                               Medicine
# ======================================================================


class Medicine(object):   # pylint: disable=R0902, R0205
    "Object for Medicine for Rudolph"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.transformations = []
        self.calibrate = ''

        # 2. Process text (if any)
        if self.text and len(self.text) > 0:
            for line in self.text:
                if '=>' in line:
                    parts = line.split(' ')
                    self.transformations.append((parts[0], parts[2]))
                else:
                    self.calibrate = line

    def expand(self, starter):
        "Returns all molecules that can be made by making one substitution"

        # 1. Start with nothing
        result = set()

        # 2. Loop for every transition
        for transform in self.transformations:

            # 3. Get the before and after parts
            before, after = transform

            # 4. Loop for all of the places "before" appears in the starter
            start = 0
            found = starter.find(before, start)
            while found >= 0:

                # 5. Add the generated string to the result
                result.add(''.join([starter[0:found], after, starter[found + len(before):]]))

                # 6. Advance to the next position (if any)
                start = found + 1
                found = starter.find(before, start)

        # 7. Return the expanded strings
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return len(self.expand(self.calibrate))

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return None


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      m e d i c i n e . p y                     end
# ======================================================================
