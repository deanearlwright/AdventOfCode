# ======================================================================
# Digital Plumber
#   Advent of Code 2017 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p i p e s . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 12,Digital Plumber"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import pipes
import aoc_12

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

EXAMPLE_TEXT = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
"""
# ======================================================================
#                                                               TestPipe
# ======================================================================


class TestPipe(unittest.TestCase):  # pylint: disable=R0904
    """Test Pipe object"""

    def test_empty_init(self):
        """Test default pipe creation"""

        # 1. Create default Pipe object
        mypipe = pipes.Pipe()

        # 2. Make sure it has the default values
        self.assertEqual(mypipe.name, None)
        self.assertEqual(mypipe.connections, [])

    def test_text_init(self):
        """Test pipe creation from text"""

        # 1. Create Pipe objects from text
        mypipe0 = pipes.Pipe(text='0 <-> 2')
        mypipe4 = pipes.Pipe(text='4 <-> 2, 3, 6')

        # 2. Make sure it has the default values
        self.assertEqual(mypipe0.name, 0)
        self.assertEqual(mypipe0.connections, [2])
        self.assertEqual(mypipe4.name, 4)
        self.assertEqual(mypipe4.connections, [2, 3, 6])

# ======================================================================
#                                                              TestPipes
# ======================================================================


class TestPipes(unittest.TestCase):  # pylint: disable=R0904
    """Test Pipes object"""

    def test_empty_init(self):
        """Test default pipes creation"""

        # 1. Create default Pipes object
        mypipes = pipes.Pipes()

        # 2. Make sure it has the default values
        self.assertEqual(mypipes.part2, False)
        self.assertEqual(mypipes.connections, {})

        # 3. Check methods
        self.assertEqual(mypipes.num_in_group(0), None)
        self.assertEqual(mypipes.number_of_groups(), None)

    def test_text_init(self):
        """Test pipes creation from test"""

        # 1. Create default Pipes object
        mypipes = pipes.Pipes(text=aoc_12.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the specified values
        self.assertEqual(mypipes.part2, False)
        self.assertEqual(len(mypipes.connections), 7)
        self.assertEqual(mypipes.connections[0], [2])
        self.assertEqual(mypipes.connections[3], [2, 4])
        self.assertEqual(mypipes.connections[5], [6])

        # 3. Check methods
        self.assertEqual(mypipes.num_in_group(0, verbose=False, limit=100), 6)

    def test_part_two(self):
        """Test part two"""

        # 1. Create default Pipes object
        mypipes = pipes.Pipes(text=aoc_12.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the specified values
        self.assertEqual(mypipes.part2, False)
        self.assertEqual(len(mypipes.connections), 7)
        self.assertEqual(mypipes.connections[0], [2])
        self.assertEqual(mypipes.connections[3], [2, 4])
        self.assertEqual(mypipes.connections[5], [6])

        # 3. Check methods
        self.assertEqual(mypipes.number_of_groups(verbose=False, limit=100), 2)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ h e x e s . p y                  end
# ======================================================================
