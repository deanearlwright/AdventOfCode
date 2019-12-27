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

INNER_OUTER = 5

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
        self.cols = max([len(self.text[_]) for _ in range(self.rows)])
        for rnum in range(self.rows):
            self.text[rnum] = self.text[rnum].ljust(self.cols)

        # 5. Loop for all the rows and process them
        for rnum, row in enumerate(self.text):
            self.process_row(rnum, row)

        # 6. Loop for all of the columns and process them for portals
        for cnum in range(self.cols):
            cdata = []
            for rrnum in range(self.rows):
                cdata.append(self.text[rrnum][cnum])
            self.process_col(cnum, ''.join(cdata))

        # 7. Connect the path squares
        self.process_path()

    def process_row(self, rnum, row):
        "Process one row of the text"

        # 1. Start with no label in the works
        second = None
        label = None
        last_passage = -1
        last_void = -1

        # 2. Loop for all of the columns
        for cnum, col in enumerate(row):

            # 3, If this is the second letter of a label, ignore it
            if cnum == second:
                second = None
                continue

            # 4. If we find a passage square, add that location
            if col == PASSAGE:
                self.add_loc(cnum, rnum)
                last_passage = cnum

                # 5. If we are processing a left hand portal, add it
                if label:
                    self.add_portal(label, cnum, rnum)
                    label = None

            # 6. if a void, remember it
            elif col == VOID:
                last_void = cnum

            # 7. If this is the start of a label, get it
            elif col.isupper() and row[cnum + 1].isupper():
                label = col + row[cnum + 1]
                second = cnum + 1

                # 8. If we are processing a right hand portal, add it
                if last_passage > last_void:
                    self.add_portal(label, last_passage, rnum)
                    label = None
                elif last_void > last_passage:
                    self.add_portal(label, cnum + 2, rnum)
                    label = None

    def process_col(self, cnum, col):
        "Process one col of the text"

        # 1. Start with no label in the works
        second = None
        label = None
        last_passage = -1
        last_void = -1

        # 2. Loop for all of the rows
        for rnum, row in enumerate(col):

            # 3, If this is the second letter of a label, ignore it
            if rnum == second:
                second = None
                continue

            # 4. If we find a passage square, remember it (but don't add it)
            if row == PASSAGE:
                last_passage = rnum

                # 5. If we are processing a top portal, add it
                if label:
                    self.add_portal(label, cnum, rnum)
                    label = None

            # 6. If this is in the void, remember it
            elif row == VOID:
                last_void = rnum

            # 7. If this is the start of a label, get it
            elif row.isupper() and col[rnum + 1].isupper():
                label = row + col[rnum + 1]
                second = rnum + 1

                # 7. If we are processing a bottom portal, add it
                if last_passage > last_void:
                    self.add_portal(label, cnum, last_passage)
                    label = None
                elif last_void > last_passage:
                    self.add_portal(label, cnum, rnum + 2)
                    label = None

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

                # 4. Set direction in location
                at_delta = self.at_loc(d_col, d_row)
                if at_delta.isalpha():
                    other = self.other_end(l_col, l_row)
                    if other is not None:
                        loc.set_dir(direction, PASSAGE)
                    else:
                        loc.set_dir(direction, WALL)
                else:
                    loc.set_dir(direction, self.at_loc(d_col, d_row))

    def other_end(self, col, row):
        "Return what is at the other end of the portal"

        # 1. Get the name of the portal
        name = self.portals_at[(col, row)]

        # 2. Look up the ends of this portal
        ends = self.portals[name]

        # 3. Get the other end of the portal
        other = None
        for end in ends:
            if end != (col, row):
                other = end

        # 4. Return the other end (if any)
        return other

    def add_loc(self, col, row):
        "Add a passage square at this location"

        self.locs[(col, row)] = location.Location((col, row))

    @staticmethod
    def delta_loc(col, row, exit_dir):
        "return the col and row in that direction"

        return (col + DELTA[exit_dir][0], row + DELTA[exit_dir][1])

    def exit_dirs(self, col, row):
        "Return the directions to non-portal locations"

        # 1. Return  the exits from this location
        return self.locs[(col, row)].exits_at()

    def exit_locs(self, col, row):
        # Return were you can go

        return [Donut.delta_loc(col, row, exit) for exit in self.exit_dirs(col, row)
                if Donut.delta_loc(col, row, exit) in self.locs]

    def non_portals(self, col, row):
        "Return the directions to non-portal locations"

        # 1. Get the exits from this location
        exits = self.locs[(col, row)].exits_at()

        # 2. Return non-portal exits
        return [exit for exit in exits
                if Donut.delta_loc(col, row, exit) not in self.portals_at]

    def inner_portal(self, loc):
        "Return True is an inner portal"

        return not self.outer_portal(loc)

    def outer_portal(self, loc):
        "Return True if an outer portal"

        return loc[0] < INNER_OUTER or \
            loc[1] < INNER_OUTER or \
            loc[0] > self.cols - INNER_OUTER or \
            loc[1] > self.rows - INNER_OUTER


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        d o n u t . p y                         end
# ======================================================================
