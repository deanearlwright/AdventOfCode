# ======================================================================
# Trick Shot
#   Advent of Code 2021 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p r o b e . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 17 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re
import math

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
START = (0, 0)
RE_INPUT = re.compile("target area: x=([0-9]+)..([0-9]+), y=(-[0-9]+)..(-[0-9]+)")
FAIL = -1

# ======================================================================
#                                                                  Probe
# ======================================================================


class Probe(object):   # pylint: disable=R0902, R0205
    "Object for Trick Shot"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.start = START
        self.target = None
        self.position = START
        self.velocity = None
        self.height = START[0]

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            match = RE_INPUT.match(text[0])
            if match:
                self.target = [int(x) for x in match.groups()]
            else:
                print("Unable to parse input")

    def is_in_target(self):
        "Returns True if position in within the target"

        return (self.target[0] <= self.position[0] <= self.target[1] and
                self.target[2] <= self.position[1] <= self.target[3])

    def is_possible(self):
        "Returns True if the probe could still make it to the target"

        # 1. Check the vertical position
        if self.position[1] < self.target[2]:
            # print(1, self.position, self.velocity, self.target)
            return False

        # 2. Check the horizontal position
        if self.position[0] > self.target[1]:
            # print(2, self.position, self.velocity, self.target)
            return False
        if self.position[0] < self.target[0]:
            need_x = self.target[0] - self.position[0]
            total_x = (self.velocity[0] * (self.velocity[0] + 1)) // 2
            if total_x < need_x:
                # print(3, self.position, self.velocity, self.target, total_x, need_x)
                return False

        # 3. There is still a chance
        return True

    def step(self):
        "Advance the probe one step"

        # 1. Can't go anywhere if no velocity
        assert self.velocity is not None

        # 2. Advance the probe
        self.position = (self.position[0] + self.velocity[0],
                         self.position[1] + self.velocity[1])

        # 3. Alter the velocity
        self.velocity = (max(0, self.velocity[0] - 1),
                         self.velocity[1] - 1)

        # 4. Record the maximum height
        if self.position[1] > self.height:
            self.height = self.position[1]

    def reload(self, velocity):
        "Reset the probe"

        # 1. Put the probe back at the start
        self.position = START
        self.height = START[0]

        # 2. Set the initial velocity
        self.velocity = velocity

    def fire(self, velocity):
        "Fire the probe, and return the max height"

        # 1. Reload
        self.reload(velocity)

        # 2. Loop until we hit or miss
        while self.is_possible():

            # 3. Are we there yet?
            if self.is_in_target():
                return self.height

            # 4. Try again
            self.step()

        # 5. Return a miss
        return FAIL

    def highest(self):
        "Return the maximum height that can be reached"

        # 1. Start with nothing
        result = 0

        # 2. Loop for the possible velocities
        for vel_x in self.x_range():
            for vel_y in self.y_range():

                # 3. Fire the probe
                highest = self.fire((vel_x, vel_y))

                # 4. Return the best
                if highest > result:
                    result = highest

        # 5. Return the best
        return result

    def count(self):
        "Return the count of possible velocities"

        # 1. Start with nothing
        result = 0

        # 2. Loop for the possible velocities
        for vel_x in self.x_range():
            for vel_y in self.y_range():

                # 3. Fire the probe
                highest = self.fire((vel_x, vel_y))

                # 4. If successful, add it to the count
                if highest != FAIL:
                    result += 1

        # 5. Return the best
        return result

    def x_range(self):
        "Return the useful values for x"

        # 1. Minimum
        min_x = int(math.sqrt(self.target[0]))

        # 2. Maximum
        max_x = self.target[1] + 1

        return range(min_x, max_x)

    def y_range(self):
        "Return the useful values for x"

        # 1. Minimum
        min_y = self.target[2]

        # 2. Maximum
        max_y = -min_y

        return range(min_y, max_y)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.highest()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.count()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         p r o b e . p y                        end
# ======================================================================
