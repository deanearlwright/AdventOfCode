# ======================================================================
# Beacon Scanner
#   Advent of Code 2021 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s c a n n e r s . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 19 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import scanner
# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
SCANNER_HEAD = '---'

# ======================================================================
#                                                               Scanners
# ======================================================================


class Scanners(object):   # pylint: disable=R0902, R0205
    "Object for Beacon Scanner"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.scnrs = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.process_text(text)

    def process_text(self, text):
        "Process the text building scanners"

        # 1. Start with the first line of text
        scanner_text = [text[0]]
        assert scanner_text[0].startswith(SCANNER_HEAD)

        # 2. Loop for the rest of the text
        for line in text[1:]:

            # 3. If this the start of a new scanner?
            if line.startswith(SCANNER_HEAD):

                # 4. Build a scanner and add it to the list
                scnr = scanner.Scanner(text=scanner_text, part2=self.part2)
                self.scnrs.append(scnr)

                # 5. Start a new scanner text
                scanner_text = [line]

            # 6. Not new scanner, add line to existing text
            else:
                scanner_text.append(line)

        # 7. One last scanner
        scnr = scanner.Scanner(text=scanner_text, part2=self.part2)
        self.scnrs.append(scnr)

    def all_beacons(self, verbose=False, limit=0):
        "Return coordinates of all of the beacons"

        # 1. The first scanner becomes the baseline
        self.scnrs[0].coordinates = (0, 0, 0)
        self.scnrs[0].adjusted = self.scnrs[0].bcns

        # 2. Start with only the first scanner's beacons
        total_beacons = self.scnrs[0].bcns.copy()
        unknown_scanners = set(range(1, len(self.scnrs)))

        # 3. Loop until we know all
        step = 0
        while len(unknown_scanners) > 0:
            step += 1
            if verbose:
                print("Step %d, %d beacons, %d unknown scanners" %
                      (step, len(total_beacons), len(unknown_scanners)))
            if limit and step > limit:
                print("Bailed at step", step)
                return total_beacons

            # 4. Look for matches
            beacons, scnr = self.find_matches(total_beacons, unknown_scanners)
            if scnr == 0:
                print("Unable to match %d scanners to %s known beacons" %
                      (len(unknown_scanners), len(total_beacons)))
                return total_beacons

            # 5. Add the beacons
            total_beacons |= beacons

            # 6. Remove the matched scanner
            if verbose:
                print("Scanner %d is at %s" % (scnr, self.scnrs[scnr].coordinates))
            unknown_scanners.remove(scnr)

        # 7. Return all the beacons (relative to scanner 0)
        return total_beacons

    def find_matches(self, total_beacons, unknown_scanners):
        "Find a scanner that matched the known beacons"

        # 0. Precondition axioms
        assert len(total_beacons) > 0
        assert len(unknown_scanners) > 0

        # 1. Loop for all the unknown scanners
        for unknown_index in unknown_scanners:
            unknown_scanner = self.scnrs[unknown_index]
            assert unknown_scanner.number != 0

            # 2. Try to match this scanner
            beacons = unknown_scanner.find_matches(total_beacons)

            # 3. Did we get a match?
            if len(beacons) > 0:
                return beacons, unknown_index

        # 4. Didn't find a match -- This shouldn't happen
        return set(), 0

    def greatest_distance(self):
        "Return the greatest distance between scanners"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the sensors
        for scanner_one in self.scnrs:

            # 3. And for all of the others
            for scanner_two in self.scnrs:

                # 4. Computer the distance between the scanners
                distance = scanner_one.manhattan_distance(scanner_two)

                # 5. Keep the greatest one
                if distance > result:
                    result = distance

        # 6. Return the greatest distance between scanners
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return len(self.all_beacons(verbose=verbose, limit=limit))

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        self.all_beacons(verbose=verbose, limit=limit)
        return self.greatest_distance()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      s c a n n e r s . p y                     end
# ======================================================================
