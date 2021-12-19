# ======================================================================
# Beacon Scanner
#   Advent of Code 2021 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s c a n n e r . p y
# ======================================================================
"Test Scanner for Advent of Code 2021 day 19, Beacon Scanner"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_19
import scanner

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_ZERO = """
--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401
"""
EXAMPLE_ONE = """
--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390
"""

# ======================================================================
#                                                            TestScanner
# ======================================================================


class TestScanner(unittest.TestCase):  # pylint: disable=R0904
    "Test Scanner object"

    def test_empty_init(self):
        "Test the default Scanner creation"

        # 1. Create default Scanner object
        myobj = scanner.Scanner()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.number, 0)
        self.assertEqual(myobj.bcns, set())
        self.assertEqual(myobj.orientations, [])
        self.assertEqual(myobj.coordinates, None)
        self.assertEqual(myobj.adjusted, set())

        # 3. Check methods
        self.assertEqual(myobj.coord_diff((0, 2, 0), (-5, 0, 0)), (5, 2, 0))
        self.assertEqual(myobj.coord_diff((3, 3, 0), (-2, 1, 0)), (5, 2, 0))
        self.assertEqual(myobj.coord_diff((4, 1, 0), (-1, -1, 0)), (5, 2, 0))

        self.assertEqual(myobj.coord_diff((-618, -824, -621), (686, 422, 578)),
                         (-1304, -1246, -1199))
        self.assertEqual(myobj.coord_diff((-537, -823, -458), (605, 423, 415)),
                         (-1142, -1246, -873))
        self.assertEqual(myobj.coord_diff((-447, -329, 318), (515, 917, -361)),
                         (-962, -1246, 679))

    def test_text_init(self):
        "Test the Scanner object creation from text"

        # 1. Create Scanner object from text
        myobj = scanner.Scanner(text=aoc_19.from_text(EXAMPLE_ZERO))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 26)
        self.assertEqual(myobj.number, 0)
        self.assertEqual(len(myobj.bcns), 25)
        self.assertEqual(len(myobj.orientations), 24)
        self.assertEqual(len(myobj.orientations[0]), 25)
        self.assertEqual(myobj.coordinates, None)
        self.assertEqual(myobj.adjusted, set())

        # 3. Check methods
        one = scanner.Scanner(text=aoc_19.from_text(EXAMPLE_ONE))
        myobj.coordinates = (0, 0, 0)
        self.assertEqual(len(one.find_matches(myobj.bcns)), 25)
        self.assertEqual(one.coordinates, (68, -1246, -43))

        self.assertEqual(myobj.manhattan_distance(one), 1357)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ s c a n n e r . p y                 end
# ======================================================================
