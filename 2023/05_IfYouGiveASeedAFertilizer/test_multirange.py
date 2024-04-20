
# ======================================================================
# IfYouGiveASeedAFertilizer
#   Advent of Code 2023 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ m u l t i r a n g e . p y
# ======================================================================
"Test Multirange for Advent of Code 2023 day 05, IfYouGiveASeedAFertilizer"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

from rangemap import Rangemap
import multirange

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_RANGES = [
    Rangemap(text="50 98 2"),
    Rangemap(text="52 50 48"),
]

# ======================================================================
#                                                         TestMultirange
# ======================================================================


class TestMultirange(unittest.TestCase):  # pylint: disable=R0904
    "Test Multirange object"

    def test_empty_init(self):
        "Test the default Multirange creation"

        # 1. Create default Multirange object
        myobj = multirange.Multirange()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.name, None)
        self.assertEqual(myobj.ranges, None)

    def test_text_init(self):
        "Test the Multirange object creation from text"

        # 1. Create Multirange object from text
        myobj = multirange.Multirange(name="seed-to-soil",
                                      ranges=EXAMPLE_RANGES)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.ranges), 2)
        self.assertEqual(myobj.name, "seed-to-soil")

        # 3. Check methods
        self.assertEqual(myobj.forward_map(79), 81)
        self.assertEqual(myobj.forward_map(14), 14)
        self.assertEqual(myobj.forward_map(55), 57)
        self.assertEqual(myobj.forward_map(13), 13)

        self.assertEqual(myobj.reverse_map(81), 79)
        self.assertEqual(myobj.reverse_map(14), 14)
        self.assertEqual(myobj.reverse_map(57), 55)
        self.assertEqual(myobj.reverse_map(13), 13)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------

if __name__ == '__main__':
    pass

# ======================================================================
# end               t e s t _ m u l t i r a n g e . p y              end
# ======================================================================
