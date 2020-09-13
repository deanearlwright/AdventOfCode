# ======================================================================
# Mode Maze
#   Advent of Code 2018 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           p a t h . p y
# ======================================================================
"Cave mapper for the Advent of Code 2018 Day 22 puzzle (from day 15&20)"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Node
# ======================================================================


class Node(object):   # pylint: disable=R0902, R0205
    "Path Node for Mode Maze"

    def __init__(self, location=None, previous=None, cave=None):

        # 1. Set the initial values
        self.location = location
        self.previous = previous
        self.cave = cave
        self.minutes = 0

        # 2. Time taken depends if movement (1) or tool change (7)
        if previous is not None and location is not None:
            self.minutes = self.previous.minutes + cave.movement_time(location, previous.location)
        else:
            self.minutes = 0

# ======================================================================
#                                                                   Path
# ======================================================================

class Path(object):   # pylint: disable=R0902, R0205
    "Cave path for Mode Maze"

    def __init__(self, start=None, cave=None):

        # 1. Set the initial values
        self.start = start
        self.cave = cave
        self.node = None
        self.nodes = {}
        self.queue = []

        # 2. Solve if we can
        if start is not None and cave is not None:
            self.find_path()

    def find_path(self):
        # 1. Create initial node
        self.node = Node(location=self.start, cave=self.cave)

        # 2. Add node to the nodes and the queue
        self.nodes[self.start] = self.node

        # 3. Process queue
        self.queue.append(self.node)
        while len(self.queue) > 0:
            # 4. Get the oldest node from the queue
            current_node = self.queue.pop(0)
            # 5. Else explore this node's adjacent nodes
            self.explore(current_node)
            if len(self.queue)>4000:
                break


    def explore(self, node):
        #if node.previous is None:
        #    print("Exploring first node loc=%d, minutes=%d" % (node.location, node.minutes))
        #else:
        #    print("Exploring loc=%d, minutes=%d previous=%s" % (node.location, node.minutes, node.previous.location))
        # 1. Loop for all of the possible moves
        for move in self.cave.determine_moves(node.location):

            # 2. Determine the cost in time for this move
            cost = self.cave.movement_time(node.location, move)

            # 2. Have we been here before?
            if move in self.nodes:

                # 2a. Yes: If there is a quicker way to get here, ignore this one
                move_node = self.nodes[move]
                if move_node.minutes <= node.minutes + cost:
                    continue
                # 2b. Our way is faster, change the adjacent node to reflect that
                #print('Changing minutes at %d from %d to %d' %
                #      (move, move_node.minutes, node.minutes + cost))
                move_node.previous = node
                move_node.minutes = node.minutes + cost
                # 2c. If this node is already set to be explored, remove it and we will re-add
                try:
                    index = self.queue.index(move_node)
                    del self.queue[index]
                except ValueError:
                    pass
            else:
                # 2d. No: never seen, create a new node
                move_node = Node(location=move, previous=node, cave=self.cave)
                #print("Adding move from %d to %d, minutes = %d" % (node.location, move, move_node.minutes))
                self.nodes[move] = move_node

            # 3. Add this node to the queue
            self.queue.append(move_node)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                            p a t h . p y                       end
# ======================================================================