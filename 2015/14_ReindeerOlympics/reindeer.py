# ======================================================================
# Reindeer Olympics
#   Advent of Code 2015 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r e i n d e e r . p y
# ======================================================================
"Reindeer for the Advent of Code 2015 Day 14 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re
# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
RE_REINDEER = re.compile("([A-Z][a-z]+) can fly ([0-9]+) km/s for ([0-9]+) seconds" +
                         ", but then must rest for ([0-9]+) seconds.")

# ======================================================================
#                                                               Reindeer
# ======================================================================


class Reindeer(object):   # pylint: disable=R0902, R0205
    "Object for Reindeer Olympics"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.name = ""
        self.speed = 0
        self.active = 0
        self.passive = 0
        self.flying = False
        self.until = 0
        self.distance = 0
        self.points = 0
        self.time = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:

            # 3. Parse the text
            match = RE_REINDEER.match(text)
            if not match:
                print("Unable to parse", text)

            # 4. Get the parts
            name, speed, active, passive = match.groups()

            # 5. Save them
            self.name = name
            self.speed = int(speed)
            self.active = int(active)
            self.passive = int(passive)

    def start(self):
        "Start the race flying"
        self.flying = True
        self.until = self.active
        self.distance = 0
        self.points = 0
        self.time = 0

    def tick(self):
        "Advance the time one second"

        # 1. "Repent, Harlequin!" said the Ticktockman
        self.time += 1

        # 2. If we are flying, we are moving
        if self.flying:
            self.distance += self.speed

        # 3. Is it time to change states?
        if self.time == self.until:
            self.flying = not self.flying
            if self.flying:
                self.until = self.time + self.active
            else:
                self.until = self.time + self.passive

    def add_point(self):
        "Increment the points score"
        self.points += 1


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      r e i n d e e r . p y                     end
# ======================================================================
