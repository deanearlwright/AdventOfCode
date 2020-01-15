# ======================================================================
# Packet Scanners
#   Advent of Code 2017 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         f i r e w a l l . p y
# ======================================================================
"A solver for Packet Scanners for Advent of Code 2017 Day 13"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                Scanner
# ======================================================================


class Scanner(object):   # pylint: disable=R0902, R0205
    """Object for a multi-level firewall"""

    def __init__(self, level=0, depth=0, position=0, direction=1):

        # 1. Set the initial values
        self.level = level
        self.depth = depth
        self.position = position
        self.direction = direction
        self.cycle = (depth - 1) * 2

    def advance(self):
        "Advance the scanner one position"

        # 1. Advance the position of the scanner
        self.position += self.direction

        # 2. If position too low, correct and change direction
        if self.position < 0:
            self.position = 1
            self.direction = 1

        # 3. If position too high, correct and change direction
        if self.position >= self.depth:
            self.position = self.depth - 2
            self.direction = -1

    def reset(self):
        "Reset the scanner back to the top"

        self.position = 0
        self.direction = 1

# ======================================================================
#                                                               Firewall
# ======================================================================


class Firewall(object):   # pylint: disable=R0902, R0205
    """Object for a multi-level firewall"""

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.levels = {}
        self.final = 0
        self.picosecond = 0

        # 2. The there is text, add connections
        if text:
            for line in text:
                ints = [int(_) for _ in line.split(':')]
                self.levels[ints[0]] = Scanner(level=ints[0],
                                               depth=ints[1])

        # 3. Determine the final layer
        if self.levels:
            self.final = max(self.levels)

    def advance(self):
        "Advance all of the scanners in the firewall"

        # 1. loop for all of the scanners
        for scanner in self.levels.values():

            # 2. Advance the scanner at this level
            scanner.advance()

        # 3. 'Repent, Harlequin!' Said the Ticktockman
        self.picosecond += 1

    def trip(self, delay=0, verbose=False, limit=0):
        "Returns total severity of a packet trip stating immediately"

        # 1. Start with no captures
        captures = []

        # 2. Wait a little (or none at all) before starting
        for _ in range(delay):
            self.advance()

        # 3. Loop for all the levels
        for level in range(self.final+1):

            # 4. Is there a scanner for this level?
            if level in self.levels:

                # 5. Is the scanner here at position 0?
                if self.levels[level].position == 0:

                    # 6. The packet has been captured
                    if verbose:
                        print("Delay %d: Packet captured at level %d at time %d" %
                              (delay, level, self.picosecond))
                    captures.append(level)

                    # 7. A single capture is a failure for part 2
                    if self.part2:
                        return level + 1

            # 8. Advance all of the scanners
            self.advance()

        # 9. Return the severity of the captures (if any)
        return self.severity(captures)

    def severity(self, captures):
        "Determine the total severity of the packet captures"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the captures
        for level in captures:

            # 3. Severity is level number times depth
            result += level * self.levels[level].depth

        # 4. Return the total severity
        return result

    def reset(self):
        "Reset the firewall back to the start"

        # 1. Reset all the scanners
        for scanner in self.levels.values():
            scanner.reset()

        # 2. Lost time is never found again
        self.picosecond = 0

    def part_two_sim(self, verbose=False, limit=0):
        "Determine the mininimal delay to reach the end without getting caught"

        # 1. Start off small and work your way up
        result = 0

        # 2. Loop until we get it right
        while True:

            # 3. Try with this delay
            score = self.trip(delay=result, verbose=verbose)

            # 4. If successful, return delay time
            if score == 0:
                return result

            # 5. Have we tried too much
            if result > limit > 0:
                if verbose:
                    print("Stopped after %d attempts" % result)
                return None

            # 6. Start the firewall back at zero
            self.reset()

            # 7. And try a larger delay
            result += 1

    def part_two_mod(self, verbose=False, limit=0):
        "Determine the mininimal delay to reach the end without getting caught"

        # 1. Start off small and work your way up
        result = 0

        # 2. Loop until we get it right
        while True:
            captured = False

            # 3. Loop for all of the scanners
            for scanner in self.levels.values():

                # 4. See if we would be past this scanner
                if (result + scanner.level) % scanner.cycle != 0:
                    continue

                # 5. Try again with a longer delay
                if verbose:
                    print("delay %d failed at level %d, depth %s" %
                          (result, scanner.level, scanner.depth))
                captured = True
                break

            # 6. If successful, return delay time
            if not captured:
                return result

            # 7. Have we tried too much
            if result > limit > 0:
                if verbose:
                    print("Stopped after %d attempts" % result)
                return None

            # 8. And try a larger delay
            result += 1

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          p i p e s . p y                       end
# ======================================================================
