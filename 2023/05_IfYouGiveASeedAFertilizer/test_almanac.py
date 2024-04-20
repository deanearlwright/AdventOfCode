
# ======================================================================
# If You Give A Seed A Fertilizer
#   Advent of Code 2023 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ a l m a n a c . p y
# ======================================================================
"Test Almanac for Advent of Code 2023 day 05, If You Give A Seed A Fertilizer"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import almanac

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "seeds: 79 14 55 13",

    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",

    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",

    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",

    "water-to-light map:",
    "88 18 7",
    "18 25 70",

    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",

    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",

    "humidity-to-location map:",
    "60 56 37",
    "56 93 4",
]

# ======================================================================
#                                                            TestAlmanac
# ======================================================================


class TestAlmanac(unittest.TestCase):  # pylint: disable=R0904
    "Test Almanac object"

    def test_empty_init(self):
        "Test the default Almanac creation"

        # 1. Create default Almanac object
        myobj = almanac.Almanac()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.seeds), 0)
        self.assertEqual(len(myobj.mappings), 0)

    def test_text_init(self):
        "Test the Almanac object creation from text"

        # 1. Create Almanac object from text
        myobj = almanac.Almanac(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 26)
        self.assertEqual(len(myobj.seeds), 4)
        self.assertEqual(len(myobj.mappings), 7)

        # 3. Check methods
        self.assertEqual(myobj.seed_to_location(79), 82)
        self.assertEqual(myobj.seed_to_location(14), 43)
        self.assertEqual(myobj.seed_to_location(55), 86)
        self.assertEqual(myobj.seed_to_location(13), 35)

        self.assertEqual(myobj.seeds_to_min_location(), 35)

        self.assertEqual(myobj.mappings["humidity-to-location"].reverse_map(82), 78)
        self.assertEqual(myobj.mappings["temperature-to-humidity"].reverse_map(78), 78)
        self.assertEqual(myobj.mappings["light-to-temperature"].reverse_map(78), 74)
        self.assertEqual(myobj.mappings["water-to-light"].reverse_map(74), 81)
        self.assertEqual(myobj.mappings["fertilizer-to-water"].reverse_map(81), 81)
        self.assertEqual(myobj.mappings["soil-to-fertilizer"].reverse_map(81), 81)
        self.assertEqual(myobj.mappings["seed-to-soil"].reverse_map(81), 79)

        self.assertEqual(myobj.location_to_seed(82), 79)
        self.assertEqual(myobj.location_to_seed(43), 14)
        self.assertEqual(myobj.location_to_seed(86), 55)
        self.assertEqual(myobj.location_to_seed(35), 13)

        self.assertEqual(myobj.brute_force_part2(), 46)
        self.assertEqual(myobj.better_part2(), 46)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ a l m a n a c . p y                 end
# ======================================================================
