# ======================================================================
# Memory Maneuver
#   Advent of Code 2018 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           n o d e . p y
# ======================================================================
"A Node for the Advent of Code 2018 Day 08 puzzle"

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
    "Object for Memory Maneuver"

    def __init__(self, children=None, metadata=None):

        # 1. Set the initial values
        self.children = []
        self.metadata = []
        self.value = 0

        # 2. arguments (if any)
        if children is not None:
            self.children = children
        if metadata is not None:
            self.metadata = metadata

        # 3. Calculate part 2 value
        self.value = self.calculate_value()

    def add_metadata_entries(self):

        # 1. Start with my metadata
        result = sum(self.metadata)

        # 2. Loop for all the children
        for child in self.children:

            # 3. Add the child's metadata
            result += child.add_metadata_entries()

        # 4. Return the sum of all the metadata
        return result

    def calculate_value(self):
        # 1. Start with nothing
        result = 0

        # 2. If there are no child nodes, sum metadata
        if len(self.children) == 0:
            return sum(self.metadata)

        # 3. Else value is sum of child values index by metadata
        for index in self.metadata:

            # 4. Ignore index that don't point to a child
            if index < 1 or index > len(self.children):
                continue

            # 5. Add in value of indexed child
            result += self.children[index - 1].value

        # 6. Return the sum of the children's values
        return result

def from_numbers(numbers):
    # 1. Get the number of children and metadata elements
    num_children = numbers.pop(0)
    num_metadata = numbers.pop(0)

    # 2. Get the children
    children = []
    for _ in range(num_children):
        children.append(from_numbers(numbers))

    # 3. Get the metadata
    metadata = []
    for _ in range(num_metadata):
        metadata.append(numbers.pop(0))

    # 4. Construct and return the node
    return Node(children=children, metadata=metadata)



# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          n o d e . p y                         end
# ======================================================================
