
# ======================================================================
# Snowverload
#   Advent of Code 2023 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      c o n n e c t i o n s . p y
# ======================================================================
"Connections for the Advent of Code 2023 Day 25 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from random import shuffle
from collections import defaultdict

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                            Connections
# ======================================================================


class Connections(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Snowverload"

    def __init__(self, components=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = None
        self.components = None
        self.edges = set()

        # 2. Process components (if any)
        if components is not None:
            self._process_components(components)

    def _process_components(self, components):
        "Assign values from components object"

        # 1. Precondition axioms
        assert components is not None

        # 2. Handle the simple assignments
        self.text = components.text
        self.part2 = components.part2

        # 3. Loop for all the components
        for component in components.components.values():
            name = component.name

            # 4. Loop for all the connections in the component
            for connection in component.connections:

                # 5. Construct the edges
                edge1 = (name, connection)
                edge2 = (connection, name)

                # 6. If the edge is already known, nothing to do
                if edge1 in self.edges or edge2 in self.edges:
                    continue

                # 7. Add the edge to the edges
                self.edges.add(edge1)

    def karger(self, cuts): # pylint: disable=R0912
        "Return the product of the sizes of the two groups after making the cuts"

        # 1. Keep trying untile we get it right
        while True:

            # 2. Always start with a clean copy of the edges
            edges = [[edge[0], edge[1]] for edge in self.edges]

            # 3. Find the nodes for these edges
            vertices = defaultdict(list)
            for edge in edges:
                vertices[edge[0]].append(edge)
                vertices[edge[1]].append(edge)

            # 4. Initially all nodes are all by themselves
            vertsizes = defaultdict(lambda: 1)

            # 5. Randomize the edges em mass rather than choising random ones
            shuffle(edges)

            # 6. procedure contract(G=V,E)
            # 6a. While |V| > 2
            while len(vertices) > 2:

                # 6b. choose e element of E at random
                keep, cut = edges.pop()
                if keep == cut:
                    continue

                # 6c. G <- G/e
                for edge in vertices[cut]:
                    if edge[0] == cut:
                        edge[0] = keep
                    elif edge[1] == cut:
                        edge[1] = keep
                    vertices[keep].append(edge)
                del vertices[cut]
                vertices[keep] = [edge for edge in vertices[keep] if edge[0] != edge[1]]

                # 7. Keep track of the number if edges for each node (for solution)
                vertsizes[keep] += vertsizes[cut]
                del vertsizes[cut]

            # 8. Have we gotten down to where we want to be?
            keys = list(vertices)
            if len(vertices[keys[0]]) <= cuts:
                break

        # 9. Return the product of the sizes of the two node clusters
        return vertsizes[keys[0]] * vertsizes[keys[1]]


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   c o n n e c t i o n s . p y                  end
# ======================================================================
