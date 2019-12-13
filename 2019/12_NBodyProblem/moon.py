# ======================================================================
# The N-Body Problem
#   Advent of Code 2019 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                             m o o n . p y
# ======================================================================
"A single moon for The N-Body Problem for Advent of Code 2019 Day 12"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
MOON_RE = re.compile(r'<x=(-?[0-9]+), y=(-?[0-9]+), z=(-?[0-9]+)>')

# ======================================================================
#                                                                   Moon
# ======================================================================


class Moon():
    """Object representing a single moon"""

    def __init__(self, pos=(0, 0, 0), vel=(0, 0, 0), text=None):

        # 1. Set the initial values
        self.pos = pos
        self.vel = vel
        self.delta = [0, 0, 0]

        # 2. If there is a text, set position
        if text:
            match = MOON_RE.match(text)
            if match is None:
                print("Unable to parse moon input %s" % text)
            else:
                self.pos = (int(match.group(1)),
                            int(match.group(2)),
                            int(match.group(3)))

    def __str__(self):
        return "pos=<x={:3d}, y={:3d}, z={:3d}>, vel=<x={:3d}, y={:3d}, z={:3d}>, nrg={:4d}".format(
            self.pos[0], self.pos[1], self.pos[2],
            self.vel[0], self.vel[1], self.vel[2],
            self.energy())


    def update_velocity_and_position(self):
        "Adjust the velocity by the gravity delta and position by the new velocity"
        self.vel = (self.vel[0] + self.delta[0],
                    self.vel[1] + self.delta[1],
                    self.vel[2] + self.delta[2])
        self.delta = [0, 0, 0]
        self.pos = (self.pos[0] + self.vel[0],
                    self.pos[1] + self.vel[1],
                    self.pos[2] + self.vel[2])

    def apply_gravity(self, other):
        "Calculate the velocity delta due to another moon -- mutually done"

        # 0. Preconditions
        assert isinstance(other, Moon)

        # 1. Loop for the three dimensions (Buckaroo Banzai has 8)
        for dim in range(3):

            # 2. No adjustment necessary if they are the same
            if self.pos[dim] == other.pos[dim]:
                continue

            # 3. If my pos is less than the others, I go up and they go down
            if self.pos[dim] < other.pos[dim]:
                self.delta[dim] += 1
                other.delta[dim] -= 1

            # 4. Else I go down and they go up
            else:
                self.delta[dim] -= 1
                other.delta[dim] += 1

    def energy(self):
        "Return total energy of the moon"

        return (abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])) * \
               (abs(self.vel[0]) + abs(self.vel[1]) + abs(self.vel[2]))

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          m o o n . p y                         end
# ======================================================================
