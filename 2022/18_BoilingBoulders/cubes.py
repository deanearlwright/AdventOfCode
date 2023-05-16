
# ======================================================================
# Boiling Boulders
#   Advent of Code 2022 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c u b e s . p y
# ======================================================================
"Cubes for the Advent of Code 2022 Day 18 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import cube

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DELTA = [
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1)
]

# ======================================================================
#                                                                  Cubes
# ======================================================================


class Cubes(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Boiling Boulders"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.cubes = []
        self.locations = set()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Loop for the lines of text
        for line in text:

            # 2. Create a cube
            a_cube = cube.Cube(text=line, part2=self.part2)

            # 3. Add it to the others
            self.cubes.append(a_cube)
            self.locations.add(a_cube.loc)

        # 4. Connect the cubes is possible
        self.connect_the_cubes()

    def connect_the_cubes(self):
        "Connect the cubes"

        # 1. Loop for all the cubes (except for the last)
        for index, a_cube in enumerate(self.cubes[:-1]):

            # 2. Loop for the other cubes
            for b_cube in self.cubes[index + 1:]:

                # 3. See if these cubes are connected
                a_cube.is_connected(b_cube)

    def total_unconnected_sides(self):
        "Return the total number of unconnected sides"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all the cubes
        for a_cube in self.cubes:

            # 3. Add the unconnected sides of this cube
            result += a_cube.unconnected_sides()

        # 4. Return the total number of unconnected sides
        return result

    def total_cooled_sides(self):
        "Return the total sides touching water/steam"

        # 1. Start with nothing
        result = 0

        # 2. Find the size of the problem space
        minimum = min(min(loc) for loc in self.locations) - 1
        maximum = max(max(loc) for loc in self.locations) + 1

        # 3. Start at one corner of the cube
        cubed = [(minimum, minimum, minimum)]
        seen = set()

        # 4. Loop while there is something to do
        while cubed:

            # 5. Get a point in space
            here = cubed.pop()

            # 6. Loop for the nearby points
            for point in Cubes.near_by(here, minimum, maximum):

                # 7. Been there, done that
                if point in seen:
                    continue

                # 8. Is this a cube? Accumulate sides seen
                if point in self.locations:
                    result += 1
                    continue

                # 9. Need to look around this point
                cubed.append(point)
                seen.add(point)

        # 10. Return total number of cooled sides
        return result

    @staticmethod
    def near_by(here, minimum, maximum):
        "Return the possible 6 connect points (within the limits)"

        # 1. Start with nothing
        result = []

        # 2. Loop for the possible next spaces
        for delta in DELTA:

            # 3. Where is the new point
            point = (here[0] + delta[0],
                     here[1] + delta[1],
                     here[2] + delta[2])

            # 4. Is the point within the problem space?
            if point[0] < minimum or point[0] > maximum:
                continue
            if point[1] < minimum or point[1] > maximum:
                continue
            if point[2] < minimum or point[2] > maximum:
                continue

            # 5. Save this point
            result.append(point)

        # 6. Return the near by points
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                         c u b e s . p y                        end
# ======================================================================
