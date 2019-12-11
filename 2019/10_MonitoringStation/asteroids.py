# ======================================================================
# Monitoring Station
#   Advent of Code 2019 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           a s t e r o i d s . p y
# ======================================================================
"Computer for Monitoring Station problem for Advent of Code 2018 Day 10"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import Counter

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                              Asteroids
# ======================================================================


class Asteroids():
    """Object representing an asteroids map"""

    def __init__(self, text=None, verbose=False):

        # 1. Set the initial values
        self.rows = 0
        self.cols = 0
        self.knts = []
        self.amap = []

        # 2. If we have text, set the rows, cols, and amap
        if text is not None:
            self.cols = len(text[0])
            for row in text:
                assert len(row) == self.cols
                self.amap.append(row)
            self.rows = len(self.amap)

        # 3. Set knts array from amap
        self.knts = self.set_counts(verbose)
        assert len(self.knts) == self.rows
        if self.rows:
            assert len(self.knts[0]) == self.cols

    def __str__(self):
        return '\n'.join(self.amap)

    def set_counts(self, verbose=False):
        "Set the counts of detectable asteroids"

        # 1. Initialize the counts to zero
        knts = [[0 for c in range(self.cols)] for r in range(self.rows)]

        # 2. Loop for the rows
        for rnum, row in enumerate(self.amap):
            if verbose:
                print("Processing row %3d: %s", (rnum, row))

            # 3. All asteroids on this row can see those on the next row
            self.add_next_row(knts, rnum)

            # 4. We can see at most one to the right
            self.add_to_the_right(knts, rnum)

        # 9. Return the counts
        return knts

    def add_to_the_right(self, knts, row):
        "We can see at most one to the right and they can see up"

        # 1. Get this row
        row_map = self.amap[row]

        # 2. Loop for all of the columns in the row with an asteroid
        for col_me in range(self.cols):
            if row_map[col_me] != '#':
                continue


            # 3. Loop for the columns tp the right looking for an asteroid
            for col_you in range(col_me+1, self.cols):
                if row_map[col_you] != '#':
                    continue

                # 4. I can see you and you can see me
                knts[row][col_me] += 1
                knts[row][col_you] += 1

                # 5. There can be only one
                break

    def add_next_row(self, knts, row):
        "We can see all the astroids in the next row and they can see us"

        # 1. Exit early if no next row
        #print("row = %d, rows = %d" % (row, self.rows))
        if row >= self.rows - 1:
            return

        # 2. Determine the number of astroids in this row and the next
        nxt = row + 1
        row_map = self.amap[row]
        nxt_map = self.amap[nxt]
        row_knt = Counter(row_map)['#']
        nxt_knt = Counter(nxt_map)['#']
        #print("row = %d, nxt = %d, row_knt = %d, nxt_knt = %d" %
        #      (row, nxt, row_knt, nxt_knt))

        # 3. For all of the asteroids in this row, add count of next row
        #    and for those in the next row add the count of this row
        #print("cols = %d, rows = %d" % (self.cols, self.rows))
        #print("knts[row] = %s" % (knts[row]))
        #print("knts[nxt] = %s" % (knts[nxt]))
        for col in range(self.cols):
            if row_map[col] == '#':
                knts[row][col] += nxt_knt
            if nxt_map[col] == '#':
                knts[nxt][col] += row_knt
        #print("knts[row] = %s" % (knts[row]))
        #print("knts[nxt] = %s" % (knts[nxt]))

    def maximum(self):
        "Return the maximum number of detectable astroids and the station loc"

        # 1. Assume no maximum
        result = (-1, (-1, -1))

        # 2. Loop for all the rows
        for rnum, row in enumerate(self.knts):

            # 3. Compute the row max
            rmax = max(row)

            # 4. If it better that the previous maximum
            if rmax > result[0]:

                # 5. Find the column with the maximum
                for cnum, col in enumerate(row):
                    if col == rmax:

                        # 6. And save the new maximum
                        result = (rmax, (cnum, rnum))
                        break

        # 7. Return (maximum asteroids, (max col, max row))
        if result[0] == -1:
            return None
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    a s t e r o i d s . p y                     end
# ======================================================================
