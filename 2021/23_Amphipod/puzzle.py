# ======================================================================
# Amphipod
#   Advent of Code 2021 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p u z z l e . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 23 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple

import burrow
import positions

# ----------------------------------------------------------------------
#                                                             namedtuple
# ----------------------------------------------------------------------
State = namedtuple('State', 'cost, text')

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
ORDER = ['A', 'B', 'C', 'D']

# ======================================================================
#                                                                 Puzzle
# ======================================================================


class Puzzle(object):   # pylint: disable=R0902, R0205
    "Object for Amphipod"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.burrow = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.burrow = burrow.Burrow(text=text, part2=part2)

    def organize(self, verbose=False):
        "Organize the amphipods into their proper rooms"

        # 1. Make sure there is a burrow
        if not self.burrow:
            return None

        # 2. Have to start somewhere
        pos = positions.Positions(text=self.burrow.positions(), part2=self.part2)
        queue = [
            State(cost=0, text=str(pos))
        ]
        result = 1000 * 16
        if self.part2:
            result *= 3

        # 3. Loop with there is something to do
        while queue:

            # 4. Take an entry off the queue
            current = queue.pop()
            # print("q=%4d c=%5d t=%s" % (len(queue), current.cost, current.text))

            # 5. Create the position
            pos.spaces = list(current.text)

            # 6. Are we done yet?
            if pos.are_all_home():
                if current.cost < result:
                    result = current.cost
                    if verbose:
                        print("New cost=%s, queue=%d" % (result, len(queue)))
                continue

            # 7. Is this state unproductive?
            if current.cost > result:
                continue

            # 8. Get all of the possible move from here
            moves = pos.all_moves()

            # 9. Add all of those moves
            for move in moves:
                new_position = pos.execute(move)
                queue.append(State(cost=current.cost + pos.cost(move),
                                   text=new_position))

        # 10. Return the total cost of moving the amphipods
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.organize(verbose=verbose)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.organize(verbose=verbose)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        p u z z l e . p y                       end
# ======================================================================
