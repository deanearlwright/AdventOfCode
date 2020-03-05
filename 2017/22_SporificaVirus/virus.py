# ======================================================================
# Sporifica Virus
#   Advent of Code 2017 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Computer implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         v i r u s . p y
# ======================================================================
"A solver for virus for Advent of Code 2017 Day 22"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

DIR_E = 'E'
DIR_W = 'W'
DIR_S = 'S'
DIR_N = 'N'

DELTA = {DIR_E: (1, 0),
         DIR_W: (-1, 0),
         DIR_N: (0, -1),
         DIR_S: (0, 1)}

LEFT = {DIR_E: DIR_N,
        DIR_W: DIR_S,
        DIR_N: DIR_W,
        DIR_S: DIR_E}

RIGHT = {DIR_E: DIR_S,
         DIR_W: DIR_N,
         DIR_N: DIR_E,
         DIR_S: DIR_W}

SAME = {DIR_E: DIR_E,
        DIR_W: DIR_W,
        DIR_N: DIR_N,
        DIR_S: DIR_S}

BACK = {DIR_E: DIR_W,
        DIR_W: DIR_E,
        DIR_N: DIR_S,
        DIR_S: DIR_N}

INITIAL_VIRUS_LOC = (0, 0)
INITIAL_VIRUS_DIR = DIR_N

VIRUS_CHAR = '#'
CLEAN_CHAR = '.'
FLAG_CHAR = 'F'
WEAK_CHAR = 'W'

PART_ONE_ITERATIONS = 10000
PART_TWO_ITERATIONS = 10000000

PART_TWO_VIRUS = {
    CLEAN_CHAR: WEAK_CHAR, # Clean nodes become weakened.
    WEAK_CHAR: VIRUS_CHAR, # Weakened nodes become infected.
    VIRUS_CHAR: FLAG_CHAR, # Infected nodes become flagged.
    FLAG_CHAR: CLEAN_CHAR, # Flagged nodes become clean.
    }

PART_TWO_MOVE = {
    CLEAN_CHAR: LEFT,  # If it is clean, it turns left.
    WEAK_CHAR: SAME,   # If it is weakened, it does not turn,
                       #  and will continue moving in the same direction.
    VIRUS_CHAR: RIGHT, # If it is infected, it turns right.
    FLAG_CHAR: BACK,   # If it is flagged, it reverses direction,
                       #  and will go back the way it came.
    }

# ======================================================================
#                                                                  Virus
# ======================================================================


class Virus(object):   # pylint: disable=R0902, R0205
    "Object for Sporifica Virus"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.grid = {}
        self.activities = 0
        self.infections = 0
        self.virus_loc = INITIAL_VIRUS_LOC
        self.virus_dir = INITIAL_VIRUS_DIR

        # 2. Process text (if any)
        if text is not None:
            self.text_to_grid(text)

    def text_to_grid(self, text):
        "Convert text map to grid coordinated"

        # 1. Not much to do it no map
        if not len(text):
            return

        # 2. Ensure that the map is square
        if len(text) != len(text[0]):
            raise Exception('Virus map is not square')

        # 3. Get the location of first row / column
        first = len(text) // 2

        # 4. Loop for all of the rows and columns
        for rnum, row in enumerate(text):
            for cnum, node in enumerate(row):

                # 5. If there is a virus here, record it
                if node == VIRUS_CHAR:
                    self.grid[(cnum-first, rnum-first)] = VIRUS_CHAR

    def burst(self):
        "A single burst of activity"

        # 1. Keep track of the number of bursts
        self.activities += 1

        # 2. If the current node is infected,
        if self.virus_loc in self.grid:
            # 2a. it turns to its right.
            self.virus_dir = RIGHT[self.virus_dir]
        else:
            # 2b. Otherwise, it turns to its left.
            self.virus_dir = LEFT[self.virus_dir]

        # 3. If the current node is clean,
        if self.virus_loc not in self.grid:
            # 3a. it becomes infected.
            self.grid[self.virus_loc] = VIRUS_CHAR
            self.infections += 1
        else:
            # 3b. Otherwise, it becomes cleaned.
            del self.grid[self.virus_loc]

        # 4. The virus carrier moves forward one node in the direction it is facing.
        delta = DELTA[self.virus_dir]
        self.virus_loc = (self.virus_loc[0] + delta[0],
                          self.virus_loc[1] + delta[1])

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Loop for required iterations
        if limit == 0:
            limit = PART_ONE_ITERATIONS
        for _ in range(limit):
            assert _ >= 0 # Shuts up warning for _ not being used

            # 2. Take a single step
            self.burst()

            # 3. Display information if requested
            if verbose:
                print("Iteration %d: infections=%d, infected=%d" %
                          (self.activities, self.infections, len(self.grid)))

        # 4. Return the number of bursts which caused an infection
        return self.infections

    def burst_two(self):
        "A single burst of activity (part two)"

        # 1. Keep track of the number of bursts
        self.activities += 1

        # 2. Ensure current grid has marked state
        if self.virus_loc not in self.grid:
            self.grid[self.virus_loc] = CLEAN_CHAR

        # 3. Determine the current infection state
        state = self.grid[self.virus_loc]

        # 4. Determine the next state of this grid node
        next_state = PART_TWO_VIRUS[state]

        # 5. Determine the next virus direction
        next_dir = PART_TWO_MOVE[state][self.virus_dir]

        # 6. Determint the next virus location
        delta = DELTA[next_dir]
        next_loc = (self.virus_loc[0] + delta[0],
                    self.virus_loc[1] + delta[1])

        # 7. Save the new state, direction, and location
        self.grid[self.virus_loc] = next_state
        self.virus_dir = next_dir
        self.virus_loc = next_loc

        # 8. Keep track of number of infections
        if next_state == VIRUS_CHAR:
            self.infections += 1


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Loop for required iterations
        if limit == 0:
            limit = PART_TWO_ITERATIONS
        for _ in range(limit):
            assert _ >= 0 # Shuts up warning for _ not being used

            # 2. Take a single step
            self.burst_two()

            # 3. Display information if requested
            if verbose:
                print("Iteration %d: infections=%d" %
                          (self.activities, self.infections))

        # 4. Return the number of bursts which caused an infection
        return self.infections


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         v i r u s . p y                        end
# ======================================================================
