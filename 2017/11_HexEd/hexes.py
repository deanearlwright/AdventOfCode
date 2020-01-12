# ======================================================================
# Hex Ed
#   Advent of Code 2017 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         h e x e s . p y
# ======================================================================
"A solver for Hex Ed for Advent of Code 2017 Day 11"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import Counter

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
REDUCERS = [('n', 's', ''), ('nw', 'se', ''), ('ne', 'sw', ''),
            ('ne', 's', 'se'), ('nw', 's', 'sw'),
            ('se', 'n', 'ne'), ('sw', 'n', 'nw'),
            ('se', 'sw', 's'), ('ne', 'nw', 'n')]

# ======================================================================
#                                                                  Knots
# ======================================================================


class Hexes(object):   # pylint: disable=R0902, R0205
    """Hex Object"""

    def __init__(self, part2=False):

        # 1. Set the initial values
        self.part2 = part2

    @staticmethod
    def steps(text=None, verbose=False, limit=0):
        "Determine the number of steps in the shortest path"

        # 1. If no text, not much to do
        if text is None:
            return None

        # 2. Count the different steps
        counts = Counter(text.split(','))
        if verbose:
            print("Beginning counts = %s" % (str(counts)))

        # 3. Reduce the steps
        Hexes.reduce(counts, verbose=verbose)

        # 6. Return the minimum number of steps
        if verbose:
            print("Ending counts = %s, steps = %d" % (str(counts), sum(counts.values())))
        return sum(counts.values())

    @staticmethod
    def reduce(counts, verbose=False):

        # 1. Loop reducing counts
        reducing = True
        while reducing:
            reducing = False

            # 2. Loop for the paired directions
            for reduce in REDUCERS:

                # 3. If there are counts for those directions ...
                if counts[reduce[0]] > 0 and counts[reduce[1]] > 0:

                    # 3a. Continue reducing
                    reducing = True

                    # 3b. How many?
                    number = min(counts[reduce[0]], counts[reduce[1]])

                    # 3c. Reduce the counts
                    counts -= Counter({reduce[0]: number, reduce[1]: number})

                    # 3d. If merged directions, add that direction
                    if reduce[2]:
                        counts += Counter({reduce[2]: number})

                    # 3e. Report (if desired)
                    if verbose:
                        print("Reducing %d %s %s to %s" %
                              (number, reduce[0], reduce[1], reduce[2]))


    @staticmethod
    def furthest(text=None, verbose=False, limit=0):
        "Determine the number of steps furthest away"

        # 1. If no text, not much to do
        if text is None:
            return None

        # 2. Start very close
        result = 0
        counts = Counter()

        # 3. Loop for each step
        for step in text.split(','):

            # 4. Add this step to the counts
            counts.update({step: 1})
            if verbose:
                print("Adding step %s, counts = %s" % (step, str(counts)))


            # 5. Reduce the counts
            Hexes.reduce(counts, verbose=verbose)

            # 6. If this is further away, record it
            knt_steps = sum(counts.values())
            if  knt_steps > result:
                if verbose:
                    print("Step %s put process %d steps away" %
                          (step, knt_steps))
                result = knt_steps

        # 7. Return the furthest number of steps
        if verbose:
            print("Furthest number of steps = %d" % result)
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          h e x e s . p y                       end
# ======================================================================
