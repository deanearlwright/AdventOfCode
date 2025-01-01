
# ======================================================================
# Reindeer Maze
#   Advent of Code 2024 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                             m a z e . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple

# ----------------------------------------------------------------------
#                                                                  types
# ----------------------------------------------------------------------
State = namedtuple("State", "loc direction actions score path")

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

TURNS = set("CA")
MOVE = "M"
ACTIONS = list("MCA")
COST = {
    "M": 1,
    "C": 1000,
    "A": 1000,
}

DELTA = {
    '^': (-1, 0),
    'v': (1, 0),
    '>': (0, 1),
    '<': (0, -1),
}
FACING = {
    '^': {"C": ">", "A": "<"},
    'v': {"C": "<", "A": ">"},
    '>': {"C": "v", "A": "^"},
    '<': {"C": "^", "A": "v"},

}

PART1_MAX = 608136 + 1
PART1_SCORE = 92432

# ======================================================================
#                                                                   Maze
# ======================================================================


class Maze(object):   # pylint: disable=R0902, R0205
    "Object for Reindeer Maze"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.walls = set()
        self.start = (0, 0)
        self.end = (0, 0)
        self.best = {}
        self.tiles = set()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text()

    def _process_text(self):
        "Assign values from text"

        assert self.text is not None and len(self.text) > 0

        # 1. Loop for every row and column in the maze
        for row, line in enumerate(self.text):
            for col, char in enumerate(line):
                loc = (row, col)

                # 2. Process the character
                match char:
                    case "#":
                        self.walls.add(loc)
                    case "S":
                        self.start = loc
                    case "E":
                        self.end = loc

    def can_move(self, loc, direction, path=None):
        "Return the next location or NONE if can't move in that direction"

        # 1. Get the direction delta
        delta = DELTA[direction]

        # 2. Determine the new location
        new_loc = (loc[0] + delta[0], loc[1] + delta[1])

        # 3. Can't go there if this is a wall
        if new_loc in self.walls:
            return None

        # 4. Don't repeat yourself
        if new_loc in path:
            return None

        # 5. Return new loc
        return new_loc

    def can_turn(self, loc, direction, path=None):
        "Return the turn actions available here"

        # 1. Start with nothing
        result = []

        # 2. Loop for the facings
        for which in TURNS:

            # 3. Determine the new direction
            new_dir = FACING[direction][which]

            # 4. Determine the new location in that facing
            new_loc = self.can_move(loc, new_dir, path=path)

            # 5. Can't go there if this is a wall
            if new_loc is None:
                continue

            # 6. Don't repeat yourself
            if new_loc in path:
                return None

            # 7. Can turn that way
            result.append(which)

        # 8. Return the viable turnings
        return result

    def available_actions(self, loc, direction, turns=True, path=None):
        "Return the list of actions available at this location and direction"

        # 1. Try the turns
        if turns:
            result = self.can_turn(loc, direction, path=path)
        else:
            result = []

        # 2. Add move if we can
        if self.can_move(loc, direction, path=path) is not None:
            result.append(MOVE)

        # 3. Return the availble actions
        return result

    def available_directions(self, loc, path=None):
        "Return the directions you can move from here"

        # 1. Start with nothing
        result = []

        # 2. Loop for all the directions
        for direction in DELTA:

            # 3. Add the direction if we can go that way
            if self.can_move(loc, direction, path=path):
                result.append(direction)

        # 4. Return the ways we can go
        return result

    def execute(self, action, state):
        "Return a new state executing the action"
        assert action in ACTIONS

        # 1. Determine the new score
        new_score = state.score + COST[action]

        # 2. Determine the new location and direction
        new_path = state.path.copy()
        if action == MOVE:
            new_loc = self.can_move(state.loc, state.direction, path=state.path)
            new_dir = state.direction
            new_path[new_loc] = new_score
            turns = True
            if self.part2:
                fudge = COST["M"] + COST["C"]
            else:
                fudge = 0
            if new_loc not in self.best or new_score <= self.best[new_loc] + fudge:
                self.best[new_loc] = new_score
            else:
                # print("execute-best: None")
                return None
        else:
            new_loc = state.loc
            new_dir = FACING[state.direction][action]
            turns = False

        # 4. Determine the available actions
        new_act = self.available_actions(new_loc, new_dir, turns, path=new_path)

        # 6. Return the new state
        return State(loc=new_loc, direction=new_dir, actions=new_act,
                     score=new_score, path=new_path)

    def best_maze(self):
        "Find the score for the best path through the maze"

        # 1. Start with a very bad score
        result = PART1_MAX

        # 2. Create the initial states
        states = []
        state = State(loc=self.start, direction=">",
                      actions=self.available_actions(self.start, ">", path={}),
                      score=0, path={})
        self.best[self.start] = 0
        # print("initial", state)
        states.append(state)

        # 3. Loop with there is something to do
        while len(states) > 0:

            # 4. Get the earliest state added (breath first)
            state = states.pop(0)
            #  print(len(states), state)

            # 5. Are we there yet
            loc = state.loc
            score = state.score
            if loc == self.end:
                if state.score < result:
                    # print(">>>>>>>>>>>", len(states), score)
                    result = score
                    continue

            # 6. Get the next states from here
            for action in state.actions:
                new_state = self.execute(action, state)
                if new_state is None:
                    continue
                if new_state.score > result:
                    continue
                states.append(new_state)

        # 7. Return the best score found
        return result

    def find_tiles(self, score=PART1_SCORE):
        "Find the sets score for the best path through the maze"

        # 1. Start knowing the best score
        result = score
        self.part2 = True

        # 2. Create the initial states
        states = []
        state = State(loc=self.start, direction=">",
                      actions=self.available_actions(self.start, ">", path={}),
                      score=0, path={})
        self.best[self.start] = 0
        self.tiles.add(self.start)
        # print("initial tiles", state)
        states.append(state)

        # 3. Loop with there is something to do
        while len(states) > 0:

            # 4. Get the earliest state added (breath first)
            state = states.pop(0)
            #  print(len(states), state)

            # 5. Are we there yet
            loc = state.loc
            score = state.score
            if loc == self.end:
                # print("at end", score)
                if state.score == result:
                    # print("setting tiles", len(state.path))
                    for tile in state.path:
                        self.tiles.add(tile)
                    self.tiles.add(loc)
                continue

            # 6. Get the next states from here
            for action in state.actions:
                new_state = self.execute(action, state)
                if new_state is None:
                    continue
                if new_state.score > result:
                    continue
                states.append(new_state)

        # 7. Return the number of tiles on the best paths
        return len(self.tiles)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        return self.best_maze()

    def part_two(self, verbose=False, limit=0, score=PART1_SCORE):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part two
        return self.find_tiles(score=score)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                          m a z e . p y                         end
# ======================================================================
