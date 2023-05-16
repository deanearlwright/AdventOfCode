
# ======================================================================
# Blizzard Basin
#   Advent of Code 2022 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         v a l l e y . p y
# ======================================================================
"Valley for the Advent of Code 2022 Day 24 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple
from collections import deque

# ----------------------------------------------------------------------
#                                                                  types
# ----------------------------------------------------------------------
Loc = namedtuple('Loc', 'col, row')
Snow = namedtuple('Snow', 'col, row, facing')
State = namedtuple('State', 'time, col, row')

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
FACINGS = frozenset(['v', '^', '<', '>'])
DELTA = {
    '^': Loc(col=0, row=-1),
    'v': Loc(col=0, row=1),
    '>': Loc(col=1, row=0),
    '<': Loc(col=-1, row=0),
}
MIN = -1
MAX = 1
SAME = 0
WARP = {
    '^': Loc(col=SAME, row=MAX),
    'v': Loc(col=SAME, row=MIN),
    '>': Loc(col=MIN, row=SAME),
    '<': Loc(col=MAX, row=SAME),
}

# ======================================================================
#                                                                 Valley
# ======================================================================


class Valley(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Blizzard Basin"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.snow = None
        self.width = 0
        self.height = 0
        self.start = None
        self.goal = None
        self.snows = []
        self.current_goal = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.find_snow()
            self.snows.append(self.snow)
            self.find_size()
            self.find_entrances()

    def find_snow(self):
        "Find all the initial blizzards in the valley"

        # 1. Start with nothing
        blizzards = []

        # 2. Loop for each row of text
        for r_num, row in enumerate(self.text):

            # 3. Loop for each column in the row
            for c_num, col in enumerate(row):

                # 4. If this is a blizzard, record it
                if col in FACINGS:
                    snow = Snow(col=c_num, row=r_num, facing=col)
                    blizzards.append(snow)

        # 5. Save the blizzards
        self.snow = frozenset(blizzards)

    def find_size(self):
        "Find the size of the valley"

        # 1. Width is the location of the right wall
        self.width = len(self.text[0]) - 1

        # 2. Height is the location of the bottom wall
        self.height = len(self.text) - 1

    def find_entrances(self):
        "Find the entrence and exit to the valley"

        # 1. The enterance is on the first row (NW corner)
        self.start = Loc(col=1, row=0)

        # 2. The exit is on the last row (SE corner)
        self.goal = Loc(col=self.width - 1, row=self.height)

    def find_path(self):
        "Find the shortest path through the valley"

        # 1. Start at the very beginning
        state = State(time=0, col=self.start.col, row=self.start.row)

        # 2. Find the fastest path to the goal
        fastest = self.find_one_path(self.goal, state)

        # 3. That's it for part one
        if not self.part2:
            return fastest

        # 4, Go back to the start
        state = State(time=fastest, col=self.goal.col, row=self.goal.row)
        fastest = self.find_one_path(self.start, state)

        # 5. And then back to the goal
        state = State(time=fastest, col=self.start.col, row=self.start.row)
        return self.find_one_path(self.goal, state)

    def find_one_path(self, goal, start):
        "Find the shortest path through the valley"

        # 1. Start at the very beginning
        states = deque()
        states.append(start)
        seen = set()
        self.current_goal = goal

        # 2. Loop while there is something to do
        while states:

            # 3. Grab the new oldest state
            state = states.popleft()
            if state in seen:
                continue
            seen.add(state)
            time, col, row = state
            # print(f"time={time}, loc=({col},{row}), states={len(states)}, " \
            #       f"snows={len(snows)}, seen={len(seen)}")

            # 4. Don't need to explore if already taken too long
            time += 1
            if time > 9999:
                break

            # 5. Get possible next locations
            next_locs = self.next_locations(col, row)

            # 6. If one of these is the goal, we have done it!
            if goal in next_locs:
                print(f"Reached {goal} at {time}")
                return time

            # 7. Determine where the snow will be
            if time == len(self.snows):
                self.snows.append(self.next_snow(self.snows[time - 1]))
                print(f"Generated snow for time {time}")

            # 8. Determine the snow less next locations
            good_locs = self.snowless(next_locs, self.snows[time])

            # 9. Add the new states
            for next_loc in good_locs:
                state = State(time=time, col=next_loc.col, row=next_loc.row)
                states.append(state)
                # print("adding", state)

        # 10. Return unable to find a path
        return None

    def next_locations(self, col, row):
        "Determine where the party can next move"

        # 1. They can always just stay here
        result = [Loc(col=col, row=row)]

        # 2. Loop for the possible directions
        for delta_col, delta_row in DELTA.values():

            # 3. Calculate the new locations
            new_col = col + delta_col
            new_row = row + delta_row

            # 4. Can't move north from the entrance or south from goal
            if new_row < 0 or new_row > self.height:
                continue

            # 5. If this is the goal, make that our only move
            if self.is_current_goal(new_col, new_row):
                return [Loc(col=new_col, row=new_row)]

            # 6. Can't move to a wall (unless it is the start or goal)
            if self.is_wall(new_col, new_row):
                if not (self.is_entrance(new_col, new_row) or
                        self.is_goal(new_col, new_row)):
                    continue

            # 8. Add this location as a possible move
            result.append(Loc(col=new_col, row=new_row))

        # 9. Return the possible moves
        return result

    def is_entrance(self, col, row):
        "Return True if this is the entrance"

        return col == self.start.col and row == self.start.row

    def is_goal(self, col, row):
        "Return True if this is the goal"

        return col == self.goal.col and row == self.goal.row

    def is_current_goal(self, col, row):
        "Return True if this is the goal"

        return col == self.current_goal.col and row == self.current_goal.row

    def is_snowless(self, loc, snows):
        "Return True if there is no snow at this location"

        # 1. Loop for the possible facings
        for facing in FACINGS:

            # 2. Is there snow here going this way?
            snow = Snow(col=loc.col, row=loc.row, facing=facing)
            if snow in snows:
                return False

        # 3. Good to go
        return True

    def snowless(self, locs, snow):
        "Keep only snowless locations"

        # 1. Start with nothing
        result = []

        # 2. Loop for the locations
        for loc in locs:

            # 3. Is it clear here?
            if self.is_snowless(loc, snow):

                # 4. We will keep this location
                result.append(loc)

        # 5. Return the snowless locations
        return result

    def is_wall(self, col, row):
        "Return True if there is a wall at this location"

        # 1. There are walls along the top and left side
        if col == 0 or row == 0:
            return True

        # 2. There are walls along the botton and right size
        if col == self.width or row == self.height:
            return True

        # 3. Otherwise it is not a wall
        return False

    def next_snow(self, current):
        "Return the location of the snow after it moves"

        # 1. Start with nothing
        blizzards = []

        # 2. Loop for all of the current snow storms
        for col, row, facing in current:

            # 3. Move the storm
            col = col + DELTA[facing].col
            row = row + DELTA[facing].row

            # 4. If we hit a wall, warp to the other side
            if self.is_wall(col, row):
                # print(f"wall at ({col},{row})")
                col, row = self.warp(col, row, facing)

            # 5. Record the new location
            # print(f"snow ({orig_col},{orig_row}) {facing} ({col},{row})")
            snow = Snow(col=col, row=row, facing=facing)
            blizzards.append(snow)

        # 6. Return the new locations
        # print(f"current = {len(current)}, blizzards = {len(blizzards)}")
        return frozenset(blizzards)

    def warp(self, col, row, facing):
        "Break on through to the other size"

        # 1. Get the warpping instructions
        warp_info = WARP[facing]

        # 2. Adjust column
        if warp_info.col == MIN:
            col = 1
        elif warp_info.col == MAX:
            col = self.width - 1

        # 3. Adjust row
        if warp_info.row == MIN:
            row = 1
        elif warp_info.row == MAX:
            row = self.height - 1

        # 4. Return the wrapped location
        return col, row


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        v a l l e y . p y                       end
# ======================================================================
