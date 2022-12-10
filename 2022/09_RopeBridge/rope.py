# ======================================================================
# Rope Bridge
#   Advent of Code 2022 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r o p e . p y
# ======================================================================
"Rope for the Advent of Code 2022 Day 09 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DIRS = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}
TWOS = {
    "U": (0, -2),
    "D": (0, 2),
    "L": (-2, 0),
    "R": (2, 0),
}
DIAG = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
TWOD = {
    (-2, -1): (-1, -1),
    (-1, -2): (-1, -1),
    (-2, 1): (-1, 1),
    (-1, 2): (-1, 1),
    (2, 1): (1, 1),
    (1, 2): (1, 1),
    (2, -1): (1, -1),
    (1, -2): (1, -1),
    (2, -2): (1, -1),
    (2, 2): (1, 1),
    (-2, 2): (-1, 1),
    (-2, -2): (-1, -1),
}

# ======================================================================
#                                                                   Rope
# ======================================================================


class Rope(object):   # pylint: disable=R0902, R0205
    "Object for Rope Bridge"

    def __init__(self, length=2):

        # 1. Set the initial values
        self.length = length
        self.visited = set()
        self.visited.add((0, 0))
        self.knots = []

        # 2. Set the location of the knots
        for _ in range(length):
            self.knots.append((0, 0))

    def move_head(self, motion):
        "Move the head"
        #print("move_head", motion)

        # 1. Break the motion into direction and length
        direction, steps = motion.split()
        steps = int(steps)

        # 2. Moving the head multiple times
        for _ in range(steps):

            # 3. Move the head once
            self.move_head_once(direction)

    @staticmethod
    def new_loc(loc, delta):
        "Return a new location"

        return (loc[0] + delta[0], loc[1] + delta[1])

    def move_head_once(self, direction):
        "Move the head in the indicated direction"
        #print("move_head_once", direction)

        # 1. Get the new location
        loc = Rope.new_loc(self.knots[0], DIRS[direction])

        # 2. Set it
        self.knots[0] = loc

        # 3. And the tail will follow
        self.move_tail(0)

        # 4. Remember where the tail went
        self.visited.add(self.tail())

    def move_tail(self, head):
        "And the tail will follow"
        #print("move_tail", head)

        # 1. If close to the head, the tail doesn't have to move
        if head + 1 >= self.length or self.is_touching(head):
            return

        # 2. Is the head two away, vertically or horizontally?
        for direction, delta in TWOS.items():
            if self.is_head_at(head, delta):

                # 3. If so move it one step in that direction
                loc = Rope.new_loc(self.knots[head + 1], DIRS[direction])
                self.knots[head + 1] = loc
                self.move_tail(head + 1)
                return

        # 4. So the head must be diagionally away
        for delta_h, delta_t in TWOD.items():
            if self.is_head_at(head, delta_h):

                # 3. If so move it one step in that direction
                loc = Rope.new_loc(self.knots[head + 1], delta_t)
                self.knots[head + 1] = loc
                self.move_tail(head + 1)
                return

        # 4. Should never get here
        print("*** move_tail disconected", head, self.knots)

    def is_head_at(self, head, delta):

        # 1. Calculate the location
        loc = Rope.new_loc(self.knots[head + 1], delta)

        # 2. Is the head there?
        return self.knots[head] == loc

    def is_touching(self, head):
        "Returns true if tail is touching the head"

        # 1. Overlapping is touching
        if self.knots[head] == self.knots[head + 1]:
            return True

        # 2. Is it one away horzontally or vertically?
        for delta in DIRS.values():
            if self.is_head_at(head, delta):
                return True

        # 3. Is it one away diagionally?
        for delta in DIAG:
            if self.is_head_at(head, delta):
                return True

        # 4. Not even close
        return False

    def tail_visited(self):
        "Return the number of places the tail visited"
        return len(self.visited)

    def head(self):
        "Return the location of the first knot"
        return self.knots[0]

    def tail(self):
        "Return the location of the last knot"
        return self.knots[-1]


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          r o p e . p y                         end
# ======================================================================
