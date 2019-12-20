# ======================================================================
# Oxygen System
#   Advent of Code 2019 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                            s h i p . p y
# ======================================================================
"Ship for droid to explore in Space Police problem for AoC 2019 Day 15"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import location

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Ship
# ======================================================================


class Ship():
    """Object representing the interoid of the space ship"""

    def __init__(self):

        # 1. Set the initial area
        self.area = {}


    def __str__(self):

        # 1. Start with nothing
        result = []

        # 2. Determine boundaries of the image
        min_col = 9999999
        min_row = 9999999
        max_col = -999999
        max_row = -999999
        for loc in self.area.values():
            if loc.loc[0] < min_col:
                min_col = loc.loc[0]
            if loc.loc[0] > max_col:
                max_col = loc.loc[0]
            if loc.loc[1] < min_row:
                min_row = loc.loc[1]
            if loc.loc[1] > max_row:
                max_row = loc.loc[1]

        # 3. Loop for all of the rows
        for row_num in range(min_row, max_row+1):
            row = []

            # 4. Loop for all of the columns in the row
            for col_num in range(min_col, max_col+1):
                loc = (col_num, row_num)
                if loc in self.area:
                    row.append(str(self.area[loc]))
                else:
                    row.append(' ')

            # 5. Add row to result
            result.append(''.join(row))

        # 6. Return the image
        return '\n'.join(result)

    def record_wall(self, loc, direction):
        "We bumped into a wall"

        # 1. If we don't have the current location, create it
        if loc not in self.area:
            self.area[loc] = location.Location(loc=loc)

        # 2. Record  the wall
        self.area[loc].set_wall(direction)
        #self.area[loc].set_dir(direction, location.IS_WALL)

    def record_move(self, loc, direction, new_loc, oxygen):
        "We managed to move"

        # 1. If we don't have the current location, create it
        if loc not in self.area:
            self.area[loc] = location.Location(loc=loc)
        if new_loc not in self.area:
            self.area[new_loc] = location.Location(loc=new_loc)

        # 2. Move forward
        if oxygen:
            at_fwd = location.IS_OXYGEN
        else:
            at_fwd = location.IS_FWD
        self.area[loc].set_dir(direction, at_fwd)

        # 3. Record the reverse movement
        self.area[new_loc].set_back(direction)

    def explore(self, loc):
        "Return the unkown directions from this location"
        return self.area[loc].unknown()

    def go_back(self, loc):
        "Return the direction to go back"
        return self.area[loc].back()

    def exits_at(self, loc):
        "Return direction that exit the location"
        return self.area[loc].exits_at()

    def oxygen_at(self, loc):
        "Return direction that exit the location"
        return self.area[loc].oxygen_at()

    def set_oxygen_time(self, loc, o_time):
        "Set when oxygen reached this location"
        self.area[loc].set_oxygen_time(o_time)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         s h i p . p y                          end
# ======================================================================
