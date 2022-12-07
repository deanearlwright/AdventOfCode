# ======================================================================
# Tuning Trouble
#   Advent of Code 2022 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d e v i c e . p y
# ======================================================================
"Device for the Advent of Code 2022 Day 06 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Device
# ======================================================================


class Device(object):   # pylint: disable=R0902, R0205
    "Object for Tuning Trouble"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.chars = set()

    def start_of_packet(self, hdrlen=4):
        "Return index of the start-of-packet marker"

        # 1. Loop for characters in the text
        for indx in range(hdrlen, len(self.text)):

            # 2. Get a chunk of the characters
            chars = self.text[indx - hdrlen:indx]
            assert hdrlen == len(chars)

            # 2. Are these characters unique?
            self.chars.update(list(chars))
            if len(self.chars) == hdrlen:
                return indx

            # 4. Clear out the set for use next time
            self.chars.clear()

        # 5. Failed to find a bunch of different characters
        return -1


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        d e v i c e . p y                       end
# ======================================================================
