
# ======================================================================
# Resonant Collinearity
#   Advent of Code 2024 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                             m a p . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 08 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import itertools

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                    Map
# ======================================================================


class Map(object):   # pylint: disable=R0902, R0205
    "Object for Resonant Collinearity"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rows = 0
        self.cols = 0
        self.antennas = {}
        self.frequencies = {}
        self.antinodes = {}

        # 2. Process text (if any)
        if text is not None and len(self.text) > 0:
            self.map_antennas()
            self.map_frequencies()
            self.map_antinodes()

    def map_antennas(self):
        "Find the antennas"

        assert self.text is not None and len(self.text) > 0

        # 1. Get the size of things
        self.rows = len(self.text)
        self.cols = len(self.text[0])

        # 2. Loop for each row and column
        for row, line in enumerate(self.text):
            for col, char in enumerate(line):

                # 3. If it is an antenna, put it in the map
                if char.isalnum():
                    self.antennas[(row, col)] = char

    def map_frequencies(self):
        "Collect anntennas with the same freqency"

        # 1. Loop for all the antennas in the map
        for loc, kind in self.antennas.items():

            # 2. Collect like frequencies
            if kind in self.frequencies:
                self.frequencies[kind].append(loc)
            else:
                self.frequencies[kind] = [loc]

    def map_antinodes(self):
        "Determine the locations of the antenna antinotes"

        # 1. Loop for all freqencies
        for frequency, antennas in self.frequencies.items():

            # 2. Start with no antinodes
            antinodes = set()

            # 3. Loop for each pair of antennas
            for pair in itertools.combinations(antennas, 2):

                # 4. Determine the antinodes for this pair
                if self.part2:
                    paired = self.get_antinodes_for_pair_two(pair)
                else:
                    paired = self.get_antinodes_for_pair(pair)

                # 5. Add them to the set for this frequency
                for antinode in paired:
                    antinodes.add(antinode)

            # 6. Save the antinodes for this frequency
            self.antinodes[frequency] = antinodes

    def is_on_the_map(self, loc):
        "Is the location on the map"

        # 1. Check for too small
        if loc[0] < 0 or loc[1] < 0:
            return False

        # 2. Check for too big
        if loc[0] >= self.rows or loc[1] >= self.cols:
            return False

        # 3. If must be just right
        return True

    def get_antinodes_for_pair(self, pair):
        "Get the antinodes for this pair of antennas"

        # 1. Determine the delta row and column between the antennas
        delta0 = (pair[0][0] - pair[1][0], pair[0][1] - pair[1][1])
        delta1 = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])

        # 2. Determine the locations of the antinodes
        anode0 = (pair[0][0] + delta0[0], pair[0][1] + delta0[1])
        anode1 = (pair[1][0] + delta1[0], pair[1][1] + delta1[1])

        # 3. Return only the ones that are on the map
        result = []
        if self.is_on_the_map(anode0):
            result.append(anode0)
        if self.is_on_the_map(anode1):
            result.append(anode1)

        # 4. Return the antinodes that are on the map
        return result

    def get_antinodes_for_pair_two(self, pair):
        "Get the antinodes for this pair of antennas"

        # 1. Start with the antannas themselves
        result = [pair[0], pair[1]]

        # 2. Determine the delta row and column between the antennas
        delta0 = (pair[0][0] - pair[1][0], pair[0][1] - pair[1][1])
        delta1 = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])

        # 3. Determine the locations of the antinodes for delta0
        anode0 = (pair[0][0] + delta0[0], pair[0][1] + delta0[1])
        while self.is_on_the_map(anode0):
            result.append(anode0)
            anode0 = (anode0[0] + delta0[0], anode0[1] + delta0[1])

        # 3. Determine the locations of the antinodes for delta0
        anode1 = (pair[1][0] + delta1[0], pair[1][1] + delta1[1])
        while self.is_on_the_map(anode1):
            result.append(anode1)
            anode1 = (anode1[0] + delta1[0], anode1[1] + delta1[1])

        # 4. Return the antinodes that are on the map
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Start with nothing
        result = set()

        # 3. Loop for all the antinodes
        for antinodes in self.antinodes.values():

            # 4. Add them in
            result.update(antinodes)

        # 5. Return the solution for part one
        return len(result)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Start with nothing
        result = set()

        # 3. Loop for all the antinodes
        for antinodes in self.antinodes.values():

            # 4. Add them in
            result.update(antinodes)

        # 5. Return the solution for part twoone
        return len(result)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                           m a p . p y                          end
# ======================================================================
