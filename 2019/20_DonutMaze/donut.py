# ======================================================================
# Donut Maze
#   Advent of Code 2019 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                            d o n u t . p y
# ======================================================================
"Donut Maze for Advent of Code 2019 Day 20"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import location

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
START = 'AA'
FINISH = 'ZZ'

VOID = ' '
WALL = '#'
PASSAGE = '.'

DELTA = {
    'N': (0, -1),
    'S': (0, 1),
    'W': (-1, 0),
    'E': (1, 0)
}

# ======================================================================
#                                                                  Donut
# ======================================================================


class Donut():
    """Object representing the teleporting donut maze"""

    def __init__(self, text=None, part2=False):

        # 1. Set the initial area
        self.text = text
        self.rows = 0
        self.cols = 0
        self.portals = {}
        self.start = START
        self.finish = FINISH
        self.locs = {}
        self.portals_at = {}
        self.part2 = part2

        # 2. If there is a text map of the donut, process it
        if self.text:
            self.process_text()

    def process_text(self, text=None):
        "Process the text we have (or new text)"

        # 1. Is there new text?
        if text:
            self.text = text

        # 2. Really, any text at all
        if not self.text:
            return

        # 3. Start the other elements as empty
        self.portals = {}
        self.locs = {}
        self.portals_at = {}

        # 4. Set Rows and Columns
        self.rows = len(self.text)
        #print("[%s]" % (self.text[0]))
        self.cols = len(self.text[0])

        # 5. Loop for all the rows and process them
        for rnum, row in enumerate(self.text):
            self.process_row(rnum, row)

        # 6. Loop for all of the columns and process them for portals
        for cnum in range(self.cols):
            self.process_col(cnum, ''.join([self.text[range(self.rows)][cnum]]))

        # 7. Connect the path squares
        self.process_path()

    def process_row(self, rnum, row):
        "Process one row of the text"

        # 1. Start with no label in the works
        second = None
        label = None
        last_loc = None

        # 2. Loop for all of the columns
        for cnum, col in enumerate(row):

            # 3, If this is the second letter of a label, ignore it
            if cnum == second:
                second = None
                continue

            # 4. If we find a passage square, add that location
            if col == PASSAGE:
                self.add_loc(cnum, rnum)
                last_loc = cnum

                # 5. If we are processing a left hand portal, add it
                if label:
                    self.add_portal(label, cnum, rnum)
                    label = None
                    last_loc = None

            # 6. If this is the start of a label, get it
            elif col.isupper():
                label = col + row[cnum+1]
                second = col + 1

                # 7. If we are processing a right hand portal, add it
                if last_loc:
                    self.add_portal(label, last_loc, rnum)
                    label = None
                    last_loc = None

    def process_col(self, cnum, col):
        "Process one col of the text"

        # 1. Start with no label in the works
        second = None
        label = None
        last_loc = None

        # 2. Loop for all of the rows
        for rnum, row in enumerate(col):

            # 3, If this is the second letter of a label, ignore it
            if rnum == second:
                second = None
                continue

            # 4. If we find a passage square, remember it (but don't add it)
            if row == PASSAGE:
                last_loc = rnum

                # 5. If we are processing a top portal, add it
                if label:
                    self.add_portal(label, cnum, rnum)
                    label = None
                    last_loc = None

            # 6. If this is the start of a label, get it
            elif row.isupper():
                label = row + col[rnum+1]
                second = rnum + 1

                # 7. If we are processing a bottom portal, add it
                if last_loc:
                    self.add_portal(label, cnum, last_loc)
                    label = None
                    last_loc = None

    def add_portal(self, label, col, row):
        "Add a portal"

        # 1. If the portal already exits, set this as second location
        if label in self.portals:
            self.portals[label].add((col, row))

        # 2. Else add the portal with this as the only location
        else:
            self.portals[label] = set([(col, row)])

        # 3. Add entry to the location to portal map
        self.portals_at[(col, row)] = label

    def at_loc(self, col, row):
        "Check if there is a wall or path at location"

        return self.text[row][col]

    def process_path(self):
        "Connect the paths -- note: we assume walls/void all around"

        # 1. Loop for all of the locations (with are paths and only paths)
        for loc in self.locs.values():
            l_col = loc.loc[0]
            l_row = loc.loc[1]

            # 2. Loop for each of the four cardinal directions
            for direction, delta in DELTA.items():

                # 3. Calculate the location in that direction
                #print("l=(%d,%d) dir=%s delta=%s" % (l_col, l_row, direction, delta))
                d_col = l_col + delta[0]
                d_row = l_row + delta[1]

                # 4. Set direction in locatation
                loc.set_dir(direction, self.at_loc(d_col, d_row))

    def add_loc(self, col, row):
        "Add a passage square at this location"

        self.locs[(col, row)] = location.Location((col, row))



# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        d o n u t . p y                         end
# ======================================================================
