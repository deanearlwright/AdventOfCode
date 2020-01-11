# ======================================================================
# Knot Hash
#   Advent of Code 2017 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s t r i n g . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 10, Knot Hash"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import knots

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

P1_EXAMPLE = "3, 4, 1, 5"
P1_VALUES = [
    [0, 1, 2, 3, 4],
    [2, 1, 0, 3, 4],
    [4, 3, 0, 1, 2],
    [4, 3, 0, 1, 2],
    [3, 4, 2, 1, 0]]
P1_CURRENT = [0, 3, 3, 1, 4]
P1_SKIP = [0, 1, 2, 3, 4]
P1_RESULT = 12

# ======================================================================
#                                                              TestKnots
# ======================================================================


class TestKnots(unittest.TestCase):  # pylint: disable=R0904
    """Test Knots object"""

    def test_empty_init(self):
        """Test default Knots creation"""

        # 1. Create default Knots object
        myknot = knots.Knots()

        # 2. Make sure it has the default values
        self.assertEqual(myknot.part2, False)
        self.assertEqual(myknot.length, 0)
        self.assertEqual(myknot.current, 0)
        self.assertEqual(myknot.skip, 0)
        self.assertEqual(myknot.values, [])


    def test_value_init(self):
        """Test Knots creation with values"""

        # 1. Create Knots object from values
        myknot = knots.Knots(length=256)

        # 2. Make sure it has the specified values
        self.assertEqual(myknot.part2, False)
        self.assertEqual(myknot.length, 256)
        self.assertEqual(myknot.current, 0)
        self.assertEqual(myknot.skip, 0)
        self.assertEqual(len(myknot.values), 256)

    def test_example_step_by_step(self):
        """Test Knots example knot by knot"""

        # 1. Create Knots object from values
        myknot = knots.Knots(length=5)

        # 2. Make sure it has the specified values
        self.assertEqual(myknot.part2, False)
        self.assertEqual(myknot.length, 5)
        self.assertEqual(myknot.current, P1_CURRENT[0])
        self.assertEqual(myknot.skip, P1_SKIP[0])
        self.assertEqual(myknot.values, P1_VALUES[0])

        # 3. Process the first knot
        myknot.process_one_knot(3, verbose=False)
        self.assertEqual(myknot.current, P1_CURRENT[1])
        self.assertEqual(myknot.skip, P1_SKIP[1])
        self.assertEqual(myknot.values, P1_VALUES[1])

        # 4. Process the second knot
        myknot.process_one_knot(4, verbose=False)
        self.assertEqual(myknot.current, P1_CURRENT[2])
        self.assertEqual(myknot.skip, P1_SKIP[2])
        self.assertEqual(myknot.values, P1_VALUES[2])

        # 5. Process the third knot
        myknot.process_one_knot(1, verbose=False)
        self.assertEqual(myknot.current, P1_CURRENT[3])
        self.assertEqual(myknot.skip, P1_SKIP[3])
        self.assertEqual(myknot.values, P1_VALUES[3])

        # 6. Process the fourth knot
        myknot.process_one_knot(5, verbose=False)
        self.assertEqual(myknot.current, P1_CURRENT[4])
        self.assertEqual(myknot.skip, P1_SKIP[4])
        self.assertEqual(myknot.values, P1_VALUES[4])

    def test_example(self):
        """Test Knots example"""

        # 1. Create Knots object from values
        myknot = knots.Knots(length=5)

        # 2. Make sure it has the specified values
        self.assertEqual(myknot.part2, False)
        self.assertEqual(myknot.length, 5)
        self.assertEqual(myknot.current, P1_CURRENT[0])
        self.assertEqual(myknot.skip, P1_SKIP[0])
        self.assertEqual(myknot.values, P1_VALUES[0])

        # 3. Process the first knot
        self.assertEqual(myknot.process_knots(text=P1_EXAMPLE),
                         P1_RESULT)
        self.assertEqual(myknot.current, P1_CURRENT[4])
        self.assertEqual(myknot.skip, P1_SKIP[4])
        self.assertEqual(myknot.values, P1_VALUES[4])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ s t r i n g . p y                 end
# ======================================================================
