# ======================================================================
# The N-Body Problem
#   Advent of Code 2019 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ m o o n . p y
# ======================================================================
"Test moon for Advent of Code 2019 day 12, The N-Body Problem"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import moon

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                               TestMoon
# ======================================================================


class TestMoon(unittest.TestCase):  # pylint: disable=R0904
    """Test Panels object"""

    def test_empty_init(self):
        """Test default Moon object creation"""

        # 1. Create default Moon object
        mymoon = moon.Moon()

        # 2. Make sure it has the default values
        self.assertEqual(mymoon.pos, (0, 0, 0))
        self.assertEqual(mymoon.vel, (0, 0, 0))
        self.assertEqual(mymoon.delta, [0, 0, 0])

        # 3. Check methods
        self.assertEqual(mymoon.energy(), 0)
        self.assertEqual(str(mymoon),
                         'pos=<x=  0, y=  0, z=  0>, vel=<x=  0, y=  0, z=  0>, nrg=   0')

    def test_value_init(self):
        "Test Moon object creation with values"

        # 1. Create Panel object with values
        mymoon = moon.Moon(pos=(2, -1, -3), vel=(3, -2, -1))

        # 2. Make sure it has the specified values
        self.assertEqual(mymoon.pos, (2, -1, -3))
        self.assertEqual(mymoon.vel, (3, -2, -1))
        self.assertEqual(mymoon.delta, [0, 0, 0])

        # 3. Check methods
        self.assertEqual(mymoon.energy(), 36)
        self.assertEqual(str(mymoon),
                         'pos=<x=  2, y= -1, z= -3>, vel=<x=  3, y= -2, z= -1>, nrg=  36')

    def test_text_init(self):
        """Test Moon object creation from text"""

        # 1. Create default Moon object
        mymoon = moon.Moon(text='<x=-1, y=0, z=2>')

        # 2. Make sure it has the default values
        self.assertEqual(mymoon.pos, (-1, 0, 2))
        self.assertEqual(mymoon.vel, (0, 0, 0))
        self.assertEqual(mymoon.delta, [0, 0, 0])

        # 3. Check methods
        self.assertEqual(mymoon.energy(), 0)
        self.assertEqual(str(mymoon),
                         'pos=<x= -1, y=  0, z=  2>, vel=<x=  0, y=  0, z=  0>, nrg=   0')

    def test_gravity(self):
        """Test Moon object creation from text"""

        # 1. Create two moons
        ganymede = moon.Moon(text='<x=3, y=4, z=7>')
        callisto = moon.Moon(text='<x=5, y=4, z=2>')

        # 2. Calculate the effects of gravity
        ganymede.apply_gravity(callisto)

        # 3. Check the change in velocities
        self.assertEqual(ganymede.delta, [+1, 0, -1])
        self.assertEqual(callisto.delta, [-1, 0, +1])

        # 4. Apply these changes in velocities
        ganymede.update_velocity_and_position()
        callisto.update_velocity_and_position()

        # 5. Check the updated velocities and positions
        self.assertEqual(ganymede.pos, (4, 4, 6))
        self.assertEqual(ganymede.vel, (1, 0, -1))
        self.assertEqual(ganymede.delta, [0, 0, 0])
        self.assertEqual(callisto.pos, (4, 4, 3))
        self.assertEqual(callisto.vel, (-1, 0, 1))
        self.assertEqual(callisto.delta, [0, 0, 0])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ m o o n . p y                     end
# ======================================================================
