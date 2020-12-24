# ======================================================================
# Password Philosophy
#   Advent of Code 2020 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p a s s w o r d s . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 02 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import policy

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                              Passwords
# ======================================================================


class Passwords(object):   # pylint: disable=R0902, R0205
    "Object for Password Philosophy"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.policies = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.policies.append(policy.Policy(text=line))

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the policies
        for pol in self.policies:

            # 3. Count the good passwords according to the policy
            if pol.is_valid():
                result += 1

        # 4. Return the solution for part one
        return result

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the policies
        for pol in self.policies:

            # 3. Count the good passwords according to the policy
            if pol.is_valid2():
                result += 1

        # 4. Return the solution for part two
        return result


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     p a s s w o r d s . p y                    end
# ======================================================================
