# ======================================================================
# Air Duct Spelunking
#   Advent of Code 2016 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d u c t s . p y
# ======================================================================
"Test Ducts for Advent of Code 2016 day 24, Air Duct Spelunking"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_24
import ducts

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
###########
#0.1.....2#
#.#######.#
#4.......3#
###########
"""

# ======================================================================
#                                                              TestDucts
# ======================================================================


class TestDucts(unittest.TestCase):  # pylint: disable=R0904
    "Test Ducts object"

    def test_empty_init(self):
        "Test the default Ducts creation"

        # 1. Create default Ducts object
        myobj = ducts.Ducts()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.num_to_loc, {})
        self.assertEqual(myobj.loc_to_num, {})

    def test_text_init(self):
        "Test the Ducts object creation from text"

        # 1. Create Ducts object from text
        myobj = ducts.Ducts(text=aoc_24.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(len(myobj.num_to_loc), 5)
        self.assertEqual(len(myobj.loc_to_num), 5)
        self.assertEqual(myobj.num_to_loc[0], (1, 1))
        self.assertEqual(myobj.num_to_loc[4], (1, 3))
        self.assertEqual(myobj.loc_to_num[(1, 1)], 0)
        self.assertEqual(myobj.loc_to_num[(1, 3)], 4)

        # 3. Check methods
        self.assertEqual(myobj.where_is(0), (1, 1))
        self.assertEqual(myobj.where_is(4), (1, 3))
        self.assertEqual(myobj.where_is(9), None)
        self.assertEqual(myobj.what_is_at((1, 1)), 0)
        self.assertEqual(myobj.what_is_at((1, 3)), 4)
        self.assertEqual(myobj.what_is_at((7, 9)), None)

        self.assertEqual(myobj.is_wall(None), True)
        self.assertEqual(myobj.is_wall((-1, -1)), True)
        self.assertEqual(myobj.is_wall((0, 0)), True)
        self.assertEqual(myobj.is_wall((1, 1)), False)

        self.assertEqual(myobj.one_step((1, 1)), [(2, 1), (1, 2)])
        self.assertEqual(myobj.one_step((1, 3)), [(2, 3), (1, 2)])

        self.assertEqual(myobj.steps_to_others(0), {1: 2, 4: 2})
        self.assertEqual(myobj.steps_to_others(1), {0: 2, 2: 6})
        self.assertEqual(myobj.steps_to_others(2), {3: 2, 1: 6})
        self.assertEqual(myobj.steps_to_others(3), {2: 2, 4: 8})
        self.assertEqual(myobj.steps_to_others(4), {0: 2, 3: 8})

        self.assertEqual(myobj.steps_to_others(0, full=True), {1: 2, 2: 8, 3: 10, 4: 2})
        self.assertEqual(myobj.steps_to_others(1, full=True), {0: 2, 2: 6, 3: 8, 4: 4})

        all_steps = myobj.all_steps()
        self.assertEqual(len(all_steps), len(myobj.num_to_loc))
        self.assertEqual(all_steps[0], {1: 2, 2: 8, 3: 10, 4: 2})
        self.assertEqual(all_steps[1], {0: 2, 2: 6, 3: 8, 4: 4})


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ d u c t s . p y                   end
# ======================================================================
