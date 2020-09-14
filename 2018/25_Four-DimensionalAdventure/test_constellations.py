# ======================================================================
# Four-Dimensional Adventure
#   Advent of Code 2018 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c o n s t e l l a t i o n s . p y
# ======================================================================
"Test solver for Advent of Code 2018 day 25, Four-Dimensional Adventure"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_25
import constellations

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TWO = """
 0,0,0,0
 3,0,0,0
 0,3,0,0
 0,0,3,0
 0,0,0,3
 0,0,0,6
 9,0,0,0
12,0,0,0
"""
EXAMPLE_FOUR = """
-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0
"""
EXAMPLE_THREE = """
1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2
"""

EXAMPLE_EIGHT = """
1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2
"""

PART_ONE_TEXT = EXAMPLE_TWO
PART_TWO_TEXT = ""

PART_ONE_RESULT = 2
PART_TWO_RESULT = None

# ======================================================================
#                                                            TestUtility
# ======================================================================
class TestUtility(unittest.TestCase):  # pylint: disable=R0904
    "Test Utility Functions"

    def test_distance(self):
        "Test the mantattan distance function"

        self.assertEqual(constellations.distance((0,0,0,0), (0,0,0,0)), 0)
        self.assertEqual(constellations.distance([0,0,0,0], (3,0,0,0)), 3)
        self.assertEqual(constellations.distance((0,0,0,0), (0,3,0,0)), 3)
        self.assertEqual(constellations.distance((0,0,0,0), (0,0,3,0)), 3)
        self.assertEqual(constellations.distance((0,0,0,0), (0,0,0,3)), 3)
        self.assertEqual(constellations.distance((0,0,0,0), (0,0,3,3)), 6)

    def test_stars_are_close(self):
        "Test the mantattan distance function with two stars"

        self.assertEqual(constellations.stars_are_close((0,0,0,0), (0,0,0,0)), True)
        self.assertEqual(constellations.stars_are_close((0,0,0,0), (1,0,0,0)), True)
        self.assertEqual(constellations.stars_are_close((0,0,0,0), (0,2,0,0)), True)
        self.assertEqual(constellations.stars_are_close((0,0,0,0), (0,0,3,0)), True)
        self.assertEqual(constellations.stars_are_close((0,0,1,0), (1,0,1,0)), True)
        self.assertEqual(constellations.stars_are_close((0,0,0,0), (4,0,0,0)), False)
        self.assertEqual(constellations.stars_are_close((0,0,0,0), (0,5,0,0)), False)
        self.assertEqual(constellations.stars_are_close((0,0,0,0), (0,0,6,0)), False)

    def test_star_is_close_to_constellation(self):
        "Test the santattan distance function with star and constellation"

        self.assertEqual(constellations.star_is_close_to_constellation((0,0,0,0), [(0,0,0,0)]), True)
        self.assertEqual(constellations.star_is_close_to_constellation((0,0,0,0), [(1,0,0,0),(10,0,0,0)]), True)
        self.assertEqual(constellations.star_is_close_to_constellation([0,1,0,0], [(0,0,7,0),(1,0,0,0)]), True)
        self.assertEqual(constellations.star_is_close_to_constellation((0,0,0,0), []), False)
        self.assertEqual(constellations.star_is_close_to_constellation((0,0,0,0), [(4,0,0,0),(0,5,0,0)]), False)

    def test_constellations_are_close(self):
        "Test the santattan distance function with two constellations"

        self.assertEqual(constellations.constellations_are_close([(0,0,0,0)], [(0,0,0,0)]), True)
        self.assertEqual(constellations.constellations_are_close([(0,0,0,0)], [(1,0,0,0),(10,0,0,0)]), True)
        self.assertEqual(constellations.constellations_are_close([[0,1,0,0],[12,16,0,4]], [[0,0,7,0],[1,0,0,0]]), True)
        self.assertEqual(constellations.constellations_are_close([(0,0,0,0)], []), False)
        self.assertEqual(constellations.constellations_are_close([], [(0,0,0,0)]), False)
        self.assertEqual(constellations.constellations_are_close([[0,0,0,0],[7,6,0,0]], [[4,0,0,0],[0,5,0,0]]), False)

# ======================================================================
#                                                     TestConstellations
# ======================================================================


class TestConstellations(unittest.TestCase):  # pylint: disable=R0904
    "Test Constellations object"

    def test_empty_init(self):
        "Test the default Constellations creation"

        # 1. Create default Constellations object
        myobj = constellations.Constellations()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.points, [])
        self.assertEqual(myobj.constellations, [])


    def test_text_init(self):
        "Test the Constellations object creation from text"

        # 1. Create Constellations object from text
        myobj = constellations.Constellations(text=aoc_25.from_text(EXAMPLE_TWO))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 8)
        self.assertEqual(len(myobj.points), 8)
        self.assertEqual(myobj.points[0], [0,0,0,0])
        self.assertEqual(myobj.points[1], [3,0,0,0])
        self.assertEqual(myobj.constellations, [])

        # 3. Join into constallations
        myobj.form_constellations()
        self.assertEqual(len(myobj.points), 8)
        self.assertEqual(len(myobj.constellations), 2)

    def test_examples(self):
        "Test multiple examples"
        myobj = constellations.Constellations(text=aoc_25.from_text(EXAMPLE_TWO))
        myobj.form_constellations()
        self.assertEqual(len(myobj.constellations), 2)

        myobj = constellations.Constellations(text=aoc_25.from_text(EXAMPLE_FOUR))
        myobj.form_constellations()
        self.assertEqual(len(myobj.constellations), 4)

        myobj = constellations.Constellations(text=aoc_25.from_text(EXAMPLE_THREE))
        myobj.form_constellations()
        self.assertEqual(len(myobj.constellations), 3)

        myobj = constellations.Constellations(text=aoc_25.from_text(EXAMPLE_EIGHT))
        myobj.form_constellations()
        self.assertEqual(len(myobj.constellations), 8)

    def test_part_one(self):
        "Test part one example of Constellations object"

        # 1. Create Constellations object from text
        myobj = constellations.Constellations(text=aoc_25.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Constellations object"

        # 1. Create Constellations object from text
        myobj = constellations.Constellations(part2=True, text=aoc_25.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end          t e s t _ c o n s t e l l a t i o n s . p y           end
# ======================================================================
