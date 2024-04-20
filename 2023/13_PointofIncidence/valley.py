
# ======================================================================
# Point of Incidence
#   Advent of Code 2023 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         v a l l e y . p y
# ======================================================================
"Valley for the Advent of Code 2023 Day 13 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
SMUDGE = {
    '.': '#',
    '#': '.',
}


def cal_ref(ver, hor):
    "Return combined reflection"
    return ver + 100 * hor

# ======================================================================
#                                                                 Valley
# ======================================================================


class Valley(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Point of Incidence"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rows = 0
        self.cols = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.rows = len(self.text)
            self.cols = len(self.text[0])
            assert self.cols == len(self.text[-1])

    def reflections(self):
        "Return the reflection value"

        # 0. Not much to do if no text
        if self.rows == 0:
            return 0

        # 1. Get the vertical and horizontal reflection points (if any)
        unsmudged = (self.vertical(), self.horizontal())

        # 2. Return the reflection value
        return cal_ref(*unsmudged)

    def corrected_reflections(self):
        "Return the reflection value"

        # 0. Not much to do if no text
        if self.rows == 0:
            return 0

        # 1. Get the smudged values
        smudged = (self.vertical(), self.horizontal())

        # 2. Loop for every row and column
        for rindx, row in enumerate(self.text):
            new_row = list(row)
            for cindx, char in enumerate(row):

                # 3. Attempt to fix a smudge
                new_row[cindx] = SMUDGE[char]
                self.text[rindx] = ''.join(new_row)

                # 4. Get the new reflections
                corrected = (self.vertical(ignore=smudged[0] - 1),
                             self.horizontal(ignore=smudged[1] - 1))

                # 5. Put the row back as it was
                new_row[cindx] = char
                self.text[rindx] = row

                # 6. If there is a new reflection, return it
                if corrected[0] != 0 or corrected[1] != 0:
                    return cal_ref(*corrected)

        # 7. I would have expected a difference
        print(f"No difference found for {smudged}")
        return 0

    def vertical(self, ignore=-1):
        "Returns location of vertical split, number of columns to left"

        # 1. Loop for most the columns
        for col in range(self.cols - 1):

            # 2. Is there a reflection point here?
            if self.is_vertical_reflection(col) and col != ignore:
                return 1 + col

        # 3. Sorry, no vertical reflection
        return 0

    def is_vertical_reflection(self, col, distance=0):
        "Is there a vertical reflection between col and col+spread"

        # 1. Any hope of a reflection?
        if not self.are_vertical_twins(col - distance, col + distance + 1):
            return False

        # 2. Have we reached the end?
        if col == 0 or col + distance > self.cols:
            return True

        # 3. Else recurse, trying columns to left and right
        return self.is_vertical_reflection(col, distance=distance + 1)

    def are_vertical_twins(self, left_col, right_col):
        "Are these two columns vertical twins"

        # 1. They match if off the map
        if left_col < 0 or right_col >= self.cols:
            return True

        # 2. Else check that the columns are the same
        for row in self.text:
            if row[right_col] != row[left_col]:
                return False
        return True

    def horizontal(self, ignore=-1):
        "Returns location of horizontal split, number of rows above"

        # 1. Loop for most the rows
        for row in range(self.rows - 1):

            # 2. Is there a reflection point here?
            if self.is_horizontal_reflection(row) and row != ignore:
                return 1 + row

        # 3. Sorry, no horizontal reflection
        return 0

    def is_horizontal_reflection(self, row, distance=0):
        "Is there a horizontal reflection between row and row+spread"

        # 1. Any hope of a reflection?
        if not self.are_horizontal_twins(row - distance, row + distance + 1):
            return False

        # 2. Have we reached the end?
        if row == 0 or row + distance > self.rows:
            return True

        # 3. Else recurse, trying rows above and below
        return self.is_horizontal_reflection(row, distance=distance + 1)

    def are_horizontal_twins(self, top_row, bot_row):
        "Are these two rows horizontal twins"

        # 1. They match if off the map
        if top_row < 0 or bot_row >= self.rows:
            return True

        # 2. Else check that the rows are the same
        return self.text[top_row] == self.text[bot_row]

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        v a l l e y . p y                       end
# ======================================================================
