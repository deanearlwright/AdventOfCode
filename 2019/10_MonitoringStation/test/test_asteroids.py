# ======================================================================
# Monitoring Station
#   Advent of Code 2019 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# codeuter simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ a s t e r o i d s . p y
# ======================================================================
"Test computer for Advent of Code 2019 day 10, Monitoring Station"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import asteroids

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
P1_EXP1_TEXT = [
    '.#..#',
    '.....',
    '#####',
    '....#',
    '...##']

P1_EXP1_KNTS = [
    [0, 7, 0, 0, 7],
    [0, 0, 0, 0, 0],
    [6, 7, 7, 7, 5],
    [0, 0, 0, 0, 7],
    [0, 0, 0, 8, 7]]

P1_EXP2_TEXT = [
    '......#.#.',
    '#..#.#....',
    '..#######.',
    '.#.#.###..',
    '.#..#.....',
    '..#....#.#',
    '#..#....#.',
    '.##.#..###',
    '##...#..#.',
    '.#....####']

P1_EXP3_TEXT = [
    '#.#...#.#.',
    '.###....#.',
    '.#....#...',
    '##.#.#.#.#',
    '....#.#.#.',
    '.##..###.#',
    '..#...##..',
    '..##....##',
    '......#...',
    '.####.###.']

P1_EXP4_TEXT = [
    '.#..#..###',
    '####.###.#',
    '....###.#.',
    '..###.##.#',
    '##.##.#.#.',
    '....###..#',
    '..#.#..#.#',
    '#..#.#.###',
    '.##...##.#',
    '.....#.#..']

P1_EXP5_TEXT = [
    '.#..##.###...#######',
    '##.############..##.',
    '.#.######.########.#',
    '.###.#######.####.#.',
    '#####.##.#.##.###.##',
    '..#####..#.#########',
    '####################',
    '#.####....###.#.#.##',
    '##.#################',
    '#####.##.###..####..',
    '..######..##.#######',
    '####.##.####...##..#',
    '.#####..#.######.###',
    '##...#.##########...',
    '#.##########.#######',
    '.####.#.###.###.#.##',
    '....##.##.###..#####',
    '.#.#.###########.###',
    '#.#.#.#####.####.###',
    '###.##.####.##.#..##']

# ======================================================================
#                                                            TestUtility
# ======================================================================

class TestUtility(unittest.TestCase):  # pylint: disable=R0904
    """Test Utility Functions"""

    def test_to_the_right(self):
        """Test to_the_right function"""


# ======================================================================
#                                                          TestAsteroids
# ======================================================================


class TestAsteroids(unittest.TestCase):  # pylint: disable=R0904
    """Test Asteroids object"""

    def test_empty_init(self):
        """Test default Asteroids object creation"""

        # 1. Create default Astroids object
        myass = asteroids.Asteroids()

        # 2. Make sure it has the default values
        self.assertEqual(myass.rows, 0)
        self.assertEqual(myass.cols, 0)
        self.assertEqual(len(myass.amap), 0)
        self.assertEqual(len(myass.knts), 0)

        # 3. Check methods
        self.assertEqual(myass.maximum(), None)
        self.assertEqual(str(myass), '')

    def test_text_init(self):
        """Test Asteroids object creation with text"""

        # 1. Create Intcode obhect with values
        myass = asteroids.Asteroids(text=P1_EXP1_TEXT)

        # 2. Make sure it has the specified values
        self.assertEqual(myass.rows, 5)
        self.assertEqual(myass.cols, 5)
        self.assertEqual(len(myass.amap), 5)
        self.assertEqual(len(myass.knts), 5)
        self.assertEqual(myass.knts, P1_EXP1_KNTS)

        # 3. Check methods
        self.assertEqual(myass.maximum(), (8, (3, 4)))

    def test_part_one_examples(self):
        """Test Asteroids object with examples from the part 1 problem"""

        # 1. Example 1
        myass = asteroids.Asteroids(text=P1_EXP1_TEXT)
        self.assertEqual(myass.maximum(), (8, (3, 4)))

        # 2. Example 2
        myass = asteroids.Asteroids(text=P1_EXP2_TEXT)
        self.assertEqual(myass.maximum(), (33, (5, 8)))

        # 3. Example 3
        myass = asteroids.Asteroids(text=P1_EXP3_TEXT)
        self.assertEqual(myass.maximum(), (35, (1, 2)))

        # 4. Example 4
        myass = asteroids.Asteroids(text=P1_EXP4_TEXT)
        self.assertEqual(myass.maximum(), (41, (6, 3)))

        # 5. Example 5
        myass = asteroids.Asteroids(text=P1_EXP5_TEXT)
        self.assertEqual(myass.maximum(), (210, (11, 13)))


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end               t e s t _ a s t e r o i d s . p y                end
# ======================================================================
