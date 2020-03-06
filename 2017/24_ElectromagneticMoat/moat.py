# ======================================================================
# Electromagnetic Moat
#   Advent of Code 2017 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Computer implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         m o a t . p y
# ======================================================================
"A solver for moat for Advent of Code 2017 Day 24"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import defaultdict
from random import choice

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Moat
# ======================================================================


class Moat(object):   # pylint: disable=R0902, R0205
    "Object for Electromagnetic Moat"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.components = []
        self.ports = defaultdict(list)

        # 2. Process text (if any)
        if text is not None:
            self.process_text(text)

    def process_text(self, text):
        "Populate components and ports from text"

        # 1. Loop for all of the components in the text
        for cnum, component in enumerate(text):

            # 2. Get the port sizes of the component
            ports = [int(x) for x in component.split('/')]

            # 3. Add the component to the list
            self.components.append((ports[0], ports[1]))

            # 4. Add the port numbers to the ports index
            self.ports[ports[0]].append(cnum)
            if ports[1] != ports[0]:
                self.ports[ports[1]].append(cnum)

    @staticmethod
    def other_port(component, port):
        "Return the port at the other end of the component"

        if port == component[0]:
            return component[1]
        return component[0]

    def last_port(self, bridge):
        "Return the bridges' empty port"

        # 1. Assume we are just starting
        result = 0

        # 1. If no bridge yet, need magnetic end
        if not bridge:
            return result

        # 2. Loop for all of the component of the bridge
        for component in bridge:

            # 3. Get the port number of the far side of this component
            result = Moat.other_port(self.components[component], result)

        # 4. Return the final port
        return result

    def build_a_bridge(self, first=False):
        "Create a bridge out of components"

        # 1. Start with nothing
        bridge = []
        need = 0

        # 2. Add components until we can add no other
        while True:

            # 3. Try to add another component
            component = self.pick_a_component(bridge=bridge, need=need, first=first)

            # 4. If no component to add, return the bridge that we have
            if component is None:
                return bridge

            # 5. What port will we need next
            need = Moat.other_port(self.components[component], need)

            # 6. Add component to bridge and try again
            bridge.append(component)

    def pick_a_component(self, bridge=None, need=None, first=False):
        "Add another component to the bridge"

        # 1. If there is no bridge, start one
        if bridge is None:
            bridge = []
            need = 0

        # 2. If need is unkown, determine it
        if need is None:
            need = self.last_port(bridge)

        # 3. Get the list of components that match the port that we need
        components = self.ports[need]

        # 4. Can only pick from the ones not already used
        pickable = [x for x in components if x not in bridge]

        # 5. If nothing to choose from, return failure
        if not pickable:
            return None

        # 6. Else select a the first (or random) component that fits
        if first:
            return pickable[0]
        return choice(pickable)

    def all_bridges(self, bridge=None):
        "Return all possible bridges, one by one"

        # 1. Start with an empty bridge if none is given
        if bridge is None:
            bridge = []

        # 2. Loop for all components that can continue the bridge
        for component in self.all_components(bridge):

            # 2. Add component to the bridge
            bridge.append(component)

            # 3. Return this bridge
            yield bridge

            # 4. Make more bridges start with the this one
            yield from self.all_bridges(bridge=bridge)

            # 5. Remove the added component
            bridge.pop(-1)

    def all_components(self, bridge=None, need=None):
        "Iterate over matching components"

        # 1. If there is no bridge, make one
        if bridge is None:
            bridge = []
            need = 0

        # 2. If need is unkown, determine it
        if need is None:
            need = self.last_port(bridge)

        # 3. Get the list of components that match the port that we need
        components = self.ports[need]

        # 4. Can only pick from the ones not already used
        pickable = [x for x in components if x not in bridge]

        # 5. Return the components one at a time
        for component in pickable:
            yield component

    def check_bridge(self, bridge):
        "Check the structural integrity of the bridge"

        # 1. Bridges must have at least one component
        if not bridge:
            return False

        # 2. Keep track of the components used and the ports needed
        used = set()
        need = 0

        # 3. Loop for all of the components in the bridge
        for component in bridge:

            # 4. It must not have been used before
            if component in used:
                return False
            used.add(component)

            # 5. The component must satisfy the need
            if need not in self.components[component]:
                return False

            # 6. Determine the next need
            need = Moat.other_port(self.components[component], need)

        # 7. Look good to me
        return True

    def strength(self, bridge):
        "Determine the strength of the bridge"

        return sum([sum(self.components[c]) for c in bridge])

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Remember the strongest
        result = -1

        # 2. Loop for all the bridges
        for bridge in self.all_bridges():

            # 3. Determine the strength of the bridge
            strength = self.strength(bridge)

            # 4. Remember the highest stength
            if strength > result:
                result = strength

        # 5. Return the highest strength found
        if result == -1:
            return None
        return result

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Remember the strongest and the longest
        result = -1
        longest = -1

        # 2. Loop for all the bridges
        for bridge in self.all_bridges():

            # 3. Determine the strength of the bridge
            strength = self.strength(bridge)

            # 4. If this isn't the longest, ignore it
            if len(bridge) < longest:
                continue
            longest = len(bridge)

            # 5. Remember the highest stength
            if strength > result:
                result = strength

        # 6. Return the highest strength of the longest bridge found
        if result == -1:
            return None
        return result


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          m o a t . p y                         end
# ======================================================================
