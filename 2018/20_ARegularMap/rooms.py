# ======================================================================
# A Regular Map
#   Advent of Code 2018 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r o o m s . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 20 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import path

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
COL_OFFSET = 500
ROW_MULT = COL_OFFSET * 2
START = 0

DIRECTIONS = {
    'N': -ROW_MULT,
    'S': ROW_MULT,
    'E': 1,
    'W': -1,
}

ROOM_CHAR = '.'
START_CHAR = 'X'
WALL_CHAR = '#'
NS_CHAR = '-'
EW_CHAR = '|'

REGEX_STR_LEN = 20
REGEX_STR_BEG = 10
REGEX_STR_END = 5
# ----------------------------------------------------------------------
#                                                      utility functions
# ----------------------------------------------------------------------


def split_out_options(regex_string):
    # 1. start with nothing
    options = []
    opt = []
    level = 1
    # 2. Loop until we find the matching right paren
    for index, char in enumerate(regex_string):
        # 3. If another right paren increase the level
        if char == '(':
            level += 1
            opt.append(char)
        # 4. If closing paren, decrease the level
        elif char == ')':
            level -= 1
            # 4a. If done, return the options and following string
            if level == 0:
                options.append(''.join(opt))
                remaining = regex_string[index + 1:]
                return (options, remaining)
            opt.append(char)
        # 5. Vertical bar splits options
        elif char == '|':
            if level == 1:
                options.append(''.join(opt))
                opt = []
            else:
                opt.append(char)
        # 6. If direction character, just collect it
        elif char in DIRECTIONS:
            opt.append(char)
        # 7. There something happening here, what it is ain't exactly clear
        else:
            print("Unexpected regex character (%s) in option %d with [%s] remaining" %
                  (char, len(options), regex_string[1:]))
    # 8. Should not reach here
    print("Unexpected end of regex string [%s] in option %d" % (regex_string, len(options)))
    return ([], '')


def loc_to_row_col(loc):
    row, col = divmod(loc + COL_OFFSET, ROW_MULT)
    return row, col - COL_OFFSET

def row_col_to_loc(row, col):
    return row * ROW_MULT + col

def check_dim(dims, loc):
    # 1. Break the location into row and column
    row, col = loc_to_row_col(loc)
    # 2. Check the row
    if row > dims['S']:
        dims['S'] = row
    if row < dims['N']:
        dims['N'] = row
    # 3. Check the column
    if col > dims['E']:
        dims['E'] = col
    if col < dims['W']:
        dims['W'] = col

def str_loc(loc):
    row, col = loc_to_row_col(loc)
    return "(r%d,c%d)" % (row, col)

def str_regex(regex):
    if len(regex) <= REGEX_STR_LEN:
        return regex
    str_beg = regex[0:REGEX_STR_BEG]
    str_end = regex[-REGEX_STR_END:]
    return "%s..%d..%s" % (str_beg, len(regex)-(REGEX_STR_BEG+REGEX_STR_END), str_end)

def str_item(item):
    loc, regex = item
    return "%s: %s" % (str_loc(loc), str_regex(regex))

# ======================================================================
#                                                                  Rooms
# ======================================================================


class Rooms(object):   # pylint: disable=R0902, R0205
    "Object for A Regular Map"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.regex = None
        self.doors = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.regex = text[0]
            self.regex_to_doors()

    def regex_to_doors(self):
        # 1. Start at the beginning with no doors and a single regex
        self.doors = set()
        queue = [(START, self.regex)]
        processed = set()
        # 2. Loop until the queue is empty
        while queue:
            # 3. Take the first item from the queue
            item = queue.pop(0)
            if item not in processed:
               # 4. Process the item
                processed.add(item)
                more = self.process_loc_regex(queue, item)
                if more is not None:
                    for item in more:
                        queue.append(item)

    def process_loc_regex(self, queue, item):
        # print(item)
        # 1. Seperate the loc and regex
        loc, regex_string = item
        # 2. Process the first character of the regex
        char = regex_string[0]
        remaining = regex_string[1:]
        # 2a. ^ -- Start of regex -- eat it
        if char == '^':
            return [(loc, remaining)]
        # 2b. $ -- End of regex -- we are done
        if char == '$':
            return None
        # 2c. letter -- Change location and add door
        if char in DIRECTIONS:
            while char in DIRECTIONS:
                new_loc = loc + DIRECTIONS[char]
                self.doors.add((loc, new_loc))
                self.doors.add((new_loc, loc))
                loc = new_loc
                if len(remaining) > 0 and remaining[0] in DIRECTIONS:
                    char = remaining[0]
                    remaining = remaining[1:]
                else:
                    char = 'X'
            return [(loc, remaining)]
        # 2d. left paren -- Start of options -- add them all
        if char == '(':
            #print('Queue %d loc=%d, remaining=%d [%s]' % (len(queue), loc, len(remaining), remaining[:10]))
            options, following = split_out_options(remaining)
            #print("  options=%d [%s...] , following=%d [%s...]" %
            #      (len(options), options[0][:10], len(following), following[:10]))
            more = []
            for opt in options:
                more.append((loc, opt + following))
            return more
        # 2e. Well this was certainly unexpected
        print("Unexpected regex character (%s) with [%s] remaining" % (char, remaining))
        return None

    def dimensions(self):
        # 1. Start with nothing
        result = {
            'N': 99999,
            'S': 0,
            'E': 0,
            'W': 99999,
        }
        # 2. Loop for all of the doors
        for door in self.doors:
            loc_from, loc_to = door
            # 3. Checkout the from location
            check_dim(result, loc_from)
            # 4. Checkout the to location
            check_dim(result, loc_to)
        # 5. Return Result
        return result

    def __str__(self):
        # 1. Start with nothing
        result = []
        # 2. Determine the dimensions and add top wall
        dim = self.dimensions()
        result.append(WALL_CHAR*(3+2*abs(dim['E']-dim['W'])))
        # 3. Loop for all of the rows
        for row_num in range(dim['N'], dim['S']+1):
            rooms = ['#']
            below = ['#']
            # 4. Loop for all of the columns
            for col_num in range(dim['W'], dim['E']+1):
                loc = row_col_to_loc(row_num, col_num)
                # 5. Add room
                if loc == START:
                    rooms.append(START_CHAR)
                else:
                    rooms.append(ROOM_CHAR)
                # 6. Add door or wall to the east
                east = loc + DIRECTIONS['E']
                if (loc,east) in self.doors:
                    rooms.append(EW_CHAR)
                else:
                    rooms.append(WALL_CHAR)
                # 7. Add door or wall to the south
                south = loc + DIRECTIONS['S']
                if (loc,south) in self.doors:
                    below.append(NS_CHAR)
                else:
                    below.append(WALL_CHAR)
                below.append(WALL_CHAR)
            # 8. Add the room and below rows
            result.append(''.join(rooms))
            result.append(''.join(below))
        # 9. Return the north pool grid
        return '\n'.join(result)

    def furthest(self):
        # 1. Get the paths
        mypath = path.Path(start=START, doors=self.doors)
        # 2. Return the length of the longest path
        return mypath.furthest()

    def at_least(self, steps=1000):
        # 1. Get the paths
        mypath = path.Path(start=START, doors=self.doors)
        # 2. Return the length of the longest path
        return mypath.at_least(steps)


    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        if verbose:
            print(str(self))
        return self.furthest()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.at_least(steps=1000)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          r o o m s . p y                       end
# ======================================================================
