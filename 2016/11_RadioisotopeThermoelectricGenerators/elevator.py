# ======================================================================
# Radioisotope Thermoelectric Generators
#   Advent of Code 2016 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         e l e v a t o r . p y
# ======================================================================
"Elevator for the Advent of Code 2016 Day 11 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
INITIAL_FLOOR = 1
MAXIMUM_FLOOR = 4
RE_ELEVATOR = re.compile("The elevator is on floor ([0-9]) of ([0-9])")

# ======================================================================
#                                                               Elevator
# ======================================================================


class Elevator(object):   # pylint: disable=R0902, R0205
    "Object for Radioisotope Thermoelectric Generators"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.floor = INITIAL_FLOOR
        self.floors = MAXIMUM_FLOOR
        self.direction = ' '
        self.last = 0
        self.items = []

        # 2. Process the text (if any)
        if text is not None and len(text) > 0:
            matched = RE_ELEVATOR.match(self.text)
            if matched:
                self.floor = int(matched.group(1))
                self.floors = int(matched.group(2))
            else:
                print("Unable to parse elevator text: %s" % self.text)

    def move_up(self):
        "Move up a floor"
        assert self.floor < self.floors
        assert len(self.items) > 0
        self.last = self.floor
        self.floor += 1
        self.direction = "^"

    def move_down(self):
        "Move down a floor"
        assert self.floor > 1
        assert len(self.items) > 0
        self.last = self.floor
        self.floor -= 1
        self.direction = "v"

    def load(self, stuff):
        "Put items on the elevator"
        assert (len(self.items) + len(stuff)) <= 2
        self.items.extend(stuff)

    def unload(self):
        "Take items off the elevator"
        stuff = self.items
        self.items = []
        return stuff

    def can_move(self):
        "Can we move the elevator"
        return len(self.items) > 0

    def can_move_up(self):
        "Can we move the elevator up"
        return len(self.items) > 0 and self.floor < self.floors

    def can_move_down(self):
        "Can we move the elevator up"
        return len(self.items) > 0 and self.floor > 1

    def is_safe(self):
        "Are the items on the elevator safe to transport"
        if len(self.items) < 2:
            return True
        return self.items[0].are_safe(self.items[1])

    def __str__(self):
        return "The elevator is on floor %d of %d" % (self.floor, self.floors)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      e l e v a t o r . p y                     end
# ======================================================================
