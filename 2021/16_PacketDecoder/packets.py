# ======================================================================
# Packet Decoder
#   Advent of Code 2021 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p a c k e t s . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import packet

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                Packets
# ======================================================================


class Packets(object):   # pylint: disable=R0902, R0205
    "Object for Packet Decoder"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.packet = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.packet = packet.Packet(text=text[0], part2=part2)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return sum(self.packet.versions())

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.packet.execute()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       p a c k e t s . p y                      end
# ======================================================================
