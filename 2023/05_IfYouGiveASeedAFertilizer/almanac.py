
# ======================================================================
# If You Give A Seed A Fertilizer
#   Advent of Code 2023 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         a l m a n a c . p y
# ======================================================================
"Almanac for the Advent of Code 2023 Day 05 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from rangemap import Rangemap
from multirange import Multirange

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
MAPPINGS = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location"
]

SGNIPPAM = MAPPINGS[:]
SGNIPPAM.reverse()

# ----------------------------------------------------------------------
#                                                                utility
# ----------------------------------------------------------------------


def is_seed_in_ranges(seed, ranges):
    "Return True if this seed number is in a previous range"

    # 1. Loop for the ranges
    for a_range in ranges:
        range_beg = a_range[0]
        range_end = range_beg + a_range[1]

        # 2. Return True if seed in this range
        if range_beg <= seed < range_end:
            return True

    # 3. Seed not in any range
    return False

# ======================================================================
#                                                                Almanac
# ======================================================================


class Almanac(object):   # pylint: disable=R0902, R0903, R0205
    "Object for If You Give A Seed A Fertilizer"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.seeds = []
        self.mappings = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Start with no section
        map_name = "unknown"
        map_values = []

        # 2. Loop for all lines in the text
        for line in text:

            # 3. If seed line, save the seed numbers
            if line.startswith("seeds:"):
                self.seeds = [int(x) for x in line[6:].split()]
                continue

            # 4. If line contains a colon,
            #    save existing mapping (if any) and start new one
            if ":" in line:
                if len(map_values) > 0:
                    multi = Multirange(name=map_name,
                                       ranges=map_values, part2=self.part2)
                    self.mappings[map_name] = multi
                map_name = line.split()[0]
                map_values = []
                continue

            # 5. Add the mapping to the currently collected values
            map_values.append(Rangemap(text=line, part2=self.part2))

        # 6. Add the last mapping (if any)
        if len(map_values) > 0:
            multi = Multirange(name=map_name,
                               ranges=map_values, part2=self.part2)
            self.mappings[map_name] = multi

    def seed_to_location(self, number):
        "Return the location number for the seed"

        # 1. Loop for the mappings
        for map_name in MAPPINGS:

            # 2. Transform the number
            number = self.mappings[map_name].forward_map(number)

        # 3. Return the transformed number
        return number

    def seeds_to_min_location(self):
        "Return the minumum location for the seeds"

        # 1. Determine the minimum locations for the seeds
        locs = [self.seed_to_location(x) for x in self.seeds]

        # 2. Return the minumim location
        return min(locs)

    def brute_force_part2(self):
        "Return the lowest location using seed ranges"

        # 1. Start with a very high location locations
        result = 999999999
        seen = []

        # 2. Loop for the seed ranges
        for indx in range(0, len(self.seeds), 2):

            # 3. Loop for the seed number
            seed_beg = self.seeds[indx]
            seed_end = seed_beg + self.seeds[indx + 1]
            for seed in range(seed_beg, seed_end):

                # 4. Ignore if we have already tried this seed
                if is_seed_in_ranges(seed, seen):
                    continue

                # 5. Get the location for this seed
                loc = self.seed_to_location(seed)

                # 6. If this is a lower location, save it
                if loc < result:
                    result = loc

            # 7. Add this range to seen
            seen.append((seed_beg, seed_end))

        # 8. Return the lowest location
        return result

    def location_to_seed(self, number):
        "Return the seed number that would be at the given location"

        # 1. Loop for the mappings in reverse order
        for map_name in SGNIPPAM:

            # 2. Transform the number
            number = self.mappings[map_name].reverse_map(number)

        # 3. Return the transformed number
        return number

    def seed_in_range(self, seed):
        "Return True if seed is in one of the seed ranges"

        # 1. Loop for the seed ranges
        for indx in range(0, len(self.seeds), 2):

            # 2. Get the beginning and end of the range
            seed_beg = self.seeds[indx]
            seed_end = seed_beg + self.seeds[indx + 1]

            # 3. If the seed is in this range, return True
            if seed_beg <= seed < seed_end:
                return True

        # 4. This is a bad seed
        return False

    def better_part2(self):
        "Return the lowest location using seed ranges"

        # 1. Loop for possible locations
        for loc in range(1, 999999999):
            if loc % 10000 == 0:
                print(loc, flush=True)

            # 2. Get the seed that would be at that location
            seed = self.location_to_seed(loc)

            # 3. If it is a valid seed, return the location
            if self.seed_in_range(seed):
                return loc

        # 4. Sadly, we never found a good location
        return None

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                       a l m a n a c . p y                      end
# ======================================================================
