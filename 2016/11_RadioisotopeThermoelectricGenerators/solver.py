# ======================================================================
# Radioisotope Thermoelectric Generators
#   Advent of Code 2016 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s o l v e r . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 11 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import deque
import state
import item

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
BIG_NUMBER = 60

PART_TWO_ITEMS = [
  "elerium generator",
  "elerium-compatible microchip",
  "dilithium generator",
  "dilithium-compatible microchip",
]

# ======================================================================
#                                                                 Solver
# ======================================================================


class Solver(object):   # pylint: disable=R0902, R0205
    "Object for Radioisotope Thermoelectric Generators"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.initial_state = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.initial_state = state.State(text=text, part2=part2)

            # 3. Add items to the first floor for part2
            if len(self.initial_state.floors) > 0 and self.part2:
                for p2_text in PART_TWO_ITEMS:
                    p2_item = item.Item(text=p2_text)
                    self.initial_state.floors[0].add(p2_item)
                    self.initial_state.items.append(p2_item)

    def number_moves(self):
        "Returns the smallest number of moves to get to a goal state"

        # 0. Nothing to solve if no initial state
        if not self.initial_state:
            return None

        # 1. Start with a large number of moves and initial moves
        result = BIG_NUMBER
        states = {}
        states[self.initial_state] = 0
        queue = deque()
        queue.append((self.initial_state, 0, self.initial_state.legal_moves()))
        count = 0

        # 2. Loop while there is states and moves to explore
        while len(queue) > 0:
            count += 1
            if count % 5000 == 0:
                print("%d: states = %d, queue = %d, result = %d" %
                      (count, len(states), len(queue), result))

            cur_state, cur_moves, legal = queue.pop()
            if len(legal) == 0:
                continue
            one_move = legal.pop()
            if len(legal) > 0:
                queue.append((cur_state, cur_moves, legal))

            # 3. Execute the move
            new_state = cur_state.execute_move(one_move)
            new_moves = cur_moves + 1

            # 4. Do we make it? Save number of moves if better
            if new_state.is_goal():
                if new_moves < result:
                    result = new_moves
                    print("%d: solution = %d steps" % (count, result))
                    continue

            # 5. Are we taking too long, maybe the other moves will be better
            if new_moves >= result:
                continue

            # 7. Is this a new state?  If so, add it to the queue
            if new_state not in states:
                states[new_state] = new_moves
                queue.append((new_state, new_moves, new_state.legal_moves()))
                # print("new state states = %d, queue = %d" % (len(states), len(queue)))
                continue

            # 8. Did we get here faster?
            if states[new_state] > new_moves:
                states[new_state] = new_moves
                queue.append((new_state, new_moves, new_state.legal_moves()))

        # 9. Return the number of moves
        print("%d: states = %d, queue = %d, result = %d -- final" %
              (count, len(states), len(queue), result))
        if result == BIG_NUMBER:
            return None
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.number_moves()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.number_moves()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        s o l v e r . p y                       end
# ======================================================================
