# ======================================================================
# Monitoring Station
#   Advent of Code 2019 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           q u a d r a n t . p y
# ======================================================================
"Laser sighting for Monitoring Station problem for Adv of Code 2019-10"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from math import atan2, sqrt, pi

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
QUADS = [
    (pi/2, 0),
    (0, -pi/2),
    (-pi/2, -pi),
    (pi, pi/2)
]
# ======================================================================
#                                                               Quadrant
# ======================================================================


class Quadrant():
    """Object representing an one-quarter of a asteroids map"""

    def __init__(self, center=(0, 0), start=0.0, finish=0.0):

        # 1. Set the initial values
        self.center = center
        self.start = start
        self.finish = finish
        self.angles = {}
        self.ordered = []
        self.blocked = []


    def add_if(self, loc):
        "If asteroid is within this quadrant, add it and return True"

        # 1. Compute the angle from the center to the asteroid
        radian = atan2(self.center[1] - loc[1], loc[0] - self.center[0])
        #print("add_if (%d, %d), (%d,%d) %f" %
        #      (loc[0], loc[1],
        #       loc[0] - self.center[0], self.center[1] - loc[1],
        #       radian))

        # 2. Return False if not within this quadrant
        if not (self.finish < radian <= self.start):
            return False

        # 3. Compute the distance
        dist = sqrt(abs(loc[0] - self.center[0]) + abs(loc[1] - self.center[1]))

        # 4. Add the asteroid
        if radian in self.angles:
            self.angles[radian].append((dist, loc))
        else:
            self.angles[radian] = [(dist, loc)]

        # 5. Return True
        return True

    def bake(self):
        "All asteroids added, create ordered and sort the distances"

        # 1. Sort the keys
        self.ordered = sorted(self.angles.keys(), reverse=True)

        # 2. Loop through the angles and ...
        for key, value in self.angles.items():

            # 3. Put the asteroids in distance order
            self.angles[key] = sorted(value)

    def __iter__(self):
        "I am my own iterator"
        return self

    def __next__(self):
        "Return the next angle in this quadrant"

        # 1. If there are any angles, return the first
        if self.ordered:
            angle = self.ordered.pop(0)
            if len(self.angles[angle]) > 1:
                self.blocked.append(angle)
            return angle

        # 2. Else set up for next time through the quadrant
        self.ordered = self.blocked
        self.blocked = []

        # 3. And return the news that we are done with this quadrant
        raise StopIteration

    def shoot(self, radian):
        "Take out an asteroid"

        # 0. Precondition
        assert self.finish < radian <= self.start
        assert radian in self.angles

        # 1. Remove the first item in the angles list
        _, loc = self.angles[radian].pop(0)

        # 2. Return the location of the late asteriod
        return loc

# ======================================================================
#                                                                  Quads
# ======================================================================


class Quads():
    """Object representing an angular of a asteroids map"""

    def __init__(self, center=(0, 0), text=None):

        # 1. Set the initial values
        self.center = center
        self.quads = []

        # 2. Create and add the quadrants
        for qnum in range(4):
            quad = Quadrant(center=center,
                            start=QUADS[qnum][0],
                            finish=QUADS[qnum][1])
            self.quads.append(quad)

        # 3. If there is an asteroid map, get the asteroids from it
        if text:
            for rnum, row in enumerate(text):
                for cnum, col in enumerate(row):
                    if col == '#' and (cnum, rnum) != self.center:
                        self.add_asteroid((cnum, rnum))
            self.bake()

    def add_asteroid(self, loc):
        "Add an asteroid to the appropiate quad"

        # 1. Assume the worst
        result = None

        # 2. Loop for all the quads
        for qnum, quad in enumerate(self.quads):

            # 3. Try to find a home for this asteroid
            accepted = quad.add_if(loc)

            # 4. If accepted, Set quad number and stop
            if accepted:
                result = 1 + qnum
                break

        # 5. Return the accepting quad number or failure
        return result

    def bake(self):
        "Bake all quadrants"

        for quad in self.quads:
            quad.bake()

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     q u a d r a n t . p y                      end
# ======================================================================
