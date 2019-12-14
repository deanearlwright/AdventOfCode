# ======================================================================
# Monitoring Station
#   Advent of Code 2019 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ q u a d r a n t . p y
# ======================================================================
"Test computer for Advent of Code 2019 day 10, Monitoring Station"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

from math import pi

import quadrant

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE = """

Giant Lasor Example

  01234567890123456
0 .#....#####...#.. 0   7
1 ##...##.#####..## 1  11
2 ##...#...#.#####. 2   9
3 ..#.....X...###.. 3   4
4 ..#.#.....#....## 4   5
  01234567890123456    36

Asteroids by Rows

0: 1, 5, 7, 8, 9, 10, 14
1: 0, 1, 5, 6, 8, 9, 10, 11, 12, 15, 16
2: 0, 1, 5, 9, 11, 12, 13, 14, 15
3: 2, 8, 12, 13, 14
4: 2, 4, 10, 15, 16

The first nine asteroids to get vaporized, in order, would be:

  01234567890123456
0 .#....###24...#.. 0
1 ##...##.13#67..9# 1
2 ##...#...5.8####. 2
3 ..#.....X...###.. 3
4 ..#.#.....#....## 4
  01234567890123456

1: ( 8, 1)
2: ( 9, 0)
3: ( 9, 1)
4: (10, 0)
5: ( 9, 2)
6: (11, 1)
7: (12, 1)
8: (11, 2)
9: (15, 1)

"""

ASTEROIDS = {
    0: [1, 6, 7, 8, 9, 10, 14],
    1: [0, 1, 5, 6, 8, 9, 10, 11, 12, 15, 16],
    2: [0, 1, 5, 9, 11, 12, 13, 14, 15],
    3: [2, 8, 12, 13, 14],
    4: [2, 4, 10, 15, 16]
}

QUAD = {
    0: [4, 4, 4, 1, 1, 1, 1],
    1: [4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1],
    2: [4, 4, 4, 1, 1, 1, 1, 1, 1],
    3: [4, 0, 2, 2, 2],
    4: [3, 3, 2, 2, 2]
}

SHOTS = {
    0: (8, 3),
    1: (8, 1),
    2: (9, 0),
    3: (9, 1),
    4: (10, 0),
    5: (9, 2),
    6: (11, 1),
    7: (12, 1),
    8: (11, 2),
    9: (15, 1),
    10: (12, 2),
    11: (13, 2),
    12: (14, 2),
    13: (15, 2),
    14: (12, 3),
    15: (16, 4),
    16: (15, 4),
    17: (10, 4),
    18: (4, 4),
    19: (2, 4),
    20: (2, 3),
    21: (0, 2),
    22: (1, 2),
    23: (0, 1),
    24: (1, 1),
    25: (5, 2),
    26: (1, 0),
    27: (5, 1),
    28: (6, 1),
    29: (6, 0),
    30: (7, 0),
    31: (8, 0),
    32: (10, 1),
    33: (14, 0),
    34: (16, 1),
    35: (13, 3),
    36: (14, 3)
}

