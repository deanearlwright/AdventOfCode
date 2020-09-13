# ======================================================================
# Experimental Emergency Teleportation
#   Advent of Code 2018 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ n a n o b o t s . p y
# ======================================================================
"""Test solver for Advent of Code 2018 day 23,
Experimental Emergency Teleportation"""

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_23
import nanobots

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 7
PART_TWO_RESULT = 36

# ======================================================================
#                                                            TestNanobot
# ======================================================================


class TestNanobot(unittest.TestCase):  # pylint: disable=R0904
    "Test Nanobot object"

    def test_empty_init(self):
        "Test the default Nanobot creation"

        # 1. Create default Nanobots object
        myobj = nanobots.Nanobot()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.x, None)
        self.assertEqual(myobj.y, None)
        self.assertEqual(myobj.z, None)
        self.assertEqual(myobj.r, None)

    def test_text_init(self):
        "Test the Nanobot object creation from text"

        # 1. Create Nanobot object from text
        myobj = nanobots.Nanobot(text='pos=<-22356506,24819383,19709017>, r=53389427')

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.x, -22356506)
        self.assertEqual(myobj.y, 24819383)
        self.assertEqual(myobj.z, 19709017)
        self.assertEqual(myobj.r, 53389427)

    def test_manhattan_distance(self):
        # 1. Create some Nanobot objects from text
        nb1 = nanobots.Nanobot(text='pos=<0,0,0>, r=4')
        nb2 = nanobots.Nanobot(text='pos=<4,0,0>, r=3')
        nb3 = nanobots.Nanobot(text='pos=<1,1,1>, r=1')
        nb4 = nanobots.Nanobot(text='pos=<1,3,1>, r=4')

        # 2. Check the distances
        self.assertEqual(nb1.manhattan_distance(nb1), 0)
        self.assertEqual(nb1.manhattan_distance(nb2), 4)
        self.assertEqual(nb1.manhattan_distance(nb3), 3)
        self.assertEqual(nb1.manhattan_distance(nb4), 5)

        # 3. Check the ranges
        self.assertEqual(nb1.in_range(nb1), True)
        self.assertEqual(nb1.in_range(nb2), True)
        self.assertEqual(nb1.in_range(nb3), True)
        self.assertEqual(nb1.in_range(nb4), False)

# ======================================================================
#                                                           TestNanobots
# ======================================================================


class TestNanobots(unittest.TestCase):  # pylint: disable=R0904
    "Test Nanobots object"

    def test_empty_init(self):
        "Test the default Nanobots creation"

        # 1. Create default Nanobots object
        myobj = nanobots.Nanobots()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.bots), 0)

    def test_text_init(self):
        "Test the Nanobots object creation from text"

        # 1. Create Nanobots object from text
        myobj = nanobots.Nanobots(text=aoc_23.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 9)
        self.assertEqual(len(myobj.bots), 9)

        # 3. Check distances
        self.assertEqual(myobj.bots[0].manhattan_distance(myobj.bots[0]), 0)
        self.assertEqual(myobj.bots[0].manhattan_distance(myobj.bots[1]), 1)
        self.assertEqual(myobj.bots[0].manhattan_distance(myobj.bots[2]), 4)
        self.assertEqual(myobj.bots[0].manhattan_distance(myobj.bots[3]), 2)
        self.assertEqual(myobj.bots[0].manhattan_distance(myobj.bots[4]), 5)
        self.assertEqual(myobj.bots[0].manhattan_distance(myobj.bots[5]), 3)
        self.assertEqual(myobj.bots[0].manhattan_distance(myobj.bots[6]), 3)
        self.assertEqual(myobj.bots[0].manhattan_distance(myobj.bots[7]), 4)
        self.assertEqual(myobj.bots[0].manhattan_distance(myobj.bots[8]), 5)

        # 4. Check range
        self.assertEqual(myobj.bots[0].in_range(myobj.bots[0]), True)
        self.assertEqual(myobj.bots[0].in_range(myobj.bots[1]), True)
        self.assertEqual(myobj.bots[0].in_range(myobj.bots[2]), True)
        self.assertEqual(myobj.bots[0].in_range(myobj.bots[3]), True)
        self.assertEqual(myobj.bots[0].in_range(myobj.bots[4]), False)
        self.assertEqual(myobj.bots[0].in_range(myobj.bots[5]), True)
        self.assertEqual(myobj.bots[0].in_range(myobj.bots[6]), True)
        self.assertEqual(myobj.bots[0].in_range(myobj.bots[7]), True)
        self.assertEqual(myobj.bots[0].in_range(myobj.bots[8]), False)

        # 4. Check strongest signal
        self.assertEqual(myobj.largest_signal_radius(), myobj.bots[0])

        # 5. Check number in range
        self.assertEqual(myobj.bots_in_range(myobj.bots[0]), 7)


    def test_part_one(self):
        "Test part one example of Nanobots object"

        # 1. Create Nanobots object from text
        myobj = nanobots.Nanobots(text=aoc_23.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Nanobots object"

        # 1. Create Nanobots object from text
        myobj = nanobots.Nanobots(part2=True, text=aoc_23.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ n a n o b o t s . p y                end
# ======================================================================
