# ======================================================================
# Rain Risk
#   Advent of Code 2020 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ f e r r y . p y
# ======================================================================
"Test moveable object for Advent of Code 2020 day 12, Rain Risk"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import ferry

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                              TestFerry
# ======================================================================


class TestFerry(unittest.TestCase):  # pylint: disable=R0904
    "Test Ferry object"

    def test_empty_init(self):
        "Test the default Ferry creation"

        # 1. Create default Ferry object
        myobj = ferry.Ferry()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.start, (0, 0))
        self.assertEqual(myobj.loc, (0, 0))
        self.assertEqual(myobj.heading, ferry.EAST)

        # 3. Check some methods
        myobj.execute('F10')
        self.assertEqual(myobj.loc, (10, 0))
        self.assertEqual(myobj.heading, ferry.EAST)

        myobj.execute('N3')
        self.assertEqual(myobj.loc, (10, -3))
        self.assertEqual(myobj.heading, ferry.EAST)

        myobj.execute('F7')
        self.assertEqual(myobj.loc, (17, -3))
        self.assertEqual(myobj.heading, ferry.EAST)

        myobj.execute('R90')
        self.assertEqual(myobj.loc, (17, -3))
        self.assertEqual(myobj.heading, ferry.SOUTH)

        myobj.execute('F11')
        self.assertEqual(myobj.loc, (17, 8))
        self.assertEqual(myobj.heading, ferry.SOUTH)

        self.assertEqual(str(myobj), 'S: east 17, south 8')

        self.assertEqual(myobj.manhattan(), 25)

    def test_part2(self):
        "Test the part2 default Ferry creation"

        # 1. Create default Ferry object
        myobj = ferry.Ferry(part2=True)

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(myobj.start, (0, 0))
        self.assertEqual(myobj.loc, (0, 0))
        self.assertEqual(myobj.waypoint, (10, -1))

        # 3. Check some methods
        myobj.execute('F10')
        self.assertEqual(myobj.loc, (100, -10))
        self.assertEqual(myobj.waypoint, (10, -1))

        myobj.execute('N3')
        self.assertEqual(myobj.loc, (100, -10))
        self.assertEqual(myobj.heading, ferry.EAST)
        self.assertEqual(myobj.waypoint, (10, -4))

        myobj.execute('F7')
        self.assertEqual(myobj.loc, (170, -38))
        self.assertEqual(myobj.waypoint, (10, -4))

        myobj.execute('R90')
        self.assertEqual(myobj.loc, (170, -38))
        self.assertEqual(myobj.waypoint, (4, 10))

        myobj.execute('F11')
        self.assertEqual(myobj.loc, (214, 72))
        self.assertEqual(myobj.waypoint, (4, 10))

        self.assertEqual(str(myobj), 'east 214, south 72; wp: east 4, south 10')

        self.assertEqual(myobj.manhattan(), 286)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ f e r r y . p y                   end
# ======================================================================
