
# ======================================================================
# Lens Library
#   Advent of Code 2023 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         b o x . p y
# ======================================================================
"Box for the Advent of Code 2023 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                    Box
# ======================================================================


class Box(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Lens Library"

    def __init__(self, number=0):

        # 1. Set the initial values
        self.number = number
        self.lenses = []
        self.lengths = []

    def operation(self, instruction):
        "Perform an operation on the box"

        # 1. If the instruction has a minus sign, it is a removal
        if "-" in instruction:
            self.remove_lens(instruction.replace("-", ""))
            return

        # 2. Else break instruction into lens and focal length
        lens, length = instruction.split("=")
        length = int(length)

        # 3. Perform the add lens instruction
        self.add_lens(lens, length)

    def add_lens(self, lens, length):
        "Add a lens to the box"

        # 1. If the lens is already in the box, update the length
        if self.has_lens(lens):
            lindx = self.lenses.index(lens)
            self.lengths[lindx] = length
            return

        # 2. Else add the lens and the length at the end
        self.lenses.append(lens)
        self.lengths.append(length)

    def remove_lens(self, lens):
        "Remove a lens from the box"

        # 1. If there is no such lens in the box, nothing to do
        if not self.has_lens(lens):
            return

        # 2. Get the index of the lens
        lindx = self.lenses.index(lens)

        # 3. Remove the lens and its length
        del self.lenses[lindx]
        del self.lengths[lindx]

    def has_lens(self, lens):
        "Return true if the already has that lens"
        return lens in self.lenses

    def power(self):
        "Return the focusing power of the lenses in the box"

        return (self.number + 1) * (
            sum((lindx + 1) * length for lindx, length in enumerate(self.lengths)))

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                           b o x . p y                          end
# ======================================================================
