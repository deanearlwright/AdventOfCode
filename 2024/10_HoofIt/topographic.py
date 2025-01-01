
# ======================================================================
# Hoof It
#   Advent of Code 2024 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         t o p o g r a p h i c . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 10 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]
HEAD_CHAR = "0"
IMPASSIBLE = "."
HEAD = 0
PEAK = 9

# ======================================================================
#                                                            Topographic
# ======================================================================


class Topographic(object):   # pylint: disable=R0902, R0205
    "Object for Hoof It"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.heights = {}
        self.trailheads = {}
        self.ratings = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text()

    def _process_text(self):
        "Assign values from text"

        assert self.text is not None and len(self.text) > 0

        # 1. Loop for all rows and columns of the text
        for row, line in enumerate(self.text):
            for col, char in enumerate(line):

                # 2. Save the height at this location
                if char != IMPASSIBLE:
                    height = int(char)
                    self.heights[(row, col)] = height

                # 3. If at a trailhead, save it
                if char == HEAD_CHAR:
                    self.trailheads[(row, col)] = set()
                    self.ratings[(row, col)] = 0

    def next_locations(self, location):
        "Get the next possible locations"

        # 1. Start with nothing
        result = []

        # 2. Determine the height of the next location
        next_height = self.heights[location] + 1
        assert HEAD < next_height <= PEAK

        # 3. Loop for the possible next directions
        for delta in DELTA:

            # 4. Get the new location
            new_loc = (location[0] + delta[0], location[1] + delta[1])

            # 5. Is this a valid possible location
            if new_loc not in self.heights:
                continue
            if next_height != self.heights[new_loc]:
                continue

            # 6. Save this possible location
            result.append(new_loc)

        # 7. Return the new possible locations
        return result

    def determine_trailhead_score_from_here(self, trailhead, location):
        "Determine the score for this trailhead from this location"

        # 1. Determine the possilbe new locations
        new_locs = self.next_locations(location)
        # if trailhead == (0, 2):
        #    print(trailhead, new_locs)

        # 2. Loop for all of the new locations
        for new_loc in new_locs:

            # 3. Have we reached a peak, record it
            if self.heights[new_loc] == PEAK:
                self.trailheads[trailhead].add(new_loc)
                self.ratings[trailhead] += 1
                # print("Updating trailhead", trailhead, len(self.trailheads[trailhead]))
                continue

            # 4. Explore from here
            self.determine_trailhead_score_from_here(trailhead, new_loc)

    def determine_trailhead_scores(self):
        "Determine the score for each trailhead"

        # 1. Loop for each of the trailheads
        for start in self.trailheads:
            # print("Starting at", start)

            # 2. Determine the score for this trailhead
            self.determine_trailhead_score_from_here(start, start)

    def sum_trailhead_scores(self):
        "Return the sum the trailhead scores"

        return sum([len(x) for x in self.trailheads.values()])

    def sum_trailhead_ratings(self):
        "Return the sum the trailhead ratings"

        return sum(self.ratings.values())

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        self.determine_trailhead_scores()
        return self.sum_trailhead_scores()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        self.determine_trailhead_scores()
        return self.sum_trailhead_ratings()

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    t o p o g r a p h i c . p y                 end
# ======================================================================
