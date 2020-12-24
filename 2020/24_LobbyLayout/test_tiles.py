# ======================================================================
# Lobby Layout
#   Advent of Code 2020 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        t e s t _ t i l e s . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 24, Lobby Layout"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_24
import tiles

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 10
PART_TWO_RESULT = 2208

# ======================================================================
#                                                              TestTiles
# ======================================================================


class TestTiles(unittest.TestCase):  # pylint: disable=R0904
    "Test Tiles object"

    def test_empty_init(self):
        "Test the default Tiles creation"

        # 1. Create default Tiles object
        myobj = tiles.Tiles()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Tiles object creation from text"

        # 1. Create Tiles object from text
        myobj = tiles.Tiles(text=aoc_24.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 20)
        self.assertEqual(len(myobj.tiles), 15)

        # 3. Test methods
        self.assertEqual(myobj.count_black(), 10)
        myobj.one_day()
        self.assertEqual(myobj.count_black(), 15)
        myobj.one_day()
        self.assertEqual(myobj.count_black(), 12)
        myobj.one_day()
        self.assertEqual(myobj.count_black(), 25)
        myobj.one_day()
        self.assertEqual(myobj.count_black(), 14)
        myobj.one_day()
        self.assertEqual(myobj.count_black(), 23)
        myobj.one_day()
        self.assertEqual(myobj.count_black(), 28)
        myobj.one_day()
        self.assertEqual(myobj.count_black(), 41)
        myobj.one_day()
        self.assertEqual(myobj.count_black(), 37)
        myobj.one_day()
        self.assertEqual(myobj.count_black(), 49)
        myobj.one_day()
        self.assertEqual(myobj.count_black(), 37)

    def test_part_one(self):
        "Test part one example of Tiles object"

        # 1. Create Tiles object from text
        myobj = tiles.Tiles(text=aoc_24.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Tiles object"

        # 1. Create Tiles object from text
        myobj = tiles.Tiles(part2=True, text=aoc_24.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ t i l e s . p y                  end
# ======================================================================
