# ======================================================================
# Mode Maze
#   Advent of Code 2018 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c a v e . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 22 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import path

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
ROW_MULT = 10000
TOOL_MULT = ROW_MULT * ROW_MULT
MOUTH = 0


ROCKY_CHAR = '.'
WET_CHAR = '='
NARROW_CHAR = '|'
MOUTH_CHAR = 'M'
TARGET_CHAR = 'T'

GEOLOGIC = 0
EROSION = 1
RTYPE = 2

ROCKY_TYPE = 0
WET_TYPE = 1
NARROW_TYPE = 2
RTYPE_CHARS = [ROCKY_CHAR, WET_CHAR, NARROW_CHAR] # Indexed by erosion level
RISK_LEVEL = [0, 1, 2] # indexed by region type

NEITHER = 0
TORCH = 1
GEAR = 2
TOOLS = [NEITHER, TORCH, GEAR]
TOOL_LOC = [t * TOOL_MULT for t in TOOLS] # Indexed by tool number
FORBIDDEN_TOOL = [NEITHER, TORCH, GEAR] # Indexed by region type
VALID_TOOLS = [[TORCH, GEAR], [NEITHER, GEAR], [NEITHER, TORCH]] # Indexed by region type
TOOL_CHARS = ['N', 'T', 'G'] # Indexed by tool number

DELTA = [-ROW_MULT, ROW_MULT, 1, -1]
DELTAROW0 = [ROW_MULT, 1, -1]
DELTACOL0 = [-ROW_MULT, ROW_MULT, 1]
DELTAMOUTH = [ROW_MULT, 1]

PAST_TARGET = 50
# ----------------------------------------------------------------------
#                                                      utility functions
# ----------------------------------------------------------------------
def loc_to_row_col(loc):
    row, col = divmod(no_tool(loc), ROW_MULT)
    return row, col

def row_col_to_loc(row, col):
    return row * ROW_MULT + col

def str_loc(loc):
    row, col = loc_to_row_col(loc)
    return "(r%d,c%d)" % (row, col)

def loc_to_row_col_tool(loc):
    tool, rc = divmod(loc, TOOL_MULT)
    row, col = divmod(rc, ROW_MULT)
    return row, col, tool

def row_col_tool_to_loc(row, col, tool):
    return row * ROW_MULT + col + TOOL_LOC[tool]

def determine_delta(loc):
    row, col = loc_to_row_col(loc)
    if row == 0 and col == 0:
        return DELTAMOUTH
    if row == 0:
        return DELTAROW0
    if col == 0:
        return DELTACOL0
    return DELTA

def no_tool(loc):
    return loc % TOOL_MULT

def just_tool(loc):
    return loc // TOOL_MULT

def delta_time(loc1, loc2):
    if no_tool(loc1) == no_tool(loc2):
        return 7
    return 1


# ======================================================================
#                                                                   Cave
# ======================================================================


