# ======================================================================
# Disk Defragmentation
#   Advent of Code 2017 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                     t e s t _ d e f r a g . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 14, Disk Defragmentation"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import knots
import defrag
import aoc_14

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

EXAMPLE_HASH_KNOT_BITS = """
##.#.#..-->
.#.#.#.#
....#.#.
#.#.##.#
.##.#...
##..#..#
.#...#..
##.#.##.-->
|      |
V      V
"""

EXAMPLE_HASH_KNOT_KEY = 'flqrgnkx'

EXAMPLE_HASH_KNOT_HEX = {'0': '....',
                         '1': '...#',
                         '2': '..#.',
                         '3': '..##',
                         '4': '.#..',
                         '5': '.#.#',
                         '6': '.##.',
                         '7': '.###',
                         '8': '#...',
                         '9': '#..#',
                         'a': '#.#.',
                         'b': '#.##',
                         'c': '##..',
                         'd': '##.#',
                         'e': '###.',
                         'f': '####',
                         }

EXAMPLE_TOTAL_BITS = 8108

EXAMPLE_TOTAL_REGIONS = 1242

# ======================================================================
#                                                               TestKnot
# ======================================================================


class TestHashKnot(unittest.TestCase):  # pylint: disable=R0904
    """Test Hash Knot for Disk Defragmenter object"""

    def test_part_one_example_bits(self):
        """Test Disk Hash Knot bits from example"""

        # 1. Loop for the eight lines of the example
        for lnum, line in enumerate(aoc_14.from_text(EXAMPLE_HASH_KNOT_BITS)):
            if line[0] == '|' or line[0] == 'V':
                continue

            # 2. Create the knot object
            myknot = knots.Knots(length=256, part2=True)

            # 3. Generate the hash key
            hash_key = EXAMPLE_HASH_KNOT_KEY + '-%d' % lnum

            # 4. Get the dense hash
            dense_hash = myknot.process_knots(text=hash_key, verbose=False)

            # 5. Convert the first two digits to bits
            hash_bits = EXAMPLE_HASH_KNOT_HEX[dense_hash[0]] + \
                EXAMPLE_HASH_KNOT_HEX[dense_hash[1]]

            # 6. Compare with example
            self.assertEqual(hash_bits, line[0:8])


# ======================================================================
#                                                             TestDefrag
# ======================================================================


class TestDefrag(unittest.TestCase):  # pylint: disable=R0904
    """Test Firewall object"""

    def test_empty_init(self):
        """Test the default disk deframenter creation"""

        # 1. Create default disk deframenter object
        mydefrag = defrag.Defrag()

        # 2. Make sure it has the default values
        self.assertEqual(mydefrag.part2, False)
        self.assertEqual(mydefrag.text, None)
        self.assertEqual(mydefrag.size, 128)
        self.assertEqual(len(mydefrag.bits), 128)
        self.assertEqual(mydefrag.region, None)

    def test_part_one_example_count(self):
        """Test Disk Hash Knot count of bits from example"""

        # 1. Create the knot object
        mydefrag = defrag.Defrag(text=EXAMPLE_HASH_KNOT_KEY)

        # 2. Check the total count of bits
        self.assertEqual(mydefrag.part_one(verbose=False),
                         EXAMPLE_TOTAL_BITS)

    def test_part_two_example_regions(self):
        """Test Disk Hash Knot count of regions from example"""

        # 1. Create the knot object
        mydefrag = defrag.Defrag(text=EXAMPLE_HASH_KNOT_KEY,
                                 part2=True)

        # 2. Check the total count of bits
        self.assertEqual(mydefrag.part_two(verbose=False),
                         EXAMPLE_TOTAL_REGIONS)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ d e f r a g . p y                  end
# ======================================================================
