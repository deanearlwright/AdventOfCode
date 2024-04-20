
# ======================================================================
# Clumsy Crucible
#   Advent of Code 2023 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c r u c i b l e . p y
# ======================================================================
"Crucible for the Advent of Code 2023 Day 17 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import heapq
from collections import namedtuple

from blocks import Blocks

# ----------------------------------------------------------------------
#                                                                  types
# ----------------------------------------------------------------------
Seen = namedtuple('Seen', 'loc, dirs')
State = namedtuple('State', 'heat, seen')

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
NORTH = '^'
SOUTH = 'v'
EAST = '>'
WEST = '<'
DIRECTIONS = [NORTH, SOUTH, EAST, WEST]
DELTA = {
    NORTH: (-1, 0),
    SOUTH: (1, 0),
    EAST: (0, 1),
    WEST: (0, -1),
}
REVERSED = {
    NORTH: SOUTH,
    SOUTH: NORTH,
    EAST: WEST,
    WEST: EAST,
}


# ======================================================================
#                                                               Crucible
# ======================================================================


class Crucible(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Clumsy Crucible"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.blocks = None
        self.loc = (0, 0)
        self.goal = (0, 0)
        self.total_heat_loss = 0
        self.directions = EAST
        self.min_steps = 1
        self.max_steps = 3
        if part2:
            self.min_steps = 4
            self.max_steps = 10

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.blocks = Blocks(text=text, part2=part2)
            self.goal = (self.blocks.rows - 1, self.blocks.cols - 1)

    def is_goal(self, loc=None):
        "Return True if at the goal"

        # 1. Get the location if not supplied
        if loc is None:
            loc = self.loc

        # 2. Are we there yet?
        return loc == self.goal

    def next_location(self, direction=EAST, loc=None):
        "Determine the next location in the given direction"

        # 0 Precondition axiom
        assert direction in DIRECTIONS

        # 1. Get the location if not supplied
        if loc is None:
            loc = self.loc

        # 1. Create the new location
        new_loc = (loc[0] + DELTA[direction][0], loc[1] + DELTA[direction][1])

        # 2. If not off your block, return the new location
        if (0 <= new_loc[0] < self.blocks.rows) and (0 <= new_loc[1] < self.blocks.cols):
            return new_loc

        # 3. Return failure
        return None

    def possible(self, loc=None, directions=None):
        "Return the possible directions from where we are"

        # 1. Start with nothing
        result = []
        if loc is None:
            loc = self.loc
        if directions is None:
            directions = self.directions

        # 2. Try all the directions
        for direction in DIRECTIONS:

            # 3. Can't reverse
            if REVERSED[direction] == directions[0]:
                continue

            # 4. Can't take too many steps (or two few steps) in the same direction
            steps = len(directions)
            if direction == directions[0] and (steps == self.max_steps):
                continue
            if direction != directions[0] and (steps < self.min_steps):
                continue

            # 5. Are we still on the grid?
            if self.next_location(loc=loc, direction=direction) is None:
                continue

            # 6. Looks good to me
            result.append(direction)

        # 7. Return the directions we can use from here
        return result

    def next_action(self, direction):
        "Adjust the crucible based on the direction"

        # 0 Precondition axiom
        assert direction in DIRECTIONS

        # 1. We can't reverse
        if direction == REVERSED[self.directions[0]]:
            return False

        # 2. Determine and check the new location
        new_loc = self.next_location(direction)
        if new_loc is None:
            return False

        # 3. If this is not a new direction, increment and check step count
        steps = len(self.directions)
        if direction == self.directions[0]:
            if steps >= self.max_steps:
                return False
            new_directions = self.directions + direction
        if direction != self.directions[0]:
            if steps < self.min_steps:
                return False
            new_directions = direction

        # 4 Determine heat loss
        new_loss = self.blocks.heat_loss(new_loc)

        # 5. Update
        self.loc = new_loc
        self.directions = new_directions
        self.total_heat_loss += new_loss

        # 6. Return success
        return True

    def search(self):
        "Search for the best bath (A*)"

        # 1. Start with nothing
        seen = set()
        heap = [
            State(heat=0, seen=Seen(loc=(0, 0), dirs=EAST)),
            State(heat=0, seen=Seen(loc=(0, 0), dirs=SOUTH))
        ]

        # 2. Loop until there is nothing to do
        while heap:

            # 3. Get the next state from the heap
            state_heat, state_seen = heapq.heappop(heap)
            state_loc, state_dirs = state_seen

            # 4. Don't explore the same place twice in the same direction
            if state_seen in seen:
                continue
            seen.add(state_seen)

            # 5. Find a suitable new direction
            for new_dir in self.possible(loc=state_loc, directions=state_dirs):

                # 6. Get the new location
                new_loc = (state_loc[0] + DELTA[new_dir][0], state_loc[1] + DELTA[new_dir][1])

                # 7. If continuing in the same direction, increase direction length
                if new_dir == state_dirs[-1]:
                    new_dir = state_dirs + new_dir

                # 8. If we have reached the goal, return the total heat loss
                new_heat = state_heat + self.blocks.heat_loss(new_loc)
                if new_loc == self.goal:
                    if len(new_dir) < self.min_steps:
                        continue
                    return new_heat

                # 9. Don't go where we have seen before
                new_seen = Seen(loc=new_loc, dirs=new_dir)
                if new_seen in seen:
                    continue

                # 10. Add where we are to the search
                heapq.heappush(heap, State(heat=new_heat, seen=new_seen))

        # 11. Failure is not an option
        return None


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      c r u c i b l e . p y                     end
# ======================================================================
