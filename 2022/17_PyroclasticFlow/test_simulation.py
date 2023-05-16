
# ======================================================================
# Pyroclastic Flow
#   Advent of Code 2022 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                   t e s t _ s i m u l a t i o n . p y
# ======================================================================
"Test Simulation for Advent of Code 2022 day 17, Pyroclastic Flow"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import simulation

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"]

PART_ONE_TESTS = [
    (2022, 3068),
    (3000, 4548),
    (4000, 6061),
    (5000, 7577),
    (6000, 9088),
    (7000, 10607),
    (8000, 12120),
    (9000, 13634)
]
PART_TWO_TESTS = [
    (2022, 3068),
    (3000, 4548),
    (4000, 6061),
    (5000, 7577),
    (6000, 9088),
    (7000, 10607),
    (8000, 12120),
    (9000, 13634),
    (1000000000000, 1514285714288)
]


# ======================================================================
#                                                         TestSimulation
# ======================================================================


class TestSimulation(unittest.TestCase):  # pylint: disable=R0904
    "Test Simulation object"

    def test_empty_init(self):
        "Test the default Simulation creation"

        # 1. Create default Simulation object
        myobj = simulation.Simulation()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.chamber, None)
        self.assertEqual(myobj.rocks, None)
        self.assertEqual(myobj.winds, None)
        self.assertEqual(myobj.next_wind, 0)

    def test_text_init(self):
        "Test the Simulation object creation from text"

        # 1. Create Simulation object from text
        myobj = simulation.Simulation(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertNotEqual(myobj.chamber, None)
        self.assertNotEqual(myobj.rocks, None)
        self.assertNotEqual(myobj.winds, None)
        self.assertEqual(myobj.next_wind, 0)

        # 3. Check methods
        self.assertEqual(myobj.run_for_n_rocks(4), 7)
        self.assertEqual(myobj.run_for_n_rocks(8), 15)
        self.assertEqual(myobj.run_for_n_rocks(2022), 3068)
        #self.assertEqual(myobj.run_for_n_rocks(3000), 4548)
        #self.assertEqual(myobj.run_for_n_rocks(4000), 6061)
        #self.assertEqual(myobj.run_for_n_rocks(5000), 7577)
        #self.assertEqual(myobj.run_for_n_rocks(6000), 9088)
        #self.assertEqual(myobj.run_for_n_rocks(7000), 10607)
        #self.assertEqual(myobj.run_for_n_rocks(8000), 12120)
        #self.assertEqual(myobj.run_for_n_rocks(9000), 13634)

    def not_test_part_one(self):
        "Test the part one examples"

        # 1. Loop for all of the part one examples
        for number, result in PART_ONE_TESTS:

            # 2. Create Simulation object from text
            myobj = simulation.Simulation(text=EXAMPLE_TEXT)

            # 3. Check that we get the expected result
            self.assertEqual(myobj.run_for_n_rocks(number), result)

    def test_part_two(self):
        "Test the part one examples"

        # 1. Loop for all of the part one examples
        for number, result in PART_TWO_TESTS:

            # 2. Create Simulation object from text
            myobj = simulation.Simulation(text=EXAMPLE_TEXT)

            # 3. Check that we get the expected result
            self.assertEqual(myobj.calculate_n_rocks(number), result)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end               t e s t _ s i m u l a t i o n . p y              end
# ======================================================================
