# ======================================================================
# Universal Orbit Map
#   Advent of Code 2019 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                             u o m a p . p y
# ======================================================================
"Map for Universal Orbit Map problem for Advent of Code 2019 Day 06"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import dag

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
COM = 'COM'
YOU = 'YOU'
SANTA = 'SAN'

# ======================================================================
#                                                                  UOMap
# ======================================================================


class UOMap(dag.DAG):
    """Object representing a Universal Orbit Map"""

    def __init__(self, pairs=None, text=None):

        # 1. Start with an empty dag
        super(UOMap, self).__init__(pairs=pairs)

        # 2. If there is text, process it
        if text is not None:

            # 3. Loop for all of the lines
            for line in text:

                # 4. Split line into the two node names
                nodes = line.split(')')

                # 5. Add nodes to graph
                self.add_node(nodes[0], nodes[1])

    def orbits(self, node):
        "Return the number of [in]direct orbits for a given node"

        # Number of orbits is path length from COM minus 1
        path = self.find_shortest_path(COM, node)
        assert path is not None
        #print("%s %d %s" % (node, len(path), path))
        return len(path) - 1

    def total_orbits(self):
        "Return the number of direct and indirect orbits"

        # 1. Start with no orbits
        result = 0

        # 2. Loop for all of the nodes
        for node in self.nodes():

            # 3. We only want terminal nodes
            if node == COM:
                continue

            # 4. Orbits is one less than the length of path from COM
            result += self.orbits(node)

        # 5. Return total number of orbits
        return result

    def count_orbits(self):
        "Count the orbits by walking the tree"

        # 1. Start with nothing, but a list of things to do
        orbits = {}
        todo = [(COM, 0)]

        # 2. Loop until there is nothing to do
        while todo:
            pass

        # 9. Return the sum of the orbits
        return sum(orbits.values())

    def bodies(self):
        "Retnumber of orbit"

        return self.nodes()

    def minimum_transfers(self, from_node, to_node):
        "Find the minimumal number of orbital transfers between two nodes"

        # 1. Assume no path
        result = []

        # 2. If from you or Santa, find where orbiting
        if from_node in [YOU, SANTA]:
            from_node = self.orbiting(from_node)

        # 3. If to you or Santa, find where orbiting
        if to_node in [YOU, SANTA]:
            to_node = self.orbiting(to_node)

        # 4. Find the shorted path from the center to each
        from_path = self.find_shortest_path(COM, from_node)
        to_path = self.find_shortest_path(COM, to_node)
        assert from_path is not None
        assert to_path is not None

        # 4. Keep only the unique parts
        for indx in range(min(len(from_path), len(to_path))):
            if from_path[indx] == to_path[indx]:
                continue
            result = from_path[indx:] + to_path[indx:]
            break

        # 5. Return length of unique legs
        return len(result)

    def orbiting(self, node):
        "What is the node orbiting?"

        # 1. Asssume the worst
        result = None

        # 2. if not the center, find where it is orbiting
        if node != COM:
            for onode, bodies in self.dag.items():
                if node in bodies:
                    result = onode
                    break

        # 3. Return where orbiting or None
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           u o m a p . p y                      end
# ======================================================================
