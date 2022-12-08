# ======================================================================
# Treetop Tree House
#   Advent of Code 2022 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         t r e e s . p y
# ======================================================================
"Trees for the Advent of Code 2022 Day 08 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRS = [UP, DOWN, LEFT, RIGHT]

# ======================================================================
#                                                                  Trees
# ======================================================================


class Trees(object):   # pylint: disable=R0902, R0205
    "Object for Treetop Tree House"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.grid = {}
        self.size = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Loop for the lines of input
        for row, line in enumerate(self.text):

            # 2. Loop for the characters of the line
            for col, height in enumerate(line):

                # 3. Save the height
                self.grid[(col, row)] = int(height)

        # 4. Verify that the grid is square
        size = len(self.text)
        assert size * size == len(self.grid)

    def is_visible(self, col, row):
        "Is the tree at the (col, row) visible"

        # 1. Examine the tree in four directions
        for offset in DIRS:
            if self.is_visible_from_edge(col, row, offset):
                return True

        # 2. The tree is not visible
        return False

    def is_visible_from_edge(self, col, row, offset):

        # 1. Get height of tree
        loc = (col, row)
        height = self.grid[loc]

        # 2. Loop toward the edge
        while loc in self.grid:

            # 3. Advance to the edge
            loc = (loc[0] + offset[0], loc[1] + offset[1])
            #print(col, row, offset, height, loc)

            # 4. If this new location is not the forest, the tree is visible
            if loc not in self.grid:
                return True

            # 5. If this tree is higher, the tree is not visible in this direction
            if self.grid[loc] >= height:
                return False

        # 6. Should not get here
        print("ivfe: Should not get here", col, row, offset)
        return True

    def count_visible(self):
        "Return the number of visible trees"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the trees
        for loc in self.grid.keys():

            # 3. If this tree is visible, increment the count
            if self.is_visible(loc[0], loc[1]):
                result += 1

        # 4. Return the number of visible trees
        return result

    def scenic_score(self, col, row):
        "Return the scenic score: product of visible trees"

        # 1. Start with nothing
        result = 1

        # 2. Examine view in four directions
        for offset in DIRS:
            score = self.visible_from_here(col, row, offset)
            #print(col, row, offset, score)
            result *= score

        # 2. Return the number of visible trees
        return result

    def visible_from_here(self, col, row, offset):

        # 1. Get height of tree
        loc = (col, row)
        height = self.grid[loc]

        # 2. Start with nothing
        result = 0

        # 3. Loop toward the edge
        while loc in self.grid:

            # 3. Advance to the edge
            loc = (loc[0] + offset[0], loc[1] + offset[1])
            #print(col, row, offset, height, loc)

            # 4. If this new location is not the forest, return the current count
            if loc not in self.grid:
                return result

            # 5. If this tree is higher, it can be seen but no more
            if self.grid[loc] >= height:
                return result + 1

            # 6. We can see this tree (and maybe more)
            result += 1

        # 7. Should not get here
        print("vfh: Should not get here", col, row, offset)
        return -1

    def highest_scenic_score(self):
        "Return the number of visible trees"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the trees
        for loc in self.grid.keys():

            # 3. If this tree has a higher score, remember it
            score = self.scenic_score(loc[0], loc[1])
            if score > result:
                result = score

        # 4. Return the highest scenic score
        return result


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         t r e e s . p y                        end
# ======================================================================
