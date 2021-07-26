# ======================================================================
# Radioisotope Thermoelectric Generators
#   Advent of Code 2016 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s t a t e . p y
# ======================================================================
"State for the Advent of Code 2016 Day 11 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import aoc_11
import elevator
import floor

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  State
# ======================================================================


class State(object):   # pylint: disable=R0902, R0205
    "Object for Radioisotope Thermoelectric Generators"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.lift = elevator.Elevator(part2=part2)
        self.floors = []
        self.items = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:

            # 3. Loop for all the text
            for line in self.text:

                # 4. Process elevator of floor
                if line.startswith("The elevator"):
                    self.lift = elevator.Elevator(text=line, part2=self.part2)
                else:
                    flr = floor.Floor(text=line, part2=self.part2)
                    self.floors.append(flr)
                    self.items.extend(flr.items)

            # 5. put the items in alphabetic order
            self.items.sort()

    def __str__(self):
        result = []
        for flr in self.floors:
            result.append(str(flr))
        result.append(str(self.lift))
        return '\n'.join(result)

    def trace(self):
        "Return the state in trace format"
        result = []
        for flr in self.floors:
            result.append(flr.trace(self.lift, self.items))
        result.reverse()
        return '\n'.join(result)

    def __eq__(self, other):
        return self.lift.floor == other.lift.floor and self.floors == other.floors

    def __hash__(self):
        return hash(str(self))

    def directions(self):
        "In which directions can the elevator move"
        return self.lift.directions()

    def safely_removable(self):
        "Returns list of items that can safely be removed"
        return self.floors[self.lift.floor - 1].safely_removable()

    def legal_moves(self):
        "Determine legal move from this position"

        # 1. Start with nothing
        result = []

        # 2. Get directions the elevator can move and what can be moved
        dirs = self.directions()
        what = self.safely_removable()

        # 3. Loop for all of the directions
        for a_dir in dirs:
            next_floor = self.floors[self.lift.next_floor(a_dir) - 1]

            # 4. Loop for all of the possible items
            for items in what:

                # 5. Check if the items can be safely move to the new floor
                if next_floor.is_safe_with(items):

                    # 6. If it is save, record the legal move
                    result.append((a_dir, items))

        # 7. Return the legal moves
        return result

    def clone(self):
        "Make a copy of the state"

        # 1. Return a copy
        return State(text=aoc_11.from_text(str(self)), part2=self.part2)

    def execute_move(self, move):
        "Return a new state after the move has been completed"

        # 1. Get a copy of the current state
        result = self.clone()

        # 2. Break the move in twain
        lift_dir, items = move
        # print("going %s from floor %d with %d items" % (lift_dir, result.lift.floor, len(items)))

        # 3. Remove the item(s) from the current floor
        old_floor = result.floors[result.lift.floor - 1]
        for an_item in items:
            old_floor.remove(an_item)

        # 4. Move to the new floor
        result.lift.floor = result.lift.next_floor(lift_dir)

        # 5. Put the item(s) on the new floor
        new_floor = result.floors[result.lift.floor - 1]
        for an_item in items:
            new_floor.add(an_item)

        # 6. Return the modified state
        return result

    def is_goal(self):
        "Returns true if this is the goal state"

        # 1. The Elevator most be on the top floor
        if self.lift.floor < self.lift.floors:
            return False

        # 2. All items must be off the lower floors
        for a_floor in self.floors[:-1]:
            if not a_floor.is_empty():
                return False

        # 3. Looks good to me
        return True

    def is_safe(self):
        "Returns true if all the floors are safe"

        # 1. Loop for all the floors
        for a_floor in self.floors:

            # 2. If any floor is not safe than the state not safe
            if not a_floor.is_safe():
                return False

        # 3. Looks good to me
        return True


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         s t a t e . p y                        end
# ======================================================================
