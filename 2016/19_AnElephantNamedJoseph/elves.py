# ======================================================================
# An Elephant Named Joseph
#   Advent of Code 2016 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         e l v e s . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 19 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Elves
# ======================================================================


class Elves(object):   # pylint: disable=R0902, R0205
    "Object for An Elephant Named Joseph"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.number = 0
        self.elves = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.number = int(text[0])
            self.elves = [1 for _ in range(self.number)]

    def on_left(self, elf):
        "Return index of elf to the left of the specified elf"

        # 1. Go around the circle clockwise
        for left in range(elf + 1, self.number + 1):
            if self.elves[left - 1] > 0:
                return left

        # 2. Try from the other end
        for left in range(1, elf):
            if self.elves[left - 1] > 0:
                return left

        # 3. There must be only one left
        return elf

    def takes(self, taker, giver):
        "Elf takes presents"

        # 1. taker gets
        self.elves[taker - 1] += self.elves[giver - 1]

        # 2. giver gets nothing
        self.elves[giver - 1] = 0

    def presents(self, elf):
        "Returns the number of presents that the elf has"
        return self.elves[elf - 1]

    def party_on(self):
        "Return the number of the elf with all the presents"

        # 1. Start the taking at the left to the specified wlf
        elf = 1
        left = self.on_left(elf)

        # 2. There can be only one
        while elf != left:

            # 3. Take the presents
            self.takes(elf, left)

            # 4. Advance to the next pair
            elf = self.on_left(elf)
            left = self.on_left(elf)

        return elf

    def across(self, elf, size):
        "Return the number of the elf across from the specified elf"

        # 1. How far is halfway?
        half = size // 2

        # 2. Start with the specified elf
        result = elf

        # 3. Go halfway around
        for _ in range(half):
            result = self.on_left(result)

        # 4. Now thats the elf
        return result

    def party_on_two(self):
        "Return the number of the elf with all the presents for part two"

        # 1. Start the with all the elves
        size = self.number
        elf = 1

        # 2. There can be only one
        while size > 1:

            # 3. Determine from who this elf take the present
            across = self.across(elf, size)

            # 3. Take the presents
            self.takes(elf, across)
            #print(size, elf, across, self.presents(elf), flush=True)
            size -= 1

            # 4. Advance to the next elf
            elf = self.on_left(elf)

        return elf

    def party_on_dude(self):
        "Return the number of the elf with all the presents for part two using science"

        # 1. Find the power of two less than the size
        power = 1
        next_power = power * 3
        while next_power <= self.number:
            power = next_power
            next_power *= 3

        # 2. Get the remainder after subtracting the power
        remainder = self.number - power

        # 3. If no remainder, result is the power
        if remainder == 0:
            return power

        # 4. If remainder is less than the power, that is the answer
        if remainder <= power:
            return remainder

        # 5. Else the results is a little more complicated
        return remainder * 2 - power

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.party_on()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.party_on_dude()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         e l v e s . p y                        end
# ======================================================================
