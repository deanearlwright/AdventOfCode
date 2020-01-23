# ======================================================================
# Spinlock
#   Advent of Code 2017 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s p i n l o c k . p y
# ======================================================================
"A solver for Spinlock for Advent of Code 2017 Day 17"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
P1_LAST_NUMBER = 2017
P2_LAST_NUMBER = 50000000 - 1

# ======================================================================
#                                                               Spinlock
# ======================================================================


class Spinlock(object):   # pylint: disable=R0902, R0205
    """Object for circular buffer spinlock"""

    def __init__(self, steps=None, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.buffer = [0]
        self.position = 0
        self.number = 1
        self.steps = steps

        # 2. Process text into steps (if any)
        if text is not None:
            self.steps = int(text)

    def __str__(self):
        result = []
        for bnum, bvalue in enumerate(self.buffer):
            if bnum == self.position:
                result.append('(%d)' % bvalue)
            else:
                result.append(' %d ' % bvalue)
        return ''.join(result).strip()

    def advance(self):
        "Advance the spinlock one round"

        # 1. Move the current position forward a certain number of steps
        self.position = (self.position + self.steps) % len(self.buffer)

        # 2. Insert the number there
        self.position += 1
        self.buffer.insert(self.position, self.number)

        # 3. Increment the number for next time
        self.number += 1

    def quick_advance(self):
        "Advance the spinlock one round but only worry about the second position"

        # 1. Move the current position forward a certain number of steps
        self.position = (self.position + self.steps) % self.number

        # 2. Insert the number there
        self.position += 1
        if self.position == 1:
            self.buffer = [self.number]

        # 3. Increment the number for next time
        self.number += 1

    def spin(self, final, verbose=False):
        "Run the spin lock a whole bunch of times"

        # 1. Loop a whole bunch of times
        while self.number <= final:

            # 2. Advance the spin lock
            self.advance()

            # 3. Output the state of the buffer (if requested)
            if verbose:
                print("%d: %s" % (self.number, self.buffer[:5]))

    def quick_spin(self, final, verbose=False):
        "Run the spin lock a whole bunch of times but only worry about the second position"

        # 1. Loop a whole bunch of times
        last_value = self.buffer[0]
        while self.number <= final:

            # 2. Advance the spin lock
            self.quick_advance()

            # 3. Output the state of the buffer (if requested)
            if verbose and last_value != self.buffer[0]:
                print("%d: %d --> %d" % (self.number, last_value, self.buffer[0]), flush=True)
                last_value = self.buffer[0]

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Spin the lock for a whole bunch of time
        self.spin(P1_LAST_NUMBER, verbose=verbose)

        # 2. Did we deposit the last number where we think we did?
        assert self.buffer[self.position] == P1_LAST_NUMBER
        assert self.buffer[0] == 0

        # 3. Return the number after the last one entered
        return self.buffer[self.position+1]


    def part_two_the_long_way(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Spin the lock for a whole bunch of time
        self.spin(P2_LAST_NUMBER, verbose=verbose)

        # 2. Did we deposit the last number where we think we did?
        assert self.buffer[self.position] == P2_LAST_NUMBER
        assert self.buffer[0] == 0

        # 3. Return the number after the last one entered
        return self.buffer[self.position+1]

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Spin the lock for a whole bunch of time
        self.quick_spin(P2_LAST_NUMBER, verbose=verbose)

        # 2. Return the number in the second position
        return self.buffer[0]




# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      s p i n l o c k . p y                     end
# ======================================================================
