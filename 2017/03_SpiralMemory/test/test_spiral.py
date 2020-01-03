# ======================================================================
# Spiral Memory
#   Advent of Code 2017 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      t e s t _ s p i r a l . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 3, Spiral Memory"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import spiral

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

P1_EXAMPLES = [
    (1, 0),
    (6, 1),
    (7, 2),
    (12, 3),
    (23, 2),
    (1024, 31)]

# ======================================================================
#                                                             TestSpiral
# ======================================================================


class TestSpiral(unittest.TestCase):  # pylint: disable=R0904
    """Test Spiral object"""

    def test_manhattan_distance(self):
        """Test default manhattan_distance utility function"""

        # 1. Near the origin
        self.assertEqual(spiral.manhattan_distance((0, 0), (0, 0)), 0)
        self.assertEqual(spiral.manhattan_distance((0, 0), (0, 1)), 1)
        self.assertEqual(spiral.manhattan_distance((0, 0), (-1, 1)), 2)

        # 2. Elsewhere
        self.assertEqual(spiral.manhattan_distance((3, 2), (4, 3)), 2)
        self.assertEqual(spiral.manhattan_distance((3, 0), (3, 1)), 1)
        self.assertEqual(spiral.manhattan_distance((3, 0), (-1, 1)), 5)

    def test_empty_init(self):
        """Test default Spiral creation"""

        # 1. Create default Spiral object
        myspiral = spiral.Spiral()

        # 2. Make sure it has the default values
        self.assertEqual(myspiral.part2, False)
        self.assertEqual(myspiral.spiral, {})

        # 3. Check methods
        self.assertEqual(myspiral.steps(1), 0)

    def test_ring_number(self):
        """Test ring_number determination"""

        # 1. Create default Spiral object
        myspiral = spiral.Spiral()

        # 2. Make sure it has the default values
        self.assertEqual(myspiral.part2, False)
        self.assertEqual(myspiral.spiral, {})

        # 3. Check ring_number()
        self.assertEqual(myspiral.ring_number(1), 0)
        self.assertEqual(myspiral.ring_number(7), 1)
        self.assertEqual(myspiral.ring_number(10), 2)
        self.assertEqual(myspiral.ring_number(15), 2)
        self.assertEqual(myspiral.ring_number(20), 2)
        self.assertEqual(myspiral.ring_number(25), 2)
        self.assertEqual(myspiral.ring_number(30), 3)
        self.assertEqual(myspiral.ring_number(35), 3)
        self.assertEqual(myspiral.ring_number(40), 3)
        self.assertEqual(myspiral.ring_number(45), 3)
        self.assertEqual(myspiral.ring_number(50), 4)

    def test_ring_side(self):
        """Test length of ring side"""

        # 1. Check ring_side()
        self.assertEqual(spiral.ring_side(0), 1)
        self.assertEqual(spiral.ring_side(1), 3)
        self.assertEqual(spiral.ring_side(2), 5)
        self.assertEqual(spiral.ring_side(3), 7)
        self.assertEqual(spiral.ring_side(4), 9)
        self.assertEqual(spiral.ring_side(21), 43)
        self.assertEqual(spiral.ring_side(30), 61)

    def test_ring_length(self):
        """Test length of ring length"""

        # 1. Check ring_side()
        self.assertEqual(spiral.ring_length(0), 1)
        self.assertEqual(spiral.ring_length(1), 8)
        self.assertEqual(spiral.ring_length(2), 16)
        self.assertEqual(spiral.ring_length(3), 24)
        self.assertEqual(spiral.ring_length(4), 32)
        self.assertEqual(spiral.ring_length(10), 80)
        self.assertEqual(spiral.ring_length(30), 240)

    def test_ring_max_min(self):
        """Test highest and lowest number on a ring"""

        # 1. Create default Spiral object
        myspiral = spiral.Spiral()

        # 2. Make sure it has the default values
        self.assertEqual(myspiral.part2, False)
        self.assertEqual(myspiral.spiral, {})

        # 3. Check ring_max()
        self.assertEqual(myspiral.ring_max(0), 1)
        self.assertEqual(myspiral.ring_max(1), 9)
        self.assertEqual(myspiral.ring_max(2), 25)
        self.assertEqual(myspiral.ring_max(3), 49)
        self.assertEqual(myspiral.ring_max(4), 81)
        self.assertEqual(myspiral.ring_max(5), 121)

        # 3. Check ring_min()
        self.assertEqual(myspiral.ring_min(0), 1)
        self.assertEqual(myspiral.ring_min(1), 2)
        self.assertEqual(myspiral.ring_min(2), 10)
        self.assertEqual(myspiral.ring_min(3), 26)
        self.assertEqual(myspiral.ring_min(4), 50)
        self.assertEqual(myspiral.ring_min(5), 82)

    def test_ring_offsets(self):
        """Test ring and side offsets"""

        # 1. Create default Spiral object
        myspiral = spiral.Spiral()

        # 2. Make sure it has the default values
        self.assertEqual(myspiral.part2, False)
        self.assertEqual(myspiral.spiral, {})

        # 3. Check ring_offset()
        self.assertEqual(myspiral.ring_offset(0), None)
        self.assertEqual(myspiral.ring_offset(1), 0)
        self.assertEqual(myspiral.ring_offset(5), 4)
        self.assertEqual(myspiral.ring_offset(10), 1)
        self.assertEqual(myspiral.ring_offset(15), 6)
        self.assertEqual(myspiral.ring_offset(20), 11)
        self.assertEqual(myspiral.ring_offset(25), 0)
        self.assertEqual(myspiral.ring_offset(30), 5)

        # 3. Check side_offset()
        self.assertEqual(myspiral.side_offset(0), None)
        self.assertEqual(myspiral.side_offset(1), 0)
        self.assertEqual(myspiral.side_offset(5), 0)
        self.assertEqual(myspiral.side_offset(10), 1)
        self.assertEqual(myspiral.side_offset(15), 2)
        self.assertEqual(myspiral.side_offset(20), 3)
        self.assertEqual(myspiral.side_offset(25), 0)
        self.assertEqual(myspiral.side_offset(30), 5)

    def test_side_distance(self):
        """Test distance to horizontal or vertical axis"""

        # 1. Create default Spiral object
        myspiral = spiral.Spiral()

        # 2. Make sure it has the default values
        self.assertEqual(myspiral.part2, False)
        self.assertEqual(myspiral.spiral, {})

        # 3. Check ring_offset()
        self.assertEqual(myspiral.side_distance(0), None)
        self.assertEqual(myspiral.side_distance(1), 0)
        self.assertEqual(myspiral.side_distance(5), 1)
        self.assertEqual(myspiral.side_distance(10), 1)
        self.assertEqual(myspiral.side_distance(15), 0)
        self.assertEqual(myspiral.side_distance(20), 1)
        self.assertEqual(myspiral.side_distance(25), 2)
        self.assertEqual(myspiral.side_distance(30), 2)

    def test_part_one_examples(self):
        """Test Spiral examples"""

        # 1. Create default Spiral object
        myspiral = spiral.Spiral()

        # 2. Make sure it has the default values
        self.assertEqual(myspiral.part2, False)

        # 3. Loop for all of the part 1 examples
        for example in P1_EXAMPLES:

            # 4. Check the number of steps from the square to the access port
            self.assertEqual(myspiral.steps(example[0],
                                            verbose=False),
                             example[1])

    def test_part_one_spiral(self):
        """Test building the part 1 spiral"""

        # 1. Create default Spiral object
        myspiral = spiral.Spiral()

        # 2. Make sure it has the default values
        self.assertEqual(myspiral.part2, False)

        # 3. Build the spiral
        result = myspiral.build_until_gt(23, verbose=False)

        # 4. Validate the spiral
        self.assertEqual(result, 24)
        self.assertEqual(myspiral.spiral[(0, 0)], 1)
        self.assertEqual(myspiral.spiral[(1, 0)], 2)
        self.assertEqual(myspiral.spiral[(1, 1)], 3)
        self.assertEqual(myspiral.spiral[(0, 1)], 4)
        self.assertEqual(myspiral.spiral[(-1, 1)], 5)
        self.assertEqual(myspiral.spiral[(-1, 0)], 6)
        self.assertEqual(myspiral.spiral[(-1, -1)], 7)
        self.assertEqual(myspiral.spiral[(-1, -2)], 22)
        self.assertEqual(myspiral.spiral[(0, -2)], 23)
        self.assertEqual(myspiral.spiral[(1, -2)], 24)
        self.assertTrue((2, -2) not in myspiral.spiral)

    def test_part_two_spiral(self):
        """Test building the part 2 spiral"""

        # 1. Create default Spiral object
        myspiral = spiral.Spiral(part2=True)

        # 2. Make sure it has the default values
        self.assertEqual(myspiral.part2, True)

        # 3. Build the spiral
        result = myspiral.build_until_gt(806, verbose=False)

        # 4. Validate the spiral
        self.assertEqual(result, 880)
        self.assertEqual(myspiral.spiral[(0, 0)], 1)
        self.assertEqual(myspiral.spiral[(1, 0)], 1)
        self.assertEqual(myspiral.spiral[(1, 1)], 2)
        self.assertEqual(myspiral.spiral[(0, 1)], 4)
        self.assertEqual(myspiral.spiral[(-1, 1)], 5)
        self.assertEqual(myspiral.spiral[(-1, 0)], 10)
        self.assertEqual(myspiral.spiral[(-1, -1)], 11)
        self.assertEqual(myspiral.spiral[(-1, -2)], 747)
        self.assertEqual(myspiral.spiral[(0, -2)], 806)
        self.assertEqual(myspiral.spiral[(1, -2)], 880)
        self.assertTrue((2, -2) not in myspiral.spiral)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ s p i r a l . p y                end
# ======================================================================