class Cave(object):   # pylint: disable=R0902, R0205
    "Object for Mode Maze"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.depth = None
        self.target = None
        self.mouth = None
        self.regions = None
        self.start = None
        self.finish = None
        self.maxrow = None
        self.maxcol = None

        # 2. Process text (if any)
        if text is not None and len(text) == 2:
            self.depth = int(text[0].split(' ')[1])
            rowcol = text[1].split(' ')[1].split(',')
            self.target = row_col_to_loc(int(rowcol[1]), int(rowcol[0]))
            self.mouth = MOUTH
            self.regions = {}
            if part2:
                self.start = self.mouth + TOOL_LOC[TORCH]
                self.finish = self.target + TOOL_LOC[TORCH]
                trow, tcol = loc_to_row_col(self.target)
                self.maxrow = trow + PAST_TARGET
                self.maxcol = tcol + PAST_TARGET

    def determine_region_type(self, loc):
        # 1. If we have already determined the region type, return it
        loc = no_tool(loc)
        if loc in self.regions:
            return self.regions[loc][RTYPE]
        # 2. Get the geologic index
        geologic = self.determine_geologic_index(loc)
        # 3. Compute the erosion level
        erosion = self.compute_erosion_level(geologic)
        # 4. Determine the region type
        result = erosion % 3
        # 5. Save the information
        self.regions[loc] = (geologic, erosion, result)
        # 6. Return the region type
        return result

    def determine_geologic_index(self, loc):
        # 1. If we have already determined the geologic index, return it
        loc = no_tool(loc)
        if loc in self.regions:
            return self.regions[loc][GEOLOGIC]
        # 2. Break location in to row(Y) and col(X)
        row, col = loc_to_row_col(loc)
        # 3. Get the geologic index
        if loc == self.mouth or loc == self.target:
            result = 0
        elif row == 0:
            result = col * 16807
        elif col == 0:
            result = row * 48271
        else:
            result = self.determine_erosion_level(loc-1) * self.determine_erosion_level(loc-ROW_MULT)
        # 4. Return the geologic index
        return result

    def compute_erosion_level(self, geologic):
        return (geologic + self.depth) % 20183

    def determine_erosion_level(self, loc):
        # 1. If we have already determined the erosion level, return it
        loc = no_tool(loc)
        if loc in self.regions:
            return self.regions[loc][EROSION]
        # 2. Else compute it from the geologic_index
        return self.compute_erosion_level(self.determine_geologic_index(loc))

    def sum_region_types(self, upper_left, lower_right):
        # 1. Start with nothing
        result = 0
        # 2. Break out the rows and columns
        ulr, ulc = loc_to_row_col(upper_left)
        lrr, lrc = loc_to_row_col(lower_right)
        # 3. Loop for all of the rows and columns
        for row in range(ulr, lrr + 1):
            for col in range(ulc, lrc + 1):
                # 4. Get the right level of this location
                risk = RISK_LEVEL[self.determine_region_type(row_col_to_loc(row, col))]
                # 5. Accumulate the risk
                result += risk

        # 6. Return the accumulated risk level
        return result

    def determine_moves(self, loc):
        # 1. Start with nothing
        result = []
        # 2. Loop for all of the possible locations
        for delta in determine_delta(loc):
            new_loc = loc + delta
            # 3. If we have the right tool for the job ...
            if self.valid_tool(new_loc):
                # ... and it's not to far out of our way, ...
                row, col = loc_to_row_col(new_loc)
                if row <= self.maxrow and col <= self.maxcol:
                    #print("dm: Adding movement from %d to %d" % (loc, new_loc))
                    # ... save the location
                    result.append(new_loc)
                #else:
                #    print("dm: ignored movement from %d to %d maxr=%d maxc=%d)" % (loc, new_loc, self.maxrow, self.maxcol))
        # 4. Loop for all the possible tools
        loc_nt = no_tool(loc)
        for tool in TOOL_LOC:
            new_tool = tool + loc_nt
            # 5. If valid for the region and not the current tool
            if new_tool != loc and self.valid_tool(new_tool):
                #print("dm: Adding tool change from %d to %d" % (loc, new_tool))
                result.append(new_tool)
        # 6. Return the valid moves
        return result

    def valid_tool(self, loc):
        # 1. Break out the location pieces
        tool = just_tool(loc)
        # 2. Determine region type
        rtype = self.determine_region_type(loc)
        # 3. Return to the tool is valid here
        result = FORBIDDEN_TOOL[rtype] != tool
        #print("vt: loc=%d, tool=%s, rtype=%s, %s" % (loc, TOOL_CHARS[tool], RTYPE_CHARS[rtype], result))
        return result

    def movement_time(self, loc1, loc2):
        return delta_time(loc1, loc2)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.sum_region_types(self.mouth, self.target)


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        mypath = path.Path(start=self.start, cave=self)
        if self.finish in mypath.nodes:
            return mypath.nodes[self.finish].minutes
        else:
            return None

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           c a v e . p y                        end
# ======================================================================
