# ======================================================================
# Permutation Promenade
#   Advent of Code 2017 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p r o m e n a d e . p y
# ======================================================================
"A solver for Permutation Promenade for Advent of Code 2017 Day 16"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
ONE_BILLION =  1000000000

# ----------------------------------------------------------------------
#                                                            Dance Moves
# ----------------------------------------------------------------------
def spin(step, dancers):
    "Execute a Spin dance move: sX"

    # 0. Precondition axioms
    assert step[0] == 's'

    # 1. Get the spin number
    number = int(step[1:])

    # 2. Split and rejoin the dancers
    # s3 on abcde produces cdeab
    dancers = dancers[-number:] + dancers[:len(dancers)-number]

    # 3. Return updated dancers
    return dancers

def exchange(step, dancers):
    "Execute an Exchange dance spin move: xA/B"

    # 0. Precondition axioms
    assert step[0] == 'x'

    # 1. Get the positions to exchange
    positions = [int(_) for _ in step[1:].split('/')]

    # 2. Makes the programs at positions A and B swap places
    tmp = dancers[positions[0]]
    dancers[positions[0]] = dancers[positions[1]]
    dancers[positions[1]] = tmp

    # 3. Return updated dancers
    return dancers

def partner(step, dancers):
    "Execute a Partner dance spin move: pA/B"

    # 0. Precondition axioms
    assert step[0] == 'p'

    # 1. Get the dancers to swap positions
    positions = [_ for _ in step[1:].split('/')]

    # 2. Makes the programs named A and B swap places
    pos_A = dancers.index(positions[0])
    pos_B = dancers.index(positions[1])
    dancers[pos_A] = positions[1]
    dancers[pos_B] = positions[0]

    # 3. Return updated dancers
    return dancers

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
MOVES = {'s': spin,
         'x': exchange,
         'p': partner
         }


# ======================================================================
#                                                              Promenade
# ======================================================================


class Promenade(object):   # pylint: disable=R0902, R0205
    """Object for dancers executing dance moves"""

    def __init__(self, number=16, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.number = number
        self.dancers = [chr(ord('a')+_) for _ in range(number)]
        self.steps = []
        self.index = 0

        # 2. Process text into steps (if any)
        if text is not None:
            self.steps = text.split(',')

    def __str__(self):
        return ''.join(self.dancers)

    def step(self, step=None, verbose=False):
        "Execute the next step of the dance"

        # 1. If not given a specific step, get the next one
        if step is None:
            step = self.steps[self.index]

        # 2. Execute the specific dance step
        new_dancers = MOVES[step[0]](step, self.dancers)

        # 3. Update the dancers and index
        if verbose:
            print("%s: %s --> %s" %
                  (step, self.dancers, new_dancers))
        self.dancers = new_dancers
        self.index += 1

        # 4. Return the update dancers
        return new_dancers

    def dance(self, verbose=False, limit=0):
        "Execute all the dance steps"

        # 1. Loop for all of the steps
        for one_step in self.steps:

            # 2. Execute the step
            new_dancers = self.step(one_step, verbose=verbose)

            # 3. Together we're unlimited (Elphaba)
            if self.index > limit > 0:
                break

        # 3. Return the final configuration of dancers
        return new_dancers

    def part_one(self, verbose=False, limit=0):
        "Returns the final dance configuration"

        # 1. Return the final dance configuration as a string
        return ''.join(self.dance(verbose=verbose, limit=limit))


    def part_two(self, verbose=False, limit=0):
        "Returns the final dance configuration"

        # 1. Save the starting position
        starting = self.dancers.copy()
        cycle = None

        # 1. Loop a whole bunch of times
        for number in range(ONE_BILLION):

            # 3. Everybody dance now (C+C Music Factory)
            self.dance()

            # 4. Have we cycled back to the starting position
            if all(s == d for s, d in zip(starting, self.dancers)):

                # 5. Yes we have, this is going to be easy
                cycle = number + 1
                if verbose:
                    print("After %d dances, the dancers returned to the starting position" % cycle)
                break

        # 6. If we did all two billion, return the final dance configuration
        if cycle is None:
            return ''.join(self.dancers)

        # 7. Determine the number of dances left to do and do them
        remaining = ONE_BILLION % cycle
        if verbose:
            print("Just %d dances more to go" % remaining)
        for number in range(remaining):
            self.dance()

        # 8. Return the final dance configuration after pertending to do 1,000,000,000 dances
        return ''.join(self.dancers)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    p r o m e n a d e . p y                     end
# ======================================================================
