# ======================================================================
# It Hangs in the Balance
#   Advent of Code 2015 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p a c k a g e s . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 24 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from math import prod
from itertools import combinations

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                               Packages
# ======================================================================


class Packages(object):   # pylint: disable=R0902, R0205
    "Object for It Hangs in the Balance"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.weights = []
        self.compartments = 0
        self.balance = 0

        # 2. Determine the number of compartments
        if self.part2:
            self.compartments = 4
        else:
            self.compartments = 3

        # 3. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.weights.append(int(line))
            self.balance = sum(self.weights) / self.compartments
            if self.balance != int(self.balance):
                print("*** The balance is off ***")
            self.balance = int(self.balance)

    @staticmethod
    def quantum_entanglement(packages):
        "Return the quantum entanglement of a group of packages"
        return prod(packages)

    @staticmethod
    def find_min_max_packages(packages, weight):
        "Determine the minimun and maximum packages to reach the weight"

        # 1. Put the packages in sorted order
        packages.sort()

        # 2. Find the minimum number of packages
        packages.reverse()
        minimum = Packages.min_max_helper(packages, weight)
        if minimum is None:
            print("*** unable to determine minimum number of %d packages for weight %d" %
                  (len(packages), weight))
            minimum = 1

        # 3. Find the maximum number of packages
        packages.reverse()
        maximum = Packages.min_max_helper(packages, weight)
        if maximum is None:
            print("*** unable to determine maximum number of %d packages for weight %d" %
                  (len(packages), weight))
            minimum = len(packages)

        # 4. Return the result
        return minimum, maximum

    @staticmethod
    def min_max_helper(packages, weight):
        "Determine number of packages needed to equal weight"

        # 1. Start with nothing
        scale = 0

        # 2. Loop until we have enough packages
        for indx, pkg in enumerate(packages):

            # 3. Accumulate the wight of the packages
            scale += pkg

            # 4. If it put us over the top, return the number of packages
            if scale >= weight:
                return indx + 1

        # 5. We should never get here
        return None

    @staticmethod
    def get_weighted(packages, weight, number):
        "Get collections of packages of the specified number that add to the given weight"

        # 1. Start with nothing
        result = []

        # 2. Loop for all of the possibilities
        for pkgs in combinations(packages, number):

            # 3. Do the weight the correct amount?  If yes, save
            if sum(pkgs) == weight:
                result.append(pkgs)

        # 4. Return the successful subset of packages (if any)
        #print("number = %d, weight = %d, result = %s" % (number, weight, str(result)))
        return result

    @staticmethod
    def is_remainder_balanced(packages, used, weight, number):
        "Can the remaining packages broken into n groups each adding up to the weight?"

        # 1. Get the remaining packages
        remaining = list(set(packages) - set(list(used)))

        # 2. Handle the base case
        if number == 1:
            if sum(remaining) == weight:
                return True
            return False

        # 3. Get the min and max for first group
        min_max = Packages.find_min_max_packages(remaining, weight)

        # 4. Loop over the min and max numbers
        for min_max_number in range(min_max[0], min_max[1]):

            # 5. Get possible packages for next group
            nxt = Packages.get_weighted(remaining, weight, min_max_number)

            # 6. Loop for all of the possiblites for the next group
            for grp in nxt:

                # 7. Is it balanced?
                if Packages.is_remainder_balanced(remaining, grp, weight, number - 1):
                    return True

        # 8. Sorry, there is no weight to balance the remaining packages
        return False

    def find_best_legroom(self):
        "Find the best legroom - fewest packages, smallest quantum_entanglement"

        # 1. Get the min and max for first group
        min_max = Packages.find_min_max_packages(self.weights, self.balance)

        # 2. Loop over the min and max numbers
        for min_max_number in range(min_max[0], min_max[1]):

            # 3. Get possible packages for the first group
            group_one = Packages.get_weighted(self.weights, self.balance, min_max_number)
            if len(group_one) == 0:
                continue

            # 4. Find the set with the smallest quantum_entanglement
            result = prod(self.weights)
            for pkgs in group_one:
                pkgs_qe = prod(list(pkgs))
                if pkgs_qe < result:
                    result = pkgs_qe

            # 5. Return the best quantum_entanglement
            return result

        # 6. So sorry
        return False

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.find_best_legroom()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.find_best_legroom()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      p a c k a g e s . p y                     end
# ======================================================================
