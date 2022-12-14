
# ======================================================================
# Distress Signal
#   Advent of Code 2022 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d e v i c e . p y
# ======================================================================
"Device for the Advent of Code 2022 Day 13 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from functools import cmp_to_key

import packet

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Device
# ======================================================================


class Device(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Distress Signal"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.packets = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

        # 3. For part2 add in another pair
        if part2:
            self._process_text(["[[2]]", "[[6]]"])

    def _process_text(self, text):
        "Assign values from text"

        # 1. Loop for pairs of text lines
        for indx in range(0, len(text), 2):

            # 2. Create a packet pair from the lines
            pkt = packet.Packet(text=[text[indx], text[indx + 1]],
                                part2=self.part2)

            # 3. Add the packet to the list
            self.packets.append(pkt)

    def right_order(self):
        "Returns the sum of the ordered packet indices"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all the packet pairs
        for indx, pkt in enumerate(self.packets):

            # 3. If pair is in order add it's index to the result
            if pkt.is_ordered():
                result += 1 + indx

        # 4. Return the sum of the indices for right order packet pairs
        return result

    def decorder_key(self):
        "Determine the decoder key for the distress signal"

        # 1. Collect all of the packet messages
        msgs = []
        for pkt in self.packets:
            msgs.append(pkt.text[0])
            msgs.append(pkt.text[1])

        # 2. Sort the packet messages
        msgs.sort(key=cmp_to_key(Device.cmp))
        #  print(msgs)

        # 3. Find the index of the divider packets
        divider_2 = 1 + msgs.index("[[2]]")
        divider_6 = 1 + msgs.index("[[6]]")
        #  print(divider_2, divider_6)

        # 4. Return the product of the two divider packers
        return divider_2 * divider_6

    @staticmethod
    def cmp(a_msg, b_msg):
        "Compare two msg texts"

        # 1. Create a packet from the two texts
        pkt = packet.Packet(text=[a_msg, b_msg])

        # 2. Compare to two msgs
        ordered = pkt.is_ordered()

        # 3. Return -1 for ordered, 0 for None, and 1 for not ordered
        if ordered is None:
            return 0
        if ordered:
            return -1
        return 1


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        d e v i c e . p y                       end
# ======================================================================
