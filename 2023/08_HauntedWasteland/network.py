
# ======================================================================
# Haunted Wasteland
#   Advent of Code 2023 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         n e t w o r k . p y
# ======================================================================
"Network for the Advent of Code 2023 Day 08 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from math import lcm
from node import Node


# ======================================================================
#                                                                Network
# ======================================================================


class Network(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Haunted Wasteland"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.directions = ""
        self.nodes = {}
        self.starts = []
        self.stops = frozenset()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 0. Precondition axiom
        assert text is not None and len(text) > 0

        # 1. Loop for all the lines in the text
        for indx, line in enumerate(text):

            # 2. First line is the directions
            if indx == 0:
                self.directions = line
                continue

            # 3. All the rest are nodes
            one_node = Node(text=line, part2=self.part2)

            # 4. Save the node
            self.nodes[one_node.name] = one_node

        # 5. Find the ghost start and ends (for part 2)
        self.find_ghosts()

    def navigate_one(self, start, stop):
        "Navigate the network and return the number of steps"

        # 0. Precondition axioms
        assert start in self.nodes
        assert stop in self.nodes

        # 1. Start at the start
        steps = 0
        current = start
        indx = 0

        # 2. Loop until we reach the end
        while current != stop:

            # 3. Do we need more instructions?
            if indx >= len(self.directions):
                indx = 0

            # 4. Go to the next location
            # print(f"at {current}, indx {indx}, dir {self.directions}")
            current = self.nodes[current].next_node(self.directions[indx])
            steps += 1
            indx += 1

        # 5. Return the number of steps required
        return steps

    def navigate_two(self, start):
        "Navigate the network and return the number of steps"

        # 0. Precondition axioms
        assert start in self.nodes

        # 1. Start at the start
        steps = 0
        current = start
        indx = 0

        # 2. Loop until we reach the end
        while current[-1] != "Z":

            # 3. Do we need more instructions?
            if indx >= len(self.directions):
                indx = 0

            # 4. Go to the next location
            # print(f"at {current}, indx {indx}, dir {self.directions}")
            current = self.nodes[current].next_node(self.directions[indx])
            steps += 1
            indx += 1

        # 5. Return the number of steps required
        return steps

    def find_ghosts(self):
        "Determine the starting and possible ending locations for the ghosts"

        # 1. Just do it (pythonicly)
        if self.part2:
            self.starts = [x for x in self.nodes if x[-1] == "A"]
            self.stops = frozenset([x for x in self.nodes if x[-1] == "Z"])
        else:
            self.starts = ["AAA"]
            self.stops = frozenset(["ZZZ"])

    def brute_navigate(self):
        "Navigate the network --- as a bunch of ghosts"

        # 0. Precondition axioms
        assert len(self.starts) > 0
        assert len(self.stops) > 0

        # 1. Start at the start
        steps = 0
        current = list(self.starts)
        indx = 0

        # 2. Loop until we reach the end
        while any(x not in self.stops for x in current):

            # 3. Do we need more instructions?
            if indx >= len(self.directions):
                indx = 0

            # 4. Loop for all the ghosGo to the next location
            direction = self.directions[indx]
            current = [self.nodes[x].next_node(direction) for x in current]
            steps += 1
            indx += 1

        # 5. Return the number of steps required
        return steps

    def navigate(self):
        "Navigate the network --- as a bunch of ghosts"

        # 0. Precondition axioms
        assert len(self.starts) > 0
        assert len(self.stops) > 0
        assert len(self.starts) == len(self.stops)

        # 1. Start with the first one
        result = self.navigate_two(self.starts[0])

        # 2. Loop for the rest of the ghosts (if any)
        for start in self.starts[1:]:

            # 3. How man steps for this ghost?
            steps = self.navigate_two(start)

            # 4. Find the commonality
            result = lcm(result, steps)

        # 5. Return the number of steps required
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                       n e t w o r k . p y                      end
# ======================================================================
