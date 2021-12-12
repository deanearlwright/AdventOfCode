# ======================================================================
# Passage Pathing
#   Advent of Code 2021 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c a v e s . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 12 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
STARTEND = frozenset(['start', 'end'])

# ----------------------------------------------------------------------
#                                                            namedtuples
# ----------------------------------------------------------------------
TODO = namedtuple('TODO', 'before at options goal twice')

# ======================================================================
#                                                                  Caves
# ======================================================================


class Caves(object):   # pylint: disable=R0902, R0205
    "Object for Passage Pathing"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.caves = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.add_path(line)

    def add_path(self, line):
        "Add a cave path to the caves"

        # 1. Split line into the two parts of the path
        cave_one, cave_two = line.split('-')

        # 2. Add the caves if this is the first time they have been seen
        if cave_one not in self.caves:
            self.caves[cave_one] = []
        if cave_two not in self.caves:
            self.caves[cave_two] = []

        # 3. Add the path to the cave definitions
        self.caves[cave_one].append(cave_two)
        self.caves[cave_two].append(cave_one)

    def find_paths(self, start_cave, end_cave):
        "Find the paths from start to end"

        # 1. Start with nothing
        paths = []
        explore = []

        # 2. Add the initial exploration
        todo = TODO(before=[], at=start_cave, options=self.caves[start_cave][:],
                    goal=end_cave, twice='')
        explore.append(todo)

        # 2a. In part 2. you can visit a selected small cave twice
        if self.part2:
            for cave in self.small_caves():
                todo = TODO(before=[], at=start_cave, options=self.caves[start_cave][:],
                            goal=end_cave, twice=cave)
                explore.append(todo)

        # 3. Loop while there is something to explore
        while len(explore) > 0:
            # print(explore)

            # 4. Take a todo from the stack
            todo = explore.pop()

            # 5. Have we reached the end? Yes --> Add it to the completed paths
            if todo.at == todo.goal:

                # 5a. If there is a designated small cave, we must visit it twice
                if todo.twice != '':
                    if Caves.times_occurs(todo.before, todo.twice) != 2:
                        continue
                paths.append(todo.before.append(todo.at))
                continue

            # 6. Are there any options? No --> This path is dead
            if len(todo.options) == 0:
                continue

            # 7. Get one of the options for the next move
            options = todo.options
            next_cave = options.pop()

            # 8. Put back to current todo (less one option)
            explore.append(
                TODO(before=todo.before, at=todo.at, options=options,
                     goal=todo.goal, twice=todo.twice))

            # 9. Craft the next todo
            before = todo.before[:]
            before.append(todo.at)
            filtered = self.filter_options(before, next_cave, todo.twice)

            # 10. Add the next todo
            explore.append(
                TODO(before=before, at=next_cave, options=filtered,
                     goal=todo.goal, twice=todo.twice))

        # 11. Return the paths
        return paths

    def filter_options(self, before, at_cave, twice=''):
        "Filter the options -- can't go to small caves twice (unless part 2)"

        # 1. Start with nothing
        result = []

        # 2. Loop for all the options
        for option in self.caves[at_cave]:

            # 3. If lowercase, check if we have been there before
            if option.islower():
                #print(before, at_cave, twice, option)
                if option in before:

                    # 3a. In part 2 we can visit the designated small cave twice
                    if option != twice:
                        continue
                    if Caves.times_occurs(before, option) > 1:
                        continue

            # 4. The option looks good
            result.append(option)

        # 5. Return the filtered options
        return result

    def small_caves(self):
        "Return the names of the small caves"

        # 1. Start with nothing
        result = []

        # 2. Loop for all of the cave
        for cave in self.caves:

            # 3. Ignore large caves
            if cave.isupper():
                continue

            # 4. Ignore the start and ending caves
            if cave in STARTEND:
                continue

            # 5. Add this small cave to the list
            result.append(cave)

        # 6. Return the names of the small caves
        return result

    @staticmethod
    def times_occurs(path, cave):
        "Return the number of times the cave appears in the path"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the caves in the path
        for one in path:

            # 3. If this is the one, increment the count
            if one == cave:
                result += 1

        # 4. Return the count
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return len(self.find_paths('start', 'end'))

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return len(self.find_paths('start', 'end'))


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         c a v e s . p y                        end
# ======================================================================
