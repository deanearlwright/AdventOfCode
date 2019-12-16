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
            if pan.loc[0] < min_col:
                min_col = pan.loc[0]
            if pan.loc[0] > max_col:
                max_col = pan.loc[0]
            if pan.loc[1] < min_row:
                min_row = pan.loc[1]
            if pan.loc[1] > max_row:
                max_row = pan.loc[1]

        # 3. Loop for all of the rows
        for row_num in range(min_row, max_row+1):
            row = []

            # 4. Loop for all of the columns in the row
            for col_num in range(min_col, max_col+1):
                loc = (col_num, row_num)
                if loc in self.panels:
                    row.append(str(self.panels[loc]))
                else:
                    row.append(' ')

            # 5. Add row to result
            result.append(''.join(row))

        # 6. Return the image
        return '\n'.join(result)

    def color(self, loc):
        "Get the color of a panel"

        # 1. If we don't have the current panel, create it
        if loc not in self.panels:
            self.panels[loc] = panel.Panel(loc=loc)

        # 2. Return the color of the panel
        return self.panels[loc].color()

    def paint(self, loc, color):
        "Paint a panel"

        # 0. Preconditions
        assert color in panel.COLORS

        # 1. If we don't have the current panel, create it
        if loc not in self.panels:
            self.panels[loc] = panel.Panel(loc=loc)

        # 2. Pain the panel
        self.panels[loc].paint(color=color)

    def at_least_once(self):
        "Return the number of panels painter at least one"

        # 1. Start with none
        result = 0

        # 2. Loop for all the panels
        for pan in self.panels.values():

            # 3. if panel has been painted, add it to the count
            if pan.painted:
                result += 1

        # 4. Return number of painted panels
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         s h i p . p y                          end
# ======================================================================
