
# ======================================================================
# RAM Run
#   Advent of Code 2024 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         m e m o r y . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 18 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple

# ----------------------------------------------------------------------
#                                                                  types
# ----------------------------------------------------------------------

State = namedtuple("State", "loc, path")

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DELTA = [(0, 1), (1, 0), (-1, 0), (0, -1)]
DEFAULT_SIZE = 70
DEFAULT_BYTES = 1024

# ======================================================================
#                                                                 Memory
# ======================================================================


class Memory(object):   # pylint: disable=R0902, R0205
    "Object for RAM Run"

    def __init__(self, text=None, part2=False,
                 size=DEFAULT_SIZE, fall=DEFAULT_BYTES):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.size = size
        self.start = (0, 0)
        self.exit = (size, size)
        self.falling = []
        self.fall = fall
        self.corrupted = set()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text()

    def _process_text(self):
        "Assign values from text"

        assert self.text is not None and len(self.text) > 0

        # 1. Loop for each line of the input text
        for line in self.text:

            # 2. Get the location of the falling bytes
            col, row = line.split(",")
            loc = (int(col), int(row))

            # 3. Save them in the list
            self.falling.append(loc)

            # 4. Make the space as corrupted, if we haven't reached the limit
            if self.fall is not None and len(self.corrupted) < self.fall:
                self.corrupted.add(loc)

    def next_step(self, loc):
        "Return the next possible locations"

        # 1. Start with nothing
        result = []

        # 2. Loop for all possible directions
        for delta in DELTA:

            # 3. Compute the new_location
            new_loc = (loc[0] + delta[0], loc[1] + delta[1])

            # 4. Is it off the map?
            if new_loc[0] < 0 or new_loc[1] < 0:
                continue
            if new_loc[0] > self.size or new_loc[1] > self.size:
                continue

            # 5. Has the new location been corrupted?
            if new_loc in self.corrupted:
                continue

            # 6. Looks good to me, add it to the list
            result.append(new_loc)

        # 7. Return the possible new locations
        return result

    def min_steps_to_exit(self):
        "Find the minimum of steps to the exit"

        # 1. Create the initial state and add it to the queue
        seen = set([self.start])
        steps = 1
        queue = [self.start]

        # 2. Loop while there is something to do
        while len(queue) > 0:

            # 3. Process all the states in the current step
            for _ in range(len(queue)):
                loc = queue.pop(0)

                # 4. Where can we go from here?
                locs = self.next_step(loc)

                # 5. Check the locations out
                for loc in locs:
                    if loc == self.exit:
                        return steps
                    if loc in seen:
                        continue

                    # 6. Looks like someplace to go
                    seen.add(loc)
                    queue.append(loc)

            # 6. Increment the steps
            steps += 1

        # 7. Can't get there from here
        return None

    def find_blockage(self):
        "Find when the exit is blocked"

        # 1. Loop for the rest of the falling blocks
        for indx in range(self.fall, len(self.falling)):
            loc = self.falling[indx]

            # 2. Add the block into corrupted blocks
            self.corrupted.add(loc)

            # 3. Is there still a path?
            steps = self.min_steps_to_exit()

            # 4. Nope, this is the blocking byte
            if steps is None:
                return loc

        # 5. Weird, I expected a blockage
        return None

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        return self.min_steps_to_exit()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part two
        loc = self.find_blockage()
        if loc is None:
            return None
        return str(loc)[1:-1].replace(" ", "")

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        m e m o r y . p y                       end
# ======================================================================
