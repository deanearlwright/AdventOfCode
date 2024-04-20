
# ======================================================================
# Sand Slabs
#   Advent of Code 2023 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         b r i c k s . p y
# ======================================================================
"Bricks for the Advent of Code 2023 Day 22 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from brick import Brick

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Bricks
# ======================================================================


class Bricks(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Sand Slabs"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.bricks = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.bricks.append(Brick(text=line, part2=part2))

        # 3. Sort the bricks by height
        self.bricks.sort(key=lambda brk: brk.corners.end0.z)

    def drop(self, modify=True, minus=None):  # pylint: disable=R0914
        "Drop all the bricks and return the number that moved"

        # 1. Start with no bricks moved
        result = 0
        heights = {}

        # 2. Loop for all of the bricks (or mostly all)
        for brk in self.bricks:
            if brk == minus:
                continue

            # 3. Get the brick's current heights
            height0 = brk.corners.end0.z
            height1 = brk.corners.end1.z

            # 4. Get the highest location that the brick covers
            grid = brk.grid()
            height = max(heights.get(loc, 0) for loc in grid)

            # 5. Determine the amount that the brick will drop (if any)
            drop = height0 - height - 1

            # 6. If dropping, make some hieght adjustments
            if drop:
                result += 1
                height1 -= drop # pylint: disable=C0103
                if modify:
                    brk.drop(drop)

            # 7. Record the new height (which might be the same as the old ones)
            for loc in grid:
                heights[loc] = height1

        # 9. Return the number of bricks that changed position
        return result

    def disingratable(self):
        "Return the number of bricks that can initially be disintegrated"

        # 1. Complete the initial fall
        self.drop()

        # 2. Start with none
        result = 0

        # 3. Loop for all of the bricks
        for brk in self.bricks:

            # 4. If it can be removed without other bricks falling, it can be disintegrated
            fell = self.drop(modify=False, minus=brk)
            if fell == 0:
                result += 1

        # 5. Return the number of bricks that can be disintegrated
        return result

    def chain_reaction(self):
        "Return the number of bricks that would fall in a chain reaction"

        # 1. Complete the initial fall
        self.drop()

        # 2. Start with none
        result = 0

        # 3. Loop for all of the bricks
        for brk in self.bricks:

            # 4. How many bricks fall if this brick is removed?
            fell = self.drop(modify=False, minus=brk)
            result += fell

        # 5. Return the number of bricks that can be disintegrated
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      b r i c k s . p y                     end
# ======================================================================
