
# ======================================================================
# Code Chronicle
#   Advent of Code 2024 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       s c h e m a t i c s . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 25 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
WIDTH = 5
DEPTH = 7
POUND = "#"
POUNDS = POUND * WIDTH
OVERLAP = DEPTH - 2

# ======================================================================
#                                                             Schematics
# ======================================================================


class Schematics(object):   # pylint: disable=R0902, R0205
    "Object for Code Chronicle"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.keys = []
        self.locks = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text()

    def _process_text(self):
        "Assign values from text"

        # 0. Initial conditions
        assert self.text is not None and len(self.text) > 0

        # 1. Start with nothing
        rows = []

        # 2. Loop for all the lines of text
        for line in self.text:

            # 3. If this is a blank line, process the collected rows
            if len(line) == 0:
                if len(rows) > 0:
                    self._process_rows(rows)
                rows = []
                continue

            # 4. Else add the line to the collected rows
            rows.append(line)

        # 5. If we have rows at the end, process thoses
        if len(rows) > 0:
            self._process_rows(rows)

    def _process_rows(self, rows):
        "Assign values from rows of text"

        # 0. Initial conditions
        assert len(rows) == DEPTH
        assert len(rows[0]) == WIDTH

        # 1. Start with nothing
        cols = []

        # 2. Get the column counts
        for col in range(WIDTH):
            cols.append(self.col_height(rows, col))

        # 3. Append the key or lock
        if rows[0] == POUNDS:
            self.locks.append(cols)
        else:
            self.keys.append(cols)

    @staticmethod
    def col_height(rows, col):
        "Returns the height/depth of the column"

        # 0. Initial conditions
        assert len(rows) == DEPTH
        assert len(rows[0]) == WIDTH
        assert 0 <= col < WIDTH

        # 1. Start with nothing
        result = 0

        # 2. Loop for all the rows
        for row in rows:

            # 3. If there is a pin/tumbler, increment col count
            if row[col] == POUND:
                result += 1

        # 4. Return the height/depth ignoring the base row
        return result - 1

    @staticmethod
    def is_overlap(lock, key):
        "Returns True if there is an overlap in the key and lock"

        # 1. Loop for each column
        for col in range(WIDTH):

            # 2. Check for overlap, return True if there is
            if lock[col] + key[col] > OVERLAP:
                return True

        # 3. Looks like a fit
        return False

    def combinations(self):
        "Returns the number of possible key and lock combinations"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the locks and keys
        for lock in self.locks:
            for key in self.keys:

                # 3. Increment count if a possible combination?
                if not self.is_overlap(lock, key):
                    result += 1

        # 4. Return the count of possible combinations
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        return self.combinations()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part two
        return None

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    s c h e m a t i c s . p y                   end
# ======================================================================
