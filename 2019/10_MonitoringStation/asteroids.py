# ======================================================================
# Monitoring Station
#   Advent of Code 2019 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           a s t e r o i d s . p y
# ======================================================================
"Computer for Monitoring Station problem for Advent of Code 2019 Day 10"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import Counter
from math import gcd

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                              Asteroids
# ======================================================================


class Asteroids():
    """Object representing an asteroids map"""

    def __init__(self, text=None, verbose=False, knts=True):

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

        # 3. Start with knts at all zeroes
        self.knts = [[0 for c in range(self.cols)] for r in range(self.rows)]

        # 4. updates the counts
        if knts:
            self.update_counts(verbose)

    def __str__(self):
        return '\n'.join(self.amap)

    def update_counts(self, verbose=False):
        "Update the counts of detectable asteroids"

        # 1. Loop for the rows
        for row_num, row in enumerate(self.amap):
            if verbose:
                print("Processing row %3d: %s" % (row_num, row))

            # 3. All asteroids on this row can see those on the next row
            self.add_next_row(row_num)

            # 4. We can see at most one to the right
            self.add_to_the_right(row_num)

            # 5. We can see at most directly down
            self.add_to_the_bottom(row_num)

            # 6. Look row by row to the bottom looking for more asteroids
            self.add_at_an_angle(row_num)

    def add_to_the_right(self, row):
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
                self.knts[row][col_me] += 1
                self.knts[row][col_you] += 1

                # 5. There can be only one
                break

    def add_to_the_bottom(self, row_me):
        "We can see at most one to the right and they can see up"

        # 1. Exit early if not at least two rows below
        if row_me >= self.rows - 2:
            return

        # 2. Loop for all of the columns in the row with an asteroid
        for col_us, ass_me in enumerate(self.amap[row_me]):
            if ass_me != '#':
                continue

            # 3. If the is an asteroid directly below me, it block any others
            if self.amap[row_me+1][col_us] == '#':
                continue

            # 4. Loop for the remaining rows below
            for row_you in range(row_me+2, self.rows):

                # 5. If this row has no asteroid, continue to the next (if any)
                if self.amap[row_you][col_us] != '#':
                    continue

                # 6. I can see you and you can see me
                self.knts[row_me][col_us] += 1
                self.knts[row_you][col_us] += 1

                # 7. There can be only one
                break

    def add_next_row(self, row):
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
        for col in range(self.cols):
            if row_map[col] == '#':
                self.knts[row][col] += nxt_knt
            if nxt_map[col] == '#':
                self.knts[nxt][col] += row_knt

    def add_at_an_angle(self, row_me):
        "Check if we can see any astroids at an angle"

        # 1. Exit early if not at least two rows below
        #print("row = %d, rows = %d" % (row, self.rows))
        if row_me >= self.rows - 2:
            return

        # 2. Loop for all of the columns in the row with an asteroid
        for col_me, ass_me in enumerate(self.amap[row_me]):
            if ass_me != '#':
                continue

            # 3. Loop for the remaining rows below
            for row_you in range(row_me+2, self.rows):

                # 4. Loop for all of the columns in the lower (you) row
                for col_you, ass_you in enumerate(self.amap[row_you]):

                    # 5. Skip if there is no asteroid or directly below me
                    if ass_you != '#' or col_me == col_you:
                        continue

                    # 6. Check if blockable and blocked
                    row_delta = row_you - row_me
                    col_delta = col_you - col_me
                    gcd_delta = gcd(row_delta, col_delta)
                    if gcd_delta != 1 and self.blocked(col_me, row_me, row_you,
                                                       col_delta//gcd_delta, row_delta//gcd_delta):
                        continue

                    # 7. Increment counts for you and me
                    self.knts[row_me][col_me] += 1
                    self.knts[row_you][col_you] += 1

    def blocked(self, from_col, from_row, to_row, delta_col, delta_row):
        "Return True if there is an asteroid on direct path between from and to"
        #print("blocked: from=(%d,%d) to=(?,%d) delta=(%d,%d)" %
        #      (from_col, from_row, to_row, delta_col, delta_row))

        # 1. Assume not blocked
        result = False

        # 2. Start at the very beginning (a very good place to start)
        next_col = from_col

        # 3. Are there there yet?
        for next_row in range(from_row + delta_row, to_row, delta_row):
            next_col += delta_col

            # 4. Is there an asteroid here?
            if self.amap[next_row][next_col] == '#':
                result = True
                break

        # 5. Return blocked (True) or not blocked (False)
        return result

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

    def str_knts(self):
        "Display nicely formatted counts"

        # 1. Start with nothing
        result = []

        # 2. Loop for every row
        for row_num, row_knts in enumerate(self.knts):
            row = ['%3d:' % row_num]

            # 3. Loop for every column
            for col_knt in row_knts:

                # 4. Add column count
                row.append("%4d" % col_knt)

            # 5. Add the row of counts
            result.append(' '.join(row))

        # 6. Return all the counts
        return '\n'.join(result)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    a s t e r o i d s . p y                     end
# ======================================================================
