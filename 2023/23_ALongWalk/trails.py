
# ======================================================================
# A Long Walk
#   Advent of Code 2023 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         t r a i l s . p y
# ======================================================================
"Trails for the Advent of Code 2023 Day 23 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple
import heapq
# ----------------------------------------------------------------------
#                                                                  types
# ----------------------------------------------------------------------
Loc = namedtuple("Loc", "r, c")
State = namedtuple("State", "key, steps, loc, prev, seen")

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
SLOPES = ["^", "v", ">", "<"]
DELTA = [Loc(-1, 0), Loc(1, 0), Loc(0, 1), Loc(0, -1)]
PATH = '.'
FOREST = "#"

# ======================================================================
#                                                                 Trails
# ======================================================================


class Trails(object):   # pylint: disable=R0902, R0903, R0205
    "Object for A Long Walk"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.start = None
        self.exit = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 0. Precondition axioms
        assert text is not None and len(text) > 0

        # 1. Find the starting location on the first row
        for cindx, col in enumerate(text[0]):
            if col == PATH:
                self.start = Loc(0, cindx)
                break

        # 2. Find the exit location on the last row
        for cindx, col in enumerate(text[-1]):
            if col == PATH:
                self.exit = Loc(len(text) - 1, cindx)
                break

        # 3. Postcondition axioms
        assert self.start is not None
        assert self.exit is not None

    def longest_hike(self):
        "Find the length of the longest hike"

        # 1. let's start at the very beginning
        result = 0
        search = [State(key=0, steps=0, loc=self.start, prev=Loc(-1, self.start.c), seen=set())]

        # 2. Loop while there is something to explore
        knt = 0
        while search:
            knt += 1

            # 3. We are here now
            state = heapq.heappop(search)

            # 4. Are we at the exit?
            if state.loc == self.exit:
                prev = result
                if state.steps > result:
                    result = state.steps
                print(f"{knt}: At exit in {state.steps} steps, previous={prev}, longest={result}")
                continue

            # 5. Get the possible next locations
            new_locs = self.next_locs(state.loc, state.prev, state.seen)

            # 6. Loop for all of the unseen next locations
            for new_loc in new_locs:

                # 7. Add the new location to the search
                new_seen = self.next_seen(state.seen, new_locs, new_loc)
                new_state = State(key=state.key - 1, steps=state.steps + 1,
                                  loc=new_loc, prev=state.loc, seen=new_seen)
                heapq.heappush(search, new_state)

        # 8. Return the length of the longest hike
        print(f"{knt} states searched")
        return result

    def next_locs(self, loc, prev, seen):
        "Return the next possible locations"

        # 1. Start with nothing
        result = []

        # 2. Are we on a steep slop?
        if not self.part2:
            at_loc = self.text[loc.r][loc.c]
            if at_loc in SLOPES:
                deltas = [DELTA[SLOPES.index(at_loc)]]
            else:
                deltas = DELTA

        # 3. Else we can try more directions
        else:
            deltas = DELTA

        # 4. Get the new possible locations
        new_locs = [Loc(loc.r + delta.r, loc.c + delta.c) for delta in deltas]

        # 5. If valid new location, add it to the result
        for new_loc in new_locs:
            if new_loc == prev:
                continue
            if new_loc in seen:
                continue
            if self.text[new_loc.r][new_loc.c] == FOREST:
                continue
            result.append(new_loc)

        # 6. Return the possible new locations
        return result

    def next_seen(self, seen, new_locs, new_loc):
        "Determine seen for the next state"

        # 1. Part 1 always has an empty seen
        if not self.part2:
            return seen

        # 2. If this is the last location, reuse seen
        if new_loc != new_locs[-1]:
            seen = seen.copy()

        # 3. Add this location to seen
        seen.add(new_loc)

        # 4. Return the new seen
        return seen

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        t r a i l s . p y                       end
# ======================================================================
