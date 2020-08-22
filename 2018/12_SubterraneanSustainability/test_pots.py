# ======================================================================
# Subterranean Sustainability
#   Advent of Code 2018 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p o t s . p y
# ======================================================================
"Test solver for Advent of Code 2018 day 12, Subterranean Sustainability"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_12
import pots

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 325
PART_TWO_RESULT = 1370 + 20 * (50000000000 - 100)

# ======================================================================
#                                                               TestPots
# ======================================================================


class TestPots(unittest.TestCase):  # pylint: disable=R0904
    "Test Pots object"

    def test_empty_init(self):
        "Test the default Pots creation"

        # 1. Create default Pots object
        myobj = pots.Pots()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.pots), 0)
        self.assertEqual(len(myobj.rules.keys()), 0)
        self.assertEqual(myobj.left, 0)
        self.assertEqual(myobj.generations, 20)


    def test_text_init(self):
        "Test the Pots object creation from text"

        # 1. Create Pots object from text
        myobj = pots.Pots(text=aoc_12.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 15)
        self.assertEqual(len(myobj.pots), 65)
        self.assertEqual(len(myobj.rules.keys()), 14)
        self.assertEqual(myobj.left, -20)
        self.assertEqual(myobj.generations, 20)

        # 3. Checkout the initial sum
        self.assertEqual(myobj.sum_pots(), 145)

        # 4. Checkout the next generation
        self.assertEqual(myobj.next(20), '#')
        self.assertEqual(myobj.next(21), '.')
        self.assertEqual(myobj.next(22), '.')
        self.assertEqual(myobj.next(23), '.')
        self.assertEqual(myobj.next(24), '#')
        self.assertEqual(myobj.next(25), '.')

        # 5. Checkout a couple of generations
        self.assertEqual(myobj.pots[17:56], '...#..#.#..##......###...###...........') # 0
        myobj.pots = myobj.next_generation()
        self.assertEqual(len(myobj.pots), 65)
        self.assertEqual(myobj.pots[17:56], '...#...#....#.....#..#..#..#...........') # 1
        myobj.pots = myobj.next_generation()
        self.assertEqual(myobj.pots[17:56], '...##..##...##....#..#..#..##..........') # 2
        myobj.pots = myobj.next_generation()
        myobj.pots = myobj.next_generation()
        myobj.pots = myobj.next_generation()
        myobj.pots = myobj.next_generation()
        myobj.pots = myobj.next_generation()
        myobj.pots = myobj.next_generation()
        myobj.pots = myobj.next_generation()
        myobj.pots = myobj.next_generation()
        self.assertEqual(myobj.pots[17:56], '..#.#..#...#.##....##..##..##..##......') # 10
        myobj.pots = myobj.next_generation()
        myobj.pots = myobj.next_generation()
        myobj.pots = myobj.next_generation()
        myobj.pots = myobj.next_generation()
        myobj.pots = myobj.next_generation()
        myobj.pots = myobj.next_generation()
        myobj.pots = myobj.next_generation()
        myobj.pots = myobj.next_generation()
        myobj.pots = myobj.next_generation()
        myobj.pots = myobj.next_generation()
        self.assertEqual(myobj.pots[17:56], '.#....##....#####...#######....#.#..##.') # 20
        self.assertEqual(myobj.sum_pots(), 325)


    def test_part_one(self):
        "Test part one example of Pots object"

        # 1. Create Pots object from text
        myobj = pots.Pots(text=aoc_12.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Pots object"

        # 1. Create Pots object from text
        myobj = pots.Pots(part2=True,
                          text=aoc_12.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(999999999370, PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ p o t s . p y                    end
# ======================================================================
