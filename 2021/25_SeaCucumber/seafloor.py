# ======================================================================
# Sea Cucumber
#   Advent of Code 2021 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s e a f l o o r . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 25 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EAST = '>'
SOUTH = 'v'
EMPTY = '.'

DELTA = {
    EAST: (1, 0),
    SOUTH: (0, 1),
}
# ======================================================================
#                                                               Seafloor
# ======================================================================


class Seafloor(object):   # pylint: disable=R0902, R0205
    "Object for Sea Cucumber"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.eastern = set()
        self.southern = set()
        self.rows = 0
        self.cols = 0
        self.steps = 0
        self.moved = True

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.rows = len(text)
            self.cols = len(text[0])
            for row, line in enumerate(text):
                for col, char in enumerate(line):
                    if char == EAST:
                        self.eastern.add((col, row))
                    elif char == SOUTH:
                        self.southern.add((col, row))

    def in_front_of(self, loc, which):
        "Return the location of the space in front of the cucumber"

        # 1. Get the next location
        new_loc = (loc[0] + DELTA[which][0], loc[1] + DELTA[which][1])

        # 2. Too far east?
        if new_loc[0] >= self.cols:
            new_loc = (0, new_loc[1])

        # 3. Or too far south
        if new_loc[1] >= self.rows:
            new_loc = (new_loc[0], 0)

        # 4. Return the location of the space in front of the cucumber
        return new_loc

    def step_east(self):
        "Move all of the eastern herd of cucumbers"

        # 1. Start with nothing
        result = set()

        # 2. Loop for all of the eastern cucumbers
        for loc in self.eastern:

            # 3. What is the next location for this cucumber
            next_loc = self.in_front_of(loc, EAST)

            # 4. Is it empty?
            if next_loc not in self.eastern and next_loc not in self.southern:

                # 5. Yes, move there
                result.add(next_loc)
                self.moved = True

            else:
                # 6. No, remain in place
                result.add(loc)

        # 8. Return the updated eastern cucumbers
        return result

    def step_south(self):
        "Move all of the souther herd of cucumbers"

        # 1. Start with nothing
        result = set()

        # 2. Loop for all of the southern cucumbers
        for loc in self.southern:

            # 3. What is the next location for this cucumber
            next_loc = self.in_front_of(loc, SOUTH)

            # 4. Is it empty?
            if next_loc not in self.eastern and next_loc not in self.southern:

                # 5. Yes, move there
                result.add(next_loc)
                self.moved = True

            else:
                # 6. No, remain in place
                result.add(loc)

        # 9. Return the updated southern cucumbers
        return result

    def step(self):
        "Move all of the cucumbers"

        # 1. Assume that there will be no movement
        self.moved = False

        # 2. Move the eastern cucumbers
        self.eastern = self.step_east()

        # 3. Move the southern cucumbers
        self.southern = self.step_south()

        # 4. Increment the number of steps
        self.steps += 1

    def run(self):
        "Advance the cucumbers until they stop"

        # 1. Loop until then stop
        while self.moved:

            # 2. Move the cucumbers
            self.step()

        # 3. Return the number of steps
        return self.steps

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.run()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.run()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      s e a f l o o r . p y                     end
# ======================================================================
