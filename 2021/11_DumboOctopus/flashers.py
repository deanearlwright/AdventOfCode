# ======================================================================
# Dumbo Octopus
#   Advent of Code 2021 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         f l a s h e r s . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 11 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DELTA = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1), ]

# ======================================================================
#                                                               Flashers
# ======================================================================


class Flashers(object):   # pylint: disable=R0902, R0205
    "Object for Dumbo Octopus"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.octos = {}
        self.flashes = 0
        self.step = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for rindex, row in enumerate(text):
                for cindex, col in enumerate(row):
                    self.octos[(cindex, rindex)] = int(col)

    def single_step(self):
        "Execute a single step"

        # 1. Start with no flashes
        flashed = set()
        flashing = []

        # 2. Increase all energies by one, and record the initial flashers
        for loc, energy in self.octos.items():
            self.octos[loc] = energy + 1
            if energy == 9:
                flashed.add(loc)
                flashing.append(loc)

        # 3. Loop while that could be more flashing
        while len(flashing) > 0:

            # 4. Get the a flasher and its neighbors
            loc = flashing.pop()
            nbrs = self.neighbors(loc)

            # 5. Loop for all of the flasher's neighbors
            for nbr in nbrs:

                # 6. Can only flash once per step
                if nbr not in flashed:

                    # 7. Increment the neighbor's energy (maybe to the flash point)
                    energy = self.octos[nbr]
                    self.octos[nbr] = energy + 1
                    if energy == 9:
                        flashed.add(nbr)
                        flashing.append(nbr)

        # 8. Set the flashers energy back to zero
        for loc in flashed:
            self.octos[loc] = 0

        # 9. Record the passage of time
        self.step += 1
        self.flashes += len(flashed)

        # 9. Return the number of flashes in this step
        return len(flashed)

    def neighbors(self, loc):
        "Return the nearby locations"

        # 1. Start with nothing
        result = []

        # 2. Loop for the neighbors
        for delta in DELTA:

            # 3. Get the location
            nloc = (loc[0] + delta[0], loc[1] + delta[1])

            # 4. Is it a valid location, add it to the list
            if nloc in self.octos:
                result.append(nloc)

        # 5. Return the location of the neighbors
        return result

    def run_until(self, step):
        "Execute steps until the specified time is reached"

        # 1. Loop until the step the step is reached
        while self.step < step:

            # 2. Execute a single step
            self.single_step()

        # 3. Return the total number of flashes
        return self.flashes

    def all_flash(self):
        "Return the step when octopuses will all flash simultaneously"

        # 1. Loop until they all flash
        while self.single_step() < 100:
            continue

        # 2. Return that mighty step number
        return self.step

    def __str__(self):
        "Return the octopuses as a string"

        # 1. Start with nothing
        result = []

        # 2. Loop for all of the rows
        for rindex in range(10):
            row = []

            # 3. Loop for all of the columns
            for cindex in range(10):

                # 4. Add the energy level to the row
                row.append(str(self.octos[(cindex, rindex)]))

            # 4. Append the row to the result
            result.append(''.join(row))

        # 5. Return the the entire grid
        return "\n".join(result)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.run_until(100)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.all_flash()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      f l a s h e r s . p y                     end
# ======================================================================
