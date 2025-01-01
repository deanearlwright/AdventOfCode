
# ======================================================================
# Restroom Redoubt
#   Advent of Code 2024 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r o b o t . p y
# ======================================================================
"Robot for the Advent of Code 2024 Day 14 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Robot
# ======================================================================


class Robot(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Restroom Redoubt"

    def __init__(self, text=None, part2=False, size=None):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.position = (0, 0)
        self.velocity = (0, 0)
        self.size = size
        self.middle = size

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

        # 3. Set the middle of the size
        if self.size is not None:
            self.middle = (self.size[0] // 2, self.size[1] // 2)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Split position and velocity
        pos, vel = self.text.split()

        # 2. Set the position
        assert pos.startswith("p=")
        pos = pos[2:].split(",")
        self.position = (int(pos[0]), int(pos[1]))

        # 3. Set the velocity
        assert vel.startswith("v=")
        vel = vel[2:].split(",")
        self.velocity = (int(vel[0]), int(vel[1]))

    def move(self):
        "Move the robot on step"
        assert self.size is not None

        # 1. Calculate the next position
        next_pos = (self.position[0] + self.velocity[0],
                    self.position[1] + self.velocity[1])

        # 2. Adjust for teleportation
        next_tel = (next_pos[0] % self.size[0],
                    next_pos[1] % self.size[1])

        # 3. Save the new position
        self.position = next_tel

        # 4. Return it as well for easier unit tests
        return next_tel

    def quadrant(self):
        """Return the quadrant number of the robot

           1 2
            0
           3 4
        """
        assert self.middle is not None

        # 1. On a dividing line?
        if self.position[0] == self.middle[0] or self.position[1] == self.middle[1]:
            return 0

        # 2. Upper left (1)
        if self.position[0] < self.middle[0] and self.position[1] < self.middle[1]:
            return 1

        # 3. Upper right (2)
        if self.position[0] > self.middle[0] and self.position[1] < self.middle[1]:
            return 2

        # 4. Lower right (3)
        if self.position[0] < self.middle[0] and self.position[1] > self.middle[1]:
            return 3

        # 5. Must be lower right
        return 4


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------

if __name__ == '__main__':
    pass

# ======================================================================
# end                      r o b o t . p y                     end
# ======================================================================
