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


    def explore_beam(self, watch=False, size=10):
        "Explore the tractor beam in a sizexsize grid"

        #
        result = intcode.STOP_INP

        # 1. Loop for all points in the grid
        for row in range(size):
            for col in range(size):

                # 2. Build a new drone
                uav = intcode.IntCode(text=self.program)

                # 3. Run the drone with this input
                result = uav.run(inp=([col, row]))
                if result != intcode.STOP_HLT:
                    return result

                # 4. Get the beam effect at this point
                output = uav.outputs()[0]
                if watch:
                    print("Drone at (%d,%d) beam=%d" % (col, row, output))

                # 5. Record the output
                self.beam_map[(col, row)] = output
                self.points += output

        # 6. Return why we stopped
        return result

    def get_points(self):
        "Ruturn the number of beam points found"
        return self.points


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         d r o n e . p y                        end
# ======================================================================