EXP5_TEXT = [
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

EXP5_CENTER = (11, 13)

EXP5_SHOTS = {
    1: (11, 12),
    2: (12, 1),
    3: (12, 2),
    10: (12, 8),
    20: (16, 0),
    50: (16, 9),
    100: (10, 16),
    199: (9, 6),
    200: (8, 2),
    201: (10, 9),
    299: (11, 1),
}

EXP5_LAST = (11, 1)
EXP5_TOTAL = 299

# ======================================================================
#                                                           TestQuadrant
# ======================================================================


class TestQuadrant(unittest.TestCase):  # pylint: disable=R0904
    """Test Quadrant object"""

    def test_empty_init(self):
        """Test default Quadrant object creation"""

        # 1. Create default quadrant object
        myquad = quadrant.Quadrant()

        # 2. Make sure it has the default values
        self.assertEqual(myquad.center, (0, 0))
        self.assertEqual(myquad.start, 0.0)
        self.assertEqual(myquad.finish, 0.0)
        self.assertEqual(myquad.angles, {})
        self.assertEqual(myquad.ordered, [])
        self.assertEqual(myquad.blocked, [])


    def test_is_quad_one(self):
        """Test in or out of quad 1"""

        # 1. Create quad 1
        quad1 = quadrant.Quadrant(center=(8, 3), start=pi/2, finish=0)

        # 2. Process all the asteroids by row
        for row in ASTEROIDS:

            # 3. Loop for all the columns (with quadrant info)
            for col, quad in zip(ASTEROIDS[row], QUAD[row]):
                if not quad:
                    continue # Ignore the laser

                # 4. Attempt to add the asteroid to quad 1
                result = quad1.add_if((col, row))
                #print("(%d, %d) %d %s"% (col, row, quad, result))

                # 5. Check the result
                self.assertEqual(result, quad == 1)

    def test_quad_iter(self):
        """Test iterating over quad 1"""

        # 1. Create quad 1
        quad1 = quadrant.Quadrant(center=(8, 3), start=pi/2, finish=0)

        # 2. Process all the asteroids by row
        for row in ASTEROIDS:

            # 3. Loop for all the columns
            for col, quad in zip(ASTEROIDS[row], QUAD[row]):

                # 4. Quad 1 only please
                if quad != 1:
                    continue # Ignore the laser

                # 5. Add the location to quad 1
                self.assertEqual(quad1.add_if((col, row)), True)

        # 6. All locations enter, order angles and distances
        quad1.bake()

        # 7. Shoot 9 asteroids from quadrant 1
        number = 0
        for angle in quad1:
            number += 1
            loc = quad1.shoot(angle)
            self.assertEqual(loc, SHOTS[number])
            if number >= 9:
                break
        # 8. Should be four more to shoot this round, three on next
        self.assertEqual(len(quad1.ordered), 4)
        self.assertEqual(len(quad1.blocked), 3)

# ======================================================================
#                                                              TestQuads
# ======================================================================


class TestQuads(unittest.TestCase):  # pylint: disable=R0904
    """Test Quadrant object"""

    def test_empty_init(self):
        """Test default Quads object creation"""

        # 1. Create default quads object
        myquads = quadrant.Quads()

        # 2. Make sure it has the default values
        self.assertEqual(myquads.center, (0, 0))
        self.assertEqual(len(myquads.quads), 4)

    def test_is_accepted(self):
        """Test which quad accepts each location"""

        # 1. Create the quads
        quads = quadrant.Quads(center=(8, 3))

        # 2. Process all the asteroids by row
        for row in ASTEROIDS:

            # 3. Loop for all the columns (with quadrant info)
            for col, quad in zip(ASTEROIDS[row], QUAD[row]):
                if not quad:
                    continue # Ignore the laser

                # 4. Attempt to add add the asteroid
                self.assertEqual(quads.add_asteroid((col, row)), quad)


    def test_quads_text(self):
        """Test which shotting across all quads on large text example"""

        # 1. Create the quads with the map
        quads = quadrant.Quads(center=EXP5_CENTER, text=EXP5_TEXT)

        # 2. All locations entered, order angles and distances
        quads.bake()

        # 3. Loop until we shoot the last one
        total = 0
        loc = None
        while loc != EXP5_LAST:

            # 4. Loop for all the quads, shooting in each
            for quad in quads.quads:
                for angle in quad:
                    loc = quad.shoot(angle)
                    total += 1

                    # 5. Is this the asteroid we were expecting
                    #print("%d %s %s" % (total, loc, SHOTS[total]))
                    if total in EXP5_SHOTS:
                        self.assertEqual(loc, EXP5_SHOTS[total])

        # 6. Are we where we want to be?
        self.assertEqual(loc, EXP5_LAST)
        self.assertEqual(total, EXP5_TOTAL)
        self.assertEqual(len(quads.quads[0].ordered), 0)
        self.assertEqual(len(quads.quads[1].ordered), 0)
        self.assertEqual(len(quads.quads[2].ordered), 0)
        self.assertEqual(len(quads.quads[3].ordered), 0)
        self.assertEqual(len(quads.quads[0].blocked), 0)
        self.assertEqual(len(quads.quads[1].blocked), 0)
        self.assertEqual(len(quads.quads[2].blocked), 0)
        self.assertEqual(len(quads.quads[3].blocked), 0)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                t e s t _ q u a d r a n t . p y                 end
# ======================================================================
