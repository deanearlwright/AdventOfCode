
# ======================================================================
# LAN Party
#   Advent of Code 2024 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         n e t w o r k . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 23 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import defaultdict, Counter

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                Network
# ======================================================================


class Network(object):   # pylint: disable=R0902, R0205
    "Object for LAN Party"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.computers = defaultdict(set)
        self.groups = set()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text()

    def _process_text(self):
        "Assign values from text"

        assert self.text is not None and len(self.text) > 0

        # 1. Loop for every line of the connection map
        for line in self.text:

            # 2. Get the the two computers
            from_cpu, to_cpu = line.split("-")

            # 3. Save the connections
            self.computers[from_cpu].add(to_cpu)
            self.computers[to_cpu].add(from_cpu)

    def fill_set(self, groups, number, level=0):
        "Get connected cpus to fill the set"

        # 1. Start with nothing if this is the start
        if level == 0:
            self.groups = set()

        # 2. Loop for all of the groups
        for group in groups:
            in_grp, out_grp = group

            # 3. Base condition
            if len(in_grp) == 0 or \
               len(out_grp) == 0:
                continue

            # 4. Loop over the the wananbes
            for cpu in out_grp:

                # 5. Ignore if not connect to each of the in group
                in_all = True
                for in_cpu in in_grp:
                    if in_cpu not in self.computers or \
                       cpu not in self.computers[in_cpu]:
                        in_all = False
                        break
                if not in_all:
                    continue

                # 6. Does this cpu help make up the whole
                in_grp.add(cpu)
                out_grp.remove(cpu)
                if len(in_grp) == number:
                    self.groups.add(frozenset(in_grp))
                else:
                    self.fill_set([(in_grp, out_grp)],
                                  number, level=level + 1)
                # 7. Clean up
                in_grp.remove(cpu)
                out_grp.add(cpu)

        # 8. Return what we found
        return self.groups

    def all_sets(self, number=3):
        "Get of connected sets of n computers"

        # 1. Start with nothing
        self.all_groups = set()

        # 2. Loop for each computer
        for cpu in self.computers:

            # 3. Get a set with that computer
            in_grp = set([cpu])
            out_grp = self.computers[cpu]
            grp = [(in_grp, out_grp)]
            self.fill_set(grp, number, 0)

            # 4. Extend all groups
            self.all_groups |= self.groups

        # 5. Return the connect cpu sets
        return self.all_groups

    def lan_sized(self, number):
        "Find a lan of the given size"

        # 1. Loop for all of the cpus
        for cpu in self.computers:
            my_shares = self.computers[cpu].copy()
            my_shares.add(cpu)

            # 2. How much to the other computers share with it
            shares = {}
            for other in self.computers[cpu]:
                other_shares = self.computers[other].copy()
                other_shares.add(other)
                shares[other] = len(my_shares & other_shares)

            # 3. Count the number of shares
            knt = Counter(shares.values())

            # 4. Have I found what I'm looking for
            if knt[number] == number - 1:

                # 5. Yes, return the connected computers
                party = [cpu]
                for other, num_shares in shares.items():
                    if num_shares == number:
                        party.append(other)
                return party

        # 6. Too bad, so sad
        return []

    def largest_subnet(self):
        "Return the computers in the largest subset of computers"

        # 1. Find the maximum number
        maximum = max(len(self.computers[cpu]) for cpu in self.computers)

        # 2. Try to get such a network
        result = self.lan_sized(number=maximum)

        # 3. Return what
        return result

    @staticmethod
    def password(group):
        "Return the password for the lan group"

        # 1. Turn the set into a list
        computers = list(group)

        # 2. Sort it
        computers.sort()

        # 3. Output it with commas
        return ",".join(computers)

    def only_prefix(self, prefix="t", number=3):
        "Return only the sets that have the desired prefix"

        # 1. Get all the sets
        self.all_sets()

        # 2. Start with nothing
        result = set()

        # 3. Loop for all the groups
        for group in self.all_groups:

            # 4. If any element start with the prefix, add to result
            for one in group:
                if one.startswith(prefix):
                    result.add(group)

        # 5. Return the groups that contain the prefix
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        return len(self.only_prefix())

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part two
        return self.password(self.largest_subnet())

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                       n e t w o r k . p y                      end
# ======================================================================
