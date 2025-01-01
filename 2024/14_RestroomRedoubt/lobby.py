
# ======================================================================
# Restroom Redoubt
#   Advent of Code 2024 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         l o b b y . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 14 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from math import prod

import robot

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DEFAULT_SIZE = (101, 103)  # cols, rows

# ======================================================================
#                                                                  Lobby
# ======================================================================


class Lobby(object):   # pylint: disable=R0902, R0205
    "Object for Restroom Redoubt"

    def __init__(self, text=None, part2=False, size=None):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.size = size
        if self.size is None:
            self.size = DEFAULT_SIZE
        self.robots = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text()

    def _process_text(self):
        "Assign values from text"

        assert self.text is not None and len(self.text) > 0

        # 1. Loop for every line the text
        for line in self.text:

            # 2. Create a robot from the text
            r2d2 = robot.Robot(text=line, part2=self.part2, size=self.size)

            # 3. Add it to the collective
            self.robots.append(r2d2)

    def move_all(self):
        "Move all the robots one step"

        # 1. Loop for all the robots
        for r2d2 in self.robots:

            # 2. Move that robot
            r2d2.move()

    def move_all_multiple(self, steps=100):
        "Move all the robots multiple times"

        # 1. Loop for all the steps
        for _ in range(steps):

            # 2. Move it, move it
            self.move_all()

    def quadrants(self):
        "Count the number of robots in each quadrant"

        # 1. Start with nothing
        results = [0, 0, 0, 0, 0]

        # 2. Loop for all the robots
        for r2d2 in self.robots:

            # 3. Get the quadrant for that robot
            quadrant = r2d2.quadrant()

            # 4. Increment the count for that quadrant
            results[quadrant] += 1

        # 5. Return the quadrant counts
        assert sum(results) == len(self.robots)
        return results

    def safety(self):
        "Return the count of the robots not in the middle row or col"
        return prod(self.quadrants()[1:])

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        self.move_all_multiple()
        return self.safety()

    def max_safety(self):
        "Determine the safest iteration - Christmas tree maybe?"

        # 1. Start with nothing
        result = 0
        max_safety = self.safety()

        # 2. Loop for quite a long while
        for iteration in range(prod(self.size)):

            # 3. Move each robot
            self.move_all()

            # 4. Get the safety at this iteration
            safety = self.safety()

            # 5. Remember it if is better
            if safety > max_safety:
                max_safety = safety
                result = iteration
                print(result, max_safety)

        # 6. Return when the safety was the greatest
        #    Hopefully this will be the time of the christmas tree
        return result

    def max_quadrant(self):
        "Determine when most of the robots are in one quadrant"

        # 1. Start with nothing
        result = 0
        max_quad = max(self.quadrants())

        # 2. Loop for quite a long while
        for iteration in range(9039):  # prod(self.size)):

            # 3. Move each robot
            self.move_all()

            # 4. Get the quatrants at this iteration
            quads = self.quadrants()
            mquad = max(quads)

            # 5. Remember it if is better
            if mquad > max_quad:
                max_quad = mquad
                result = iteration
                print(result, max_quad)

        # 6. Return when most robots were in one quadrant
        #    Hopefully this will be the time of the christmas tree
        return result

    def locations(self):
        "Determine the location of all of the robots"

        # 1. Start with nothing
        result = set()

        # 2. Loop for all the robots
        for r2d2 in self.robots:

            # 3. Remember the robot's location
            result.add(r2d2.position)

        # 4. Return the robot locations
        return result

    def min_overlap(self):
        "Determine when most of the robots are non-overlapping"

        # 1. Start with nothing
        result = 0
        max_locations = len(self.locations())

        # 2. Loop for quite a long while
        for iteration in range(9039):  # prod(self.size)):

            # 3. Move each robot
            self.move_all()

            # 4. Get the quatrants at this iteration
            locs = len(self.locations())

            # 5. Remember it if is better
            if locs > max_locations:
                max_locations = locs
                result = iteration
                print(result, max_locations)

        # 6. Return when most robots are the least overlapped
        #    Hopefully this will be the time of the christmas tree
        return result

    def max_in_a_row(self):
        "Determine when most of the robots are non-overlapping"

        # 1. Start with nothing
        result = 0
        max_locations = len(self.locations())

        # 2. Loop for quite a long while
        for iteration in range(9039):  # prod(self.size)):

            # 3. Move each robot
            self.move_all()

            # 3a. We know that it is not before iteration 7501
            if iteration < 7501:
                continue

            # 4. Get the quatrants at this iteration
            locs = len(self.locations())

            # 5. Remember it if is better
            if locs > max_locations:
                max_locations = locs
                result = iteration
                print(result, max_locations)

        # 6. Return when most robots are the least overlapped
        #    Hopefully this will be the time of the christmas tree
        return result

    def draw_it(self):
        "Determine when most of the robots are drawing a tree"

        # 1. Start with nothing
        result = 0

        # 2. Loop for quite a long while
        for iteration in range(9039):  # prod(self.size)):

            # 3. Move each robot
            self.move_all()

            # 3a. We know that it is not before iteration 7501
            if iteration < 7501:
                continue

            # 4. Get the image for this iteration
            print(iteration)
            print(self)
            print(iteration)
            print("\n")
            input()

        # 5. Return when most robots are the least overlapped
        #    Hopefully this will be the time of the christmas tree
        return result

    def in_a_row(self, row_min=10):
        "Determine when at least n robots are in a row"

        # 1. Start with nothing
        robots = "*" * row_min
        print(row_min, robots)

        # 2. Loop for quite a long while
        for iteration in range(9039):  # prod(self.size)):

            # 3. Move each robot
            self.move_all()

            # 3a. We know that it is not before iteration 7501
            if iteration < 7001:
                continue

            # 4. Get the image for this iteration
            image = str(self)

            # 5. Loop for all the rows in the image
            for line in image.splitlines():

                # 6. Are there the required lined up robots?
                if line.find(robots) > 0:
                    print(image)
                    return iteration

        # 7. Never found enought robots in a line
        return None

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part two
        # return self.max_safety()  # 9039 Too high
        # return self.max_quadrant() # 7501 Too log
        # return self.min_overlap() # 7501 Too low
        return self.in_a_row() # 7501 which is too low but looks good
        # return self.draw_it() # looks good at 7501 but 7502 is the answer that was accepted

    def __str__(self):
        "Return a visual represention of the robots"

        # 1. Start with a blank image
        line = "." * self.size[0]
        result = [line for _ in range(self.size[1])]

        # 2. Loop for all the robots
        for r2d2 in self.robots:

            # 3. Get the robot's location
            pos = r2d2.position

            # 4. Place the robot on the image
            line = result[pos[1]]
            result[pos[1]] = line[:pos[0]] + "*" + line[pos[0] + 1:]

        # 5. Return the image
        return "\n".join(result)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                         l o b b y . p y                        end
# ======================================================================
