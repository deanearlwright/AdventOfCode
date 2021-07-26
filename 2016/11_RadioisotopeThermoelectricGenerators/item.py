# ======================================================================
# Radioisotope Thermoelectric Generators
#   Advent of Code 2016 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         i t e m . p y
# ======================================================================
"Item for the Advent of Code 2016 Day 11 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
ITEM_TYPES = set(["microchip", "generator"])
ITEM_ELEMENTS = set(["hydrogen", "lithium", "thulium", "plutonium",
                     "strontium", "promethium", "ruthenium",
                     "elerium", "dilithium"])
OTHER = {
    'microchip': 'generator',
    'generator': 'microchip',
}

# ======================================================================
#                                                                   Item
# ======================================================================


class Item(object):   # pylint: disable=R0902, R0205
    "Object for Radioisotope Thermoelectric Generators"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.itype = "?"
        self.ielement = "??"

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            parts = self.text.replace("-compatible", "").strip().split(" ", 2)
            self.ielement = parts[0]
            self.itype = parts[1]
            assert self.ielement in ITEM_ELEMENTS
            assert self.itype in ITEM_TYPES

    def __str__(self):

        if self.is_microchip():
            return "a %s-compatible microchip" % self.ielement
        if self.is_generator():
            return "a %s generator" % self.ielement
        return '?? ?'

    def __eq__(self, other):
        return self.itype == other.itype and self.ielement == other.ielement

    def __lt__(self, other):
        if self.ielement == other.ielement:
            return self.itype < other.itype
        return self.ielement < other.ielement

    def __hash__(self):
        return hash((self.itype, self.ielement))

    def initials(self):
        "Return item as EeT, e.g. HyM for hydrogen microchip"
        return ''.join([self.ielement[:2].capitalize(), self.itype[0].capitalize()])

    def is_generator(self):
        "Returns true if the item is a generator"
        return self.itype == "generator"

    def is_microchip(self):
        "Returns true if the item is a microchip"
        return self.itype == "microchip"

    def is_element(self, element):
        "Returns true if the item is for the specified element"
        return self.ielement == element

    def clone(self):
        "Return a copy of item"

        # 1. Create a new item
        other = Item()

        # 2. Copy the information
        other.text = "clone of " + self.text
        other.part2 = self.part2
        other.ielement = self.ielement
        other.itype = self.itype

        # 3. Return the clone
        return other

    def other(self):
        "Return an item of the other type"

        # 1. Make a clone
        other = self.clone()

        # 2. Change it to the other
        other.text = "other of " + self.text
        other.itype = OTHER[self.itype]

        # 3. Return an item of the other type
        return other

    def are_safe(self, other):
        "Return True if the two item are safe together"
        if self.itype == other.itype:
            return True
        if self.ielement == other.ielement:
            return True
        return False


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          i t e m . p y                         end
# ======================================================================
