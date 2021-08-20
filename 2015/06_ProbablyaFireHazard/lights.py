# ======================================================================
# Probably a Fire Hazard
#   Advent of Code 2015 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         l i g h t s . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 06 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re
# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
INST = re.compile(r'(turn on|toggle|turn off) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)')

# ======================================================================
#                                                                 Lights
# ======================================================================


class Lights(object):   # pylint: disable=R0902, R0205
    "Object for Probably a Fire Hazard"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.lights = {}

    def execute(self, verbose=False):
        "Turn lights on and off"

        # 1. Set them all off
        self.lights = {}

        # 2. Loop for all of the instructions
        # - turn on 0,0 through 999,999 would turn on (or leave on) every light.
        # - toggle 0,0 through 999,0 would toggle the first line of 1000 lights,
        #    turning off the ones that were on, and turning on the ones that were
        #    off.
        # - turn off 499,499 through 500,500 would turn off (or leave off) the
        #    middle four lights.
        for inst in self.text:

            # 3. Decode the instruction
            decoded = INST.match(inst)

            # 4. Handle problems
            if decoded is None:
                print("Unable to decode %s" % inst)
                continue

            # 5. Get the instruction information
            what, beg_x, beg_y, end_x, end_y = decoded.groups()

            # 6. Execute the instructions
            if what == 'turn on':
                self.turn_on(int(beg_x), int(beg_y), int(end_x), int(end_y))
            elif what == 'turn off':
                self.turn_off(int(beg_x), int(beg_y), int(end_x), int(end_y))
            elif what == 'toggle':
                self.toggle(int(beg_x), int(beg_y), int(end_x), int(end_y))
            else:
                print("Unable to determine verb in %s" % inst)
            if verbose:
                print(inst, "-->", self.count_lights(), self.total_brightness())

    def turn_on(self, beg_x, beg_y, end_x, end_y):
        "Turn on a bunch of lights"

        # 1. Loop for the columns and rows
        for col in range(beg_x, end_x + 1):
            for row in range(beg_y, end_y + 1):

                # 2. This is the light locations
                loc = (col, row)

                # 3a. P1: Turn on the light
                if not self.part2:
                    self.lights[loc] = 1
                # 3b. P2: Increase illumination
                else:
                    if loc in self.lights:
                        self.lights[loc] += 1
                    else:
                        self.lights[loc] = 1

    def turn_off(self, beg_x, beg_y, end_x, end_y):
        "Turn off a bunch of lights"

        # 1. Loop for the columns and rows
        for col in range(beg_x, end_x + 1):
            for row in range(beg_y, end_y + 1):

                # 2. This is the light locations
                loc = (col, row)

                # 3a. P1: Turn off the light
                if not self.part2:
                    if loc in self.lights:
                        del self.lights[loc]
                # 3b. P2: Increase illumination
                else:
                    if loc in self.lights:
                        self.lights[loc] -= 1
                        if self.lights[loc] <= 0:
                            del self.lights[loc]

    def toggle(self, beg_x, beg_y, end_x, end_y):
        "Turn on a bunch of lights"

        # 1. Loop for the columns and rows
        for col in range(beg_x, end_x + 1):
            for row in range(beg_y, end_y + 1):

                # 2. This is the light locations
                loc = (col, row)

                # 3a. P1: Turn on/off the light
                if not self.part2:
                    if loc in self.lights:
                        del self.lights[loc]
                    else:
                        self.lights[loc] = 1
                # 3b. P2: Increase illumination
                else:
                    if loc in self.lights:
                        self.lights[loc] += 2
                    else:
                        self.lights[loc] = 2

    def count_lights(self):
        "Return the number of lights that are on"
        return len(self.lights)

    def total_brightness(self):
        "Return the total brightness of lights"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the lights
        for value in self.lights.values():

            # 3. Increment the total of the brightness
            result += value

        # 4. Return the total brightness
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        self.execute(verbose=verbose)
        return self.count_lights()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        self.execute(verbose=verbose)
        return self.total_brightness()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        l i g h t s . p y                       end
# ======================================================================
