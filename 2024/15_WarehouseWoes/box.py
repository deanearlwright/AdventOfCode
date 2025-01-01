
# ======================================================================
# Warehouse Woes
#   Advent of Code 2024 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         b o x . p y
# ======================================================================
"Box for the Advent of Code 2024 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                    Box
# ======================================================================


class Box(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Warehouse Woes"

    def __init__(self, loc=(0, 0), part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.loc = loc

    def move(self, loc):
        "Unconditionally move the box"
        self.loc = loc

    def can_move(self, delta, ware):
        "Can the box be moved"
        # print("can_move", self.loc, delta)

        # 1. Get the new location
        new_loc = (self.loc[0] + delta[0], self.loc[1] + delta[1])
        new_loc2 = (new_loc[0], new_loc[1] + 1)

        # 2. Can't move if it runs into a wall
        if ware.is_wall(new_loc):
            return False
        if self.part2:
            if ware.is_wall(new_loc2):
                return False

        # 3. If there is no box there, this box can be moved
        box1 = ware.is_box(new_loc)
        box2 = ware.is_box(new_loc2)
        if box1 is None or box1 == self:
            if self.part2:
                if box2 is None or box2 == self:
                    return True
            else:
                return True

        # 4. One (or two boxes) to check
        if box1 is not None and box1 != self:
            if not box1.can_move(delta, ware):
                return False
        if self.part2:
            if box2 is not None and box1 != box2 and box2 != self:
                if not box2.can_move(delta, ware):
                    return False

        # 5. Good to go
        # print("can_move True", self.loc, delta)
        return True

    def move_if(self, delta, ware):
        "More the box if we can"
        # print("move_if", self.loc, delta)

        # 1. if we can't move it, we can't move it
        if not self.can_move(delta, ware):
            return False

        # 2. Move myself and any other boxes if we have to
        # print("moving all", self.loc, delta)
        self.move_all(delta, ware)

        # 4. We have been moved
        # print("move if True", self.loc, delta)
        return True

    def move_all(self, delta, ware):
        "Move the other boxes"

        # 1. Get other locations
        new_loc = (self.loc[0] + delta[0], self.loc[1] + delta[1])
        new_loc2 = (new_loc[0], new_loc[1] + 1)

        # 2. Get the boxes
        box1 = ware.is_box(new_loc)
        box2 = ware.is_box(new_loc2)

        # 3. Move the first box
        if box1 is not None and box1 != self:
            # print("move all 1", box1.loc, delta)
            box1.move_all(delta, ware)

        # 4. And maybe another
        if self.part2 and box2 is not None and box2 != box1 and box2 != self:
            # print("move all 2", box2.loc, delta)
            box2.move_all(delta, ware)

        # 5. And finally myself
        # print("move all myself", self.loc, new_loc)
        ware.move_box(self.loc, new_loc)

    def gps(self):
        "Return the boxes GPS coordinates"
        return 100 * self.loc[0] + self.loc[1]

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                           b o x . p y                          end
# ======================================================================
