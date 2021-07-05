# ======================================================================
# Radioisotope Thermoelectric Generators
#   Advent of Code 2016 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s t a t e . p y
# ======================================================================
"State for the Advent of Code 2016 Day 11 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import elevator
import floor

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  State
# ======================================================================


class State(object):   # pylint: disable=R0902, R0205
    "Object for Radioisotope Thermoelectric Generators"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.previous = None
        self.lift = elevator.Elevator
        self.floors = []
        self.items = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:

            # 3. Loop for all the text
            for line in self.text:

                # 4. Process elevator of floor
                if line.startswith("The elevator"):
                    self.lift = elevator.Elevator(text=line, part2=self.part2)
                else:
                    flr = floor.Floor(text=line, part2=self.part2)
                    self.floors.append(flr)
                    self.items.extend(flr.items)

            # 5. put the items in alphabetic order
            self.items.sort()

    def __str__(self):
        result = []
        for flr in self.floors:
            result.append(str(flr))
        result.append(str(self.lift))
        return '\n'.join(result)

    def trace(self):
        "Return the state in trace format"
        result = []
        for flr in self.floors:
            result.append(flt.trace(self.lift, self.items)
        return '\n'.join(result)



# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         s t a t e . p y                        end
# ======================================================================
