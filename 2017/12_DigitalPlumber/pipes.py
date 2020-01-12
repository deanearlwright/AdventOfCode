# ======================================================================
# Digital Plumber
#   Advent of Code 2017 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p i p e s . p y
# ======================================================================
"A solver for Digital Plumber for Advent of Code 2017 Day 12"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
PIPE_MATCH = re.compile(r'([0-9]+) <-> ([0-9, ]+)')

# ======================================================================
#                                                                   Pipe
# ======================================================================


class Pipe(object):   # pylint: disable=R0902, R0205
    """Object for a single pipe"""

    def __init__(self, text=None, name=None, connections=None):

        # 1. Set the initial values
        self.name = name
        if connections is not None:
            self.connections = connections
        else:
            self.connections = []

        # 2. Process text (if any)
        if text is not None:
            match = PIPE_MATCH.match(text)
            if match is not None:
                self.name = int(match.group(1))
                self.connections = [int(_) for _ in match.group(2).split(',')]
            else:
                raise SyntaxError(text)


# ======================================================================
#                                                                  Pipes
# ======================================================================


class Pipes(object):   # pylint: disable=R0902, R0205
    """Object for a collection of pipes"""

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.connections = {}
        self.member_of = {}

        # 2. The there is text, add connections
        if text:
            for line in text:
                apipe = Pipe(text=line)
                self.connections[apipe.name] = apipe.connections

    def num_in_group(self, group_id, verbose=False, limit=0):
        "Returns number of programs in a group"

        # 1. Ensure that we know the group_id
        if group_id not in self.connections:
            return None

        # 2. Start with no connections
        group_connects = set()
        connections_to_add = set([group_id])
        count = 0

        # 3. Loop while there are connections to add
        while connections_to_add:

            # 4. Take one of the connections
            connection = connections_to_add.pop()

            # 5. If a new connections, add it and it's connections
            if connection not in group_connects:
                if verbose:
                    print("%d: Adding %s with connections to %s" %
                          (group_id, connection, self.connections[connection]))
                group_connects.add(connection)
                connections_to_add.update(set(self.connections[connection]))
                self.member_of[connection] = group_id

            # 6. Don't loop too much
            count += 1
            if count > limit > 0:
                print("Loop %d times" % count)
                break

        # 7. Return number of connections in this group
        if verbose:
            print("%d connections in group %d" %
                  (len(group_connects), group_id))
        return len(group_connects)

    def number_of_groups(self, verbose=False, limit=0):
        "Returns number of programs in a group"

        # 1. Ensure that we have some connections
        if not self.connections:
            return None

        # 2. Start with no groups
        result = 0

        # 3. Loop for all of the programs
        for prog_id in self.connections:

            # 4. If this program is not yet been grouped ...
            if prog_id not in self.member_of:
                if verbose:
                    print("Starting new group %d" % prog_id)

                # 5. Collect all the programs in this group
                self.num_in_group(prog_id, verbose=verbose, limit=limit)

                # 6. Increment the number of groups
                result += 1

            # 7. This program is already in a group
            elif verbose:
                print("Program %d is in group %d" % (prog_id, self.member_of[prog_id]))

        # 8. Return the number of groups
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          p i p e s . p y                       end
# ======================================================================
