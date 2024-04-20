
# ======================================================================
# Haunted Wasteland
#   Advent of Code 2023 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         n o d e . p y
# ======================================================================
"Node for the Advent of Code 2023 Day 08 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DIRECTIONS = 'LR'

# ======================================================================
#                                                                   Node
# ======================================================================


class Node(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Haunted Wasteland"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.name = ""
        self.next = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 0. Precondition axiom
        assert text is not None and len(text) > 0

        # 1. Get the name and next nodes
        self.name, nodes = text.split(' = ')

        # 2. Split the next node into left and right
        left, right = nodes.replace('(', '').replace(')', '').split(', ')

        # 3. Save the next nodes
        self.next['L'] = left
        self.next['R'] = right

    def next_node(self, direction):
        "Return the next node"

        # 0. Precondition axiom
        assert direction in DIRECTIONS

        # 1. Return the next note
        return self.next[direction]

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                          n o d e . p y                         end
# ======================================================================
