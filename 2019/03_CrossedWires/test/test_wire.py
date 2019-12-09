# ======================================================================
# Crossed Wires
#   Advent of Code 2019 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# codeuter simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ w i r e . p y
# ======================================================================
"Test Wire object for Advent of Code 2019 day 3, Crossed Wires"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import wire

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                            TestUtility
# ======================================================================

class TestUtility(unittest.TestCase):  # pylint: disable=R0904
    """Test utilty function"""

    def test_manhattan(self):
        """Test manhattan distance function"""

        self.assertEqual(wire.manhattan((0, 0), (0, 0)), 0)
        self.assertEqual(wire.manhattan((0, 0), (3, 3)), 6)
        self.assertEqual(wire.manhattan((0, 0), (5, 5)), 10)
        self.assertEqual(wire.manhattan((3, 3), (5, 5)), 4)

    def test_intersect(self):
        "Test wire segment intersections"

        self.assertEqual(wire.intersect((0, 0), (8, 0), (8, 0), (0, 5)), (8, 0))
        self.assertEqual(wire.intersect((0, 0), (8, 0), (5, 8), (5, 3)), None)
        self.assertEqual(wire.intersect((5, 8), (5, 3), (5, 3), (2, 3)), (5, 3))
        self.assertEqual(wire.intersect((0, 0), (8, 0), (5, 3), (2, 3)), None)
        self.assertEqual(wire.intersect((8, 5), (3, 5), (6, 7), (6, 3)), (6, 5))
        self.assertEqual(wire.intersect((3, 1), (3, 5), (2, 3), (6, 3)), (3, 3))

# ======================================================================
#                                                               TestWire
# ======================================================================


class TestWire(unittest.TestCase):  # pylint: disable=R0904
    """Test Wire object"""

    def test_empty_init(self):
        """Test default intcode object creation"""

        # 1. Create default Intcode object
        mywire = wire.Wire()

        # 2. Make sure it has the default values
        self.assertEqual(len(mywire.points), 1)
        self.assertEqual(mywire.start, (0, 0))
        self.assertEqual(mywire.finish, (0, 0))

        # 3. Check methods
        self.assertEqual(mywire.begin(), (0, 0))
        self.assertEqual(mywire.end(), (0, 0))
        self.assertEqual(mywire.num_points(), 1)
        self.assertEqual(mywire.num_segments(), 0)

    def test_value_init(self):
        """Test Wire object creation with values"""

        # 1. Create Wire obhect with values
        mywire = wire.Wire(start=(2, 1))

        # 2. Make sure it has the specified values
        self.assertEqual(len(mywire.points), 1)
        self.assertEqual(mywire.start, (2, 1))
        self.assertEqual(mywire.finish, (2, 1))

        # 3. Check methods
        self.assertEqual(mywire.begin(), (2, 1))
        self.assertEqual(mywire.end(), (2, 1))
        self.assertEqual(mywire.num_points(), 1)
        self.assertEqual(mywire.num_segments(), 0)

    def test_text_init(self):
        """Test Intcode object creation with text"""

        # 1. Create Wire obhect with values
        mywire = wire.Wire(text='R8,U5,L5,D3')

        # 2. Make sure it has the specified values
        self.assertEqual(len(mywire.points), 5)
        self.assertEqual(mywire.start, (0, 0))
        self.assertEqual(mywire.finish, (3, 2))

        # 3. Check methods
        self.assertEqual(mywire.begin(), (0, 0))
        self.assertEqual(mywire.end(), (3, 2))
        self.assertEqual(mywire.num_points(), 5)
        self.assertEqual(mywire.num_segments(), 4)
        self.assertEqual(mywire.segment(0), ((0, 0), (8, 0)))
        self.assertEqual(mywire.segment(1), ((8, 0), (8, 5)))
        self.assertEqual(mywire.segment(2), ((8, 5), (3, 5)))
        self.assertEqual(mywire.segment(3), ((3, 5), (3, 2)))

    def test_samples(self):
        """Test Wire object with samples from problem description"""

        # 1. Sample 1
        wire1 = wire.Wire(text='R8,U5,L5,D3')
        wire2 = wire.Wire(text='U7,R6,D4,L4')
        inter = wire1.intersections(wire2)
        self.assertEqual(inter, [(3, 3), (6, 5)])
        self.assertEqual(wire.closest((0, 0), inter), (3, 3))
        self.assertEqual(wire.manhattan((0, 0), wire.closest((0, 0), inter)), 6)
        self.assertEqual(wire1.time_to((3, 3)), 20)
        self.assertEqual(wire2.time_to((3, 3)), 20)
        self.assertEqual(wire1.time_to((6, 5)), 15)
        self.assertEqual(wire2.time_to((6, 5)), 15)
        self.assertEqual(wire.fastest(inter, [wire1, wire2]), 30)

        # 2. Sample 2
        wire1 = wire.Wire(text='R75,D30,R83,U83,L12,D49,R71,U7,L72')
        wire2 = wire.Wire(text='U62,R66,U55,R34,D71,R55,D58,R83')
        inter = wire1.intersections(wire2)
        self.assertEqual(wire.manhattan((0, 0), wire.closest((0, 0), inter)), 159)
        self.assertEqual(wire.fastest(inter, [wire1, wire2]), 610)

        # 3. Sample 3
        wire1 = wire.Wire(text='R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51')
        wire2 = wire.Wire(text='U98,R91,D20,R16,D67,R40,U7,R15,U6,R7')
        inter = wire1.intersections(wire2)
        self.assertEqual(wire.manhattan((0, 0), wire.closest((0, 0), inter)), 135)
        self.assertEqual(wire.fastest(inter, [wire1, wire2]), 410)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ w i r e . p y                     end
# ======================================================================
