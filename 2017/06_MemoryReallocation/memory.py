# ======================================================================
# Memory Reallocation
#   Advent of Code 2017 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                          m e m o r y . p y
# ======================================================================
"A solver for Memory Reallocation for Advent of Code 2017 Day 06"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Memory
# ======================================================================


class Memory(object):
    """Object representing a memory redistribution solver"""

    def __init__(self, part2=False, text=None):

        # 1. Set the initial values
        self.part2 = part2
        if text is not None:
            self.banks = [int(_) for _ in text.split()]
        else:
            self.banks = []
        self.previous = {}

    def __str__(self):
        return '|'.join(str(_) for _ in self.banks)

    def previously_seen(self):
        "Return True of current configuration was seen previously"

        return str(self) in self.previous

    def maximum(self):
        "Return the number of the memory bank with the most blocks"

        # 1. Assume the first
        result = 0
        max_blocks = self.banks[0]

        # 2. Loop for the rest of the banks
        for bnum, blocks in enumerate(self.banks):

            # 3. If this one has more blocks, save new high water mark
            if blocks > max_blocks:
                result = bnum
                max_blocks = blocks

        # 4. Return the number of the bank with the most blocks
        return result

    def distribute(self, bank):
        "Distribute the memory blocks in the specified bank"

        # 1. Get the number of blocks in the bank
        blocks = self.banks[bank]

        # 2. Zero out the blocks in that bank
        self.banks[bank] = 0

        # 3. Is there enough for everyone?
        everyone = blocks // len(self.banks)

        # 4. Give everone what we can
        if everyone > 0:
            self.banks = [everyone + _ for _ in self.banks]
            blocks -= everyone * len(self.banks)

        # 5. Distribute the rest of the memory blocks to each bank in turn
        while blocks > 0:

            # 6. Advance to the next bank
            bank += 1
            bank %= len(self.banks)

            # 7. Give that bank one memory
            self.banks[bank] += 1
            blocks -= 1

    def one_cycle(self, verbose=False):
        "Execute one jump for the current location"

        # 1. Find the bank with the most blocks
        max_bank = self.maximum()
        max_blocks = self.banks[max_bank]

        # 2. Distribute the memory blocks
        self.distribute(max_bank)
        if verbose:
            print("Distributed %d memory blocks from bank %d" %
                  (max_blocks, max_bank))

        # 3. Return number of blocks distributed
        return max_blocks

    def cycle_until_seen(self, verbose=False, limit=0):
        "Redistribute memory blocks until we get a feeling of deja vu"

        # 1. Start loop counter at zero
        result = 0

        # 2. Loop until previously seen
        while not self.previously_seen():

            # 3. Remember the current configuration
            self.previous[str(self)] = result

            # 4. Execute one memory distribution cycle
            self.one_cycle(verbose=verbose)

            # 5. Increment loop counter
            result += 1

            # 6. Did we the iteration limit?
            if 0 < limit < result:
                result = None
                break

        # 7. Announce the number of cycles (if requested)
        if verbose:
            if result is None:
                print("Limit of %d cycles reached" % (limit))
            else:
                print("After %d cycles, the configuration of %s is repeated" %
                      (result, self.banks))

        # 8. Return the number of cycles until a repeat (or for part2 length of cycle)
        if self.part2:
            return result - self.previous[str(self)]
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         m e m o r y . p y                      end
# ======================================================================
