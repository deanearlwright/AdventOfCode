# ======================================================================
# A Maze of Twisty Trampolines, All Alike
#   Advent of Code 2017 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                          j u m p s . p y
# ======================================================================
"A solver for Twisty Trampolines for Advent of Code 2017 Day 05"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Jumps
# ======================================================================


class Jumps(object):
    """Object representing a jump instruction solver"""

    def __init__(self, part2=False, text=None, location=0):

        # 1. Set the initial values
        self.part2 = part2
        if text is not None:
            self.offsets = [int(_) for _ in text]
        else:
            self.offsets = []
        self.location = location

    def escaped(self):
        "Returns True if escaped the maze"

        return self.location < 0 or self.location >= len(self.offsets)

    def one_jump(self, verbose=False):
        "Execute one jump for the current location"

        # 1. Return True if escaped already
        if self.escaped():
            return True

        # 2. Get the current jump offset
        offset = self.offsets[self.location]

        # 3. Compute new jump offset
        if self.part2 and offset >= 3:
            new_offset = self.offsets[self.location] - 1
        else:
            new_offset = self.offsets[self.location] + 1

        # 4. Advance the location pointer
        new_location = self.location + offset

        # 5. Report on the jump (if desired)
        if verbose:
            print("At location %d offset is %d (now %d) jumped to %d" %
                  (self.location, offset, new_offset, new_location))

        # 6. Set the new offset and location
        self.offsets[self.location] = new_offset
        self.location = new_location

        # 7. Return True if escaped
        return self.escaped()

    def goto_the_exit(self, verbose=False):
        "Return the number of steps necessary to reach the exit"

        # 1. Start at zero steps
        result = 0

        # 2. Loop until escaped
        while not self.escaped():

            # 3. Execute a single jump
            self.one_jump(verbose=verbose)

            # 4. Increment step counter
            result += 1

        # 5. Return the number of steps it took to escape
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          j u m p s . p y                       end
# ======================================================================
