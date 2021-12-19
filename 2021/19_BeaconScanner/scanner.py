# ======================================================================
# Beacon Scanner
#   Advent of Code 2021 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s c a n n e r . p y
# ======================================================================
"Scanner for the Advent of Code 2021 Day 19 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
# Derived from https://www.euclideanspace.com/maths/algebra/matrix/transforms/examples/index.htm
ORIENTATIONS = [
    ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    ((1, 0, 0), (0, 0, -1), (0, 1, 0)),
    ((1, 0, 0), (0, -1, 0), (0, 0, -1)),
    ((1, 0, 0), (0, 0, 1), (0, -1, 0)),

    ((0, -1, 0), (1, 0, 0), (0, 0, 1)),
    ((0, 0, 1), (1, 0, 0), (0, 1, 0)),
    ((0, 1, 0), (1, 0, 0), (0, 0, -1)),
    ((0, 0, -1), (1, 0, 0), (0, -1, 0)),

    ((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
    ((-1, 0, 0), (0, 0, -1), (0, -1, 0)),
    ((-1, 0, 0), (0, 1, 0), (0, 0, -1)),
    ((-1, 0, 0), (0, 0, 1), (0, 1, 0)),

    ((0, 1, 0), (-1, 0, 0), (0, 0, 1)),
    ((0, 0, 1), (-1, 0, 0), (0, -1, 0)),
    ((0, -1, 0), (-1, 0, 0), (0, 0, -1)),
    ((0, 0, -1), (-1, 0, 0), (0, 1, 0)),

    ((0, 0, -1), (0, 1, 0), (1, 0, 0)),
    ((0, -1, 0), (0, 0, -1), (1, 0, 0)),
    ((0, 0, 1), (0, -1, 0), (1, 0, 0)),
    ((0, 1, 0), (0, 0, 1), (1, 0, 0)),

    ((0, 0, -1), (0, -1, 0), (-1, 0, 0)),
    ((0, -1, 0), (0, 0, 1), (-1, 0, 0)),
    ((0, 0, 1), (0, 1, 0), (-1, 0, 0)),
    ((0, 1, 0), (0, 0, -1), (-1, 0, 0)),
]

# ======================================================================
#                                                                Scanner
# ======================================================================


class Scanner(object):   # pylint: disable=R0902, R0205
    "Object for Beacon Scanner"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.number = 0
        self.bcns = set()
        self.orientations = []
        self.coordinates = None
        self.adjusted = set()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.process_text(text)

    def process_text(self, text):
        "Assign values from text"

        # 1. The first line has the scanner number
        self.number = int(text[0].split()[2])

        # 2. Loop over the remaining text
        for line in text[1:]:

            # 3. Get the coordinates from the line
            coords = tuple(int(c) for c in line.split(','))

            # 4. Add in the beacon coordinates
            self.bcns.add(coords)

        # 5. Generation the 24 possible positive/negative/ups
        for orientation in ORIENTATIONS:
            orientations = []
            for bcn in self.bcns:
                o_x = sum(b * o for b, o in zip(bcn, orientation[0]))
                o_y = sum(b * o for b, o in zip(bcn, orientation[1]))
                o_z = sum(b * o for b, o in zip(bcn, orientation[2]))
                orientations.append((o_x, o_y, o_z))
            self.orientations.append(orientations)

    @staticmethod
    def coord_diff(one, two):
        "Return the differences in x, y, z"
        return tuple(one[i] - two[i] for i in range(3))

    @staticmethod
    def coord_sum(one, two):
        "Return the sum in x, y, z"
        return tuple(one[i] + two[i] for i in range(3))

    def find_matches(self, known_beacons):
        """Return our beacons in the some orientation the known beacons match
           Returns empty set if there isn't a match"""

        # 0. Precondition axioms
        assert len(known_beacons) > 0

        # 1. Loop for each of the 24 beacon orientations
        for orientation in self.orientations:

            # 2. Loop for all of the known beacons
            for known in known_beacons:

                # 3. Loop for each of the oriented beacons
                for oindex, beacon in enumerate(orientation):

                    # 4. Is a match still possible?
                    if oindex + 12 > len(orientation):
                        break

                    # 5. Get the offsets
                    offset = Scanner.coord_diff(known, beacon)

                    # 6. Start with this one as a match
                    knt = 1

                    # 7. Loop for the rest of beacons in this orientation, counting matches
                    for obeacon in orientation[oindex + 1:]:
                        offset_beacon = Scanner.coord_sum(obeacon, offset)
                        if offset_beacon in known_beacons:
                            knt += 1

                    # 8. If we have a match, return adjusted beacon coordinates
                    if knt >= 12:
                        adjusted = set(Scanner.coord_sum(beacon, offset)
                                       for beacon in orientation)
                        self.adjusted = adjusted
                        self.coordinates = offset
                        return adjusted

        # 9. No match
        return set()

    def manhattan_distance(self, other):
        "Determine the manhattan (taxi cab) distance between two sensors"

        # 0. Precondition axioms
        assert self.coordinates
        assert other.coordinates

        # 1. Return the distance
        return sum([abs(s - o) for s, o in zip(self.coordinates, other.coordinates)])


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       s c a n n e r . p y                      end
# ======================================================================
