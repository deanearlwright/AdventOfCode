
# ======================================================================
# Beacon Exclusion Zone
#   Advent of Code 2022 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d e v i c e . p y
# ======================================================================
"Device for the Advent of Code 2022 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import sensor

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Device
# ======================================================================


class Device(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Beacon Exclusion Zone"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.sensors = {}
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
        self.middle = (0, 0)

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Loop for all of the rows of the text
        for line in text:

            # 2. Create a sensor from this information
            snsr = sensor.Sensor(text=line, part2=self.part2)

            # 3. Add the sensor to the list
            self.sensors[snsr.loc] = snsr

        # 4. Find the edge sensors
        self.top = snsr
        self.bottom = snsr
        self.left = snsr
        self.right = snsr
        for snsr in self.sensors.values():
            if snsr.loc[1] < self.top.loc[1]:
                self.top = snsr
            if snsr.loc[1] > self.bottom.loc[1]:
                self.bottom = snsr
            if snsr.loc[0] < self.left.loc[0]:
                self.left = snsr
            if snsr.loc[0] > self.right.loc[0]:
                self.right = snsr

        # 4. Determine the middle of the sensors
        self.middle = (self.left.loc[0] +
                       (self.right.loc[0] - self.left.loc[0]) // 2,
                       self.top.loc[1] +
                       (self.bottom.loc[1] - self.top.loc[1]) // 2)

    def count_not_beacons_row(self, row=2000000):
        "How many spaces cannot contain a beacon in the specified row"

        # 1. Start with nothing
        result = 0

        # 2. Determine maximum left and right
        left = self.left.loc[0] - self.left.dist
        right = self.right.loc[0] + self.right.dist
        print(f"Checking row {row} from {left} to {right}")

        # 3. Loop over the columns
        for col in range(left, right):
            if 0 == col % 1000:
                print(f"Checking row {row} from {left} to {right}: "
                      f"column {col} count={result}")

            # 4. What is the opinion of the sensors
            guess = self.is_a_beacon((col, row))

            # 5. If none of think it is a beacon, count the square
            if guess is False:
                result += 1

        # 6. Return the number of spaces that can't contain a beacon
        return result

    def is_a_beacon(self, loc):
        "Return True if it is a beacon, False if not, None if unknown"

        # 1. Loop for all the sensors
        for snsr in self.sensors.values():

            # 2. What does this sensor know
            result = snsr.is_beacon(loc)

            # 3. If it knows something, return it
            if result is not None:
                return result

        # 4. We just don't know
        return None

    def find_unknown_beacon_brute_force(self, limit=20):
        "Return the location of the unknown beacon"

        # 1. Loop for all possible rows
        for row in range(limit + 1):

            # 2. Loop for all possible cols
            for col in range(limit + 1):
                if 0 == col % 10000:
                    print(f"row = {row} col = {col}")

                # 3. Is this a beacon?
                isit = self.is_a_beacon((col, row))
                if isit is None:
                    print(f"Unknown at ({col},{row})")
                    return (col, row)

        # 4. Too bad so sad
        return None

    def find_unknown_beacon(self, limit=20):
        "Return the location of the unknown beacon"

        # 1. Loop for all the sensors
        for snsr in self.sensors.values():
            print(f"Checking sensor {snsr.loc}")

            # 2. Loop for the range of that sensor
            for dist in range(snsr.dist + 1):

                # 3. Loop at the extreames
                for edge_x, edge_y in snsr.edge(dist):

                    # 4. if the loc is within the possible search area
                    if 0 <= edge_x <= limit and 0 <= edge_y <= limit:

                        # 5. Is the location within any sensor?
                        known = self.is_a_beacon((edge_x, edge_y))
                        if known is None:
                            print(f"Found ({edge_x},{edge_y})")
                            return (edge_x, edge_y)

        # 6. Too bad so sad
        return None

    def tuning_frequency(self, row=20):
        "Return the tuning frequency of the distress beacon"

        # 1. Get the location of the beacon
        beacon = self.find_unknown_beacon(limit=row)

        # 2. If not found, return the bad news
        if beacon is None:
            return None

        # 3. Return the tuning requency
        return 4000000 * beacon[0] + beacon[1]


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      d e v i c e . p y                     end
# ======================================================================
