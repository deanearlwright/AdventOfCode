
# ======================================================================
# Distress Signal
#   Advent of Code 2022 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p a c k e t . p y
# ======================================================================
"Packet for the Advent of Code 2022 Day 13 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Packet
# ======================================================================


class Packet(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Distress Signal"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.left = []
        self.right = []

        # 2. Process text (if any)
        if text is not None and len(text) == 2:
            self.left = eval(text[0])  # pylint: disable=W0123
            self.right = eval(text[1])  # pylint: disable=W0123

    def is_ordered(self):
        "Are the packets in the correct order?"
        # print(f"is_ordered {self.left}  {self.right}")

        return Packet.ordered(self.left, self.right)

    @staticmethod
    def ordered(left, right):  # pylint: disable=R0911
        "Return True if the ordered according to the rules"
        # print(f"ordered {left}  {right}")

        # 1. If both values are integers, the lower integer should come first
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return True
            if left > right:
                return False
            return None

        # 2. If both values are lists, compare thier elements
        if isinstance(left, list) and isinstance(right, list):
            for left_item, right_item in zip(left, right):
                cmpr = Packet.ordered(left_item, right_item)
                if isinstance(cmpr, bool):
                    return cmpr
            if len(left) < len(right):
                return True
            if len(right) < len(left):
                return False
            return None

        # 3. If exactly one value is an integer, convert to list
        if isinstance(left, int):
            return Packet.ordered([left], right)
        return Packet.ordered(left, [right])


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        p a c k e t . p y                       end
# ======================================================================
