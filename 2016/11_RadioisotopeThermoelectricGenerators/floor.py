# ======================================================================
# Radioisotope Thermoelectric Generators
#   Advent of Code 2016 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         f l o o r . p y
# ======================================================================
"Floor for the Advent of Code 2016 Day 11 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re
from itertools import combinations

import item

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
ORDINAL = ["Unknown", "first", "second", "third", "fourth", "fifth", "sixth"]

RE_FLOOR = re.compile('The ([a-z]+) floor contains ([a-z, -]+).')
NOTHING = "nothing relevant"

# ======================================================================
#                                                                  Floor
# ======================================================================


class Floor(object):   # pylint: disable=R0902, R0205
    "Object for Radioisotope Thermoelectric Generators"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.number = 0
        self.ordinal = "UNKNOWN"
        self.items = set()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Split the text into floor number and items
        match = RE_FLOOR.fullmatch(text)
        if not match:
            print("Unable to parse floor: %s" % text)
            return

        # 2. Save the floor number
        self.ordinal = match.group(1)
        self.number = ORDINAL.index(self.ordinal)

        # 3. Break up the items
        parts = match.group(2).replace(" and ", ",").replace(",,", ",").split(",")

        # 4. Handle nothing floors -- they have no items
        if len(parts) == 1 and parts[0].startswith(NOTHING):
            return

        # 5. Loop for all the parts
        for part in parts:
            part = part.replace("a ", "").strip()

            # 6. Create the item
            an_item = item.Item(part)

            # 7. Add it to the items on the floor
            self.items.add(an_item)

    def __str__(self):
        floor = "The %s floor contains" % self.ordinal
        if len(self.items) == 0:
            return "%s %s." % (floor, NOTHING)
        parts = [str(_) for _ in self.items]
        parts.sort()
        pstr = ', '.join(parts)
        if len(self.items) == 1:
            return "%s %s." % (floor, pstr)
        if len(self.items) == 2:
            return "%s %s." % (floor, pstr.replace(",", " and"))
        parts = pstr.rpartition(', ')
        return "%s %s, and %s." % (floor, parts[0], parts[2])

    def __hash__(self):
        return hash((self.number, frozenset(self.items)))

    def is_empty(self):
        "Returns True if there are no items on this floor"
        return len(self.items) == 0

    def has(self, an_item):
        "Returns True if the item is on the floor"
        return an_item in self.items

    def has_pair(self, an_item):
        "Returns True if the item's pair is on the floor"

        # 1. Create the other
        other = an_item.other()

        # 2. Is the pair on the floor?
        return self.has(other)

    def elements(self):
        "Return the elements to be found on the floor"
        result = set()
        for an_item in self.items:
            result.add(an_item.ielement)
        return result

    def element_items(self, element):
        "Returns the items for a given element"
        result = []
        for an_item in self.items:
            if an_item.ielement == element:
                result.append(an_item)
        return sorted(result)

    def generators(self):
        "Returns the generators on the floor"
        result = []
        for an_item in self.items:
            if an_item.is_generator():
                result.append(an_item)
        return sorted(result)

    def microchips(self):
        "Returns the generators on the floor"
        result = []
        for an_item in self.items:
            if an_item.is_microchip():
                result.append(an_item)
        return sorted(result)

    def trace(self, elevator, items):
        "Output floor in trace format: 'F4 . HyG ... LiG ...'"

        # 1. Floor number and elevator flag
        if elevator:
            if elevator.floor == self.number:
                result = ["F%d E" % self.number]
            elif elevator.last == self.number:
                result = ["F%d %s" % (self.number, elevator.direction)]
            else:
                result = ["F%d ." % self.number]
        else:
            result = ["F%d ." % self.number]

        # 3. Loop for all of the items
        for an_item in items:

            # 4. If we have the item add it, else dots
            if self.has(an_item):
                result.append(an_item.initials())
            else:
                result.append("...")

        # 5. Return the trace line
        return ' '.join(result)

    def remove(self, an_item):
        "Take away the specified item"
        assert an_item in self.items
        self.items.remove(an_item)

    def add(self, an_item):
        "Add the specified item"
        if an_item in self.items:
            print("Already have %s on floor %d" % (str(an_item), self.number))
        assert an_item not in self.items
        self.items.add(an_item)

    def is_safe(self):
        "Return True is none of the microchips (if any) will be fried"

        # 1. It is safe if there are no microchips OR if there are no generators
        microchips = self.microchips()
        if len(microchips) == 0:
            return True
        if len(self.generators()) == 0:
            return True

        # 2. Loop for all of the microchips
        for microchip in microchips:

            # 3. It is fried not paired with its generator
            if not self.has_pair(microchip):
                return False

        # 4. All of the microchips on this mixed floor are paired
        return True

    def clone(self):
        "Returns a copy of the floor"

        # 1. Create a new floor
        other = Floor()

        # 2. Copy information
        other.text = "Clone " + self.text
        other.part2 = self.part2
        other.number = self.number
        other.ordinal = self.ordinal

        # 3. Copy the items
        for an_item in self.items:
            other.items.add(an_item.clone())

        # 4. Return the clone
        return other

    def is_safe_with(self, items):
        "Is the floor safe with the added items"

        # 1. Clone the current floor
        other = self.clone()

        # 2. Add the items
        for an_item in items:
            other.add(an_item)

        # 3. Is the floor still safe
        return other.is_safe()

    def is_safe_without(self, items):
        "Is the floor safe with the removed items"

        # 1. Clone the current floor
        other = self.clone()

        # 2. Remove the items
        for an_item in items:
            other.remove(an_item)

        # 3. Is the floor still safe
        return other.is_safe()

    def __eq__(self, other):
        "Returns true if the floors have the same number and items"
        if self.number != other.number:
            return False
        if len(self.items) != len(other.items):
            return False
        for an_item in self.items:
            if not other.has(an_item):
                return False
        return True

    def safely_removable(self):
        "Returns list of items that can safely be removed"

        # 1. Start with nothing
        result = []

        # 2. Try singular items
        for an_item in self.items:

            # 3. Is it safe to remove it?
            if self.is_safe_without([an_item]):

                # 4. Yes, Ass them to the result
                # print("SR adding %s" % str(an_item))
                result.append([an_item])

        # 5. Try things is pairs
        for pair in combinations(self.items, 2):

            # 6. Is it safe to remove them and are they safe together?
            if pair[0].are_safe(pair[1]) and self.is_safe_without(pair):

                # 7. Yes, add them to the result
                result.append(pair)

        # 8. Return items that are safe to remove (if any)
        return result


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         f l o o r . p y                        end
# ======================================================================
