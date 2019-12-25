# ======================================================================
# Planet of Discord
#   Advent of Code 2019 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# codeuter simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ b u g s . p y
# ======================================================================
"Test artificial life for Advent of Code 2019 day 24, Planet of Discord"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import bugs
import aoc_pd

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
P1_EXAMPLE = """
! Initial state:
....#
#..#.
#..##
..#..
#...."""

P1_EXAMPLE_DUP = "...............#.....#..."
P1_EXAMPLE_GEN = 86

P1_EXAMPLE_BIODIVERSITY = 2129920

P2_GEN_10 = {
    -5: '..#...#.#...?.#.#.#...#..',
    -4: '...#....##..?.....##...#.',
    -3: '#.#...#.....?...#...#.#..',
    -2: '.#.##....#..?.#...##.###.',
    -1: '#..##...##..?.....#..####',
    0: '.#....#.##.#?............',
    1: '.##..#..##..?.###.#######',
    2: '###..##.#.#.?...#.###.#..',
    3: '..###.....#.?..#....#...#',
    4: '.###.#..#.#.?..##.#......',
    5: '####.#..#.#.?#.####......'
}

P2_GEN_10_KNT = 99

# ======================================================================
#                                                               TestBugs
# ======================================================================


class TestBugs(unittest.TestCase):  # pylint: disable=R0904
    """Test Bugs object"""

    def test_empty_init(self):
        """Test default Bugs object creation"""

        # 1. Create default Astroids object
        mybugs = bugs.Bugs()

        # 2. Make sure it has the default values
        self.assertEqual(mybugs.size, bugs.SIZE)
        self.assertEqual(mybugs.length, bugs.SIZE * bugs.SIZE)
        self.assertEqual(len(mybugs.current), mybugs.length)
        self.assertEqual(mybugs.minute, 0)
        self.assertEqual(len(mybugs.adjacent), mybugs.length)
        self.assertEqual(len(mybugs.levels), 0)

    def test_text_init(self):
        "Test Bugs object creation with text"

        # 1. Create Bugs object with text
        mybugs = bugs.Bugs(text=aoc_pd.from_text(P1_EXAMPLE))

        # 2. Make sure it has the specified values
        self.assertEqual(mybugs.size, bugs.SIZE)
        self.assertEqual(mybugs.length, bugs.SIZE * bugs.SIZE)
        self.assertEqual(len(mybugs.current), mybugs.length)
        self.assertEqual(mybugs.current, '....##..#.#..##..#..#....')
        self.assertEqual(mybugs.minute, 0)
        self.assertEqual(len(mybugs.adjacent), mybugs.length)
        self.assertEqual(len(mybugs.levels), 0)

    def test_smaller(self):
        "Test Creating a smaller grid"

        # 1. Create a world with only a 3x3 grid
        mybugs = bugs.Bugs(size=3)

        # 2. Make sure it has the specified values
        self.assertEqual(mybugs.size, 3)
        self.assertEqual(mybugs.length, 9)
        self.assertEqual(mybugs.current, '.........')
        self.assertEqual(mybugs.minute, 0)
        self.assertEqual(mybugs.adjacent,
                         [[1, 3], [2, 0, 4], [1, 5],
                          [4, 6, 0], [5, 3, 7, 1], [4, 8, 2],
                          [7, 3], [8, 6, 4], [7, 5]])
        self.assertEqual(len(mybugs.levels), 0)

    def test_part_one_next_genertion(self):
        "Test the first few generations of the part one example"

        # 1. Create Bugs object with text
        mybugs = bugs.Bugs(text=aoc_pd.from_text(P1_EXAMPLE))

        # 2. Check Generation 0
        self.assertEqual(mybugs.current, '....##..#.#..##..#..#....')

        # 3. Check Generation 1
        mybugs.next_generation()
        self.assertEqual(mybugs.current, '#..#.####.###.###.##.##..')

        # 4. Check Generation 2
        mybugs.next_generation()
        self.assertEqual(mybugs.current, '#####....#....#...#.#.###')

        # 5. Check Generation 3
        mybugs.next_generation()
        self.assertEqual(mybugs.current, '#....####....###.##..##.#')

        # 6. Check Generation 4
        mybugs.next_generation()
        self.assertEqual(mybugs.current, '####.....###..#.....##...')

    def test_run_until_duplicate(self):
        "Test running until a duplicate generation"

        # 1. Create Bugs object with text
        mybugs = bugs.Bugs(text=aoc_pd.from_text(P1_EXAMPLE))

        # 2. Run until there is a duplicate generation
        generation = mybugs.run_until_duplicate()

        # 3. Check the results
        self.assertEqual(mybugs.current, P1_EXAMPLE_DUP)
        self.assertEqual(generation, P1_EXAMPLE_GEN)

    def test_biodiversity_rating(self):
        """Test biodiversity rating using part one example"""

        # 1. Create Bugs object with text
        mybugs = bugs.Bugs(text=aoc_pd.from_text(P1_EXAMPLE))

        # 2. Replace current with part one example final state
        mybugs.current = P1_EXAMPLE_DUP

        # 3. Check biodiversity rating
        self.assertEqual(mybugs.get_biodiversity_rating(),
                         P1_EXAMPLE_BIODIVERSITY)

    def test_smaller_recursive(self):
        "Test Creating a smaller grid"

        # 1. Create a world with only a 3x3 grid
        mybugs = bugs.Bugs(size=3, recursive=True)

        # 2. Make sure it has the specified values
        self.assertEqual(mybugs.size, 3)
        self.assertEqual(mybugs.length, 9)
        self.assertEqual(mybugs.current, '.........')
        self.assertEqual(mybugs.minute, 0)
        self.assertEqual(mybugs.adjacent,
                         [[1, -103, 3, -101], [2, 0, 100, 101, 102, -101], [-105, 1, 5, -101],
                          [100, 103, 106, -103, 6, 0], [5, 3, 7, 1], [-105, 102, 105, 108, 8, 2],
                          [7, -103, -107, 3], [8, 6, -107, 106, 107, 108], [-105, 7, -107, 5]])
        self.assertEqual(len(mybugs.levels), 1)

    def test_part_two_ten_genertions(self):
        "Test the first few generations of the part one example"

        # 1. Create Bugs object with text
        mybugs = bugs.Bugs(text=aoc_pd.from_text(P1_EXAMPLE), recursive=True)

        # 2. Run the simulation for 10 generations
        mybugs.run_until(10)

        # 3. Check the levels
        for key, current in P2_GEN_10.items():
            self.assertEqual(mybugs.levels[key], current)

        # 4. And the total number of bugs
        self.assertEqual(mybugs.total_bug_count(), P2_GEN_10_KNT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ b u g s . p y                     end
# ======================================================================
