# ======================================================================
# Universal Orbit Map
#   Advent of Code 2019 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                              d a g . p y
# ======================================================================
"DAC for Universal Orbit Map problem for Advent of Code 2019 Day 06"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                      Utility Functions
# ======================================================================

# ======================================================================
#                                                                    DAG
# ======================================================================


class DAG(object):
    """Directed Acyclic Graph"""

    def __init__(self, pairs=None):

        # 1. Start with nothing
        self.dag = {}

        # 2. Add any pairs we have
        self.add_pairs(pairs)

    def nodes(self):
        "Returns the names of all the nodes"

        # 1. Start with nothing
        result = set()

        # 2. Loop for the whole of the dag
        for node, links in self.dag.items():

            # 3. Add all of this to the result
            result.add(node)
            result.update(set(links))

        # 4. Return the node names
        return result

    def __len__(self):
        "Returns number of nodes in the graph"

        return len(self.dag)

    def add_node(self, from_node, to_node):
        "Add a node to the graph"

        # 1. If the nodes are not in the map, add them
        if from_node not in self.dag:
            self.dag[from_node] = []
#        if to_node not in self.dag:
#            self.dag[to_node] = []

        # 2. Add the to_node as a child of the from_node
        self.dag[from_node].append(to_node)

    def add_pairs(self, pairs=None):
        "Add pairs of (from, to) nodes"

        # 1. Can't add nothing if you only got nothing
        if pairs is not None:

            # 2. Loop for all of the pairs
            for pair in pairs:

                # 3. Add a pair
                self.add_node(pair[0], pair[1])

    def find_path(self, from_node, to_node, path=None):
        "Find a path from the from_node to the to_node"

        # 1. Append the from node the path
        if path is None:
            path = []
        path.append(from_node)

        # 2. If we are where we want to be, we are done
        if from_node == to_node:
            return path

        # 3. Is there anywhere to go from here?
        if from_node not in self.dag:
            return None

        # 4. Loop for all of ways forward from here
        for node in self.dag[from_node]:

            # 5. Ignore places we have already been
            if node not in path:

                # 6. Recursively try this node
                newpath = self.find_path(node, to_node, path)

                # 7. If we found a path from here to there, use it
                if newpath:
                    return newpath

        # 8. Return a failure if you can't get there from here
        return None

    def find_shortest_path(self, from_node, to_node, path=[]):
        "Find shortest path from the from_node to the to_node"

        path = path + [from_node]
        if from_node == to_node:
            return path
        if from_node not in self.dag:
            return None
        shortest = None
        for node in self.dag[from_node]:
            if node not in path:
                newpath = self.find_shortest_path(node, to_node, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    def find_dqueue_shortest_path(self, from_node, to_node):
        "Find shortest path from the from_node to the to_node"
        dist = {from_node: [from_node]}
        q = [] #deque(from_node)
        while len(q):
            at = q.popleft()
            for next_node in self.dag[at]:
                if next_node not in to_node:
                    dist[next_node] = [dist[at], next_node]
                    q.append(next_node)
        return dist[to_node]

    def direct_links(self):
        "Returns number of direct links"

        # 1. Start with none
        result = 0

        # 2. Loop for all of the nodes
        for node, links_to in self.dag.items():

            # 3. Add number of links from this node
            result += len(links_to)

        # 4. Return number of direct links
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           d a g . p y                          end
# ======================================================================
