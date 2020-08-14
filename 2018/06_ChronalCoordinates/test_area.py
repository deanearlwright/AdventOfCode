# ======================================================================
# Chronal Coordinates
#   Advent of Code 2018 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ a r e a . p y
# ======================================================================
"Test solver for Advent of Code 2018 day 06, Chronal Coordinates"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_06
import area

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 17
PART_TWO_RESULT = 16

# ======================================================================
#                                                               TestArea
# ======================================================================


class TestArea(unittest.TestCase):  # pylint: disable=R0904
    "Test Area object"

    def test_empty_init(self):
        "Test the default Area creation"

        # 1. Create default Area object
        myobj = area.Area()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.coords), 0)
        self.assertEqual(len(myobj.closest), 0)
        self.assertEqual(myobj.maxX, 0)
        self.assertEqual(myobj.maxY, 0)
        self.assertEqual(myobj.total, 10000)
        self.assertEqual(len(myobj.distances), 0)
        self.assertEqual(myobj.distCoord, None)


    def test_text_init(self):
        "Test the Area object creation from text"

        # 1. Create Area object from text
        myobj = area.Area(text=aoc_06.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(len(myobj.coords), 6)
        self.assertTrue(len(myobj.closest) > 0)
        self.assertEqual(myobj.coords[0].x, 1)
        self.assertEqual(myobj.coords[0].y, 1)
        self.assertEqual(myobj.coords[5].x, 8)
        self.assertEqual(myobj.coords[5].y, 9)
        self.assertEqual(myobj.maxX, 8)
        self.assertEqual(myobj.maxY, 9)
        self.assertEqual(myobj.total, 10000)
        self.assertEqual(len(myobj.distances), 0)
        self.assertEqual(myobj.distCoord, None)

        # 3. Test the nearest method
        self.assertEqual(myobj.nearest(0, 0), myobj.coords[0])
        self.assertEqual(myobj.nearest(1, 1), myobj.coords[0])
        self.assertEqual(myobj.nearest(2, 2), myobj.coords[0])
        self.assertEqual(myobj.nearest(3, 3), myobj.coords[3])
        self.assertEqual(myobj.nearest(4, 4), myobj.coords[3])
        self.assertEqual(myobj.nearest(5, 5), myobj.coords[4])
        self.assertEqual(myobj.nearest(6, 6), myobj.coords[4])
        self.assertEqual(myobj.nearest(7, 7), myobj.coords[5])
        self.assertEqual(myobj.nearest(8, 8), myobj.coords[5])
        self.assertEqual(myobj.nearest(9, 9), myobj.coords[5])
        self.assertEqual(myobj.nearest(0, 9), myobj.coords[1])
        self.assertEqual(myobj.nearest(9, 0), myobj.coords[2])
        self.assertEqual(myobj.nearest(5, 1), None)
        self.assertEqual(myobj.nearest(3, 6), None)
        self.assertTrue(len(myobj.closest) > 0)

        # 4. Test infinite or finiate
        self.assertEqual(myobj.coords[0].minX, 0)
        self.assertEqual(myobj.coords[0].minY, 0)
        self.assertEqual(myobj.coords[0].maxX, 4)
        self.assertEqual(myobj.coords[0].maxY, 3)
        self.assertEqual(myobj.coords[0].isInfinite, True)
        self.assertEqual(myobj.coords[1].isInfinite, True)
        self.assertEqual(myobj.coords[2].isInfinite, True)
        self.assertEqual(myobj.coords[3].isInfinite, False)
        self.assertEqual(myobj.coords[4].isInfinite, False)
        self.assertEqual(myobj.coords[5].isInfinite, True)

        # 5. Test area
        self.assertEqual(myobj.coords[3].area, 12)
        self.assertEqual(myobj.coords[4].area, 28)
        self.assertEqual(myobj.coords[3].closest, 9)
        self.assertEqual(myobj.coords[4].closest, 17)

    def test_part2_init(self):
        "Test the Area object creation from text for part2"

        # 1. Create Area object from text
        myobj = area.Area(text=aoc_06.from_text(EXAMPLE_TEXT),
                          part2=True, total=32)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(len(myobj.coords), 6)
        self.assertEqual(len(myobj.closest), 0)
        self.assertEqual(myobj.coords[0].x, 1)
        self.assertEqual(myobj.coords[0].y, 1)
        self.assertEqual(myobj.coords[5].x, 8)
        self.assertEqual(myobj.coords[5].y, 9)
        self.assertEqual(myobj.maxX, 8)
        self.assertEqual(myobj.maxY, 9)
        self.assertEqual(myobj.total, 32)
        self.assertTrue(len(myobj.distances) > 0)

        # 3. Test total distance
        self.assertEqual(myobj.totalDistance(4,3), 30)

        # 4. Test distCoord
        self.assertNotEqual(myobj.distCoord, None)
        self.assertEqual(myobj.distCoord.x, 4)
        self.assertEqual(myobj.distCoord.y, 4)
        #print("%d %d %d %d" % (myobj.distCoord.minX, myobj.distCoord.minY, myobj.distCoord.maxX, myobj.distCoord.maxY))
        self.assertEqual(myobj.distCoord.minX, 1)
        self.assertEqual(myobj.distCoord.minY, 3)
        self.assertEqual(myobj.distCoord.maxX, 7)
        self.assertEqual(myobj.distCoord.maxY, 6)
        self.assertEqual(myobj.distCoord.isInfinite, False)



    def test_part_one(self):
        "Test part one example of Area object"

        # 1. Create Area object from text
        myobj = area.Area(text=aoc_06.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Area object"

        # 1. Create Area object from text
        myobj = area.Area(part2=True, total=32, text=aoc_06.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ a r e a . p y                    end
# ======================================================================
