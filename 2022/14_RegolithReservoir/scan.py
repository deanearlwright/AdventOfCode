
# ======================================================================
# Regolith Reservoir
#   Advent of Code 2022 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s c a n . p y
# ======================================================================
"Scan for the Advent of Code 2022 Day 14 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
NEXT = [(0, 1), (-1, 1), (1, 1)]
ROCK = "#"
SAND = "o"
AIR = '.'

# ======================================================================
#                                                                   Scan
# ======================================================================


class Scan(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Regolith Reservoir"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.source = None
        self.slice = {}
        self.rocks = 0
        self.sand = 0
        self.lowest = 0
        self.floor = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.source = Scan.coordinate(text)

    def add_path(self, path):
        "Add a rock path to the scan"

        # 1. Break the path into segments
        segments = path.split(" -> ")

        # 2. Loop for the start and end of each segment
        for indx in range(0, len(segments) - 1):

            # 3. Add a segment to the scan
            self.add_segment(segments[indx], segments[indx + 1])

    def add_segment(self, beg, end):
        "Add a segment of the rock path to the scan"
        # print(f"Adding {beg} to {end}")

        # 1. Convent to coordinates
        beg = Scan.coordinate(beg)
        end = Scan.coordinate(end)

        # 2. If no change in column, add vertical wall
        if beg[0] == end[0]:
            start = min(beg[1], end[1])
            finish = max(beg[1], end[1])
            # print(f"Adding wall {beg} to {end}, {start} to {finish}")
            for row in range(start, finish + 1):
                coord = (beg[0], row)
                if coord not in self.slice:
                    self.rocks += 1
                self.slice[coord] = ROCK

        # 3. Else add a horizontal floor
        else:
            start = min(beg[0], end[0])
            finish = max(beg[0], end[0])
            # print(f"Adding floor {beg} to {end}, {start} to {finish}")
            for col in range(start, finish + 1):
                coord = (col, beg[1])
                if coord not in self.slice:
                    self.rocks += 1
                self.slice[coord] = ROCK

    @staticmethod
    def coordinate(text):
        "Convert the text to a coordinate"
        col, row = text.split(",")
        return (int(col), int(row))

    def find_lowest(self):
        "Find the lowest rock"

        # 1. Loop for all the items in the scan
        for loc in self.slice.keys():

            # 2. If this rock is lower, save row
            if loc[1] > self.lowest:
                self.lowest = loc[1]

        # 3. For part2, we have a floor
        if self.part2:
            self.floor = self.lowest + 2
            self.lowest = self.floor + 1

    def drop(self):
        "Drop a grain of sand"

        # 1. It has to start somewhere
        if self.source is None:
            return None
        loc = self.source
        # print(f"Starting at {loc}, lowest = {self.lowest}")

        # 2. Let the sand fall until it stops or enters the void
        while loc[1] < self.lowest and loc not in self.slice:
            # print(f"Sand at {loc}")

            # 3. Assume that we can't continue to fall
            stopped = True

            # 4. The sand can fall in one of three ways
            for way in NEXT:

                # 5. Determine the new location
                new_loc = (loc[0] + way[0], loc[1] + way[1])

                # 5.5 If part2 there is a floor
                if self.part2:
                    if new_loc[1] == self.floor:
                        break

                # 6. If there is nothing there, we go that way
                if new_loc not in self.slice:
                    loc = new_loc
                    stopped = False
                    break

            # 7. Is this the end?
            if stopped:
                self.slice[loc] = SAND
                self.sand += 1
                return loc

        # 8. We have reached the void
        return None


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          s c a n . p y                         end
# ======================================================================
