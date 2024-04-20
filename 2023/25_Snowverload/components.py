
# ======================================================================
# Snowverload
#   Advent of Code 2023 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        c o m p o n e n t s . p y
# ======================================================================
"Components for the Advent of Code 2023 Day 25 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple

# ----------------------------------------------------------------------
#                                                                  types
# ----------------------------------------------------------------------
Component = namedtuple("Component", "name, connections")

# ======================================================================
#                                                             Components
# ======================================================================


class Components(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Snowverload"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.components = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 0. Precondition axioms
        assert text is not None and len(text) > 0

        # 1. Loop for all of the lines in the text
        for line in text:

            # 2. Break up the line into the component name and connections
            parts = line.split(": ")
            assert len(parts) == 2
            name = parts[0]
            connections = set(parts[1].split())

            # 3. If a new component, add it
            if name not in self.components:
                self.components[name] = Component(name=name, connections=connections)

            # 4. Else add the connections to the existing component
            else:
                current = self.components[name].connections
                self.components[name] = Component(name=name,
                                                  connections=current.union(connections))

            # 5. Ensure that connections connect somewhare
            for connection in connections:
                if connection not in self.components:
                    self.components[connection] = Component(name=connection,
                                                            connections=set([name]))
                else:
                    current = self.components[connection].connections
                    current.add(name)
                    self.components[connection] = Component(name=connection,
                                                            connections=current)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    c o m p o n e n t s . p y                   end
# ======================================================================
