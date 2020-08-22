# ======================================================================
# The Stars Align
#   Advent of Code 2018 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ l i g h t s . p y
# ======================================================================
"Test solver for Advent of Code 2018 day 10, The Stars Align"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_10
import lights

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = ""

PART_ONE_RESULT = "HI"
PART_TWO_RESULT = None

# ======================================================================
#                                                              TestLight
# ======================================================================


class TestLight(unittest.TestCase):  # pylint: disable=R0904
    "Test Light object"

    def test_empty_init(self):
        "Test the default Light creation"

        # 1. Create default Light object
        myobj = lights.Light()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.posX, 0)
        self.assertEqual(myobj.posY, 0)
        self.assertEqual(myobj.velX, 0)
        self.assertEqual(myobj.velY, 0)

        # 3. Move forward a step
        myobj.step()
        self.assertEqual(myobj.posX, 0)
        self.assertEqual(myobj.posY, 0)
        self.assertEqual(myobj.velX, 0)
        self.assertEqual(myobj.velY, 0)

    def test_text_init(self):
        "Test the Lights object creation from text"

        # 1. Create Lights object from text
        myobj = lights.Light(text="position=<-3, 11> velocity=< 1, -2>")

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text.startswith('position'), True)
        self.assertEqual(myobj.posX, -3)
        self.assertEqual(myobj.posY, 11)
        self.assertEqual(myobj.velX, 1)
        self.assertEqual(myobj.velY, -2)

        # 3. Move forward a step
        myobj.step()
        self.assertEqual(myobj.posX, -2)
        self.assertEqual(myobj.posY, 9)
        self.assertEqual(myobj.velX, 1)
        self.assertEqual(myobj.velY, -2)

# ======================================================================
#                                                             TestLights
# ======================================================================


class TestLights(unittest.TestCase):  # pylint: disable=R0904
    "Test Lights object"

    def test_empty_init(self):
        "Test the default Lights creation"

        # 1. Create default Lights object
        myobj = lights.Lights()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.points), 0)

    def test_text_init(self):
        "Test the Lights object creation from text"

        # 1. Create Lights object from text
        myobj = lights.Lights(text=aoc_10.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 31)
        self.assertEqual(len(myobj.points), 31)
        self.assertEqual(myobj.points[0].posX, 9)
        self.assertEqual(myobj.points[0].posY, 1)
        self.assertEqual(myobj.points[0].velX, 0)
        self.assertEqual(myobj.points[0].velY, 2)
        self.assertEqual(myobj.points[1].posX, 7)
        self.assertEqual(myobj.points[1].posY, 0)
        self.assertEqual(myobj.points[1].velX, -1)
        self.assertEqual(myobj.points[1].velY, 0)
        self.assertEqual(myobj.rows(), 16)

        # 3. Move forward a step
        myobj.step()
        self.assertEqual(myobj.points[0].posX, 9)
        self.assertEqual(myobj.points[0].posY, 3)
        self.assertEqual(myobj.points[0].velX, 0)
        self.assertEqual(myobj.points[0].velY, 2)
        self.assertEqual(myobj.points[1].posX, 6)
        self.assertEqual(myobj.points[1].posY, 0)
        self.assertEqual(myobj.points[1].velX, -1)
        self.assertEqual(myobj.points[1].velY, 0)
        self.assertEqual(myobj.rows(), 12)

        # 4. And a couple of more steps
        myobj.step()
        self.assertEqual(myobj.rows(), 10)
        myobj.step()
        self.assertEqual(myobj.rows(), 8)
        print(myobj.display())
        myobj.step()
        self.assertEqual(myobj.rows(), 11)


    def test_part_one(self):
        "Test part one example of Lights object"

        # 1. Create Lights object from text
        myobj = lights.Lights(text=aoc_10.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False, limit=5), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Lights object"

        # 1. Create Lights object from text
        myobj = lights.Lights(part2=True, text=aoc_10.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ l i g h t s . p y                end
# ======================================================================
