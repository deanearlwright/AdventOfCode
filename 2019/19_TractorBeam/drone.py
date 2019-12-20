# ======================================================================
# Tractor Beam
#   Advent of Code 2019 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                            d r o n e . p y
# ======================================================================
"Drone for Tractor Beam problem for Advent of Code 2019 Day 19"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import intcode

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
SANTA = 100

# ======================================================================
#                                                                  Drone
# ======================================================================


class Drone():
    """Object representing tractor beam exploring drome"""

    def __init__(self, text=None):

        # 1. Set the initial values
        self.program = text
        self.beam_map = {}
        self.points = 0
        self.drones = 0


    def explore_beam(self, watch=False, size=10):
        "Explore the tractor beam in a sizexsize grid"

        # 1. Loop for all points in the grid
        for row in range(size):
            for col in range(size):

                # 2. Get the beam effect at this point
                output = self.check_loc(col, row)
                if watch:
                    print("Drone at (%d,%d) beam=%d" % (col, row, output))

        # 6. Return the number of points
        return self.points

    def check_loc(self, col, row):
        "Check a location, dispathing a drone if necessary"

        # 1. If we already know what happens at a location, just return it
        if (col, row) in self.beam_map:
            #print("(%d,%d) already mapped as %d" % (col, row, self.beam_map[(col, row)]))
            return self.beam_map[(col, row)]

        # 2. Build a new drone
        #print("Building a drone to check (%d,%d)" % (col, row))
        uav = intcode.IntCode(text=self.program)
        self.drones += 1

        # 3. Run the drone with this input
        result = uav.run(inp=([col, row]))
        if result != intcode.STOP_HLT:
            print("drone stopped with %d for (%d,%d)" % (result, col, row))
            return 0

        # 4. Get the beam effect at this point
        output = uav.outputs()[0]

        # 5. Record the output
        self.beam_map[(col, row)] = output
        self.points += output

        # 6. Return output (0 if no beam, 1 if beam)
        return output

    def find_row_left(self, row):
        "Check a location, dispathing a drone if necessary"

        # 1. Check the diagonal
        if self.check_loc(row, row):

            # 2. Work to left to find the last beamed location
            col = row
            while col >= 0 and self.check_loc(col, row):
                col -= 1
            return col + 1

        # 2. Else look from the left
        col = 0
        for col in range(row*row):
            if self.check_loc(col, row):
                return col

        # 3. Should never happen
        return 0

    def wide_enough(self, col, row, size=SANTA):
        "See if the beam at the row is wide enough for Santa"

        # 1. Return True if wide enough
        return self.check_loc(col, row) == 1 and self.check_loc(col+size-1, row) == 1

    def big_enough(self, col, row, size=SANTA):
        "See if the beam here is big enough for Santa"

        # 1. Return True if big enough
        return (self.check_loc(col, row) == 1 and
                self.check_loc(col+size-1, row) == 1 and
                self.check_loc(col, row+size-1) == 1 and
                self.check_loc(col+size-1, row+size-1) == 1)

    def find_santa_size(self, size=SANTA, watch=False):
        "find upper left where the beam is big enough for Santa"

        # 1. Loop over the rows
        for row in range(10, size*size*size):

            # 2. Find the left most column of the beam
            left = self.find_row_left(row)
            if watch:
                print("Left most column of row %d is %d" % (row, left))

            # 3. Is this row wide enough?
            while self.wide_enough(left, row, size=size):
                if watch:
                    print("Row %d (col=%d) is wide enough" % ((row, left)))

                # 4. Is if big enough?
                if self.big_enough(left, row, size=size):
                    if watch:
                        print("Upper left (%d,%d) is big enough" % ((row, left)))
                    return (left, row)

                # 5. Try one column to the right
                left += 1
                if watch:
                    print("Checking row %d col %d for wide enough" % ((row, left)))

        # 6. Should not happen
        return (0, 0)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         d r o n e . p y                        end
# ======================================================================
