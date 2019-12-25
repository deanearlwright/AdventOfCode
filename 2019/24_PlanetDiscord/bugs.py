# ======================================================================
# Planet of Discord
#   Advent of Code 2019 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                            b u g s . p y
# ======================================================================
"Artificial Life for the Planet of Discord problem for AoC 2019 Day 24"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import Counter

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EMPTY = '.'
BUGS = '#'
INNER = '?'

KNT = {EMPTY: 0, BUGS: 1, INNER: 0}

REMAINS = set([1])
INFESTS = set([1, 2])

SIZE = 5

DELTA = [(1, 0), (-1, 0), (0, 1), (0, -1)]

CENTER_UP = 100
EDGES_DOWN = -100

# ======================================================================
#                                                                   Bugs
# ======================================================================


class Bugs():
    """Object representing the indigenous life form on Eris"""

    def __init__(self, text=None, size=SIZE, recursive=False):

        # 1. Set the initial values
        self.size = size
        self.length = size * size
        self.current = EMPTY * self.length
        self.minute = 0
        self.levels = {}

        # 2. If there is a text, set the current state
        if text is not None:
            self.current = self.set_current_from_text(text)

        # 3. Compute the adjacency indexes based on the size
        self.adjacent = self.set_adjacency(recursive)

        # 4. If doing recursie (prob two), set level 0
        if recursive:
            self.levels[0] = self.current

    def set_current_from_text(self, text):
        "Set the current state from input text"

        # 0. Preconditions
        assert len(text) == self.size
        assert len(text[0]) == self.size

        # 1. Start with nothing
        result = []

        # 2. Loop through the rows of the the text
        for row in text:

            # 3. Append the row to the result
            result.append(row)

        # 4. Return the adjoined rows
        return ''.join(result)

    def set_adjacency(self, recursive=False):
        "Compute and set the adjacent indexes"

        # 1. Start with nothing
        result = [[] for _ in range(self.length)]

        # 2. Loop for all the rows and all the columns
        for row in range(self.size):
            for col in range(self.size):
                index = col + self.size * row

                # 3. Loop for the sourounding spaces
                for delta in DELTA:
                    delta_col = col + delta[0]
                    delta_row = row + delta[1]

                    # 4. If doing recursive, things get more complicated
                    if recursive:
                        result[index].extend(self.recursive_adj(delta, delta_col, delta_row))

                    # 5. Not recursive just worried about going off an edge
                    else:
                        if delta_col < 0 or delta_col == self.size:
                            continue
                        if delta_row < 0 or delta_row == self.size:
                            continue
                        result[index].append(delta_col + self.size * delta_row)

        # 6. Return the adjacent indexes
        return result

    def recursive_adj(self, delta, delta_col, delta_row):
        "Need to worry about recurising into center and off the edges"

        # 1. Start with nothing
        result = []
        center = self.size // 2
        abs_center = center + self.size * center

        # 1. Left edge reaches down into surrounding grid
        if delta_col < 0:
            result.append(EDGES_DOWN - (abs_center - 1))

        # 2. Right edge reaches down into surrounding grid
        elif delta_col == self.size:
            result.append(EDGES_DOWN - (abs_center + 1))

        # 3. Top edge reaches down into surrounding grid
        elif delta_row < 0:
            result.append(EDGES_DOWN - (abs_center - self.size))

        # 4. Bottom edges reaches down into surrounding grid
        elif delta_row == self.size:
            result.append(EDGES_DOWN - (abs_center + self.size))

        # 5. Center square is up in the enclosed grid
        elif delta_col == center and delta_row == center:

            # 5a. Right of center reaches up to the left cells of the enclosed grid
            if delta[0] == -1:
                result.extend([CENTER_UP + _ for _ in range(self.size - 1, self.length, self.size)])

            # 5b. Left of center reaches up to the right cells of the enclosed grid
            elif delta[0] == 1:
                result.extend([CENTER_UP + _ for _ in range(0, self.length, self.size)])

            # 5c. Below center reaches up to the bottom cells of the enclosed grid
            elif delta[1] == -1:
                result.extend([CENTER_UP + _ for _ in range(self.length - self.size, self.length)])

            # 5d. Above center reaches up to the top cells of the enclosed grid
            elif delta[1] == 1:
                result.extend([CENTER_UP + _ for _ in range(0, self.size)])

        # 6. Otherwise this is just a regular adjency
        else:
            result.append(delta_col + self.size * delta_row)

        # 6. Return the adjacent cells
        return result

    def run_until_duplicate(self, watch=False, maxtime=0):
        "Run the simulation untile there is a duplicate pattern"

        # 1. Start with nothing previous
        previous = set()

        # 2. Output generation 0 (if you want it)
        if watch:
            print("%d: %s" % (self.minute, self.current))

        # 3. Loop until there is a duplicate or we run out of time
        while self.current not in previous:

            # 4. Compute the next generation
            previous.add(self.current)
            self.next_generation()

            # 5. See if we have spent too much time
            self.minute += 1
            if watch:
                print(str(self))
            if self.minute > maxtime > 0:
                return None

        # 6. Return the reason we stopped
        return self.minute

    def next_generation(self):
        "Compute the next generation of bugs"

        # 1. Assume everything will stay the same
        result = [_ for _ in self.current]

        # 2. Loop for for every location
        for index, current in enumerate(self.current):

            # 3. Get the count of neighbors
            knt = 0
            for neighbor in self.adjacent[index]:
                knt += KNT[self.current[neighbor]]

            # 4. A bug dies unless there is exactly one bug adjacent
            if current == BUGS:
                if knt not in REMAINS:
                    result[index] = EMPTY

            # 5. An empty space becomes infested if there are 1 or 2 bug adjacent
            elif knt in INFESTS:
                result[index] = BUGS

        # 6. Set the next generation as a string
        self.current = ''.join(result)

    def __str__(self):
        if self.levels:
            result = []
            for key in sorted(self.levels):
                level = self.levels[key]
                knts = Counter(level)
                if knts[BUGS] > 0:
                    result.append("m=%d l=%d: %s" % (self.minute, key, level))
            return '\n'.join(result)
        return "m=%d: %s" % (self.minute, self.current)

    def get_biodiversity_rating(self):
        "Returns biodiversity rating"

        # 1. Start with zero
        result = 0

        # 2. Loop for all of current locations
        for index, loc in enumerate(self.current):

            # 3. If there are bugs, add to rating
            if loc == BUGS:
                result += 2**index

        # 4. Return the total biodiversity rating
        return result

    def run_until(self, minute, watch=False):
        "Run a recursive simulation until specified minute"

        # 1. Loop until we reach the desired generation
        while self.minute < minute:

            # 2. Show the levels (if desired)
            if watch:
                print(str(self))

            # 3. Calculate the next generation
            self.next_gen_recursive()

        # 4. Show the final level
        if watch:
            print(str(self))

    def next_gen_recursive(self):
        "Compute the next generation of bugs up and down the levels"

        # 1. Determine counts at each of the existing levels
        counts = {}
        for key in self.levels:
            counts[key] = self.level_bug_count(key)

        # 2. Get lowest and highest levels where bugs > 0
        non_zero = [key for key in counts if counts[key] > 0]
        lowest = min(non_zero) - 1
        highest = max(non_zero) + 1

        # 3. If these levels to not exist, add them
        if lowest not in self.levels:
            self.levels[lowest] = EMPTY * self.length
        if lowest - 1 not in self.levels:
            self.levels[lowest - 1] = EMPTY * self.length
        if highest not in self.levels:
            self.levels[highest] = EMPTY * self.length
        if highest + 1 not in self.levels:
            self.levels[highest + 1] = EMPTY * self.length

        # 4. Loop from the lowest to highest levels
        next_levels = {}
        for level in range(lowest, highest + 1):

            # 5. Compute the next generation for this level
            next_levels[level] = self.next_gen_level(level)

        # 6. The next levels replace the existing levels
        self.levels = next_levels

        # 7. And time marches on
        self.minute += 1

    def next_gen_level(self, level):
        "Return the next generation of this recursive level"

        # 1. Assume everything will stay the same
        result = [_ for _ in self.levels[level]]
        center = self.size // 2
        abs_center = center + self.size * center
        result[abs_center] = INNER

        # 2. Loop for for every location on this level
        for index, current in enumerate(self.levels[level]):
            if index == abs_center:
                continue

            # 3. Get the count of neighbors
            knt = 0
            for neighbor in self.adjacent[index]:
                neighbor_level = neighbor // CENTER_UP
                if neighbor_level < 0:
                    neighbor_level += 1
                neighbor_index = abs(neighbor) % CENTER_UP
                # print("l=%d, n=%d, nl=%d, ni=%d" %
                # (level, neighbor, neighbor_level, neighbor_index))
                knt += KNT[self.levels[level + neighbor_level][neighbor_index]]

            # 4. A bug dies unless there is exactly one bug adjacent
            if current == BUGS:
                if knt not in REMAINS:
                    result[index] = EMPTY

            # 5. An empty space becomes infested if there are 1 or 2 bug adjacent
            elif knt in INFESTS:
                result[index] = BUGS

        # 6. Return next generation as a string
        return ''.join(result)

    def total_bug_count(self):
        "Return the total number of bugs on all level"

        # 1. Start with nothing
        knts = Counter()

        # 2. Loop for all the levels
        for value in self.levels.values():

            # 3. Get the counts at this level
            knt = Counter(value)

            # 4. Accumulate the counts
            knts += knt

        # 5. Return the count of bugs
        return knts[BUGS]

    def level_bug_count(self, level):
        "Return the total number of bugs on one level"

        return Counter(self.levels[level])[BUGS]



# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          b u g s . p y                         end
# ======================================================================
