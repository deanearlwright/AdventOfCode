# ======================================================================
# Packet Decoder
#   Advent of Code 2021 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p a c k e t . p y
# ======================================================================
"Packet for the Advent of Code 2021 Day 16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import math

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
TYPE_LITERAL = 4

# ======================================================================
#                                                                 Packet
# ======================================================================


class Packet(object):   # pylint: disable=R0902, R0205
    "Object for Packet Decoder"

    def __init__(self, text=None, bits=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.bits = ""
        self.version = 0
        self.ptype = 0
        self.ltype = 0
        self.length = 0
        self.size = 0
        self.literal = 0
        self.packets = []

        # 2. If we have some text, fill out the rest of the information
        if text and len(text) > 0:
            self.bits = str(bin(int(text, 16)))[2:].zfill(len(text * 4))
            self.decode()

        # 3. If we have some text, fill out the rest of the information
        elif bits and len(bits) > 0:
            self.bits = bits[:]
            self.decode()

    def decode(self):
        "Decode the packet (and possible sub-packets"

        # 1. Get the version and type (3 bits each)
        self.version = int(self.bits[0:3], 2)
        self.ptype = int(self.bits[3:6], 2)

        # 2. Decode the rest of the bits
        if self.is_literal():
            self.decode_literal()
        else:
            self.decode_operator()

    def decode_literal(self):
        "Decode a literal packet"

        # 1. Start with nothing
        digits = []

        # 2. Loop grabbing digits
        for index in range(6, len(self.bits), 5):

            # 3. Grab the flag + digit
            flag = self.bits[index]
            digit = self.bits[index + 1: index + 5]

            # 4. Append the digit to the digits
            digits.append(digit)

            # 5. Are we done yet?
            if flag == "0":
                break

        # 6. Set the number and the value as the value is the number
        self.literal = int(''.join(digits), 2)

        # 7. And the size of the literal packet
        self.size = 6 + 5 * len(digits)

    def decode_operator(self):
        "Decode an operator packet"

        # 1. Decode the length type and length
        self.ltype = int(self.bits[6])
        if self.ltype == 0:
            self.length = int(self.bits[7:22], 2)
        else:
            self.length = int(self.bits[7:18], 2)

        # 2. Decode the inner packets
        if self.ltype == 0:
            self.decode_op_bits()
        else:
            self.decode_op_pkts()

    def decode_op_bits(self):
        "Decode packets based on the number of bits"

        # 1. Get the bits for the packets
        packet_bits = self.bits[22:23 + self.length]

        # 2. Loop while we have bits
        packet_index = 0
        while packet_index + 7 < self.length:

            # 3. Create a packet
            one_packet = Packet(bits=packet_bits[packet_index:], part2=self.part2)

            # 4. Add the packet to the packets for this packet
            self.packets.append(one_packet)

            # 5. Advance the packet_index
            packet_index += one_packet.size

        # 6. Save the size of this operator packet
        self.size = 7 + 15 + self.length

    def decode_op_pkts(self):
        "Decode packets based on the number of packets"

        # 1. Get the bits for the packets
        packet_bits = self.bits[18:]

        # 2. Loop for the number of packets
        packet_index = 0
        for _ in range(self.length):

            # 3. Create a packet
            one_packet = Packet(bits=packet_bits[packet_index:], part2=self.part2)

            # 4. Add the packet to the packets for this packet
            self.packets.append(one_packet)

            # 5. Advance the packet_index
            packet_index += one_packet.size

        # 6. Save the size of this operator packet
        self.size = 7 + 11 + packet_index

    def is_literal(self):
        "Return True if this is a literal packet"
        return self.ptype == TYPE_LITERAL

    def is_operator(self):
        "Return True if this is an operator packet"
        return self.ptype != TYPE_LITERAL

    def versions(self):
        "Return the version number of the packet in all sub-packets"

        # 1. Start with this packet's version number
        result = [self.version]

        # 2. Loop for all of the sub-packets
        for sub_packet in self.packets:

            # 3. Get and append the sub-packet version number(s)
            result.extend(sub_packet.versions())

        # 4. Return all of the version numbers (or just the one)
        return result

    def values(self):
        "Return the value of the packet in all sub-packets"

        # 1. Start with nothing
        result = []

        # 2. If the packet is a literal, return its value
        if self.is_literal():
            return [self.literal]

        # 3. Loop for all of the sub-packets
        for sub_packet in self.packets:

            # 4. Get and append the sub-packet's value
            result.append(sub_packet.execute())

        # 5. Return all of the values numbers
        return result

    def execute(self):
        "Return the value from executing the packet"

        # 1. Get the values of the sub-packets
        values = self.values()

        # 2. Switch based on the ptype
        if self.ptype == 0:  # sum
            value = sum(values)
        elif self.ptype == 1:  # product
            value = math.prod(values)
        elif self.ptype == 2:  # minimum
            value = min(values)
        elif self.ptype == 3:  # maximum
            value = max(values)
        elif self.ptype == 4:  # literal
            value = values[0]
        elif self.ptype == 5:  # greater than
            value = int(values[0] > values[1])
        elif self.ptype == 6:  # less then
            value = int(values[0] < values[1])
        elif self.ptype == 7:  # equal to
            value = int(values[0] == values[1])

        # 3. Return the computed value of the packet
        return value


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        p a c k e t . p y                       end
# ======================================================================
