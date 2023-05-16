
# ======================================================================
# Pyroclastic Flow
#   Advent of Code 2022 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s i m u l a t i o n . p y
# ======================================================================
"Simulation for the Advent of Code 2022 Day 17 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple

import chamber
import rocks

# ----------------------------------------------------------------------
#                                                                  types
# ----------------------------------------------------------------------
State = namedtuple('State', 'rock, wind, heights')

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DEQUE_SIZE = 30

# ======================================================================
#                                                             Simulation
# ======================================================================


class Simulation(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Pyroclastic Flow"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.chamber = None
        self.rocks = None
        self.winds = None
        self.next_wind = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.winds = text[0]
            self.chamber = chamber.Chamber(text="7", part2=part2)
            self.rocks = rocks.Rocks(text=rocks.ROCKS, part2=part2)

    def one_step(self):
        "Execute one step of the simulation"

        # 0. I need something to work with
        if not self.chamber:
            return

        # 1. If there are no falling rocks, set one falling
        if self.chamber.falling is None:
            self.chamber.add_rock(self.rocks.next_rock())

        # 2. Push the rock sideways
        self.chamber.push_rock(self.winds[self.next_wind])
        self.next_wind = (self.next_wind + 1) % len(self.winds)

        # 3. Let the rock fall
        self.chamber.move_down()

    def one_rock(self):
        "Execure the simulation until a rock comes to rest"

        # 1. Get the current number of rocks
        num_rocks = self.chamber.rocks

        # 2. Loop until we the number of rocks changes
        while num_rocks == self.chamber.rocks:

            # 3. Execute a single step of the simulation
            self.one_step()

        # 4. Return the number of fallen rocks
        return self.chamber.rocks

    def run_for_n_rocks(self, number, delta=0, verbose=False):
        "Run the simulation until the specific number of rocks come to rest"

        # 0. I need something to work with
        if not self.chamber:
            return None

        # 1. Loop until we get enough rocks
        while self.chamber.rocks < number:

            # 2. Execute the simulation until the number of rocks increase
            rocks = self.one_rock()
            if verbose and 0 == rocks % 100:
                print(f"run_for_n_rocks, {rocks} down, {number - rocks} more to go")

        # 3. Return the height of the tower of rocks
        return self.chamber.get_highest(delta=delta)

    def calculate_n_rocks(self, number, verbose=False):
        "Run the simulation until the specific number of rocks come to rest"

        # 0. I need something to work with
        if not self.chamber:
            return None

        # 1. Set up for finding a cycle
        seen = {}
        last_height = 0

        # 2. Loop until we get enough rocks (or we find a cycle)
        while self.chamber.rocks < number:

            # 3. Execute a single simulation step (side/down)
            rocks = self.one_rock()
            if 0 == rocks % 100:
                print(f"look for cycle, {rocks} down, {number - rocks} more to go")

            # 4. Generate the current state
            heights = self.chamber.relative_heights()
            next_rock = self.rocks.next_rock
            next_wind = self.next_wind
            cur_rocks = self.chamber.rocks
            cur_height = self.chamber.get_highest()
            state = State(rock=next_rock, wind=next_wind, heights=heights)

            # 5. If this is a new state, add it and continue
            if state not in seen:
                seen[state] = (cur_rocks, cur_height)
                continue

            # 6. Found a cycle
            if verbose:
                print(f"found a cycle after {self.chamber.rocks} rocks")
            start_rocks, start_height = seen[state]
            cycle_rocks = cur_rocks - start_rocks
            cycle_height = cur_height - start_height
            if verbose:
                print(f"At start of cycle: rocks={start_rocks}, height = {start_height}")
                print(f"At end of cycle: rocks={cur_rocks}, height = {cur_height}")
                print(f"  difference in rocks={cycle_rocks}, height={cycle_height}")
            cycles_to_do = (number - cur_rocks) // cycle_rocks
            add_rocks = cycles_to_do * cycle_rocks
            add_height = cycles_to_do * cycle_height
            if verbose:
                print(f"Cycles left={cycles_to_do}")
                print(f"  additional rocks={add_rocks}, height={add_height}")

            # 7. Finish off the similation
            self.chamber.rocks += add_rocks
            return self.run_for_n_rocks(number, delta=add_height)

            #
        # 3. Return the height of the tower of rocks
        return self.chamber.get_highest()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    s i m u l a t i o n . p y                   end
# ======================================================================
