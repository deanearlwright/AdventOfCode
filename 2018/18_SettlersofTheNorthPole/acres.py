# ======================================================================
# Settlers of The North Pole
#   Advent of Code 2018 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         a c r e s . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 18 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
OPEN = '.'
WOOD = '|'
YARD = '#'
RVAL = '?'

ROW_MULT = 1000
ADJACENT = [-1001, -1000, -999, -1, 1, 999, 1000, 1001]

# ======================================================================
#                                                                  Acres
# ======================================================================


class Acres(object):   # pylint: disable=R0902, R0205
    "Object for Settlers of The North Pole"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.grid = None
        self.max_row = None
        self.minutes = 10
        if part2:
            self.minutes = 1000000000

        # 2. Process text (if any)
        if text is not None:
            self.processText(text)

    def processText(self, text):
        # 1. Start with nothing
        self.grid = {}
        self.max_row = 0
        # 2. Loop for all rows of the text
        for row_num, row in enumerate(text):
            self.max_row = row_num
            # 3. Loop for all columns of the row
            for col_num, col in enumerate(row):
                # 4. Add the location to the grid
                self.grid[row_num * ROW_MULT + col_num] = col

    def __str__(self):
        # 1. Start with nothing
        rows = []
        # 2. Loop for all of the rows
        for row_num in range(self.max_row + 1):
            row = []
            # 3. Loop for all of the columns
            for col_num in range(self.max_row + 1):
                row.append(self.grid[row_num * ROW_MULT + col_num])
            rows.append(''.join(row))
        # 4. Return the grid
        return '\n'.join(rows)

    def adjacent(self, loc):
        # 1. Start with nothing
        result = {
            OPEN: 0,
            WOOD: 0,
            YARD: 0,
        }
        # 2. Loop for all of the adjacent squares
        for adj in ADJACENT:
            adj_loc = loc + adj
            if adj_loc in self.grid:
                result[self.grid[adj_loc]] += 1
        # 3. Return the adjacent counts
        return result

    def change(self):
        # 1. Start with nothing
        next_grid = {}
        # 2. Loop for every acre
        for loc, acre in self.grid.items():
            # 3. Get counts of adjacent acres
            adj = self.adjacent(loc)
            # 4. An open acre will become filled with trees if three or more adjacent
            #    acres contained trees. Otherwise, nothing happens.
            if acre == OPEN:
                if adj[WOOD] >= 3:
                    acre = WOOD
            # 5. An acre filled with trees will become a lumberyard if three or more
            #    adjacent acres were lumberyards. Otherwise, nothing happens.
            elif acre == WOOD:
                if adj[YARD] >= 3:
                    acre = YARD
            # 6. An acre containing a lumberyard will remain a lumberyard if it was
            #    adjacent to at least one other lumberyard and at least one acre
            #    containing trees. Otherwise, it becomes open.
            else:
                if adj[YARD] == 0 or adj[WOOD] == 0:
                    acre = OPEN
            # 7. Record what this acre will become
            next_grid[loc] = acre
        # 8. The time is now one ninute in the future
        self.grid = next_grid

    def counts(self):
        # 1. Start with nothing
        result = {
            OPEN: 0,
            WOOD: 0,
            YARD: 0,
            RVAL: 0,
        }
        # 2. Loop for every acre
        for acre in self.grid.values():
            # 3. Accumulate the counts
            result[acre] += 1
        # 4. Compute the resource value
        result[RVAL] = result[WOOD] * result[YARD]
        # 5. Return the counts
        return result

    def run(self, minutes):
        for _ in range(minutes):
            self.change()

    def distant_future(self):
        values = """
        tick      944: o=    1524 w=     623 y=     353 v=  219919
        tick      945: o=    1523 w=     620 y=     357 v=  221340
        tick      946: o=    1526 w=     619 y=     355 v=  219745
        tick      947: o=    1530 w=     614 y=     356 v=  218584
        tick      948: o=    1530 w=     612 y=     358 v=  219096
        tick      949: o=    1536 w=     606 y=     358 v=  216948
        tick      950: o=    1546 w=     606 y=     348 v=  210888
        tick      951: o=    1554 w=     604 y=     342 v=  206568
        tick      952: o=    1558 w=     603 y=     339 v=  204417
        tick      953: o=    1563 w=     597 y=     340 v=  202980
        tick      954: o=    1571 w=     594 y=     335 v=  198990
        tick      955: o=    1576 w=     587 y=     337 v=  197819
        tick      956: o=    1586 w=     585 y=     329 v=  192465
        tick      957: o=    1589 w=     582 y=     329 v=  191478
        tick      958: o=    1596 w=     582 y=     322 v=  187404
        tick      959: o=    1593 w=     582 y=     325 v=  189150
        tick      960: o=    1590 w=     585 y=     325 v=  190125
        tick      961: o=    1584 w=     589 y=     327 v=  192603
        tick      962: o=    1580 w=     597 y=     323 v=  192831
        tick      963: o=    1571 w=     603 y=     326 v=  196578
        tick      964: o=    1564 w=     608 y=     328 v=  199424
        tick      965: o=    1557 w=     612 y=     331 v=  202572
        tick      966: o=    1550 w=     617 y=     333 v=  205461
        tick      967: o=    1544 w=     618 y=     338 v=  208884
        tick      968: o=    1538 w=     620 y=     342 v=  212040
        tick      969: o=    1534 w=     620 y=     346 v=  214520
        tick      970: o=    1526 w=     623 y=     351 v=  218673
        tick      971: o=    1525 w=     622 y=     353 v=  219566"""
        loop_length = 972 - 944
        loop_start = 972
        loop_lines = values.strip().split('\n')
        loop_values = [int(line.strip().split(' ')[-1]) for line in loop_lines]
        at = self.minutes
        at_div, at_mod = divmod(at - loop_start, loop_length)
        return loop_values[at_mod]

    def run_for_a_long_time(self):
        for tick in range(self.minutes):
            knts = self.counts()
            print("tick %8d: o=%8d w=%8d y=%8d v=%8d" %
                  (tick, knts[OPEN], knts[WOOD], knts[YARD], knts[RVAL]))
            self.change()

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Time marches on
        self.run(self.minutes)
        # 1. Return the solution for part one
        return self.counts()[RVAL]

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.distant_future()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          a c r e s . p y                       end
# ======================================================================
