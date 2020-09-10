# ======================================================================
# A Regular Map
#   Advent of Code 2018 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           p a t h . p y
# ======================================================================
"Room mapper for the Advent of Code 2018 Day 20 puzzle (from day 15)"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DELTA = [-1000, 1000, 1, -1]

# ======================================================================
#                                                                   Node
# ======================================================================


class Node(object):   # pylint: disable=R0902, R0205
    "Path Node for A Regular Map"

    def __init__(self, location=None, previous=None, doors=None):

        # 1. Set the initial values
        self.location = location
        self.previous = previous
        self.doors = doors
        self.shortest = []

        # 2. Steps is one more than the previous steps
        if self.previous is not None:
            self.steps = self.previous.steps + 1
        else:
            self.steps = 0

        # 3. Determine the doors to nearby locations (if we can)
        self.adjacent = [None, None, None, None]
        if location is not None and doors is not None:
            for index, delta in enumerate(DELTA):
                adj_loc = location + delta
                if (location, adj_loc) in self.doors:
                    self.adjacent[index] = adj_loc

# ======================================================================
#                                                                   Path
# ======================================================================

class Path(object):   # pylint: disable=R0902, R0205
    "Rooms path for A Regular Map"

    def __init__(self, start=None, doors=None):

        # 1. Set the initial values
        self.start = start
        self.doors = doors
        self.node = None
        self.nodes = {}
        self.queue = []

        # 2. Solve if we can
        if start is not None and doors is not None:
            self.find_path()

    def find_path(self):
        # 1. Create initial node
        self.node = Node(location=self.start, doors=self.doors)

        # 2. Add node to the nodes and the queue
        self.nodes[self.start] = self.node

        # 3. Process queue
        self.queue.append(self.node)
        while len(self.queue) > 0:
            # 4. Get the oldest node from the queue
            current_node = self.queue.pop(0)
            # 5. Else explore this node's adjacent nodes
            self.explore(current_node)


    def explore(self, node):
        # 1. Loop for all of the adjacent locations
        for adj_loc in node.adjacent:
            if adj_loc is None:
                continue

            # 2. Have we been to this adjacent node before?
            if adj_loc in self.nodes:

                # 2a. Yes: If there is a shorter path to the adjacent node, ignore this one
                adj_node = self.nodes[adj_loc]
                if adj_node.steps <= node.steps + 1:
                    continue
                # 2b. Our way is faster, change the adjacent node to reflect that
                print('Changing steps on path from %d node %d from %d to %d' %
                      (self.start, adj_loc, adj_node.steps, node.steps + 1))
                adj_node.previous = node
                adj_node.steps = node.steps + 1
                # 2c. If this node is already set to be explored, remove it and we will readd
                try:
                    index = self.queue.index(adj_node)
                    del self.queue[index]
                except ValueError:
                    pass
            else:
                # 2d. No: never seen, create a new node
                adj_node = Node(location=adj_loc, previous=node, doors=self.doors)
                self.nodes[adj_loc] = adj_node

            # 3. Add this node to the queue
            self.queue.append(adj_node)

    def furthest(self):
        # 1. If there are no nodes, there is no door count
        if self.nodes is None:
            return None
        # 2. Start with the nothing
        result = 0
        # 3. Loop for all of the nodes
        for node in self.nodes.values():
            # 4. Remember the greatest number of steps
            if node.steps > result:
                result = node.steps
        # 5. Return the maximum steps
        return result

    def at_least(self, steps=1000):
        # 1. If there are no nodes, there is no door count
        if self.nodes is None:
            return None
        # 2. Start with the nothing
        result = 0
        # 3. Loop for all of the nodes
        for node in self.nodes.values():
            # 4. If it takes at least the given number of steps to
            #    reach this room, increment the total
            if node.steps >= steps:
                result += 1
        # 5. Return the maximum steps
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                            p a t h . p y                       end
# ======================================================================