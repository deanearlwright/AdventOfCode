
# ======================================================================
# Beacon Exclusion Zone
#   Advent of Code 2022 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s e n s o r . p y
# ======================================================================
"Sensor for the Advent of Code 2022 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Sensor
# ======================================================================


class Sensor(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Beacon Exclusion Zone"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.loc = None
        self.beacon = None
        self.dist = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Break the text into tokens
        tokens = text.split()
        if len(tokens) != 10:
            print(f"text {text} has {len(tokens)} tokens")
            return
        if not (tokens[2].startswith("x")
                and tokens[3].startswith("y")
                and tokens[8].startswith("x")
                and tokens[9].startswith("y")):
            print(f"Unexpected text {text}")

        # 2. Save the location of the sensor
        self.loc = (Sensor.clean(tokens[2]), Sensor.clean(tokens[3]))

        # 3. Save the location of the nearest beacon
        self.beacon = (Sensor.clean(tokens[8]), Sensor.clean(tokens[9]))

        # 4. Determine the distance from the sensor to the nearest beacon
        self.dist = self.distance(self.beacon)

    @staticmethod
    def clean(token):
        "Clean the junk off a numeric token"

        # 1. Get rid of the x= (or y=)
        token = token[2:]

        # 2. if the token ends with a comma or colon, lose it
        if token[-1] in ",:":
            token = token[:-1]

        # 3. Convert to integer
        return int(token)

    def distance(self, loc):
        "Return the distance from this sensor to the location"

        return abs(self.loc[0] - loc[0]) + abs(self.loc[1] - loc[1])

    def is_beacon(self, loc):
        "Returns False if the sensor feels there is no beacon there"

        # 1. Is the location our beacon?
        if loc == self.beacon and self.part2 is False:
            return True

        # 2. How far is it to the location from our sensor
        dist = self.distance(loc)

        # 3. If our beacon is closer than this location?
        if dist <= self.dist:
            return False

        # 4. We just don't know
        return None

    def edge(self, dist):
        "Return a locations along the edge"

        edge_1 = (self.loc[0] - self.dist - 1 + dist, self.loc[1] - dist)
        edge_2 = (self.loc[0] + self.dist + 1 - dist, self.loc[1] - dist)
        edge_3 = (self.loc[0] - self.dist - 1 + dist, self.loc[1] + dist)
        edge_4 = (self.loc[0] + self.dist + 1 - dist, self.loc[1] + dist)

        return edge_1, edge_2, edge_3, edge_4


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      s e n s o r . p y                     end
# ======================================================================
