# ======================================================================
# Reactor Reboot
#   Advent of Code 2021 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c u b e s . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 22 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import step

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Cubes
# ======================================================================


class Cubes(object):   # pylint: disable=R0902, R0205
    "Object for Reactor Reboot"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.steps = []
        self.state = set()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.steps.append(step.Step(text=line, part2=part2))

    def step(self, inst):
        "Execute a single instruction step"

        # 1. Get on or off
        which = inst.turn_on

        # 2. Get the limited dimensions
        limited = inst.limited()

        # 3. Loop for all of the dimensions
        for x_dim in range(limited[0][0], limited[0][1] + 1):
            for y_dim in range(limited[1][0], limited[1][1] + 1):
                for z_dim in range(limited[2][0], limited[2][1] + 1):

                    # 4. Turn the cube on or off
                    if which:
                        self.state.add((x_dim, y_dim, z_dim))
                    else:
                        self.state.discard((x_dim, y_dim, z_dim))

        # 4. Return number of "on" cubes -- mainly for testing
        return len(self.state)

    def all_steps(self):
        "Execute all instruction steps"

        # 1. Loop for all the steps
        for inst in self.steps:

            # 2. Execure the single statement
            self.step(inst)

        # 3. Return the number of "on" cubes
        return len(self.state)

    def step_two(self, inst, insts):
        "Execute a single instruction step"

        # 1. Start with entire area and no conflicts
        result = inst.size()
        overlaps = []

        # 2. Processing limited dimension can cause wonky results
        if result <= 0:
            return 0

        # 3. Loop for the remaining instruction steps
        for inst2 in insts:

            # 4. Do these two instructions overlap?
            overlap = inst.overlap(inst2)

            # 5. No, nothing to see here
            if not overlap:
                continue

            # 6. Else, Record the overlap -- Spent way too much time debugging, needed part2!!!!
            overlaps.append(step.Step(on=inst2.turn_on, ranges=overlap, part2=inst.part2))

        # 7. Loop for all of the conflicts
        for indx, overlap in enumerate(overlaps):

            # 8. Subtract out the holes (on or off -- we just don't care)
            result -= self.step_two(overlap, overlaps[indx + 1:])

        # 9. Return the size of area (minus any holes)
        return result

    def all_two(self):
        "Execute all instruction steps for two"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all the steps
        for indx, inst in enumerate(self.steps):

            # 3. Only worry about on
            if not inst.turn_on:
                continue

            # 4. Execure the single statement
            result += self.step_two(inst, self.steps[indx + 1:])

        # 5. Return the number of "on" cubes
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.all_steps()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.all_two()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         c u b e s . p y                        end
# ======================================================================
