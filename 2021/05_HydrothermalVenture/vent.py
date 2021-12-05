# ======================================================================
# Hydrothermal Venture
#   Advent of Code 2021 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         v e n t . p y
# ======================================================================
"Vent for the Advent of Code 2021 Day 05 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
RE_INPUT = re.compile("([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)")

# ======================================================================
#                                                                   Vent
# ======================================================================


class Vent(object):   # pylint: disable=R0902, R0205
    "Object for Hydrothermal Venture"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.locs = set()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Parse the text
        match = RE_INPUT.match(text)
        if match is None:
            print("Unable to parse", text)
            return

        # 2. Get the values
        values = [int(x) for x in match.groups()]

        # 3. Determine the differences
        min_x = min(values[0], values[2])
        max_x = max(values[0], values[2])
        min_y = min(values[1], values[3])
        max_y = max(values[1], values[3])

        # 3. Fill out the vertical lines
        if min_x == max_x:
            for y_index in range(min_y, max_y + 1):
                self.locs.add((min_x, y_index))

        # 4. Fill out the horizontal lines
        elif min_y == max_y:
            for x_index in range(min_x, max_x + 1):
                self.locs.add((x_index, min_y))

        # 5. Part 2 adds diagonal lines
        elif self.part2:
            if min_x == values[0]:
                y_start = values[1]
                y_end = values[3]
            else:
                y_start = values[3]
                y_end = values[1]
            if y_start > y_end:
                y_delta = -1
            else:
                y_delta = 1
            y_index = y_start
            for x_index in range(min_x, max_x + 1):
                self.locs.add((x_index, y_index))
                y_index += y_delta
        #print(text, self.locs)

    def __len__(self):
        return len(self.locs)

    def __in__(self, value):
        return value in self.locs


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          v e n t . p y                         end
# ======================================================================
