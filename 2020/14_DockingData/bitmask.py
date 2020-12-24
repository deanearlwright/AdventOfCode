# ======================================================================
# Docking Data
#   Advent of Code 2020 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         b i t m a s k . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 14 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DEFAULT_MASK = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
RE_MASK = re.compile('mask = ([01X]+)')
RE_MEM = re.compile('mem\[([0-9]+)\] = ([0-9]+)')
BIN36_FORMAT = '#038b'

# ======================================================================
#                                                                Bitmask
# ======================================================================


class Bitmask(object):   # pylint: disable=R0902, R0205
    "Object for Docking Data"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.mask = DEFAULT_MASK
        self.memory = {}

    def save_memory(self, line):
        "Save a masked value in memory"

        # 1. Parse the 'mem' line
        parts = RE_MEM.match(line)
        if parts is None:
            print('Unable to parse memory: %s' % line)
            return
        loc = int(parts.group(1))
        value = int(parts.group(2))

        # 2. Execute the mem instruction for part 1 or 2
        if self.part2:
            self.save_masked_loc(loc, value)
        else:
            self.save_masked_value(loc, value)

    def save_masked_value(self, loc, value):
        "Save masked value at location (part 1)"

        # 1. Get the masked value
        masked = self.apply_mask_to_value(value)
        # print('%d = %d (%d)' % (loc, value, masked))

        # 2. Save it to the specified location
        self.memory[loc] = masked

    def apply_mask_to_value(self, value):
        "Return the value with the mask applied"

        # 1. Get the value as 36 character bits
        value36 = format(value, BIN36_FORMAT)[2:]
        assert len(value36) == 36

        # 2. Apply the mask
        bits = []
        for v, m in zip(value36, self.mask):
            if m == 'X':
                bits.append(v)
            else:
                bits.append(m)

        # 3. Return the masked value as an integer
        return int(''.join(bits), 2)

    def save_masked_loc(self, loc, value):
        "Save value at masked location (part 2)"

        # 1. Get the masked location
        masked = self.apply_mask_to_loc(loc)

        # 2. Save the value to one or more locations
        self.save_multi_loc(masked, value)

    def apply_mask_to_loc(self, loc):
        "Return the loc with the mask applied"

        # 1. Get the location as 36 character bits
        loc36 = format(loc, BIN36_FORMAT)[2:]
        assert len(loc36) == 36

        # 2. Apply the mask
        bits = []
        for v, m in zip(loc36, self.mask):
            if m == 'X' or m == '1':
                bits.append(m)
            else:
                bits.append(v)

        # 3. Returned the masked loc as a character string (0s, 1s, and Xs)
        return ''.join(bits)

    def save_multi_loc(self, masked, value):
        "Save the value to multiple locations"

        # 1. Locate the first floating bit in the masked location
        first_x = masked.find('X')

        # 2. If there aren't any, save the value at the location
        if first_x == -1:
            loc = int(masked, 2)
            # print('%s (%d) = %d ' % (masked, loc, value))
            self.memory[loc] = value
            return

        # 3. Replace the floating bit with a 0 and with a 1
        mask_0 = masked[0:first_x] + '0' + masked[first_x + 1:]
        mask_1 = masked[0:first_x] + '1' + masked[first_x + 1:]

        # 4. Save the value at those two locations (which may also expand further)
        self.save_multi_loc(mask_0, value)
        self.save_multi_loc(mask_1, value)

    def save_mask(self, line):
        "Save a new mask value"

        # 1. Parse the 'mask' line
        parts = RE_MASK.match(line)
        if parts is None:
            print('Unable to parse mem: %s' % line)
            return
        mask = parts.group(1)
        assert len(mask) == 36

        # 2. Save the mask
        self.mask = mask

    def execute(self):
        "Run the initialization code"

        # 1. Loop for all instructions in the initialization code
        for line in self.text:

            # 2. Execute a mask or mem instruction as indicated
            if line.startswith('mask'):
                self.save_mask(line)
            else:
                self.save_memory(line)

        # 3. Return the sum of all of the memory locations
        return sum(self.memory.values())

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.execute()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.execute()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       b i t m a s k . p y                      end
# ======================================================================
