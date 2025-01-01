
# ======================================================================
# Warehouse Woes
#   Advent of Code 2024 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r o b o t . p y
# ======================================================================
"Robot for the Advent of Code 2024 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DELTA = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1),
}

# ======================================================================
#                                                                  Robot
# ======================================================================


class Robot(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Warehouse Woes"

    def __init__(self, text=None, part2=False, loc=(0, 0)):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.loc = loc
        self.instructions = ""
        self.instindex = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        self.instructions = ''.join(self.text)
        self.instindex = 0

    def add_instructions(self, text):
        "Add more instruction text"

        if self.text is None:
            self.text = text
        else:
            self.text = self.text + "\n" + text
        self.instructions = self.instructions + text

    def move(self, ware):
        "Move the robot (maybe) and a box (maybe)"

        # 1. If no more instructions, return False
        if self.instindex >= len(self.instructions):
            return False

        # 2. Get the instruction to execute
        instruction = self.instructions[self.instindex]
        self.instindex += 1
        # print(self.loc, instruction)

        # 3. Get the postion delta and the new location
        delta = DELTA[instruction]
        new_loc = (self.loc[0] + delta[0], self.loc[1] + delta[1])

        # 4. Can't move if it runs into a wall
        if ware.is_wall(new_loc):
            return True

        # 5. If there is a box, try to move it
        box = ware.is_box(new_loc)
        if box is not None:
            if box.move_if(delta, ware):
                self.loc = new_loc
            return True

        # 6. Just move it, move it
        self.loc = new_loc
        return True


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                         r o b o t . p y                        end
# ======================================================================
