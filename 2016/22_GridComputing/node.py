# ======================================================================
# Grid Computing
#   Advent of Code 2016 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         n o d e . p y
# ======================================================================
"Node for the Advent of Code 2016 Day 22 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
RE_NODE = re.compile("^/dev/grid/node-x([0-9]+)-y([0-9]+) +([0-9]+)T +([0-9]+)T +([0-9]+)T")
DELTA = [
  (-1, 0),
  (1, 0),
  (0, -1),
  (0, 1)
]
WALL = 200

# ======================================================================
#                                                                   Node
# ======================================================================


class Node(object):   # pylint: disable=R0902, R0205
    "Object for Grid Computing"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.loc = (0, 0)
        self.size = 0
        self.used = 0
        self.avail = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            mobj = RE_NODE.match(text)
            if not mobj:
                print("*** Unable to match <<<%s>>>" % text)
            else:
                numbers = [int(x) for x in mobj.groups()]
                self.loc = (numbers[0], numbers[1])
                self.size, self.used, self.avail = numbers[2:]

    def is_empty(self):
        "Returns True if no bytes have been used"
        return self.used == 0

    def is_wall(self):
        "Returns True if really big diruve with not much storage left"
        return self.used > WALL

    def can_hold(self, amount):
        "Returns True if can hold more"
        return self.avail >= amount

    def receive(self, amount):
        "Add amount to node, Returns True if successful"

        # 1. Check if we can hold it
        if self.can_hold(amount):

            # 2. Yes, Add it in
            self.used += amount
            self.avail -= amount
            return True

        # 3. If we can't, return False
        return False

    def nearby(self):
        "Returns nearby locations - can test for too low but not too high"

        # 1. Start with nothing
        result = []

        # 2. Loop for the four directions
        for delta in DELTA:

            # 3. Compute the new x and y
            new_x = self.loc[0] + delta[0]
            new_y = self.loc[1] + delta[1]

            # 4. If too low, ignore
            if new_x < 0 or new_y < 0:
                continue

            # 5. Add the new location
            result.append((new_x, new_y))

        # 6. Return tuples of nearby locations
        return result

    def distance(self, other):
        "Taxi-cab distance between two nodes"
        return abs(self.loc[0] - other.loc[0]) + abs(self.loc[1] - other.loc[1])


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          n o d e . p y                         end
# ======================================================================
