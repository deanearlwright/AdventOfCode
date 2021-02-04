# ======================================================================
# Jurassic Jigsaw
#   Advent of Code 2020 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                            i m a g e . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 20 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import math
import re

import tile
import tiles

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
MONSTER = """                  #
#    ##    ##    ###
 #  #  #  #  #  #   """

MONSTER_RE1 = re.compile('..................#.')
MONSTER_RE2 = re.compile('#....##....##....###')
MONSTER_RE3 = re.compile('.#..#..#..#..#..#...')

MONSTER_IMAGE = """
.####...#####..#...###..
# ..#..#.#.####..#.#.
.#.#...#.###...#.##.##..
#.#.##.###.#.##.##.#####
..##.###.####..#.####.##
...#.#..##.##...#..#..##
# .##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
# .####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
# ...#...###..####....##.
.#.##...#.##.#.#.###...#
# .###.#..####...##..#...
# .###...#.##...#.######.
.###.###.#######..#####.
..##.#..#..#.#######.###
# .#..##.########..#..##.
# .#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#
""".strip()

# ----------------------------------------------------------------------
#                                                                utility
# ----------------------------------------------------------------------


def find_all_starts(regex, text):
    "Find all (could be over lapping) starts"

    # 1. Start with nothing
    result = []
    pos = 0

    # 2. Loop for every search hit
    search = regex.search(text, pos)
    while search:

        # 3. Record this match
        result.append(search.start())

        # 4. Advance and try again
        pos = search.start() + 1
        search = regex.search(text, pos)

    # 5. Return all starting locations
    return result

# ======================================================================
#                                                                  Image
# ======================================================================


class Image(object):   # pylint: disable=R0902, R0205
    "Object for Jurassic Jigsaw"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.tiles = None
        self.image = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.tiles = tiles.Tiles(text=text, part2=part2)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Pre-condition axioms
        assert limit >= 0

        # 1. Put the tiles in a grid
        self.tiles.position_tiles()
        if self.tiles.grid is None:
            return None

        # 2. Return the solution for part one
        if verbose:
            for row_num, row in enumerate(self.tiles.grid):
                print("Grid[%d] = %s" % (row_num, [_[0].number for _ in row]))

        return math.prod([self.tiles.number_at(0, 0),
                          self.tiles.number_at(0, -1),
                          self.tiles.number_at(-1, 0),
                          self.tiles.number_at(-1, -1),
                          ])

    @staticmethod
    def count_pounds_in_image(image):
        "Return the number of pound signs"
        return image.count('#')

    @staticmethod
    def count_monsters_in_image(image):
        "Returns the number of monsters found"

        # 1. Start with nothing
        result = 0

        # 1. Get width of image
        width = len(image.splitlines()[0]) + 1

        # 2. Find where the monster could reside
        #    We are ignoring the top of the head for now (lots of hits)
        starts_re2 = find_all_starts(MONSTER_RE2, image)
        starts_re3 = find_all_starts(MONSTER_RE3, image)

        # 3. Verify the finds
        for start2 in starts_re2:
            if start2 + width in starts_re3:
                result += 1

        # 4. Return the verified count
        return result

    @staticmethod
    def image_orientations(image):
        "Produce different orientations of the image"

        # 1. Break up the image into rows and columns
        matrix_image = [list(_) for _ in image.splitlines()]

        # 2. Use the tile rotater/flipper to get multiple images
        matrix_images = tile.get_orientations(matrix_image)

        # 3. Turn these back to strings
        result = []
        for oriented in matrix_images:
            image_rows = []
            for row in oriented:
                image_rows.append(''.join(row))
            result.append('\n'.join(image_rows))

        # 4. Return the image in various orientations
        assert image == result[0]
        return result

    def find_image_with_monsters(self):
        "Find an image with the most monsters"

        # 1. Get the base image
        image = self.tiles.get_image()
        if image is None:
            return None

        # 2. Get rotated and flipped versions of the image
        images = self.image_orientations(image)

        # 3. Assume the first one is the best
        best_image = None
        best_count = 0

        # 3. Loop for all the images, looking for a monster
        for the_image in images:
            the_count = self.count_monsters_in_image(the_image)
            print("image %d" % the_count)
            if the_count > best_count:
                best_image = the_image
                best_count = the_count

        # 4. Return the best image (if any)
        return best_image

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Pre-condition axioms
        assert limit >= 0

        # 1. Put the tiles in a grid
        self.tiles.position_tiles()
        if self.tiles.grid is None:
            return None

        # 2. Get and image with monsters
        image = self.find_image_with_monsters()
        if image is None:
            return None

        # 3. Get the number of monsters
        monsters = self.count_monsters_in_image(image)

        # 4. Get the number of pounds signs
        monster_pounds = self.count_pounds_in_image(MONSTER)
        image_pounds = self.count_pounds_in_image(image)
        if verbose:
            print("Found %d monsters of %d squares each in rough seas of %d squares" %
                  (monsters, monster_pounds, image_pounds))

        # 2. Return the solution for part two
        return image_pounds - monsters * monster_pounds


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         i m a g e . p y                        end
# ======================================================================
