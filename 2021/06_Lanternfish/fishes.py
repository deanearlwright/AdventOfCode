# ======================================================================
# Lanternfish
#   Advent of Code 2021 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         f i s h e s . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 06 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Fishes
# ======================================================================


class Fishes(object):   # pylint: disable=R0902, R0205
    "Object for Lanternfish"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.fishes = []
        self.day = 0
        self.fish_timer = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.fishes = [int(x) for x in text[0].split(',')]
            for fish in self.fishes:
                self.fish_timer[fish] += 1
            # print("FT", self.fish_timer, sum(self.fish_timer))

    def next_day(self):
        "Count down the fish"

        # 1. Assume no new fish
        new_fish = 0

        # 2. Loop for all the fishies
        for index, timer in enumerate(self.fishes):

            # 3. Decrement the timer
            new_time = timer - 1

            # 4. Was there a birth?
            if new_time < 0:
                new_fish += 1
                new_time = 6

            # 5. Save the updated timer
            self.fishes[index] = new_time

        # 6. Add the new fish to the end
        self.fishes.extend([8 for _ in range(new_fish)])

        # 7. Update the big clock
        self.day += 1

    def next_day_two(self):
        "Count down the fish"

        # 1. Start with no fishes
        new_fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        # 2. Start Loop for all the fishies timers
        for index, number in enumerate(self.fish_timer):
            # print("Before", self.day, index, number, new_fish)

            # 3. Decrement the timer
            new_time = index - 1

            # 4. Was there a birth?
            if new_time < 0:
                new_fish[8] = number
                new_time = 6

            # 5. Save the updated timer
            new_fish[new_time] += number

        # 6. Set the new fish time counts
        self.fish_timer = new_fish

        # 7. Update the big clock
        self.day += 1

    def go_until(self, day=80):
        "Day by day by day by day"

        # 1. Loop until we reach the indicated day
        while self.day < day:

            # 2. "Repent, Harlequin!" Said the Ticktockman
            self.next_day()
            # print("%d,%d" % (self.day, len(self.fishes)))

        # 3. Return the number of fish
        return len(self.fishes)

    def go_until_two(self, day=80):
        "Day by day by day by day"

        # 1. Loop until we reach the indicated day
        while self.day < day:

            # 2. "Repent, Harlequin!" Said the Ticktockman
            self.next_day_two()
            # print("%d,%d" % (self.day, sum(self.fish_timer)))

        # 3. Return the number of fish
        return sum(self.fish_timer)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.go_until()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.go_until_two(day=256)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        f i s h e s . p y                       end
# ======================================================================
