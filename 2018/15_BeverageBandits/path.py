# ======================================================================
# Beverage Bandits
#   Advent of Code 2018 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           p a t h . p y
# ======================================================================
"Cave mapper for the Advent of Code 2018 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import cave
import person

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Node
# ======================================================================


class Node(object):   # pylint: disable=R0902, R0205
    "Path Node for Beverage Bandits"

    def __init__(self, location=None, previous=None, cave=None):

        # 1. Set the initial values
        self.location = location
        self.previous = previous
        self.cave = cave
        self.shortest = []
        self.distance = None

        # 2. Steps is one more than the previous steps
        if self.previous is not None:
            self.steps = self.previous.steps + 1
        else:
            self.steps = 0

        # 3. Determine the nearby empty locations (if we can)
        self.adjacent = [None, None, None, None]
        if location is not None and cave is not None:
            for index, delta in enumerate(person.ADJACENT):
                adj_loc = location + delta
                if cave.get_by_location(adj_loc) is None:
                    self.adjacent[index] = adj_loc

# ======================================================================
#                                                                   Path
# ======================================================================

class Path(object):   # pylint: disable=R0902, R0205
    "Cave path for Beverage Bandits"

    def __init__(self, source=None, destination=None, cave=None):

        # 1. Set the initial values
        self.source = source
        self.destination = destination
        self.cave = cave
        self.node = None
        self.distance = None
        self.nodes = {}
        self.queue = []

        # 2. Solve if we can
        if source is not None and destination is not None and cave is not None:
            self.find_path()

    def find_path(self):
        # 1. Start with no distance
        self.distance = None

        # 2. Create initial node
        self.node = Node(location=self.source, cave=self.cave)

        # 3. Add node to the nodes and the queue
        self.nodes[self.source] = self.node

        # 4. If we are next to the destination, just set the path
        if person.adjacent(self.source, self.destination):
            self.distance = 1
            for adj_loc in self.node.adjacent:
                if adj_loc == self.destination:
                    adj_node = Node(location=adj_loc, previous=self.node, cave=self.cave)
                    adj_node.distance = 1
                    self.nodes[self.destination] = adj_node
            return

        # 5. Process queue
        self.queue.append(self.node)
        while len(self.queue) > 0:
            # 6. Get the oldest node from the queue
            current_node = self.queue.pop(0)
            # 7. Ignore this node if it took to long to get here
            if self.distance is not None and current_node.steps > self.distance:
                continue
            # 8. If this is where we wanted to go, process distance
            if current_node.location == self.destination:
                self.distance = current_node.steps
                prev_node = current_node.previous
                while prev_node is not None:
                    prev_node.distance = self.distance
                    prev_node = prev_node.previous
                continue
            # 9. Else explore this node's adjacent nodes
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
                print('Changing steps on path from %d to %d node %d from %d to %d' %
                      (self.source, self.destination, adj_loc, adj_node.steps, node.steps + 1))
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
                adj_node = Node(location=adj_loc, previous=node, cave=self.cave)
                self.nodes[adj_loc] = adj_node

            # 3. Add this node to the queue
            self.queue.append(adj_node)

    def reachable(self):
        # 1. Return True only if we can reach the destination
        if self.distance == None:
            return False
        return True

    def move(self):
        # 1. We can only move if we can get where we want to go
        if not self.reachable():
            return None
        # 2. Get the adjacent locations that match the distance
        moves = []
        for adj_loc in self.node.adjacent:
            if adj_loc is not None:
                if adj_loc in self.nodes:
                    adj_node = self.nodes[adj_loc]
                    if adj_node.distance == self.distance:
                        moves.append(adj_loc)
        # 3. Get the single move in reading order
        if len(moves) > 1:
            moves.sort()
        # 4. Return the new location
        return moves[0]


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                            p a t h . p y                       end
# ======================================================================