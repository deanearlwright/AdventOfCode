# ======================================================================
# Seating System
#   Advent of Code 2020 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c o n w a y . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 11 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
FLOOR = '.'
EMPTY = 'L'
OCCUP = '#'

DELTA = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]

# ======================================================================
#                                                                 Conway
# ======================================================================


class Conway(object):   # pylint: disable=R0902, R0205
    "Object for Seating System"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rows = 0
        self.cols = 0
        self.rnds = 0
        self.seats = set()
        self.current = set()
        self.previous = None
        self.limit = 4
        if part2:
            self.limit = 5

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.process_text(text)

    def process_text(self, text):
        "Get location of the seats"
        self.rows = len(text)
        self.cols = len(text[0])
        self.seats = set()
        for row, line in enumerate(text):
            assert len(line) == self.cols
            for col, space in enumerate(line):
                if space == EMPTY:
                    self.seats.add((col, row))

    def fill_all_seats(self):
        "Butts in seats"
        self.previous = set()
        self.current = set()
        for location in self.seats:
            self.current.add(location)
        self.rnds = 1

    def count_occupied(self):
        "Return total number of occupied seats"
        return len(self.current)

    def adjacent(self, loc):
        "Return the number of adjacent occupied seats"
        result = 0
        for delta in DELTA:
            if self.nearby(loc, delta):
                result += 1
        return result

    def nearby(self, loc, delta):
        "Returns True if the nearby seat is occupied"
        # 1. Determine the adjacent location
        nloc = (loc[0] + delta[0], loc[1] + delta[1])
        # 2. Part one only cares about that location
        if not self.part2:
            return nloc in self.current
        # 3. Part 2 takes a longer view
        while self.in_bounds(nloc):
            if nloc in self.current:
                return True
            if nloc in self.seats:
                return False
            nloc = (nloc[0] + delta[0], nloc[1] + delta[1])
        return False

    def in_bounds(self, loc):
        "Returns True is location is in the seating area"
        col, row = loc
        if col < 0 or row < 0 or col >= self.cols or row >= self.rows:
            return False
        return True

    def next_round(self):
        "Ring a round the rosy"

        # 1. Save the current status
        self.previous = self.current.copy()

        # 2. Start with a clean slate
        nxt = set()

        # 3. See if an occupied seat stays occupied
        for loc in self.current:
            if self.adjacent(loc) < self.limit:
                nxt.add(loc)

        # 4. See if an empty seat gets filled
        for loc in self.seats:
            if loc not in self.current:
                if self.adjacent(loc) == 0:
                    nxt.add(loc)

        # 5. Finish the round
        self.current = nxt
        self.rnds += 1

    def unchanged(self):
        "Returns True if there have been no changes in seating"
        return self.current == self.previous

    def run_until_no_change(self):
        "Run the simulation until no change in seating and return the number of seats"
        self.fill_all_seats()
        while not self.unchanged():
            self.next_round()
        return self.count_occupied()

    def __str__(self):
        result = []
        for row in range(self.rows):
            line = []
            for col in range(self.cols):
                loc = (col, row)
                if loc not in self.seats:
                    line.append(FLOOR)
                elif loc in self.current:
                    line.append(OCCUP)
                else:
                    line.append(EMPTY)
            result.append(''.join(line))
        return '\n'.join(result)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.run_until_no_change()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.run_until_no_change()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        c o n w a y . p y                       end
# ======================================================================
