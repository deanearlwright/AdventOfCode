# ======================================================================
# Sonar Sweep
#   Advent of Code 2021 Day 01 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s o n a r . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 01 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Sonar
# ======================================================================


class Sonar(object):   # pylint: disable=R0902, R0205
    "Object for Sonar Sweep"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text

    def more_than_previous(self):
        "Return the more than previous count"

        # 1. Start with nothing
        result = 0
        previous = int(self.text[0])

        # 2. Loop for all the readings
        for reading in self.text:
            reading = int(reading)

            # 3. Check and increment if more
            if reading > previous:
                result += 1

            # 4. Save new previous
            previous = reading

        # 5. Return count
        return result

    def do_windows(self, window=3):
        "Like above but in chunks"

        # 1. Start with nothing
        result = 0
        previous = [int(x) for x in self.text[0:window]]

        # 2. Loop for all the readings
        for reading in self.text[window:]:
            reading = int(reading)

            # 3. Check and increment if more
            latest = previous[1:]
            latest.append(reading)
            #print(previous, reading, latest)
            if sum(latest) > sum(previous):
                result += 1

            # 4. Save new previous
            previous = latest

        # 5. Return count
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.more_than_previous()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.do_windows()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         s o n a r . p y                        end
# ======================================================================
