# ======================================================================
# Lobby Layout
#   Advent of Code 2020 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           t i l e s . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 24 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
NUMBER_OF_DAYS = 100

DELTA = {
    'E': (1, 0),
    'W': (-1, 0),
    'NE': (0.5, -0.5),
    'SE': (0.5, 0.5),
    'NW': (-0.5, -0.5),
    'SW': (-0.5, 0.5)}

# ======================================================================
#                                                                  Tiles
# ======================================================================


class Tiles(object):   # pylint: disable=R0902, R0205
    "Object for Lobby Layout"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.tiles = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                loc = self.location(line)
                if loc in self.tiles:
                    self.tiles[loc] = not self.tiles[loc]
                else:
                    self.tiles[loc] = True

    @staticmethod
    def location(text):
        "Deterimine the location of this tile"

        # 1. Add commas between directions
        insts = text.replace('nw', 'NW,').replace('ne', 'NE,')
        insts = insts.replace('sw', 'SW,').replace('se', 'SE,')
        insts = insts.replace('e', 'E,').replace('w', 'W,')

        # 2. Start at the reference tile
        result = [0, 0]

        # 3. Loop for the instructions
        for inst in insts[:-1].split(','):

            # 4. Adjust location
            result[0] += DELTA[inst][0]
            result[1] += DELTA[inst][1]

        # 5. Return the final location
        return result[0], result[1]

    def count_black(self):
        "Count the number of black tiles"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the tiles
        for side in self.tiles.values():

            # 3. If the dark side is showing, increment the count
            if side:
                result += 1

        # 4. Return the number of black tiles
        return result

    @staticmethod
    def neighbors(loc):
        "Return the location of tiles near this tile"

        # 1. Start with nothing
        result = []

        # 2. Loop for all of the directions
        for delta in DELTA.values():
            result.append((loc[0] + delta[0], loc[1] + delta[1]))

        # 3. Return the location of all of the neighbors
        return result

    def copy_and_fill(self):
        "Copy the black tiles and fill around them with white ones"

        # 1. Start with nothing
        next_tiles = {}

        # 2. Loop for all of the current tile locations
        for loc, color in self.tiles.items():

            # 3. Not really interested in the white ones
            if not color:
                continue

            # 4. Loop for all of the neighbors of the black tile
            for near in self.neighbors(loc):

                # 5. If the tile isn't already in the new set ...
                if near not in next_tiles:

                    # 6. Copy color of the neighbor if we know it, else it is white
                    if near in self.tiles:
                        next_tiles[near] = self.tiles[near]
                    else:
                        next_tiles[near] = False

            # 7. Lastly, copy the black tile that we were surrounding with others
            next_tiles[loc] = True

        # 8. Return the tiles
        return next_tiles

    def count_black_neighbors(self, loc):
        "The number of nearby black tiles"

        # 1. Start with nothing
        result = 0

        # 2. Loop for the nearby locations
        for near in self.neighbors(loc):

            # 3. If there is a black neighbor, increment the count
            if near in self.tiles and self.tiles[near]:
                result += 1

        # Return the number of nearby black tiles
        return result

    def one_day(self):
        "Flip some tiles for the new day"

        # 1. Get a new set of tiles to play with
        new_tiles = self.copy_and_fill()

        # 2. Loop for all of those tiles
        for loc, color in new_tiles.items():

            # 3. Get the count of black tiles
            count = self.count_black_neighbors(loc)

            # 4. Flip black tile with zero or more than 2 black tiles
            if color:
                if count == 0 or count > 2:
                    new_tiles[loc] = False

            # 5. Flip white tile with exactly 2 black tiles
            elif count == 2:
                new_tiles[loc] = True

        # 6. Make the new tiles the current tiles
        self.tiles = new_tiles

    def many_days(self, days):
        "Run the floor exhibit for the specified number of days"

        # 1. Loop for the specified number of days
        for day in range(days):
            assert day >= 0

            # 2. Do the art thing
            self.one_day()

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.count_black()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        assert verbose in [True, False]
        assert limit >= 0

        # 1. Back to the future
        self.many_days(NUMBER_OF_DAYS)

        # 2. Return the solution for part two
        return self.count_black()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          t i l e s . p y                       end
# ======================================================================
