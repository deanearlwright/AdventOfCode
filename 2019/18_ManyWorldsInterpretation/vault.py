# ======================================================================
# Many-Worlds Interpretation
#   Advent of Code 2019 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                            v a u l t . p y
# ======================================================================
"Many-Worlds Interpretation Vault Maze for Advent of Code 2019 Day 18"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import location

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
ORIGIN = '@'
WALL = '#'
PATH = '.'

DELTA = {
    'N': (0, -1),
    'S': (0, 1),
    'W': (-1, 0),
    'E': (1, 0)
}

PART2 = ["@#@","###","@#@"]

# ======================================================================
#                                                                  Vault
# ======================================================================


class Vault():
    """Object representing the key and Door vault"""

    def __init__(self, text=None, part2=False):

        # 1. Set the initial area
        self.text = text
        self.rows = 0
        self.cols = 0
        self.clean = None
        self.keys = {}
        self.doors = {}
        self.origin = None
        self.origins = None
        self.locs = {}
        self.key_at = {}
        self.door_at = {}

        # 2. If there is a text map of the vault, process it
        if self.text:
            self.process_text(part2=part2)

    def process_text(self, text=None, part2=False):
        "Process the text we have (or new text)"

        # 1. Is there new text?
        if text:
            self.text = text

        # 2. Really, any text at all
        if not self.text:
            return

        # 3. Set Rows and Columns
        self.rows = len(self.text)
        #print("[%s]" % (self.text[0]))
        self.cols = len(self.text[0])

        # 4. Start the other elements as empty
        self.clean = []
        self.keys = {}
        self.key_at = {}
        self.doors = {}
        self.door_at = {}
        self.origin = None
        self.origins = None
        self.locs = {}

        # 5. Is this a a part two maze, redo the middle
        if part2:
            self.mess_with_middle_of_maze()

        # 6. Loop for all the rows and process them
        for rnum, row in enumerate(self.text):
            self.clean.append(self.process_row(rnum, row))

        # 7. Connect the path squares
        self.process_path()

    def mess_with_middle_of_maze(self):
        "Alter the middle of the maze to create four sub-mazes"

        # 1. Find the original origin of the maze
        for rnum, row in enumerate(self.text):
            if ORIGIN not in row:
                continue
            origin_row = rnum
            origin_col = row.index(ORIGIN)

            # 2. Replace the original text around the origin
            self.text[rnum-1] = self.text[rnum-1][:origin_col-1] + PART2[0] + self.text[rnum-1][origin_col+2:]
            self.text[rnum] = self.text[rnum][:origin_col-1] + PART2[1] + self.text[rnum][origin_col+2:]
            self.text[rnum+1] = self.text[rnum+1][:origin_col-1] + PART2[2] + self.text[rnum+1][origin_col+2:]

            # 3. Set the multiple origins
            self.origins = [(origin_col-1, origin_row-1), (origin_col+1, origin_row-1),
                            (origin_col-1, origin_row+1), (origin_col+1, origin_row+1)]

            # 4. Thats all we need to do
            #print('\n'.join(self.text))
            break

    def process_row(self, rnum, row):
        "Process one row of the text"

        # 1. Assume that we will be clean (or close to it)
        clean = []

        # 2. Loop for all of the columns
        for cnum, col in enumerate(row):

            # 3. Process what we find at that column
            if col == ORIGIN:
                self.origin = (cnum, rnum)
                clean_col = PATH
            elif col.islower():
                self.add_key(col, cnum, rnum)
                clean_col = PATH
            elif col.isupper():
                self.add_door(col, cnum, rnum)
                clean_col = PATH
            else:
                clean_col = col

            # 4. If the cleaned square is a path, add it
            if clean_col == PATH:
                self.add_path(cnum, rnum)

            # 5. Add the clean column
            clean.append(clean_col)

        # 6. return the cleaned row
        return ''.join(clean)

    def at_loc(self, col, row):
        "Check if there is a wall or path at location"

        return self.clean[row][col]

    def process_path(self):
        "Connect the paths -- note: we assume walls all around"

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

    def add_key(self, key, col, row):
        "Add a key at this location"

        self.keys[key] = (col, row)
        self.key_at[(col, row)] = key

    def add_door(self, door, col, row):
        "Add a door at this location"

        self.doors[door.lower()] = (col, row)
        self.door_at[(col, row)] = door.lower()

    def add_path(self, col, row):
        "Add a path square at this location"

        self.locs[(col, row)] = location.Location((col, row))



# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        v a u l t . p y                         end
# ======================================================================
